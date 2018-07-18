import time
import random
import atexit
from flask import Flask, render_template, request, Response
app = Flask(__name__)

MAX_IMAGES_PER_CAMERA = 1000
NUM_CAMERAS = 1000

image_chunk_template = '{{"file_size": {}}}'
camera_chunk_template = '{{"camera_id": {}, "images": [{}]}}'

@app.route("/camera/<id>")
def getCamera(id):
	if int(id) < 1 or int(id) > NUM_CAMERAS:
		return Response(status=404)
	# randomly sleep to simulate slow requests or timeouts
	slow_cam = random.randint(1, NUM_CAMERAS)
	print(slow_cam)
	if(slow_cam % 5 == 0):
		print('simulating slow or dropped request')
		time.sleep(60)
	
	# now randomly generate the response json
	image_chunk = ""
	num_images = random.randint(1, MAX_IMAGES_PER_CAMERA)
	# print(num_images)
	for image in range(num_images+1):
		# print(image)
		image_size = random.randint(1, 100000)
		image_chunk += image_chunk_template.format(image_size) + (", " if (image < num_images) else "")

	camera_chunk = camera_chunk_template.format(id, image_chunk)
	return Response(response=camera_chunk, mimetype="application/json")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)
