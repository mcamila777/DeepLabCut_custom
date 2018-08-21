import os
import cv2


images_path = '/is/ps2/calvarez2/zebra_project/Zebra_dataset_camila/raw_single_images/Tanya_data'
new_path = '/is/ps2/calvarez2/zebra_project/Zebra_dataset_camila/single_images_03'

images = os.listdir(images_path)

max_input_size = 1000.0

for i in xrange(0, len(images)):
    image = cv2.imread(os.path.join(images_path, images[i]))
    new_name = 'frame0%i.png' %i
    height, width, channels = image.shape
    
    if(width * height > max_input_size*max_input_size):
        factor = (max_input_size*0.9)/max(height, width)
        image = cv2.resize(image, None, fx = factor, fy = factor, interpolation = cv2.INTER_CUBIC)
    
    cv2.imwrite( os.path.join(new_path, new_name) , image)
