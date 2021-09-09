import cv2

frameWidth = 640
frameHeight = 480

# 0 = webcam
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

classNames = []
classfile = "coco.names"
with open(classfile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

print(classNames)

while True:
    success, img = cap.read()
    
    cv2.imshow("Cutecumber Dectection Software",img)
    
    #closes with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    