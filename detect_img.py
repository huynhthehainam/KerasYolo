import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image
import glob
import os
from convertannotation import convert_annotation
import cv2
from datetime import datetime


def bb_intersection_over_union(boxA, boxB):
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])
    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
    boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
    boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
    iou = interArea / float(boxAArea + boxBArea - interArea)
    return iou


def detect_img(yolo, file_name_path):
    # text_write = ''
    file_name_path = file_name_path.replace('\\', '/')
    img = Image.open(file_name_path)
    #img = Image.fromarray(imgInput) if input is a img from cv2
    text = ''
    box_heli, box_arrow = yolo.detect_image(img)
    text += str(datetime.timestamp(datetime.now())) +','
    if (len(box_heli)>0):
        width = box_heli[2]- box_heli[0]
        height = box_heli[3] - box_heli[1]
        center_x = (box_heli[2] + box_heli[0])/2
        center_y = (box_heli[3] + box_heli[1])/2
        aa = [center_x, center_y, width, height]

        # cv2.rectangle(img, (box_heli[0], box_heli[1]),
        #                     (box_heli[2], box_heli[3]), (225, 0, 0), 2)
        aa = [str(int(bb)) for bb in aa]
        text += '|'.join(aa)
    text +=','
    if (len(box_arrow)>0):
        width = box_heli[2]- box_heli[0]
        height = box_heli[3] - box_heli[1]
        center_x = (box_heli[2] + box_heli[0])/2
        center_y = (box_heli[3] + box_heli[1])/2
        aa = [center_x, center_y, width, height]
        aa = [str(int(bb)) for bb in aa]
        text += '|'.join(aa)

    print(text)
    return text
    # r_image.show()
    # yolo.close_session()



if __name__ == '__main__':
    yolo = YOLO()
    detect_img(yolo,'./video/outputframe/outputframe1.jpg')
