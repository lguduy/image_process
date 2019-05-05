# -*- coding: utf-8 -*-
"""
Read and save image

@author: liangyu
Created on Sat May  4 19:19:02 2019
"""
from scipy import misc


def read_image(image_path):
    """
    """
    return misc.imread(image_path)


def save_image(path, array):
    """
    仅支持保存为无损格式，如：png, bmp
    """
    misc.imsave(path, array) # imsave基于PIL.Image实现

