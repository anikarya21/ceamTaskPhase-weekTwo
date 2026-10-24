import cv2 as cv
import numpy as np

img = cv.imread('road.jpg')
cv.imshow('ROAD',img)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

h,s,v = cv.split(hsv)
# cv.imshow('HUE',h)
# cv.imshow('SATURATION',s)
# cv.imshow('VALUE',v)

blur = cv.GaussianBlur(v, (7,7), 1) #Bilateral Filter is better
cv.imshow('BLUR', blur)

canny = cv.Canny(blur, 220, 255)
cv.imshow('CANNY EDGE', canny)

blurSat = cv.GaussianBlur(s, (7,7), 1)

mask = cv.inRange(blur, 180, 255)
result = cv.bitwise_and(hsv, hsv, mask=mask)
cv.imshow('MASKED', result)

maskSat = cv.inRange(blurSat, 0, 50)
resultSat = cv.bitwise_and(hsv, hsv, mask=maskSat)
cv.imshow('MASKED SATURATION', resultSat)

resultmaskFinal = cv.bitwise_and(result, resultSat)
cv.imshow('FINAL MASKED', resultmaskFinal)

cv.waitKey(0)