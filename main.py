import cv2

# Window demensions 
frameWidth = 640
frameHeight = 480

# 0 = webcam
cap = cv2.VideoCapture(0)

cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    success, img = cap.read()
    cv2.imshow("Nicky is a boomer",img)
    #closes with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
