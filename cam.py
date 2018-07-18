import asyncio
import aiohttp

REQUEST_TIMEOUT = 5
NUM_CAMERAS = 1000
DCS_URL = 'http://localhost:8888/camera/{}'

async def get_camera_info(camera_number, camera_info, timed_out_cams):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(DCS_URL.format(camera_number), timeout=REQUEST_TIMEOUT) as response:
                data = await response.json()
                #print(data)
                camera_info.append(data)
    except Exception as e:
        # retry?
        print('Camera ', camera_number, ' timed out')
        timed_out_cams.append(camera_number)


def analyse_camera_info(camera_info, timed_out_cams):
    max_data_cam = 0
    max_images_cam = 0
    max_images = 0
    max_data = 0
    cam_largest_image = 0
    cam_largest_image_size = 0
    # cam_info = cam_response.json()
    cam_data_size = 0

    for cam_no in range(len(camera_info)):
        # check if this camera has more no. of images than any previous ones
        if len(camera_info[cam_no]['images']) > max_images:
            max_images = len(camera_info[cam_no]['images'])
            max_images_cam = camera_info[cam_no]['camera_id']

        # now add up all the image sizes from this camera
        for image in range(len(camera_info[cam_no]['images'])):
            cam_data_size += camera_info[cam_no]['images'][image]['file_size']
            if camera_info[cam_no]['images'][image]['file_size'] > cam_largest_image_size:
                cam_largest_image_size = camera_info[cam_no]['images'][image]['file_size']
                cam_largest_image = image
        
        print ('For camera ', camera_info[cam_no]['camera_id'], ' largest image is ' , cam_largest_image, ' of size ', cam_largest_image_size)
        
    if cam_data_size > max_data:
        max_data = cam_data_size
        max_data_cam = camera_info[cam_no]['camera_id']

    print ('========== SUMMARY ==========')
    print ('Camera ', max_data_cam, ' has used most data')
    print ('Camera ', max_images_cam, ' has most images')
    print ('These cameras timed out ', timed_out_cams)

timed_out_cams = []
camera_info = []
loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(
        *(get_camera_info(cam_no, camera_info, timed_out_cams) for cam_no in range(1, NUM_CAMERAS+1))
    )
)
#print(camera_info)
analyse_camera_info(camera_info, timed_out_cams)

    #print(cam_response.json()['images'][0]['file_size'])
    #print(len(cam_response.json()['images']))

