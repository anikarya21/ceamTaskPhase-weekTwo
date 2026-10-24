import cv2 as cv
import numpy as np

img = cv.imread('road.jpg')
cv.imshow('ROAD',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY',gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

blur = cv.GaussianBlur(gray, (7,7), 0)
cv.imshow('BLUR', blur)

edge = cv.Canny(blur, 200, 255)
cv.imshow('CANNY EDGE', edge)

mask = cv.inRange(cv.GaussianBlur(hsv, (9,9), 0), np.array([0,0,110]), np.array([60,60,200]))
result = cv.bitwise_and(hsv, hsv, mask=mask)
cv.imshow('MASKED', result)

contours, hierarchy = cv.findContours(edge, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, -1, (0,0,255), 3)
cv.imshow('CONTOURS IMG', img)

cv.waitKey(0)