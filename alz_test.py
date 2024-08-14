import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Function to predict the class of an image
def predict_image_class(image_path, model_path):
    model = tf.keras.models.load_model(model_path)
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Rescale pixel values to [0, 1]
    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction)
    class_labels = ['Mild Impairment', 'Moderate Impairment', 'No Impairment', 'Very Mild Impairment']
    predicted_class = class_labels[predicted_class_index]
    return predicted_class

# Example usage:
image_path = 'C:/Desktop/Mini/alz_no2.jpg'
model_path = 'alzheimers_model.keras'  # Specify the path to your image
predicted_class = predict_image_class(image_path, model_path)
print("Predicted class:", predicted_class)
