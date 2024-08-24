import mlflow
import sys
from mlflow.tracking import MlflowClient
from DataSc_project.logger import (logger)
from DataSc_project.exceptions import (CustomException)
from pathlib import Path
from DataSc_project.entity.config_entity import (ModelPredictionConfig)
from DataSc_project.config import (ConfigurationManager)

class ModelPrediction:
    def __init__(self, config: ModelPredictionConfig):
        self.config = config
        
        
    def predict_best_model_uri(self):
        try:
            mlflow.set_tracking_uri(self.config.mlflow_uri)
            logger.info("tracking uri is set")
            client = MlflowClient()
            #====================================================================
            registered_models = client.list_registered_models()
            best_model_uri = self.compare(registered_models=registered_models,best_rmse=float('inf'),client=client)
            return best_model_uri
        except Exception as e:
            logger.info(f"Exception: {e}")
            raise CustomException(e, sys)
        
        
    def compare(self,registered_models,best_rmse,client):
        try:
            best_model_uri = None
            for model in registered_models:
                model_name = model.name  
                versions = client.search_model_versions(f"name='{model_name}'")
    
                for version in versions:
                    run_id = version.run_id
                    run = client.get_run(run_id)
                    rmse = float(run.data.metrics["rmse"])  

                    if rmse < best_rmse:
                        best_rmse = rmse
                        best_model_uri = f"models:/{model_name}/{version.version}"
                        
            return best_model_uri
        
        except Exception as e:
            logger.info(f"Exception: {e}")
            raise CustomException(e, sys)
        
    