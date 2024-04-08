import cv2 as cv
import numpy as np

#zeros function creates blank block,datatype of the image is uint8

blank = np.zeros((500,500,3),dtype='uint8')
#cv.imshow('blank',blank)

#painting
#blank[:]=0,255,0
#cv.imshow('green',blank)

# drawing rectangle
#if thickness is filled it fils the shape with the color by cv.FILLed or -1
#cv.rectangle(blank,(0,0),(200,200),(0,250,0),thickness=2)

#cv.imshow('rectangle',blank)

# draw circle

#cv.circle(blank,(250,250),100,(0,0,255),thickness=-1)
#cv.imshow('circle',blank)
#draw a line 
#cv.line(blank,(0,250),(250,25),(255,255,255),thickness=2)
#cv.imshow('line',blank)

# WRITING TEXT
#cv.putText(blank,'Hey..! Its Matanki here :)',(2570,250),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255))
#cv.imshow('text',blank)

#blur
img = cv.imread('img/madi.jpg')
#cv.imshow('dog',img)


blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

cv.waitKey(0)