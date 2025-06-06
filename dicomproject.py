# -*- coding: utf-8 -*-
"""DicomProject.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Oz546-c4YJeJbKfkQSltovva2L0NUn92
"""

# train_model.py
import os
import numpy as np
import cv2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split


import kagglehub

# Download latest version
path = kagglehub.dataset_download("navoneel/brain-mri-images-for-brain-tumor-detection")

print("Path to dataset files:", path)

IMG_SIZE = 128
DATA_DIR = path  # Replace with actual path
CATEGORIES = ["yes", "no"]

def load_data():
    data = []
    for category in CATEGORIES:
        path = os.path.join(DATA_DIR, category)
        label = 1 if category == "yes" else 0
        for img_name in os.listdir(path):
            try:
                img_path = os.path.join(path, img_name)
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
                data.append((img, label))
            except Exception as e:
                print(f"Error: {e}")
    return data

# Load and shuffle data
data = load_data()
np.random.shuffle(data)

X = np.array([i[0] for i in data]).reshape(-1, IMG_SIZE, IMG_SIZE, 1) / 255.0
y = np.array([i[1] for i in data])

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 1)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])

# Train
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Save
model.save("tumor_model.h5")
print("Model saved as tumor_model.h5")