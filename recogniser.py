import cv2, numpy as np;
import sys

face_cas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0);

recognizer = cv2.face.LBPHFaceRecognizer_create();
print('Reading the saved model.....')
recognizer.read('trainer/trainer.yml');

print("Data Read Succesfully.")

id=0;
names={1:'user1',2:'user2',3:'user3'}
print("Searching..............")

font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, img = cap.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    faces = face_cas.detectMultiScale(gray, 1.2, 5);
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,100,0),2);
        id,conf=recognizer.predict(roi_gray)
        if(conf < 50):
            prob = "{:.2f}%".format(conf * 100)
            cv2.putText(img,names[id]+">"+prob,(x+20,y+20),font,0.5,(0,255,0),1)
            print(prob,names[id])
            continue

        else:
            cv2.putText(img,"Unknown"+">"+prob,(x+30,y+30),font,0.5,(0,0,255),1)
            print(prob,'Unknown, can not recognize')
            id = 'Unknown, can not recognize'
            break
        
       
    cv2.imshow('frame',img);
    
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break;

cap.release();
cv2.destroyAllWindows();
