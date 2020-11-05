#!/usr/bin/env python3
import requests
import glob

PATH = "supplier-data/images/"
URL = "http://localhost/upload/"

try:
    for image in glob.glob(PATH+'*.jpeg'):
        with open(image, 'rb') as opened:
            r = requests.post(URL, files={'file': opened})
except Exception as err:
    print(err)
