#import json
import requests

REQUEST_TIMEOUT = 5
NUM_CAMERAS = 100
DCS_URL = 'http://localhost:8888/camera/{}'

max_data_cam = 0
max_images_cam = 0
max_images = 0
max_data = 0

timed_out_cams = []

for cam_no in range(1, NUM_CAMERAS+1):

    try:
        cam_response = requests.get(DCS_URL.format(cam_no), timeout=REQUEST_TIMEOUT)
    except requests.exceptions.Timeout:
        # retry?
        print('Camera ', cam_no, ' timed out')
        timed_out_cams = timed_out_cams + [cam_no]
        continue
    except requests.exceptions.RequestException as e:
        print('Fatal exception in request to camera ', cam_no)
        print(e)
        continue
    
    if cam_response.status_code != requests.codes.ok:
        print('Camera ', cam_no, ' reports status code ', cam_response.status_code)
        continue

    #print(cam_response.json()['images'][0]['file_size'])
    #print(len(cam_response.json()['images']))
    cam_largest_image = 0
    cam_largest_image_size = 0
    cam_info = cam_response.json()
    cam_data_size = 0

    # check if this camera has more no. of images than any previous ones
    if len(cam_info['images']) > max_images:
        max_images = len(cam_info['images'])
        max_images_cam = cam_no

    # now add up all the image sizes from this camera
    for image in range(len(cam_response.json()['images'])):
        cam_data_size += cam_info['images'][image]['file_size']
        if cam_info['images'][image]['file_size'] > cam_largest_image_size:
            cam_largest_image_size = cam_info['images'][image]['file_size']
            cam_largest_image = image
        
    if cam_data_size > max_data:
        max_data = cam_data_size
        max_data_cam = cam_no

    print ('For camera ', cam_no, ' largest image is ' , cam_largest_image, ' of size ', cam_largest_image_size)

print ('========== SUMMARY ==========')
print ('Camera ', max_data_cam, ' has used most data')
print ('Camera ', max_images_cam, ' has most images')
print ('These cameras timed out ', timed_out_cams)