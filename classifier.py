


import numpy as np
from tensorflow.keras.layers import Dense
import cv2

model = load_model('tumor_model.h5')

def preprocess_image(img):
    img_resized = cv2.resize(img, (128, 128))
    img_resized = img_resized / 255.0
    return np.expand_dims(img_resized, axis=(0, -1))

def predict(img):
    input_img = preprocess_image(img)
    pred = model.predict(input_img)
    return "Tumor" if pred[0][0] > 0.5 else "Normal"