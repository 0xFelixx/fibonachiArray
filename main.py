import numpy as np
import cv2
import time

cv2.namedWindow("windows")

num = 17
color = 255
imSizeX = 1400
imSizeY = 700
x = 700
y = 350


arr = np.zeros(
(imSizeY,imSizeX,3),
"uint8"
)
for o in range(1000):

    fibo2 = 0
    fibo1 = 1
    fibo = fibo1 + fibo2

    eksx1 = x# ekstra x1 so we're able to go not go in minus and thereby fuck it up without fucking it up
    eksx2 = x
    eksy1 = y
    eksy2 = y

    if o % 2 == 0:
        color = 255
    if o % 2 == 1:
        color = 0


    for i in range(num):
        x1 = eksx1
        x2 = eksx2
        y1 = eksy1
        y2 = eksy2

        if x2 < 0:
            x2 = 0

        if x1 < 0:
            x1 = 0

        if y2 < 0:
            y2 = 0

        if y1 < 0:
            y1 = 0

        arr[y1 + 1:y2 + 1,x1 + 1:x2 + 1] = [0,color,0]

        if i % 4 == 0:
            eksy1 += fibo1
            eksx2 += fibo2
            eksy2 += fibo

        elif i % 4 == 1:
            eksx1 += fibo1
            eksy1 -= fibo2
            eksx2 += fibo

        elif i % 4 == 2:
            eksx1 -= fibo2
            eksy1 -= fibo
            eksy2 -= fibo1

        elif i % 4 == 3:
            eksx1 -= fibo
            eksx2 -= fibo1
            eksy2 += fibo2

        time.sleep(.1)

        fibo2 = fibo1 # Swapping around the variables
        fibo1 = fibo
        fibo = fibo1 + fibo2 # Calculating the next number in the fibonachi sequence

        cv2.imshow("windows", arr)
        key = cv2.waitKey(1)

        if key == 27:
            break
    if key == 27:
        break

time.sleep(5)
cv2.destroyWindows = cv2.destroyWindow
cv2.destroyWindows("windows")

