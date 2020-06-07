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
2) img_type (string): the image can be saved in two formats ('RGB', 'grayscale').
3) edit_name (string): the filename of the saved image default 'image'
4) extension (string): the extension of the image file. default '.jpg'
5) show (bool): whether to display the image. default false
    
returns: nothing
"""

def save_image(img, img_type, edit_name = 'image',extension = '.jpg', show = False):
    try:
        if img_type == 'rgb':
            img_new = Image.fromarray(img, 'RGB')
        if img_type == 'grayscale':
            img_new = Image.fromarray(img, 'L')
            
    except:
        print("\nThe numpy.ndarray cannot be converted to an image")
        return img
    edit_name += extension
    try: 
        img_new.save(edit_name)
    except:
        print("\nAn error occurred while saving the image.")
    if show == True:
        try:
            img_new.show()
        except:
            print("\nAn error occurred while displaying the image.")
