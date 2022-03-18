import cv2
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os



#this is the way to open an image using Opencv Lib
#cv2.IMREAD_UNCHANGED to open the image as it is
#include the image file in the project folder

img = cv2.imread("Mecca.jpeg", cv2.IMREAD_UNCHANGED )

#Note!
#OpenCV uses BGR image format. So, when we read an image using cv2.
#imread() it interprets in BGR format by default.
#We can use cvtColor() method to convert a BGR image to RGB and vice-versa
#But since we can convert direcrtly from BGR to HSV so...

#Converting from BGR/RGB to HSV/HSI
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#This creates a GUI window with a title name of your choice

#cv2.imshow("HSV Mecca",hsv_img)
#cv2.imshow("RGB Mecca", img)

#specified number is the time in milliseconds
#if you pass 0 as an argument it will not close unless you do so

#cv2.waitKey(0)

#cv2.destroyAllWindows()

#Accessing a single pixel value in OpenCV
#In our case we are going to access the Voxel since it has 3-channels
print(f"This is the value of voxel at (0,0): {img[0,0]} for the BGR Image")
print(f"This is the value of voxel at (0,0): {rgb_img[0,0]} for the RGB Image")
print(f"This is the value of voxel at (0,0): {hsv_img[0,0]} for the HSV Converted Image")

root = Tk()
root.geometry("800x600+300+150")
root.resizable(width=True,height=True)
myLabel = Label(root,text="IP Homework1")
myLabel.pack()

root.mainloop()