import cv2 as cv
img = cv.imread("img/parrot.jpeg")
cv.imshow("madi",img)

grayimg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",grayimg)


dog = cv.imread("img/dog2.jpg")
cv.imshow("dog",dog)

#blur
blur = cv.GaussianBlur(dog,(7,7),cv.BORDER_DEFAULT)
cv.imshow("blur",blur)

#canny
out = cv.Canny(dog,50,50)
cv.imshow('outline',out)

#dialtung 
d = cv.dilate(out,(7,7),iterations = 2)
cv.imshow('dialated',d)

#eroding 
eroding = cv.erode(d,(7,7),iterations=3)
cv.imshow('eroding',eroding)

#resizing
resize = cv.resize(img ,(500,500))
cv.imshow('resized',resize)

#crop
crop = img[20:500,200:400]
cv.imshow('croped',crop)
cv.waitKey(0)