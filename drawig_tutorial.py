import cv2

img = cv2.imread('/Users/sheugumbie/Projects/OpenSource/opencv/opencv/samples/data/lena.jpg', -1)

img = cv2.rectangle(img, (20,20), (255,255), (0, 0, 255), 5)
cv2.imshow("My First Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()