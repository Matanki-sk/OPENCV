import cv2 as cv
img = cv.imread("img/parrot.jpeg")
cv.imshow("madi",img)

grayimg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",grayimg)



cv.waitKey(0)