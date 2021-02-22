import numpy as np
import cv2
import time

cv2.namedWindow("windows")

num = 15
fibo2 = 0
fibo1 = 1
# fibo = 0
x1 = 300
x2 = 300
y1 = 200
y2 = 200
color = 255
imSizeX = 500
imSizeY = 500

arr = np.zeros(
(imSizeY,imSizeX,3),
"uint8"
)

for i in range(num):
    fibo = fibo1 + fibo2 # Calculating the next number in the fibonachi sequence

    arr[y1:y2,x1:x2] = [0,color,0]

    color -= 10

    if i % 4 == 0:
        y1 += fibo1
        x2 += fibo2
        y2 += fibo

    elif i % 4 == 1:
        x1 += fibo1
        y1 -= fibo2
        x2 += fibo

    elif i % 4 == 2:
        x1 -= fibo2
        y1 -= fibo
        y2 -= fibo1

    elif i % 4 == 3:
        x1 -= fibo
        x2 -= fibo1
        y2 += fibo2

    time.sleep(.5)

    fibo2 = fibo1 # Swapping around the variables
    fibo1 = fibo

    cv2.imshow("windows", arr)
    key = cv2.waitKey(1)

time.sleep(5)
cv2.destroyWindow("windows")
