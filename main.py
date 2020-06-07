# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 17:20:30 2020

@author: vgadi
"""

import filters
import img_io
import canny_detector

img_name = "img.jpg"

img = filters.apply_filter(img_name, filter = 'average', display = True, read_method = 1, flip_scheme = True)
img_io.save_image(img, 'rgb', edit_name = 'flipped_blur_avg')


img = filters.apply_filter(img_name, filter = 'average', display = True, read_method = 1, flip_scheme = False)
img_io.save_image(img, 'rgb', edit_name = 'blur_avg')



img = filters.apply_filter(img_name, filter = 'gaussian', display = True, read_method = 1, flip_scheme = True)
img_io.save_image(img, 'rgb', edit_name = 'flipped_blur_gaussian')


img = filters.apply_filter(img_name, filter = 'gaussian', display = True, read_method = 1, flip_scheme = False)
img_io.save_image(img, 'rgb', edit_name = 'blur_gaussian')



img = filters.apply_filter(img_name, filter = 'median', display = True, read_method = 1, flip_scheme = True)
img_io.save_image(img, 'rgb', edit_name = 'flipped_blur_median')


img = filters.apply_filter(img_name, filter = 'median', display = True, read_method = 1, flip_scheme = False)
img_io.save_image(img, 'rgb', edit_name = 'blur_median')




img = filters.apply_filter(img_name, filter = 'gaussian', display = True, read_method = 1, flip_scheme = True)
img = canny_detector.auto_canny(img)
img_io.save_image(img, 'grayscale', edit_name = 'edge_flipped_blur_gaussian')


img = filters.apply_filter(img_name, filter = 'gaussian', display = True, read_method = 1, flip_scheme = False)
img = canny_detector.auto_canny(img)
img_io.save_image(img, 'grayscale', edit_name = 'edge_blur_gaussian')


img = filters.apply_filter(img_name, filter = 'gaussian', display = True, read_method = 1, flip_scheme = True)
img = canny_detector.auto_canny(img, method = 'mode')
img_io.save_image(img, 'grayscale', edit_name = 'edge_flipped_blur_gaussian_method_mode')


img = filters.apply_filter(img_name, filter = 'gaussian', display = True, read_method = 1, flip_scheme = False)
img = canny_detector.auto_canny(img, method = 'mode')
img_io.save_image(img, 'grayscale', edit_name = 'edge_blur_gaussian_method_mode')
