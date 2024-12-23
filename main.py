import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 0 para WebCam, 2 para OBS
cap = cv2.VideoCapture(0) # Este es el numero que hay que cambiar para cambiar la cama (ir probando 0, 1, 2...). 


while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('img', img)
    k = cv2.waitKey(30)
    if k == 27: #27 es la tecla ESC
        break

cap.release()