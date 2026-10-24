import cv2 as cv
import numpy as np

img = cv.imread('road.jpg')
cv.imshow('ROAD',img)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

h,s,v = cv.split(hsv)
cv.imshow('VALUE',v)

blur = cv.GaussianBlur(v, (7,7), 0) #Bilateral Filter is better
cv.imshow('BLUR',blur)

canny = cv.Canny(blur, 200, 255)
cv.imshow('CANNY EDGE', canny)

contour, hierarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contour, -1, (0,0,255), 4)
cv.imshow('CONTOURS IMG', img)

cv.waitKey(0)