import cv2
url= "http://10.165.24.99:8080/video"

cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Failed to open video stream")
else:
    while True:
        ret,frame = cap.read()
        if not ret:
            print("Failed to read frame")
            break
        cv2.imshow("Video Stream", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()