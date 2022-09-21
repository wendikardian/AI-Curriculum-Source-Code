import cv2 
# Tambahkan code di bawah ini
import numpy as np

img = cv2.imread("avanger.jpg")


print(img.shape)
# Tambahkan dibawah code print(img.shape)

# img = cv2.resize(img, (300, 400)) diberi komentar
img = cv2.resize(img, ( 0,0), fx=0.5, fy=0.5)
# Tambahkan code dibawah ini

# img = cv2.blur(img, (20,20))  

averaging = cv2.boxFilter(img, -1, (21, 21)) 
GaussianBlur = cv2.GaussianBlur(img, (21,21), 0)
cv2.imshow("Averaging", averaging)
cv2.imshow("Gaussian", GaussianBlur)

mask = np.zeros(img.shape[:2], dtype="uint8")
cv2.circle(mask, (160,200), 165, 255, -1)
img = cv2.bitwise_and(img, img, mask = mask)

# Tambahkan code sebelum show image
# cv2.imshow("Mask", mask) berikan komentar pada code ini
# Tambahkan code dibawah ini
height, width, channel = img.shape
cv2.line(img, (0,0), (width, height), (0,255,0), 6)
# Tambahkan code dibawah
cv2.line(img, (width,0), (0, height), (55,200,255), 3)
# Tambahkan code dibawah
cv2.rectangle(img, (0, 300), (width, height), (255,0,0), 5)
cv2.rectangle(img, (0, 0), (width, 100), (0,255,0), -1)
# Tambahkan code dibawah ini
cv2.circle(img, (100, 100), 40, (0,0,255), -1)
cv2.circle(img, (100, 100), 20, (255,255,255), -1)
cv2.circle(img, (250, 100), 40, (0,0,255), -1)
cv2.circle(img, (250, 100), 20, (255,255,255), -1)
# Tambahkan code dibawah
# red = ([0, 0, 30], [50, 56, 255])
# blue = ([30,0, 0], [255, 150, 50])
# green = ([0, 30, 0], [100, 255, 100])
# white = ([255, 255, 255], [255, 255, 255])
# boundaries = [red,blue,green,white]
# for (lower, upper) in boundaries:
# 	lower = np.array(lower, dtype = "uint8")
# 	upper = np.array(upper, dtype = "uint8")
# 	# cv2.imshow("Lower", lower)
 
# 	mask = cv2.inRange(img, lower, upper)
# 	output = cv2.bitwise_and(img, img, mask = mask)
# 	cv2.imshow("Color Detection", output)
# 	cv2.waitKey(0)

cv2.imshow("images", img)
cv2.waitKey(0)

