import cv2
import os
import numpy as n

thres = 0.5

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
cap.set(10,70)

img = 'pain peko/lena.png'

classNames = []
classfile = 'pain peko/test.names'
with open(classfile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = 'pain peko/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightPath = 'pain peko/frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightPath, configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)
 
while True:
    success,img = cap.read()
    classIds, confs, bbox = net.detect(img, confThreshold = thres)
    print(classIds,bbox) 

    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            cv2.rectangle(img,box,color=(0,255,0),thickness=2)
            cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
            cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
            cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    
    #if classIds == [[1]]:
        #print("person")

    cv2.imshow('Cutecumber Dectection Software', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    