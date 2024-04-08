import cv2 as cv

#IMG CAPTURE
"""
photo= cv.imread('img/parrot.jpeg')
cv.imshow('parrot',photo)
cv.waitKey(0)"""
#VDEO CAPTURE
def resizeframe(frame,scale=0.10):
    height=int(frame.shape[0]*scale)
    width=int(frame.shape[1]*scale)
    dimension=(width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
#IMG CAPTURE
photo= cv.imread('img/parrot.jpeg')
cv.imshow('parrot',photo)
photoresize=resizeframe(photo)
cv.imshow('resize',photoresize)
cv.waitKey(0)
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()
while True:
    isTrue, frame=cap.read()
    #frameresize = resizeframe(frame)
    cv.imshow('me',frame)
    #cv.imshow('resized',frameresize)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
cap.release()
cv.destroyAllWindows()
