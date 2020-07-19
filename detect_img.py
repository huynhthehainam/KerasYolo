import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image, ImageDraw, ImageFont
import glob
import os
import cv2
from datetime import datetime
import numpy as np
from convert_annotation import convert_annotation
import math


def bb_intersection_over_union(boxA, boxB):
    xA = max(boxA['x_min'], boxB['x_min'])
    yA = max(boxA['y_min'], boxB['y_min'])
    xB = min(boxA['x_max'], boxB['x_max'])
    yB = min(boxA['y_max'], boxB['y_max'])
    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
    boxAArea = (boxA['x_max'] - boxA['x_min'] + 1) * \
        (boxA['y_max'] - boxA['y_min'] + 1)
    boxBArea = (boxB['x_max'] - boxB['x_min'] + 1) * \
        (boxB['y_max'] - boxB['y_min'] + 1)
    iou = interArea / float(boxAArea + boxBArea - interArea)
    return iou


def calculate_cle(boxA, boxB):
    cle = math.sqrt((boxA['center_x'] - boxB['center_x'])
                    ** 2 + (boxA['center_y'] - boxB['center_y'])**2)
    return cle


def convert_center_width_height_to_x_y(box):
    x_min = box['center_x'] - int(box['width']/2)
    x_max = box['center_x'] + int(box['width']/2)
    y_min = box['center_y'] - int(box['height']/2)
    y_max = box['center_y'] + int(box['height']/2)
    return {
        'x_min': x_min,
        'x_max': x_max,
        'y_min': y_min,
        'y_max': y_max,
    }


def convert_x_y_to_center_width_height(box):
    center_x = int((box['x_max'] + box['x_min'])/2)
    width = box['x_max'] - box['x_min']
    center_y = int((box['y_max'] + box['y_min'])/2)
    height = box['y_max'] - box['y_min']
    return {
        'center_x': center_x,
        'width': width,
        'center_y': center_y,
        'height': height,
    }


def detect_img(yolo, img):
    box_heli, box_arrow = yolo.detect_image(img)
    result = {'time': datetime.timestamp(
        datetime.now()), 'helipad': None, 'arrow': None}
    if (len(box_heli) > 0):
        width = box_heli[2] - box_heli[0]
        height = box_heli[3] - box_heli[1]
        center_x = (box_heli[2] + box_heli[0])/2
        center_y = (box_heli[3] + box_heli[1])/2
        result['helipad'] = {'center_x': center_x,
                             'center_y': center_y, 'width': width, 'height': height}
    if (len(box_arrow) > 0):
        width = box_arrow[2] - box_arrow[0]
        height = box_arrow[3] - box_arrow[1]
        center_x = (box_arrow[2] + box_arrow[0])/2
        center_y = (box_arrow[3] + box_arrow[1])/2
        result['arrow'] = {'center_x': center_x,
                           'center_y': center_y, 'width': width, 'height': height}
    return result


def draw_box(image, box, color, text):
    text = ''
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font='font/FiraMono-Medium.otf',
                              size=np.floor(3e-2 * image.size[1] + 0.5).astype('int32'))

    draw.rectangle(((box['x_min'], box['y_min']),
                    (box['x_max'], box['y_max'])), outline=color, width=3)
    label = text
    label_size = draw.textsize(label, font)

    if box['y_min'] - label_size[1] >= 0:
        text_origin = np.array(
            [box['x_min'], box['y_min'] - label_size[1]])
    else:
        text_origin = np.array(
            [box['x_min'], box['y_min'] + 1])
    draw.rectangle(
        [tuple(text_origin), tuple(text_origin + label_size)],
        fill=color)
    draw.text(text_origin, label, fill=(0, 0, 0), font=font)


def draw_center(image, box, color, thickness):
    draw = ImageDraw.Draw(image)
    draw.rectangle(((box['center_x'] - int(thickness/2), box['center_y'] - int(thickness/2)),
                    (box['center_x'] + int(thickness/2), box['center_y'] + int(thickness/2))), outline=color, width=thickness)


if __name__ == '__main__':
    results = []
    yolo = YOLO()
    file_names = glob.glob('./video/images/*.jpg')
    count = 0
    for file_name in file_names:
        if 'snapshot' in file_name:
            text_name = file_name.replace('jpg', 'txt')
            if os.path.exists(text_name):
                raw_data = ''
                with open(text_name, 'r') as f:
                    raw_data = f.read()
                if raw_data != '':

                    image = Image.open(file_name)
                    result = detect_img(yolo, image)
                    if result['helipad'] is not None:
                        if count == 1000:
                            break
                        count += 1
                        result['helipad_x_y'] = convert_center_width_height_to_x_y(
                            result['helipad'])
                        draw_box(image, result['helipad_x_y'],
                                 'green', 'helipad_predict')
                        draw_center(image, result['helipad'], 'green', 4)
                        lines = raw_data.split('\n')
                        for line in lines:
                            truth = convert_annotation(line)
                            if truth['class'] == 0:
                                truth_box = {'helipad_x_y': {
                                    'x_min': truth['x_min'],
                                    'y_min': truth['y_min'],
                                    'x_max': truth['x_max'],
                                    'y_max': truth['y_max'],
                                }}
                                truth_box['helipad'] = convert_x_y_to_center_width_height(
                                    truth_box['helipad_x_y'])
                                draw_box(
                                    image, truth_box['helipad_x_y'], 'blue', 'helipad_truth')
                                draw_center(
                                    image, truth_box['helipad'], 'blue', 4)
                                results.append({
                                    'area': truth_box['helipad']['width'] * truth_box['helipad']['height'],
                                    'iou': bb_intersection_over_union(result['helipad_x_y'], truth_box['helipad_x_y']),
                                    'cle': calculate_cle(result['helipad'], truth_box['helipad']),
                                    'center_x_truth': truth_box['helipad']['center_x'],
                                    'center_y_truth': truth_box['helipad']['center_y'],
                                    'width_truth': truth_box['helipad']['width'],
                                    'height_truth': truth_box['helipad']['height'],
                                    'center_x_predict': result['helipad']['center_x'],
                                    'center_y_predict': result['helipad']['center_y'],
                                    'width_predict': result['helipad']['width'],
                                    'height_predict': result['helipad']['height'],
                                })
                        print(count)
                        image.save(f'./video/compare/{count}.jpg')
    lines = []
    for result in results:
        print(result)
        keys = result.keys()
        words = []
        for key in keys:
            words.append(result[key])
        line = ','.join([str(word) for word in words])
        lines.append(line)
    with open('./video/result.csv', 'w') as f:
        f.write('\n'.join(lines))

        # image = Image.open(file_name)
        # result = detect_img(yolo, image)
        # draw_box(image, result)
