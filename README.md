# Image Processing App

## Description
This is a Flask-based web application that allows users to upload an image, processes it using a pre-trained machine learning model, and returns the processed image.

## Setup Instructions

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/ML-ebs.git
    cd ML-ebs
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the application:**
    ```sh
    python app.py
    ```

4. **Access the application:**
    Open a web browser and go to `http://localhost:8000`.

## Deployment
To deploy this application on AWS Elastic Beanstalk, follow these steps:

1. Create an Elastic Beanstalk environment.
2. Configure the environment using the `.ebextensions` provided.
3. Deploy the application using the Elastic Beanstalk CLI or AWS Management Console.

## License
This project is licensed under the MIT License.
