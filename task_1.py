import cv2
image = cv2.imread("OIP.jpg.")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255), 3)

cv2.imshow("Найденные лица", image)
cv2.waitKey(0)
cv2.destroyAllWindows()