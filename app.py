from flask import Flask, request, jsonify, abort
import os
import joblib
from pathlib import Path
import mlflow
import mlflow.pyfunc
#best_model = mlflow.pyfunc.load_model(model_uri=best_model_uri)
from src.DataSc_project.pipeline.model_prediction_pipeline import (ModelPredictionPipeline)
import numpy as np
from dotenv import load_dotenv,find_dotenv
from src.DataSc_project.logger import logger

load_dotenv(find_dotenv())

app = Flask(__name__)

API_KEY = os.getenv('API_KEY') 

mlflow.set_tracking_uri("https://dagshub.com/Som-III/DataScience_Project.mlflow")

model_name = "GradientBoosting"
model_version = 1
logger.info("tracking server is set")
local_model_path = Path("artifacts/model_prediction/model.joblib")
#mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{model_version}")
if os.path.exists(local_model_path):
    model = joblib.load(local_model_path)
    logger.info("locally stored best model version is loaded")
else:
    model = mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{model_version}")
    joblib.dump(model, local_model_path)
    logger.info("model is loaded from mlflow registry and saved successfully")
logger.info("model is loaded")

def require_api_key(func):
    def wrapper(*args, **kwargs):
        logger.info("inside wrapper")
        api_key_rec:str = request.headers.get('request-key')
        logger.info(f"api key is recived from header")
        if api_key_rec and api_key_rec == API_KEY:
            return func(*args, **kwargs)
        else:
            logger.info("\n\n>>>>>>>>>>>>>>>>>>>>>>>>>> API verification aborded <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n")
            abort(401)
    wrapper.__name__ = func.__name__
    return wrapper

@app.route('/predict', methods=['POST'])
@require_api_key
def predict():
    try:
        data = request.get_json(force=True)
        features = [
                data['DATE'],
                data['BMI'],
                data['HBA1C'],
                data['HeartIssues'],
                data['AnyTransplants'],
                data['CancerHistory'],
                data['NumberOfMajorSurgeries'],
                data['Smoker'],
                data['Children'],
                data['HospitalTier'],
                data['CityTier'],
                data['StateID']
            ]
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    
    features = np.array(features).reshape(1, -1)
    try:
        prediction = model.predict(features)[0]
        logger.info("predictions are done")
        return jsonify({'prediction': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)
    

