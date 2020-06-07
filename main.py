# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 17:20:30 2020

@author: vgadi
"""

import filters
import img_io


img = "IMG_0624.JPG"
"""
the apply function has the paramters:
1) img (string): the image name
2) filter (string) : the filter to be applied ('median', 'gaussian', 'average'). default is 'average'
3) kernel_size (int) : the size of the kernel which would be used for convolution. default size is 5
4) display (bool): if set to true, displays the image. default false
"""
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
img_med = filters.apply_filter(img, filter = 'median', kernel_size = 5, display = True)
img_io.save_image(img_med, img_type = 'RGB', height = 3000 , width = 4000, edit_name = 'median_blur')


img_gauss = filters.apply_filter(img, filter = 'gaussian', kernel_size = 5, display = True)
img_io.save_image(img_gauss, img_type = 'RGB', height = 3000 , width = 4000, edit_name = 'gaussian_blur')


img_average = filters.apply_filter(img, filter = 'average', kernel_size = 5, display = True)
img_io.save_image(img_average, img_type = 'RGB',height = 3000 , width = 4000, edit_name = 'average_blur')

print(type(img))
