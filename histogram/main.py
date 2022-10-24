import cv2
import numpy as np

resim = cv2.imread("resim.jpg",0)

cv2.imshow("Image",resim)

hist_dizi = np.zeros(256)

str,stn = resim.shape

for i in range(str):
    for j in range(stn):
        a = resim[i,j]
        hist_dizi[a] = hist_dizi[a]+1

print(hist_dizi)

cv2.waitKey()


