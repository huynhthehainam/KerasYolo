import glob
import cv2
def abc():
    list_files = glob.glob('./*.txt')
    write_data = ''
    for file_name in list_files:
        raw_data = ''
        with open(file_name, 'r') as f:
            raw_data = f.read()
        if raw_data != '':
            raw_data = raw_data.split(' ')
            raw_data = [float(num) for num in raw_data]
            center_x = int(raw_data[1]*640)
            center_y = int(raw_data[2]*480)
            width = int(raw_data[3]*640)
            height = int(raw_data[4]*480)
            x_min = center_x - int(width/2)
            y_min = center_y - int(height/2)
            x_max = center_x + int(width/2)
            y_max = center_y + int(height/2)
            # file_image = file_name.replace('txt', 'jpg')
            # file_image = file_image.replace('.\\', './model_data/dataset/img/')
            # write_data += file_image + ' ' + str(x_min) + ','+str(y_min)+','+ str(x_max)+','+str(y_max)+','+'0'+'\n'

            # img = cv2.imread(file_image)
            # cv2.rectangle(img,(x_min,y_min),(x_max, y_max),(255,0,0), 2)
            # cv2.imshow('img',img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
    with open('label.txt','w') as f:
        f.write(write_data)

def convert_annotation(path):
    raw_data = ''
    with open(path, 'r') as f:
        raw_data = f.read()
    if raw_data != '':
        raw_data = raw_data.split(' ')
        raw_data = [float(num) for num in raw_data]
        center_x = int(raw_data[1]*640)
        center_y = int(raw_data[2]*480)
        width = int(raw_data[3]*640)
        height = int(raw_data[4]*480)
        x_min = center_x - int(width/2)
        y_min = center_y - int(height/2)
        x_max = center_x + int(width/2)
        y_max = center_y + int(height/2)
        return [x_min, y_min, x_max, y_max]