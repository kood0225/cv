import cv2
import numpy as np



lena = cv2.imread('lena.bmp', 0)
img = np.asarray(lena)
row, col = img.shape
print(row, col)
print(lena)

for i in range(0, row//2):
    for j in range(0, col):
        img[i][j], img[row-i-1][j] = img[row-i-1][j], img[i][j]

print(img)
cv2.imwrite('upsidedown.png', img)

cv2.imshow('lena', img)
cv2.waitKey(0)
