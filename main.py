# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 17:20:30 2020

@author: vgadi
"""

import filters
import img_io


img = "IMG_0624.JPG"

img_med = filters.apply_filter(img, filter = 'median', kernel_size = 5, display = True)
img_io.save_image(img_med, img_type = 'RGB', height = 3000 , width = 4000, edit_name = 'median_blur')


img_gauss = filters.apply_filter(img, filter = 'gaussian', kernel_size = 5, display = True)
img_io.save_image(img_gauss, img_type = 'RGB', height = 3000 , width = 4000, edit_name = 'gaussian_blur')


img_average = filters.apply_filter(img, filter = 'average', kernel_size = 5, display = True)
img_io.save_image(img_average, img_type = 'RGB',height = 3000 , width = 4000, edit_name = 'average_blur')

print(type(img))
