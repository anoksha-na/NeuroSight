import os
import numpy as np
#import matplotlib.pyplot as plt
from tensorflow import keras
from sklearn.model_selection import train_test_split
from PIL import Image

data_dir = "C:/Desktop/Mini/covid19_ct/train"

# Function to load images and labels
def load_data(data_dir):
    images = []
    labels = []
    for folder in os.listdir(data_dir):
        label = folder
        folder_path = os.path.join(data_dir, folder)
        for filename in os.listdir(folder_path):
            img = Image.open(os.path.join(folder_path, filename))
            img = img.convert('L')
            img = img.resize((128, 128))
            img = np.array(img)
            images.append(img)
            labels.append(label)
    return np.array(images), np.array(labels)

# Load the data
images, labels = load_data(data_dir)

# Normalize the images
images = images.astype('float32') / 255.0

# Convert labels to binary encoding
label_dict = {'covid': 1, 'non-covid': 0}
labels_encoded = np.array([label_dict[label] for label in labels])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(images, labels_encoded, test_size=0.2, random_state=42)

model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 1)),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(128, (3, 3), activation='relu'),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')  # Output layer with 1 neuron for binary classification
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train.reshape(-1, 128, 128, 1), y_train, epochs=50, batch_size=32, validation_split=0.2)

test_loss, test_accuracy = model.evaluate(X_test.reshape(-1, 128, 128, 1), y_test, verbose=2)
print(f"Test accuracy: {test_accuracy}")

# Save the model
model.save("covid_model.h5")

# Make predictions on new images
def predict_image(model, image_path):
    img = Image.open(image_path)
    img = img.convert('L')
    img = img.resize((128, 128))
    img = np.array(img)
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)
    img = np.expand_dims(img, axis=3)
    prediction = model.predict(img)
    predicted_class = 'COVID' if prediction > 0.5 else 'Normal'
    return predicted_class

# Example usage: Replace 'image_path' with your image file path
image_path = "C:/Desktop/Mini/covid19_ct/test/covid/COVID-19_7137.png"
predicted_class = predict_image(model, image_path)
print(f"The predicted class for the image is: {predicted_class}")