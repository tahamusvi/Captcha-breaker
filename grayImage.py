import cv2

# وارد کردن تصویر
img = cv2.imread('test/0.png')

# تبدیل تصویر به حالت طیف خاکستری
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# نمایش تصویر در حالت طیف خاکستری
cv2.imshow('Gray Image', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()