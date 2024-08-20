#root_dir , test_data_path, diff_model paths, metric filename, mlflow_uri, local_uri?
import sys
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from DataSc_project.logger import (logger)
from DataSc_project.exceptions import (CustomException)
from pathlib import Path
from DataSc_project.entity.config_entity import (ModelEvaluationConfig)
from DataSc_project.utils.helpers import (update_metrics)
import dagshub


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        dagshub.init(repo_owner='Som-III', repo_name='DataScience_Project', mlflow=True)

    
    def eval_metrics(self,actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    def log_model_performance(self,model_name:str):
        try:
            test_data = pd.read_csv(self.config.test_data_path)
            logger.info(self.config.model_paths[model_name])
            model = joblib.load(self.config.model_paths[model_name])
            logger.info(f"model {model} is loaded")
            X_test = test_data.drop([self.config.target_column], axis=1)
            y_test = test_data[[self.config.target_column]].values.flatten()
            
            with mlflow.start_run(run_name=model_name):
                y_predicted = model.predict(X_test)
                logger.info(f"for model {model} prediction array is optained with shape {y_predicted.shape} and test data shape {y_test.shape}")
                (rmse, mae, r2) = self.eval_metrics(y_test, y_predicted)
                mlflow.log_metric("rmse", rmse)
                mlflow.log_metric("mae", mae)
                mlflow.log_metric("r2", r2)
                mlflow.sklearn.log_model(model, "model")
                scores = {"rmse": rmse, "mae": mae, "r2": r2}
                update_metrics(path=Path(self.config.metric_file_name),model_name=model_name,metrics=scores)

                return {"model_name": model_name, "rmse": rmse, "mae": mae, "r2": r2}
        except Exception as e:
            logger.info(f"Exception: {e}")
            raise CustomException(e, sys)
        
        
        
    def compare_models(self):
        try:
            mlflow.set_tracking_uri(uri=self.config.mlflow_uri)
            mlflow.set_experiment("Local model comparision")
            logger.info("experiment started for model comparision")
            best_model = None
            best_rmse = float("inf")
            all_scores = []

            for model_name in self.config.model_paths.keys():
                scores = self.log_model_performance(model_name)
                all_scores.append(scores)
                if scores["rmse"] < best_rmse:
                    best_rmse = scores["rmse"]
                    best_model = model_name

            return best_model, all_scores   
        except Exception as e:
            logger.info(f"Exception: {e}")
            raise CustomException(e, sys)
    
    
    def register_best_model(self, best_model_name:str):
        try:
            mlflow.set_registry_uri(self.config.mlflow_uri)
            logger.info("model registry for storing best model is connected")
            best_model_path = self.config.model_paths[best_model_name]
            best_model = joblib.load(best_model_path)

            with mlflow.start_run(run_name=f"Register_{best_model_name}"):
                logger.info(f"best model added to the registry named {best_model_name}")
                mlflow.sklearn.log_model(best_model, "model", registered_model_name=best_model_name)
        except Exception as e:
            logger.info(f"Exception: {e}")
            raise CustomException(e, sys)
    
    
