# -*- coding: utf-8 -*-
"""
二值图像形态学处理

ROI
binary threshold
dilate and erode
TODO:
开源到GitHub
自适应阈值二值化
连通域提取
连通成分标记
特征提取：欧拉数

@author: liangyu
Created on Wed May  1 19:05:16 2019
"""
import os
import numpy as np

from read_save import read_image, save_image
from colorspace_transform import rgb2gray


def cut_image(image_array, box):
    """
    """
    x_start, y_start, x_end, y_end = box[0], box[1], box[2], box[3]
    cut_image = image_array[y_start:y_end, x_start:x_end, :]

    return cut_image


def binary_threshold(gray_array, threshold):
    """
    """
    # TODO:
    # gray_array 是否为灰度图
    if threshold < 0 or threshold > 255:
        raise ValueError('threshold is not in 0~255 in binary_threshold.')
    
    width, heigth = gray_array.shape[0], gray_array.shape[1]
    binary_array = np.zeros((width, heigth), 'uint8')
    binary_array[gray_array <= threshold] = 0
    binary_array[gray_array > threshold] = 255

    return binary_array
    
    
def binary(gray_array):
    """
    TODO:
    自适应阈值二值化
    """
    
    return 


def dilate_or_erode(binary_array, kernel_size, mode):
    """
    膨胀 腐蚀
    """
    # TODO:
    # binary_array 是否为二值图像
    if kernel_size not in [3, 5]:
        raise ValueError('kernel_size is not 3 or 5 in dilate_or_erode.')
    
    if mode not in ['dilate', 'erode']:
        raise ValueError('mode is not \'dilate\' or \'erode\' in dilate_or_erode.')
        
    if kernel_size == 3:
        padding_size = 1
    else:
        padding_size = 2
    
    # padding
    padding_array = np.pad(binary_array, (padding_size, padding_size), 'constant')
    width, heigth = padding_array.shape[0], padding_array.shape[1]

    dst_array = np.zeros_like(binary_array) # dst_array
    
    for i in range(padding_size, width-padding_size):
        for j in range(padding_size, heigth-padding_size):
            kernel = padding_array[i-padding_size:i+padding_size+1, j-padding_size:j+padding_size+1]
            if mode == 'dilate':
                dst_array[i-padding_size, j-padding_size] = np.max(kernel)
            else:
                dst_array[i-padding_size, j-padding_size] = np.min(kernel)
    
    return dst_array
    
    
# main
if __name__ == '__main__':
    # image path
    project_path = "D:\\python\\image_process\\"
    data_path = "data\\"
    image_filename = "United States, North America_.jpg"
    roi_image_filename = "roi.bmp"
    gray_image_filename = "gray.bmp"
    binary_image_filename = "binary.bmp"
    dialte_image_filename_3 = "dialte_3.bmp"
    dialte_image_filename_5 = "dialte_5.bmp"
    erode_image_filename_3 = "erode_3.bmp"
    erode_image_filename_5 = "erode_5.bmp"
    dilate_erode_image_filename_3 = "dilate_erode_3.bmp"
    erode_dilate_image_filename_3 = "erode_dilate_3.bmp"

    
    # open image
    image_path = os.path.join(project_path, data_path, image_filename)
    ori_image = read_image(image_path)
    
    # roi
    x_start, y_start, x_end, y_end = 200, 100, 400, 200 # 图像左上角原点
    cut_box = (x_start, y_start, x_end, y_end)
    roi_image = cut_image(ori_image, cut_box)
    #save_image(os.path.join(project_path, data_path, roi_image_filename), roi_image)
    

    # RGB to gray image
    gray_image = rgb2gray(roi_image)
    #save_image(os.path.join(project_path, data_path, gray_image_filename), gray_image) 

    # gray to binary image
    threshold = 125
    binary_image = binary_threshold(gray_image, threshold)
    #save_image(os.path.join(project_path, data_path, binary_image_filename), binary_image)

    # dilate or erode
    dialte_image_3 = dilate_or_erode(binary_image, 3, 'dilate')
    #dialte_image_5 = dilate_or_erode(binary_image, 5, 'dilate')
    erode_image_3 = dilate_or_erode(binary_image, 3, 'erode')
    #erode_image_5 = dilate_or_erode(binary_image, 5, 'erode')
    
    dilate_erode_3 = dilate_or_erode(dialte_image_3, 3, 'erode') # dilate and erode
    erode_dilate_3 = dilate_or_erode(erode_image_3, 3, 'dilate') # erode and dilate

    save_image(os.path.join(project_path, data_path, dialte_image_filename_3), dialte_image_3)
    #save_image(os.path.join(project_path, data_path, dialte_image_filename_5), dialte_image_5)
    #save_image(os.path.join(project_path, data_path, erode_image_filename_3), erode_image_3)
    #save_image(os.path.join(project_path, data_path, erode_image_filename_5), erode_image_5)
    #save_image(os.path.join(project_path, data_path, dilate_erode_image_filename_3), dilate_erode_3)
    #save_image(os.path.join(project_path, data_path, erode_dilate_image_filename_3), erode_dilate_3)
