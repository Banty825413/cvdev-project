import cv2

img = cv2.imread("Akbash 1.webp")
print(img)
# img2 = cv2.imread("Akbash 1.webp", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Color_Image", img)
# cv2.imshow("GreyImage", img2)
cv2.waitKey(0)