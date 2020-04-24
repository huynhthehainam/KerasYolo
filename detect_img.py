import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image
import glob
import os
from convertannotation import convert_annotation
import cv2


def bb_intersection_over_union(boxA, boxB):
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])
    # compute the area of intersection rectangle
    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
    # compute the area of both the prediction and ground-truth
    # rectangles
    boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
    boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = interArea / float(boxAArea + boxBArea - interArea)
    # return the intersection over union value
    return iou


def detect_img(yolo):
    file_names = glob.glob('./video/outputframe/*.jpg')
    count = 0
    text_write = ''
    for file_name in file_names:
        file_name = file_name.replace('\\', '/')
        file_label = file_name.replace('jpg', 'txt')
        if os.path.exists(file_name) and os.path.exists(file_label):
            box_A = convert_annotation(file_label)
            # img = Image.open(file_name)

            # box_B = yolo.detect_image(img)

            # if box_A is not None and box_B is not None:
            #     count+=1
                # print(box_A[0],box_A[1],box_A[2], box_A[3])
                # print(box_B[0],box_B[1],box_B[2], box_B[3])
                # iou = bb_intersection_over_union(box_A, box_B)
                # img = cv2.imread(file_name)
                # cv2.rectangle(img, (box_A[0], box_A[1]),
                #               (box_A[2], box_A[3]), (225, 0, 0), 2)
                # cv2.rectangle(img, (box_B[0], box_B[1]),
                #               (box_B[2], box_B[3]), (0, 225, 0), 2)
                # new_file_name = './compare/'+str(count)+'.jpg'
                # cv2.imwrite(new_file_name,img)
                # text_write += new_file_name +','+str(iou)+'\n'
               
        img = Image.open(file_name)

        box_B = yolo.detect_image(img)
        if box_B is not None:
            text_write += file_name +','+ str(1)+'\n'
        else:
            text_write += file_name +','+ str(0)+'\n'
    with open('./compare.csv','w') as f:
        f.write(text_write)
    # r_image.show()
    # yolo.close_session()


FLAGS = None

if __name__ == '__main__':
    # class YOLO defines the default value, so suppress any default here
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    '''
    Command line options
    '''
    parser.add_argument(
        '--model', type=str,
        help='path to model weight file, default ' +
        YOLO.get_defaults("model_path")
    )

    parser.add_argument(
        '--anchors', type=str,
        help='path to anchor definitions, default ' +
        YOLO.get_defaults("anchors_path")
    )

    parser.add_argument(
        '--classes', type=str,
        help='path to class definitions, default ' +
        YOLO.get_defaults("classes_path")
    )

    parser.add_argument(
        '--gpu_num', type=int,
        help='Number of GPU to use, default ' +
        str(YOLO.get_defaults("gpu_num"))
    )

    parser.add_argument(
        '--image', default=False, action="store_true",
        help='Image detection mode, will ignore all positional arguments'
    )
    '''
    Command line positional arguments -- for video detection mode
    '''
    parser.add_argument(
        "--input", nargs='?', type=str, required=False, default='./path2your_video',
        help="Video input path"
    )

    parser.add_argument(
        "--output", nargs='?', type=str, default="",
        help="[Optional] Video output path"
    )

    FLAGS = parser.parse_args()

    if FLAGS.image:
        """
        Image detection mode, disregard any remaining command line arguments
        """
        print("Image detection mode")
        if "input" in FLAGS:
            print(" Ignoring remaining command line arguments: " +
                  FLAGS.input + "," + FLAGS.output)

        detect_img(YOLO(**vars(FLAGS)))
    elif "input" in FLAGS:
        yolo = YOLO(**vars(FLAGS))
        detect_video(YOLO(**vars(FLAGS)), FLAGS.input, FLAGS.output)
    else:
        print("Must specify at least video_input_path.  See usage with --help.")
