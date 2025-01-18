import cv2
from matplotlib import pyplot as plt
# alt + j select mutiple strings
img1 = cv2.imread("image1.jpg")
# Alt + F12 terminal

img_gray = cv2.cvtColor(img1, cv2. COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img1, cv2. COLOR_BGR2RGB)

plt.subplot(1, 1, 1)
plt.imshow(img_rgb)
plt.show()

stop_data = cv2.CascadeClassifier('stop_data.xml')

found = stop_data.detectMultiScale(img_gray,)


class Object:
    def __init__(self, object, amount, number):
        self.amount = amount
        self.object = object
        self.number = number
