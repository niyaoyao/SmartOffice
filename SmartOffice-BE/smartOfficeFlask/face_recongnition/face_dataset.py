

import cv2
import os



def getfaceDataSet(faceId):
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video width
    cam.set(4, 480)  # set video height

    face_detector = cv2.CascadeClassifier('/Users/qimingyang/Documents/jh2/smartOffice/smartOffice/smartOfficeFlask/face_recongnition/haarcascade_frontalface_default.xml')

    # For each person, enter one numeric face id
    face_id = faceId


    count = 0

    while True:

        ret, img = cam.read()
        # img = cv2.flip(img, -1) # flip video image vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1

            # Save the captured image into the datasets folder
            cv2.imwrite("/Users/qimingyang/Documents/jh2/smartOffice/smartOffice/smartOfficeFlask/face_recongnition/dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])


            print('第{}张训练集'.format(str(count)))
            # cv2.imshow('第{}张训练集'.format(str(count)), img)

        k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 30:  # Take 30 face sample and stop video
            break
    cam.release()
    return 'getSuccess'


if __name__ == '__main__':
    getfaceDataSet(3)