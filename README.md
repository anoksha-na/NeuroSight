# NeuroSight Analytics

NeuroSight Analytics is a web application designed to predict medical conditions from MRI and CT scan images using Convolutional Neural Networks (CNNs). The application features a responsive and user-friendly frontend and integrates advanced image processing and prediction capabilities.

## Features

- **Image Uploads:** Seamless upload of MRI and CT scan images.
- **Condition Prediction:** Accurate classification of medical conditions using trained CNN models.
- **Responsive Design:** User-friendly interface designed with HTML, CSS, and JavaScript.
- **Backend Integration:** Robust backend for user authentication, secure data management, and efficient scan data processing.

## Tech Stack

- **Programming Language:** Python
- **Machine Learning Framework:** TensorFlow, Keras
- **Web Framework:** Flask
- **Frontend Technologies:** HTML, CSS, JavaScript
- **Database:** SQLite

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/anoksha-na/NeuroSight.git
   ```

2. Navigate to the project directory:

   ```bash
   cd NeuroSight
   ```

3. Set up a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Configure the application:

   - Ensure the Flask application is set up properly in `config.py`.
   - Place the trained CNN models in the appropriate directory.

7. Run the application:

   ```bash
   python app.py
   ```

8. Access the application in your web browser at `http://127.0.0.1:5000`.

## Usage

1. Open the web application in your browser and login as Doctor or Patient.
2. Upload an MRI or CT scan image using the provided interface (as Doctors).
3. View the predicted medical condition displayed on the results page (as Patients).

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/anoksha-na/NeuroSight/blob/master/LICENSE) file for more details.
