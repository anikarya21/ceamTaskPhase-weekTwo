# TASK ceamTaskPhase-weekTwo

    This is for Ceam Task Phase - Week 2 assignments.

<br>

## Whole Pipeline
    - Load BGR static images
    - Convert BGR to HSV
    - Convert BGR to GRAY
    - Apply Gaussian Blur to GRAY and HSV
    - Apply Canny Edge Detection to GRAY
    - Mask layer of Gaussian Blur (HSV)
    - Mask the layer onto the image (HSV)
    - Contours of Canny Edge
    - Draw the Contours on the BGR image.

<br>

## BGR Image
```
img = cv.imread('road.jpg')
cv.imshow('ROAD',img)
```
<img src='road.jpg' width=50% height=50%>

<br>

## HSV Image
```
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)
```
<img src='hsv.png' width=50% height=50%>

<br>

## GRAY Image
```
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY',gray)
```
<img src='gray.png' width=50% height=50%>

<br>

## Gaussian Blur Image (GRAY)
```
blur = cv.GaussianBlur(gray, (7,7), 0)
cv.imshow('BLUR', blur)
```
<img src='blur.png' width=50% height=50%>

<br>

## Canny Edge Detection (BGR)
```
edge = cv.Canny(blur, 200, 255)
cv.imshow('CANNY EDGE', edge)
```
<img src='edge.png' width=50% height=50%>

<br>

## Masked Image (HSV) - Color Filters
```
mask = cv.inRange(cv.GaussianBlur(hsv, (9,9), 0), np.array([0,0,110]), np.array([60,60,200]))
result = cv.bitwise_and(hsv, hsv, mask=mask)
cv.imshow('MASKED', result)
```
<img src='maskedHsv.png' width=50% height=50%>

<br>

## Contours Drawn on Image (BGR)
```
contours, hierarchy = cv.findContours(edge, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, -1, (0,0,255), 3)
cv.imshow('CONTOURS IMG', img)
```
<img src='contours.png' width=50% height=50%>

<br>

### OTHER REFERENCES
[README.md - Youtube](https://www.youtube.com/watch?v=jeOfS90Flf8)\
[HSV Colorspace - Youtube](https://www.youtube.com/watch?v=VvTA-yHhtQ4)\
[GRAYSCALE Transformation - Guide](https://medium.com/@niiicolai/digital-image-processing-grayscale-442461769fd2)\
[CONTOURS Detection - Guide](https://www.educative.io/answers/edge-detection-vs-contour-detection-in-computer-vision)


