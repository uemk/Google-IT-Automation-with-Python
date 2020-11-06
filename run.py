#! /usr/bin/env python3

import os
import requests

PATH = "supplier-data/descriptions/"
URL = "http://localhost/fruits/"


def fruits_upload(url: str, path: str) -> None:
    """
    Posts data about fruits to a given url.
    :param url: url for uploading the data
    :param path: path to directory with text files holding fruit descriptions
    """
    for infile in os.listdir(path):
        if infile.endswith('.txt'):
            fruit = {}
            with open(path + infile, "r") as txt_file:
                fruit['name'] = txt_file.readline().strip('\n\r')
                fruit['weight'] = int(txt_file.readline().strip('\n\r').split(' ')[0])
                fruit['description'] = txt_file.readline().strip('\n\r')
                # to bind previously uploaded fruit image with fruit description
                fruit['image_name'] = infile.replace('.txt', '.jpeg')

                print(fruit)
                try:
                    response = requests.post(url, data=fruit)
                    print(response.status_code)
                    response.raise_for_status()
                except Exception as err:
                    print("ERROR: ", err)


fruits_upload(URL, PATH)
