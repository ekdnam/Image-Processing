# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 17:53:09 2020

@author: vgadi
"""

from PIL import Image
import numpy as np
import io

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