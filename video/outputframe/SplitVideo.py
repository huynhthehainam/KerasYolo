
import cv2
video = cv2.VideoCapture('output.mp4')
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

fps = video.get(cv2.CAP_PROP_FPS)
success,image = video.read()
count = 0
while success:
  cv2.imwrite('./output'+'frame%d.jpg' % count, image)     # save frame as JPEG file      
  success,image = video.read()
  count += 1