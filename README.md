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