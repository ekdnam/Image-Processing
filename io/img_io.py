# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 17:53:09 2020

@author: vgadi
"""

from PIL import Image
import numpy as np
import io


"""
the save_image function has the following parameters:
1) img (numpy.ndarray): the matrix that would be converted to an image
2) img_type (string): the image can be saved in two formats ('RGB', 'grayscale'). currently only 'RGB' supported.
3) height (int): the height of the saved image
4) width (int): the width of the saved image
5) edit_name (string): the filename of the saved image default 'image'
6) extension (string): the extension of the image file. default '.jpg'
7) show (bool): whether to display the image. default false
"""

def save_image(img, height, width, img_type, edit_name = 'image',extension = '.jpg', show = False):
    try:
        if img_type == 'RGB':
            img = Image.fromarray(img, img_type)
        if img_type == 'grayscale':
            img = Image.fromarray(img, 'L')
            
    except:
        print("\nThe numpy.ndarray cannot be converted to an image")
    edit_name += extension
    try: 
        img.save(edit_name)
    except:
        print("\nAn error occurred while saving the image.")
    if show == True:
        try:
            img.show()
        except:
            print("\nAn error occurred while displaying the image.")
