#!/usr/bin/bash
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py 
python3 -m pip install flask
rm get-pip.py
