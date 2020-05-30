import cv2

img = cv2.imread('/Users/sheugumbie/Projects/OpenSource/opencv/opencv/samples/data/lena.jpg', -1)

print(img)
cv2.imshow("My First Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()