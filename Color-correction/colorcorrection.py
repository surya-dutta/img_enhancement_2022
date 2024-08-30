# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 11:38:31 2021

@author: vsidd
"""
import cv2
import math
import numpy as np
import sys

def apply_mask(matrix, mask, fill_value):
    masked = np.ma.array(matrix, mask=mask, fill_value=fill_value)
    return masked.filled()

def apply_threshold(matrix, low_value, high_value):
    low_mask = matrix < low_value
    matrix = apply_mask(matrix, low_mask, low_value)

    high_mask = matrix > high_value
    matrix = apply_mask(matrix, high_mask, high_value)

    return matrix
def simplest_cb(img, percent):
    out_channels = []
    channels = cv2.split(img)
    totalstop = channels[0].shape[0] * channels[0].shape[1] * percent / 200.0
    for channel in channels:
        bc = np.bincount(channel.ravel(), minlength=256)
        lv = np.searchsorted(np.cumsum(bc), totalstop)
        hv = 255-np.searchsorted(np.cumsum(bc[::-1]), totalstop)
        out_channels.append(cv2.LUT(channel, np.array(tuple(0 if i < lv else 255 if i > hv else round((i-lv)/(hv-lv)*255) for i in np.arange(0, 256)), dtype="uint8")))
    return cv2.merge(out_channels)


if __name__ == '__main__':
    img = cv2.imread("image.jpg")
    out = simplest_cb(img, 1)
    cv2.imshow("before", img)
    cv2.imshow("after", out)
    cv2.waitKey(0)
