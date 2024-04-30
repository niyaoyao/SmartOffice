import cv2
import numpy as np
from PIL import Image
import os

def train_face_recognizer():
    """
    Train a face recognizer using images from the 'dataset' directory and save the trained model.

    Returns:
    None
    """
    dataset_path = '/Users/qimingyang/Documents/jh2/smartOffice/smartOffice/smartOfficeFlask/face_recongnition/dataset'
    output_path = '/Users/qimingyang/Documents/jh2/smartOffice/smartOffice/smartOfficeFlask/face_recongnition/trainer/trainer.yml'

    # Load face data
    detector = cv2.CascadeClassifier("/Users/qimingyang/Documents/jh2/smartOffice/smartOffice/smartOfficeFlask/face_recongnition/haarcascade_frontalface_default.xml")
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    image_paths = [os.path.join(dataset_path, f) for f in os.listdir(dataset_path)]
    face_samples = []
    ids = []

    for image_path in image_paths:
        PIL_img = Image.open(image_path).convert('L')  # Convert image to grayscale
        img_numpy = np.array(PIL_img, 'uint8')

        label = int(os.path.split(image_path)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)

        for (x, y, w, h) in faces:
            face_samples.append(img_numpy[y:y + h, x:x + w])
            ids.append(label)

    # Train the recognizer
    print("\n[INFO] Training faces. Please wait...")
    recognizer.train(face_samples, np.array(ids))

    # Save the trained model
    recognizer.write(output_path)

    print("\n[INFO] {0} faces trained. Model saved at: {1}".format(len(np.unique(ids)), output_path))

    return 'trainSuccess'

if __name__ == "__main__":
    train_face_recognizer()
