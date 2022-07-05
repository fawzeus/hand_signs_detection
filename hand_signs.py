import cv2
from cvzone.HandTrackingModule import HandDetector
import sys
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

OFFSET = 20

while True:
    success,img = cap.read()
    hands,img = detector.findHands(img)
    if hands:
        try:
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
            
            cv2.imshow("corped image",corped_img)
        except:
            continue


    
    cv2.imshow("Live",img)
    k = cv2.waitKey(1)
    if k ==ord("q"):
        cv2.destroyAllWindows
        sys.exit(0)
