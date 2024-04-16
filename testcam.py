import cv2
cap = cv2.VideoCapture(0)# cam mac dinh may tinh
while True:
    _, image = cap.read()#dấu _ :true hoặc false

    cv2.imshow("nude show", image)
    if cv2.waitKey(1) == ord('x'):
        break