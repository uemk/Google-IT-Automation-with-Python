#!/usr/bin/env python3

import os
import glob
from PIL import Image

PATH = "supplier-data/images/"


def change_image(source_dir, dest_dir):
    error = False
    try:
        if not os.path.exists(source_dir):
            raise FileExistsError
        if not os.path.isdir(source_dir):
            raise NotADirectoryError

        for image in glob.glob(source_dir + '*.tiff'):
            base = os.path.basename(image)
            name = os.path.splitext(base)[0]

            with Image.open(image) as img:
                if img.mode != 'RGB':
                    img = img.convert('RGB')

                new_img = img.resize((600, 400))
                new_img.save(dest_dir + name + '.jpeg', 'JPEG')

    except FileExistsError:
        print(f"[Error] Not such directory: '{source_dir}'")
        error = True
    except NotADirectoryError:
        print(f"[Error] '{source_dir}' is a file, not a directory")
        error = True
    except FileNotFoundError:
        print(f"[Error] Not such directory: '{dest_dir}'")
        error = True
    except PermissionError:
        print(f"[Error] Permission denied to write in directory: '{dest_dir}'")
        error = True
    finally:
        pass

    if not error:
        print("Image transformation finished successfully")


change_image(PATH, PATH)

