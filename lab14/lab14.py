import cv2
import numpy as np
image = cv2.imread("TW.jpg")    #先讀取圖片
image2 = cv2.cvtColor(cv2.imread("TW.jpg"), cv2.COLOR_BGR2GRAY)#先讀取圖片，把圖片轉成灰色
imgInfo = image.shape
height = imgInfo[0]
width = imgInfo[1]
dst = np.zeros((height,width,3),np.uint8)#手動把圖片調成灰色
for i in range(0,height):
    for j in range(0,width):
        (b,g,r) = image[i,j]
        gray2 = (int(b)+int(g)+int(r))/3
        dst[i,j] = np.uint8(gray2)
_,gray3= cv2.threshold(image2, 245, 255, cv2.THRESH_BINARY) #將圖片弄成二值化的結果，因為原本會回傳兩個值，所以需要打_,
cv2.imshow('image2',dst)#顯示圖片
cv2.imshow("image1", image) #顯示圖片
cv2.imshow("image3", image2)#顯示圖片
cv2.imshow("image4", gray3)#顯示圖片
cv2.waitKey(0)             #等待 enter被按下
cv2.destroyAllWindows()    #關閉opencv開啟的視窗