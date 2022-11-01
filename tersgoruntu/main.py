import cv2
import numpy as np

foto = cv2.imread("gunes.jpg")
cv2.imshow("gunes",foto)

resim = cv2.imread("gunes.jpg",0)

cv2.imshow("grey",resim)





str,stn = resim.shape

for i in range(str):
    for j in range(stn):
        resim[i,j] = np.max(resim) - resim[i,j]

cv2.imshow("ters",resim)



cv2.waitKey()