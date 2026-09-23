import cv2 
import numpy as np


img = np.zeros((512, 512, 3), np.uint8)
img[:] = [255, 2, 255]


# cv2.line(img, (10,10), (10,100),(233,45,56),5)

cv2.rectangle(img, (20,20), (430,490), (0,255,0), 3)
cv2.rectangle(img, (50,50), (390,450), (0,255,0), 3)
cv2.rectangle(img, (80,80), (350,410), (0,255,0), 3)
cv2.rectangle(img, (110,110), (310,370), (0,255,0), 3)
cv2.rectangle(img, (140,140), (270,330), (0,255,0), 3)
cv2.rectangle(img, (170,170), (230,290), (0,255,0), 3)
# cv2.circle(img, (200,200) , 300, (30,250,255), 2)

# cv2.putText(img, "Banty kumar" , (180,500),cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
img2=np.hstack((img,img))
cv2.imshow('image', img2)
cv2.waitKey(0)