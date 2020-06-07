# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 20:55:56 2020

@author: vgadi
"""

import numpy as np
import argparse # parser for cli options, args and sub commands
import glob     # Unix style pathname pattern expansion
import cv2
from scipy import stats

"""
the auto_canny function has the following parameters

1) image (numpy.ndarray): the image on which the edges would be detected. image should be black and white
2) sigma (int): a threshold value
3) method (string): the method which helps to calculate the lower and upper values. 'median', 'mode', 'mean'. default: 'median'
4) flip_scheme (bool): a flag, which if set, flips the color schema of the image

returns: numpy.ndarray
"""

def auto_canny(image, sigma = 0.33, method = 'median', flip_scheme = False):
    # the method used to calculate v
    try:
        if method == 'median':
            v = np.median(image)
        elif method == 'mean':
            v = np.mean(image)
        elif method == 'mode':
            v = stats.mode(image, axis = None)
            v = v[0]

        else:
            print("\nThe entered way of calculating the edge intensity is wrong.")
            return image
       
    except:
        print('\nAn error occurred while calculating ' + method + ' of the flattened image array.')
        return image
    
    # apply automatic canny detection ising the computed method
    
    lower = int(max(0, (1.0 - sigma)*v))
    upper = int(min(255, (1.0 + sigma)*v))
    
    # apply canny edge detector
    try:
        edged = cv2.Canny(image, lower, upper)
    except:
        print("\nAn error occured while calling the cv2.Canny() method.")
        return image
    # change the background to white and the edges to black
    if flip_scheme == True:
        edged = cv2.bitwise_not(edged)
    
    return edged

