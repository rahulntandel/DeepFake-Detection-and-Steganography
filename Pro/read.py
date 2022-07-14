import cv2 as cv

img = cv.imread('photos/rahul.jpg')

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('GrayScale', gray)

cv.waitKey(0)

