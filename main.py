#bruh

# IMPORTS
##############################
# OpenCv Module 
import cv2
# Numpy Module
import numpy
# Direct Os Module
import os

# SET MAIN DIRECTORY TO FILE
##############################
directory_path = os.path.dirname(__file__)

# IMAGE
##############################
apple_file_path = os.path.join(directory_path, 'pic/apple.jpg')
apple_img = cv2.imread(apple_file_path)

# TESTING
##############################
print(type(img))
print("hello")

# Display
##############################
cv2.imshow('Original Image', img) 

cv2.waitKey(0)