import cv2
import numpy as np
def detect_colored_objects(frame):
    #chuyển từ hình ảnh BGR sang HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #xác định khoảng giá trị màu đỏ trong không gian HSV
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([9, 255, 255])
    #xác định khoảng giá trị màu vàng trong không gian HSV
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    #xác định khoảng giá trị màu xanh trong không gian HSV
    lower_blue = np.array([90, 100, 100])
    upper_blue = np.array([110, 255, 255])

    #taọ mask để chỉ giữ lại pixel có màu nằm trong vùng giá trị đã xác định
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_red = cv2.inRange(hsv, lower_red, upper_red)

    #tìm contours của các vùng màu vàng, xanh
    contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2. CHAIN_APPROX_SIMPLE)
    contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2. CHAIN_APPROX_SIMPLE)
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2. CHAIN_APPROX_SIMPLE)

    #duyet qua cac contours và vẽ bounding box cho chúng
    for contour in contours_yellow:
        area = cv2.contourArea(contour)
        if area > 200:
            x, y, w, h =cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x +w, y+h), (0, 255, 255), 2)#màu theo B-G-R
            cv2.putText(frame, "yellow", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
    for contour in contours_blue:
        area = cv2.contourArea(contour)
        if area > 200:
            x, y, w, h =cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x +w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, "blue", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)     
    for contour in contours_red:
        area = cv2.contourArea(contour)
        if area > 200:
            x, y, w, h =cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x +w, y+h), (0, 0, 255), 2)
            cv2.putText(frame, "red", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2) 
            return frame
def main():
    #mở kết nối web cam
    cap = cv2.VideoCapture(0)

    while True:
        #đọc frame từ webcam
        ret, frame = cap.read()
        #phát hiện vật có màu vàng, xanh,do
        colored_objects = detect_colored_objects(frame)
        #hiển thị frame gốc và frame sau khi phát hiện màu sắc
        cv2.imshow('Colored objects',colored_objects)
        #thoat khoi vong lap khi nhan q
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()  