import cv2
logo = cv2.imread('F:\\opcd_xx\\ldh\\3_1.jpg')
logo = cv2.imread('F:\\opcd_xx\\ldh\\3_1.jpg')


zrn = cv2.imread("F:\\opcd_xx\\ldh\\3_1.jpg")
print("图片类型",type(zrn))
print(zrn.shape)
blue = logo[190,168,0]
green=logo[190,168,1]
red=logo[190,168,2]
print(blue,green,red)











































# logo = cv2.imread('3_1.jpg')
# blue=logo[190,168,0]
# green=logo[190,168,1]
# red=logo[190,168,2]
# print(blue,green,red)