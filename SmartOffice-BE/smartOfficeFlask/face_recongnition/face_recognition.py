from PIL import Image
import io
import base64
import cv2
import numpy as np
from flask import jsonify

# Initialize face recognizer and other variables
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('/Users/qimingyang/Documents/jh2/smartOffice/smartOffice/smartOfficeFlask/face_recongnition/trainer/trainer.yml')
cascadePath = "/Users/qimingyang/Documents/jh2/smartOffice/smartOffice/smartOfficeFlask/face_recongnition/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
names = ['None', 'qmy', 'Paula', 'Ilza', 'Z', 'W']


def recognize_face(imageBase64):
    results = []
    for i in range(10):
        base64_data = imageBase64.replace("data:image/jpeg;base64,", "")

        # Decode Base64 data
        image_data = base64.b64decode(base64_data)

        # Load image data into PIL Image object
        image = Image.open(io.BytesIO(image_data))

        # Convert PIL Image object to numpy array
        image_np = np.array(image)

        # Encode image data to JPEG format
        _, buffer = cv2.imencode('.jpg', image_np)

        # Decode image data from memory buffer
        img = cv2.imdecode(buffer, cv2.IMREAD_COLOR)

        # Convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(30, 30)
        )

        # Recognize faces and append the result to the results list
        for (x, y, w, h) in faces:
            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            # Check if the face is recognized with a high confidence level
            if confidence < 100:
                print(id)
                name = names[id]
                results.append({'name': name})
            else:
                results.append({'name': 'Unknown'})

    return jsonify(results)

