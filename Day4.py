import cv2 

# Reading the Image
img = cv2.imread("img2.webp")
print(img.shape)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Reading Video
path = "video.mp4"
cap = cv2.VideoCapture(path)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed")
        break
    else:
        cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()