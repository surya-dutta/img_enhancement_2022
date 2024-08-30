import numpy as np
import cv2
from glob import glob
import re

def singleScaleRetinex(img,variance):
    retinex = np.log10(img) - np.log10(cv2.GaussianBlur(img, (0, 0), variance))
    #cv2.imshow("reddd",retinex)
    return retinex

def multiScaleRetinex(img, variance_list):
    retinex = np.zeros_like(img)
    for variance in variance_list:
        retinex += singleScaleRetinex(img, variance)
    retinex = retinex / len(variance_list)
    return retinex

   

def MSR(img, variance_list):
    img = np.float64(img) + 1.0
    img_retinex = multiScaleRetinex(img, variance_list)
   
    for i in range(img_retinex.shape[2]):
        unique, count = np.unique(np.int32(img_retinex[:, :, i] * 100), return_counts=True)
        
        for u, c in zip(unique, count):
            if u == 0:
                zero_count = c
                break            
        low_val = unique[0] / 100.0
        high_val = unique[-1] / 100.0
        for u, c in zip(unique, count):
            if u < 0 and c < zero_count * 0.1:
                low_val = u / 100.0
            if u > 0 and c < zero_count * 0.1:
                high_val = u / 100.0
                break            
        img_retinex[:, :, i] = np.maximum(np.minimum(img_retinex[:, :, i], high_val), low_val)
        
        img_retinex[:, :, i] = (img_retinex[:, :, i] - np.min(img_retinex[:, :, i])) / \
                               (np.max(img_retinex[:, :, i]) - np.min(img_retinex[:, :, i])) \
                               * 255
    img_retinex = np.uint8(img_retinex)        
    return img_retinex



def SSR(img, variance):
    img = np.float64(img) + 1.0
    
    img_retinex = singleScaleRetinex(img, variance)
    #print(np.unique(np.int32(img_retinex[:,:,0]*100)))
    
    for i in range(img_retinex.shape[2]):
        unique, count = np.unique(np.int32(img_retinex[:, :, i] * 100), return_counts=True)
        
        for u, c in zip(unique, count):
            if u == 0:
                zero_count = c
                break            
        low_val = unique[0] / 100.0
        high_val = unique[-1] / 100.0
        for u, c in zip(unique, count):
            if u < 0 and c < zero_count * 0.1:
                low_val = u / 100.0
            if u > 0 and c < zero_count * 0.1:
                high_val = u / 100.0
                break            
        img_retinex[:, :, i] = np.maximum(np.minimum(img_retinex[:, :, i], high_val), low_val)
        
        img_retinex[:, :, i] = (img_retinex[:, :, i] - np.min(img_retinex[:, :, i])) / \
                               (np.max(img_retinex[:, :, i]) - np.min(img_retinex[:, :, i])) \
                               * 255
        
    img_retinex = np.uint8(img_retinex)        
    return img_retinex


variance_list=[15, 80, 30]
variance=300
filenames = glob(r"C:\Users\vsidd\Desktop\python\CAPSTONE\INPUT IMAGES\*.jpg")
#filenames.sort()
filenames = sorted(filenames, key=lambda x:float(re.findall("(\d+)",x)[0]))
images = [cv2.imread(img) for img in filenames]
i=1
for img in images:
    lab = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
    L,A,B=cv2.split(lab)
    
    img_m=MSR(img,variance_list)
    img_s=SSR(img, variance)
    #img_msr=cv2.merge([img_m,A,B])
    #img_ssr=cv2.merge([img_s,A,B])
    #img_msr=cv2.cvtColor(img_m,cv2.COLOR_LAB2BGR)
    #img_ssr=cv2.cvtColor(img_s,cv2.COLOR_LAB2BGR)
    img_msr = cv2.bilateralFilter(img_m, 5, 60, 60)
    img_ssr=cv2.bilateralFilter(img_s, 5, 60, 60)
    cv2.imwrite('SSR' +str(i)+ '.jpg', img_ssr)
    cv2.imwrite('MSR' +str(i)+ '.jpg',img_msr)
    i+=1

    
##img = cv2.imread('image11.jpg')
##img_msr=MSR(img,variance_list)
##img_ssr=SSR(img, variance)
##
##cv2.imshow('Original', img)
##cv2.imshow('MSR', img_msr)
##cv2.imshow('SSR', img_ssr)
##cv2.imwrite('SSR.jpg', img_ssr)
##cv2.imwrite('MSR.jpg',img_msr)


##cv2.waitKey(0)
##cv2.destroyAllWindows()
