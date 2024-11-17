# Salary-Prediction-App
A Flask-based web application that predicts employee salary based on experience, test scores, and interview scores. This project demonstrates the integration of a machine learning model with a web interface.

# Features
: Predict employee salaries using a trained Linear Regression model.

: User-friendly HTML interface for input and output.

: Hosted using Flask and includes Jinja2 templates for dynamic content rendering.

# Directory Structure
project-folder/

    ├── app.py             # Main Flask application

    ├── model.py           # Script to train the model

    ├── model.pkl          # Pre-trained machine learning model

    ├── templates/         # HTML templates for the web app


          └── index.html

    ├── static/            # Static files (CSS/JS, if any)

    ├── requirements.txt   # List of Python dependencies

# How to Set Up and Run Locally

1. Clone the repository:

       git clone https://github.com/jehmegh/salary-prediction-app.git

       cd salary-prediction-app


3. Install dependencies: Ensure you have Python 3.x installed. Then, run:
 
       pip install -r requirements.txt


4. Run the Flask app:

       python app.py


5. Access the web application: Open your browser and navigate to:

       http://127.0.0.1:5000/


# How to Use

1. Enter the following inputs in the web interface:

   --> Experience: Number of years (e.g., 2 or five).

   --> Test Score: Test score out of 10 (e.g., 8).

   --> Interview Score: Score out of 10 (e.g., 6).

3. Click the "Predict" button to calculate the predicted salary.

4. The predicted salary will be displayed on the page.

# Dependencies

The project relies on the following Python libraries:

: Flask

: Numpy

: Pandas

: Scikit-learn

: Pickle

These dependencies are listed in the requirements.txt file.

# License

This project is licensed under the MIT License. 
