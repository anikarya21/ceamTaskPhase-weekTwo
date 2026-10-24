import cv2 as cv
import numpy as np

img = cv.imread('road.jpg')
cv.imshow('ROAD',img)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

h,s,v = cv.split(hsv)
cv.imshow('SATURATION',s)
cv.imshow('VALUE',v)

blurValue = cv.GaussianBlur(v, (7,7), 1) #Bilateral Filter is better
cv.imshow('BLUR VALUE', blurValue)

canny = cv.Canny(blurValue, 220, 255)
cv.imshow('CANNY EDGE', canny)

blurSaturation = cv.GaussianBlur(s, (7,7), 1)
cv.imshow('BLUR SATURATION', blurSaturation)

maskValue = cv.inRange(blurValue, 180, 255)
resultValue = cv.bitwise_and(hsv, hsv, mask=maskValue)
cv.imshow('MASKED VALUE', resultValue)

maskSaturation = cv.inRange(blurSaturation, 0, 50)
resultSaturation = cv.bitwise_and(hsv, hsv, mask=maskSaturation)
cv.imshow('MASKED SATURATION', resultSaturation)

resultFinal = cv.bitwise_and(resultValue, resultSaturation)
cv.imshow('FINAL MASKED', resultFinal)

cv.waitKey(0)