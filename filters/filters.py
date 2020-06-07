# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 16:56:53 2020

@author: vgadi
"""
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt


"""
the apply function has the paramters:
1) img (string): the image name
2) filter (string) : the filter to be applied ('median', 'gaussian', 'average'). default is 'average'
3) kernel_size (int) : the size of the kernel which would be used for convolution. default size is 5
4) display (bool): if set to true, displays the image. default false
5) read_method (int): how the image is going to be read. 1 for color, 0 for grayscale, -1 for unchanged. default 1
6) flip_scheme (bool): if set to true, flips the color scheme, that is black becomes white and vice a versa
    
returns: a numpy.ndarray
"""

def apply_filter(img_name,
                 filter = 'average',
                 kernel_size = 5, 
                 display = False,
                 read_method = 1,
                 flip_scheme = False
                 ):
    # get image
    try:    
        img = cv2.imread(img_name, read_method)
        if flip_scheme == True:
            img = cv2.bitwise_not(img)
        """
        if conv2BW == True:
            try:
                img = rgb2gray(img)
            except:
                print("\An error occurred while saving the image in grayscale format. Applying the filters in RGB format.")
        """
        try:
            # apply the filters
            if filter == 'average':
                blur = cv2.blur(img, (kernel_size, kernel_size))
    
            elif filter == 'gaussian':
                blur = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)
    
            elif filter == 'median':
                blur = cv2.medianBlur(img, kernel_size)
            else:
                print("\nIncorrect filter entered.")
                return img
            
    
            # if the filters can be applied, then display the image
            try:
                if display == True:
                    plt.subplot(121),plt.imshow(img),plt.title('Original')
                    plt.xticks([]), plt.yticks([])
                    plt.subplot(122),plt.imshow(blur),plt.title(filter)
                    plt.xticks([]), plt.yticks([])
                    plt.show()
                
            # in case the image cannot be displayed
            except:
                print("\nAn error occurred while displaying the image.")
        # in case the filtering process cannot be carried out
        except:
            print("\nThe kernel size is larger than the image dimensions.")
            return img
    # the file does not exist
    except:
        print("\nThe file does not exist in the directory.")
        return -1
        
    return blur
