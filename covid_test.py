import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from PIL import Image

# Function to load and preprocess a single image
def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.convert('L')
    img = img.resize((128, 128))
    img = np.array(img)
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)
    img = np.expand_dims(img, axis=3)
    return img

# Function to make predictions on new images
def predict_image(image_path, model):
    img = preprocess_image(image_path)
    prediction = model.predict(img)
    predicted_class = 'COVID' if prediction > 0.5 else 'Normal'
    return predicted_class

# Load the trained model
model = tf.keras.models.load_model("covid_model.h5")

# Example usage: Replace 'image_path' with your image file path "C:\Desktop\Mini\covid19_ct\test\non-covid\Non-COVID-19_643.png"
image_path = "C:/Desktop/Mini/covid19_ct/test/non-covid/Non-COVID-19_643.png"
predicted_class = predict_image(image_path, model)
print(f"The predicted class for the image is: {predicted_class}")