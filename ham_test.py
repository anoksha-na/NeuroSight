from keras.preprocessing import image
from keras.models import load_model
import numpy as np

def load_image(img_path, size=(224, 224)):
    img = image.load_img(img_path, target_size=size)
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = expanded_img_array / 255.
    return preprocessed_img

def predict_brain_condition(img_path, model_path):
    # Loads a saved model from the specified path
    model = load_model(model_path)

    # Loads and preprocesses an image from the specified path
    img = load_image(img_path)
    predictions = model.predict(img)

    if predictions[0][0] >= 0.5:
        return "Heamorrhage Condition"
    else:
        return "Normal Condition"

# Path to image file 
img_path = 'C:/Desktop/Mini/ham_n1.jpg' 

# Path to saved model file 
model_path = 'C:/Desktop/Mini/brain_heamorrhage_model.keras'

# Call the predict_brain_condition function with the image and model paths
prediction = predict_brain_condition(img_path, model_path)

# Print the prediction result
print(prediction)
