# -*- coding: utf-8 -*-
"""
Color space transform

RGB -> Gray

Created on Sat May  4 19:24:35 2019
@author: liangyu
"""

def rgb2gray(rgb_array):
    """
    G=0.30*R+0.59*G+0.11*B
    """
    r, g, b = rgb_array[:,:,0], rgb_array[:,:,1], rgb_array[:,:,2]
    gray_image = r*0.3 + g*0.59 + b*0.11
    
    return gray_image