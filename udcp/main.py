import os
import numpy as np
import cv2
from RefinedTramsmission import Refinedtransmission
from getAtomsphericLight import getAtomsphericLight
from getGbDarkChannel import getDarkChannel
from getTM import getTransmission
from sceneRadiance import sceneRadianceRGB

if __name__ == '__main__':
    pass


img = cv2.imread(r"C:\Users\vsidd\Desktop\python\CAPSTONE\InputImages\shark.jpg")
blockSize = 9
GB_Darkchannel = getDarkChannel(img, blockSize)
AtomsphericLight = getAtomsphericLight(GB_Darkchannel, img)
transmission = getTransmission(img, AtomsphericLight, blockSize)
transmission = Refinedtransmission(transmission, img)
sceneRadiance = sceneRadianceRGB(img, transmission, AtomsphericLight)
cv2.imwrite( '_UDCP_TM.jpg', np.uint8(transmission* 255))
cv2.imwrite('_UDCP.jpg', sceneRadiance)


