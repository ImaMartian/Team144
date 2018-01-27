#!/bin/sh
# launcher.sh
# navigate to home directory, then execute python script, then back home

cd /
cd /home/pi/Git/pixy/build/libpixyusb_swig
sudo python VisionPixy1.py
cd /
