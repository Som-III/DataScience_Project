### Data Science project
Here's a sample GitHub README for your project:

---

# Insurance Prediction API

## Overview

This project is an end-to-end **Insurance Prediction API** built using Flask. It replicates industry-level workflows by incorporating modular coding, DevOps tools, Docker for containerization, and Postman for API testing. The project integrates code version control with GitHub, DVC, and MLflow, all within a seamless format on Dagshub. The entire application follows industry-standard practices to ensure a robust and scalable solution.

## Key Features

- **End-to-End Data Science Pipelines**: 
  - Comprehensive data ingestion, preprocessing, and transformation pipelines.
  - Regression models are built, trained, and validated.
  - Model experiment runs are tracked and stored in MLflow, with the best model version registered for production use.

- **API Development**: 
  - Flask-based API for insurance prediction.
  - API endpoints for model inference and prediction.
  - Thoroughly tested using Postman.

- **DevOps & CI/CD**:
  - **Docker**: Containerized API for seamless deployment.
  - **DVC**: Version control for data and models.
  - **yaml files**:  Configuration files for setting up and managing the CI/CD pipelines, Docker configurations, and DVC settings.
  - **Version Control**: Integrated with GitHub and DVC for tracking code and data changes.
  - **MLflow**: Tracks experiments, manages model registry, and facilitates model versioning.
  - **Automated Versioning**: Any code change triggers a new patch version, starting from version `0.0.1`.

- **Code Structure**:
  - **Modular Design**: Clean, maintainable, and scalable codebase.
  - **Logging & Custom Exceptions**: Comprehensive logging and custom exception handling for robust error management.
  - **Utility Functions**: Reusable utility functions for common tasks.
  - **Setup.py**: Script for package distribution and installation.
  - **Template.py**: Template for consistent code structure and standards.

## Project Workflow

1. **Data Ingestion & Preprocessing**:
   - Ingest raw data.
   - Clean, transform, and preprocess data.

2. **Model Training & Experiment Tracking**:
   - Train multiple regression models.
   - Track experiment metrics and parameters using MLflow.
   - Compare models and select the best-performing one.

3. **Model Registry & Deployment**:
   - Register the best model in MLflow.
   - Deploy the model as a RESTful API using Flask.
   - Containerize the application with Docker.

4. **Continuous Integration/Continuous Deployment (CI/CD)**:
   - Version control integrated with GitHub and DVC.
   - Automated versioning for each new patch.
   - Continuous monitoring and updating of the API.

## Installation
There are 2 ways for installation and running in device is to clone the repositiory or download the docker image and run it without explicitly creating environment
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Som-III/DataScience_Project.git
   cd DataScience_Project
   ```

2. **Set Up the Environment**:
   - Create a virtual environment:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the API**:
   ```bash
   python app.py
   ```
## Note 
  The api won't run unless you provide api key with key of `request-key`

4. **Testing with Postman**:
   - Import the Postman collection from the `postman/` directory.
   - Send a GET request to `http://127.0.0.1:5000/predict` with the API
   - add api key `request-key` value pair in the header section for authentication(api key value is singular and not present in readme)
   -sample body format
   ```json
    {  
        "DATE": 2023,  
        "BMI": 27.5,  
        "HBA1C": 5.9,  
        "HeartIssues": 0,  
        "AnyTransplants": 1,  
        "CancerHistory": 0,  
        "NumberOfMajorSurgeries": 0,  
        "Smoker": 0,  
        "Children": 2,   
        "HospitalTier": 2,  
        "CityTier": 2,  
        "StateID": 1012  
    }     
   ```
   - Test the API endpoints.

Second mechanism

5. **Docker Deployment**:
   - Build the Docker image:
     ```bash
     docker build -t som0/proj_api .
     ```
   - Run the Docker container:
     ```bash
     docker run -p 5000:5000 som0/proj_api
     ```


### Links
Following are the links to all references
1. Git clone
    ```
    https://github.com/Som-III/DataScience_Project.git 
    ```
2. Dagshub
    ```
    https://dagshub.com/Som-III/DataScience_Project 
    ```
3. DockerHub
    ```
    https://hub.docker.com/repository/docker/som0/proj_api
    ```

## References
1. https://github.com/krishnaik06/mlprojecthindi
2. https://mlflow.org/docs/latest/getting-started/intro-quickstart/notebooks/tracking_quickstart.html
3. https://dagshub.com/docs/integration_guide/mlflow_tracking/index.html




---

