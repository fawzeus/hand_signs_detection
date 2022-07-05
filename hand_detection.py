from pickletools import uint8
import cv2
from cvzone.HandTrackingModule import HandDetector
import sys
import numpy as np
from math import ceil

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

OFFSET = 20
IMG_SIZE=300

while True:
    success,img = cap.read()
    hands,img = detector.findHands(img)
    
    if hands:
        try:
            white_img = np.ones((IMG_SIZE,IMG_SIZE,3),dtype=np.uint8)*255

            #corping the hand image
            hand = hands[0]
            x, y, w, h = hand['bbox']
            start_y,start_x,end_y,end_x = y,x,h,w
            h_img,w_img,_ = img.shape
            if y-OFFSET > 0:
                start_y = y-OFFSET
            if x-OFFSET > 0:
                start_x = x-OFFSET
            if y+h+OFFSET < h_img :
                end_y=y+h+OFFSET
            if x+w+OFFSET < w_img :
                end_x=x+w+OFFSET
            corped_img = img[start_y:end_y,start_x:end_x]

            #costumize the corped image size
            ASPET_RATIO = w/h
            if ASPET_RATIO > 1:
                zoom = IMG_SIZE/w
                new_h = ceil(zoom*h)
                custom_img = cv2.resize(corped_img,(IMG_SIZE,new_h))
                mid = (IMG_SIZE-new_h)//2

                white_img[mid:new_h+mid,:]= custom_img
            
            else:
                zoom = IMG_SIZE/h
                new_w = ceil(zoom*w)
                custom_img = cv2.resize(corped_img,(new_w,IMG_SIZE))
                mid = (IMG_SIZE-new_w)//2

                white_img[:,mid:new_w+mid]= custom_img

            #cv2.imshow("corped image",corped_img)
            cv2.imshow("white image",white_img)
        except:
            pass
        

        

    cv2.imshow("Live",img)
    k = cv2.waitKey(1)
    if k ==ord("q"):
        cv2.destroyAllWindows
        sys.exit(0)
