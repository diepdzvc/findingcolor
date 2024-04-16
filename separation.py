import cv2
import numpy as np

# Đọc ảnh và chuyển đổi sang không gian màu HSV
image = cv2.imread('D:\\xanhtest.jpg')
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)



# Chọn tọa độ pixel muốn phân tích
x = 100
y = 50

# Lấy giá trị màu của pixel tại tọa độ (x, y) trong không gian màu BGR
bgr_pixel = image[y, x]

# Chuyển đổi giá trị màu sang không gian màu HSV
hsv_pixel = cv2.cvtColor(np.uint8([[bgr_pixel]]), cv2.COLOR_BGR2HSV)[0][0]

# In giá trị màu của pixel
print("BGR Pixel Value:", bgr_pixel)
print("HSV Pixel Value:", hsv_pixel)
