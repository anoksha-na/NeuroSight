import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

def predict_chest_class(image_path, model_path):
    loaded_model = tf.keras.models.load_model(model_path)
    IMAGE_SIZE = (150, 150)
    
    img = image.load_img(image_path, target_size=IMAGE_SIZE)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0  # Rescale to [0,1]
    prediction = loaded_model.predict(img_array)
    if prediction[0][0] > 0.5:
        return "Squamous"
    else:
        return "Normal"

image_path = 'C:/Desktop/Mini/chest_ct/img/test/nor/cn4.png'
model_path = 'chest_ct_model.h5'  

prediction = predict_chest_class(image_path, model_path)
print("Prediction:", prediction)