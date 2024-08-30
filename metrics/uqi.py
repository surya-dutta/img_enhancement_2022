from sewar.full_ref import uqi
import cv2

im1 = cv2.imread("image.jpg")
im2=cv2.imread("_UDCP.jpg")
print(uqi(im1,im2))
