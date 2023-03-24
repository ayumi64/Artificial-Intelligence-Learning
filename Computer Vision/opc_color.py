import cv2 as cv

src = cv.imread("/Users/gaoyuhang/Project/Python/AI-Lab/page.png")

cv.imshow('BGR',src)
image = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imshow('gray_penguins',image)