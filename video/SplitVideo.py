
import cv2
vidcap = cv2.VideoCapture('20190926_125848.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("./20190926_125848/frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  count += 1