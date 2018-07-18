# Overview
This repo is my response to the Osprey Infomatics coding challenge.

There are two python applications, dcs.py and cam.py

## dcs.py
This is the "Dummy Camera Service" application, using Flask. This simulates the camera information endpoint and returns random data for each camera that is queried. This also randomly simulates request timeouts.

## cam.py
This is the actual client application which queries all the cameras. It prints the following information:

    - Which cameras have used the most data?
    - Which cameras have the highest number of images?
    - What are the largest images per camera?

At the end, it also prints a list of cameras to which the requests timed out. This can be used to re-request their information.

To run:

```
# 1. clone the repo
git clone https://github.com/sandman0/osp_challenge.git

# 2. setup a virtualenv for this project
cd osp_challenge
python3 -m venv osp

# 3. activate the virtualenv
source osp/bin/activate

# 4. install required packages in the virtualenv
pip install flask aiohttp

# 5. run the dummy server in one terminal
python dcs.py

# repeat steps 2 and 3 in another terminal and run the camera client
python cam.py
```

On the server side, there are two constants (variables, really) which are configurable:

MAX_IMAGES_PER_CAMERA = 1000
NUM_CAMERAS = 1000

On the camera client side, there are three configuration variables:

REQUEST_TIMEOUT = 5 (in seconds)
NUM_CAMERAS = 1000
DCS_URL = 'http://localhost:8888/camera/{}'

