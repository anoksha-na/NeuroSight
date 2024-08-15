NeuroSight Analytics
NeuroSight Analyticsis is a web application designed to predict medical conditions from MRI and CT scan images using Convolutional Neural Networks (CNNs). The application features a responsive and user-friendly frontend and integrates advanced image processing and prediction capabilities.

Features
Image Uploads: Seamless upload of MRI and CT scan images.
Condition Prediction: Accurate classification of medical conditions using trained CNN models.
Responsive Design: User-friendly interface designed with HTML, CSS, and JavaScript.
Backend Integration: Robust backend for user authentication, secure data management, and efficient scan data processing.

Tech Stack
Programming Language: Python
Machine Learning Framework: TensorFlow, Keras
Web Framework: Flask
Frontend Technologies: HTML, CSS, JavaScript
Database: SQLite

Installation
Clone the repository:

bash
git clone https://github.com/anoksha-na/NeuroSight.git

Navigate to the project directory
Set up a virtual environment:
python -m venv venv

Activate the virtual environment

Install the required dependencies:
pip install -r requirements.txt

Configure the application:
Ensure the Flask application is set up properly in config.py.
Place the trained CNN models in the appropriate directory.

Run the application
Access the application in your web browser at http://127.0.0.1:5000.

Usage
Open the web application in your browser.
Upload an MRI or CT scan image using the provided interface.
View the predicted medical condition displayed on the results page.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
