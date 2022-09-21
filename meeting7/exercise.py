import cv2 
# Tambahkan code di bawah ini
import numpy as np

img = cv2.imread("exercise.jpg")


print(img.shape)
# Tambahkan dibawah code print(img.shape)

# img = cv2.resize(img, (300, 400)) diberi komentar
# img = cv2.resize(img, ( 0,0), fx=0.5, fy=0.5)
# Tambahkan code dibawah ini

# img = cv2.blur(img, (20,20))  

# img = cv2.boxFilter(img, -1, (10, 10)) 
# img = cv2.GaussianBlur(img, (201,201), 0)



# Tambahkan code sebelum show image
# cv2.imshow("Mask", mask) berikan komentar pada code ini
# Tambahkan code dibawah ini
height, width, channel = img.shape
print(width, height)
# Tambahkan code dibawah
# Tambahkan code dibawah
cv2.rectangle(img, (400, 260), (600, 400), (255,0,0), 3)
cv2.putText(img, "Laptop", (400, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0))
# Tambahkan code dibawah ini
cv2.circle(img, (390, 370), 60, (0,0,255), 3)
cv2.putText(img, "Coffe", (370, 300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
# Face
cv2.rectangle(img, (300, 20), (450, 160), (0,255,0), 3)
cv2.putText(img, "Face", (300, 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,255,0))



cv2.imshow("images", img)
cv2.waitKey(0)

