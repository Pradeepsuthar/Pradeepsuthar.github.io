import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
img = cv2.imread('pexels-photo-614810.jpeg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img,1.3,5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('DetectFaces',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    


