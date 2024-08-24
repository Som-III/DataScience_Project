import sys
from DataSc_project.logger import logger
from DataSc_project.exceptions import (CustomException)
from DataSc_project.components.model_prediction import (ModelPrediction)
from DataSc_project.config import (ConfigurationManager)



class ModelPredictionPipeline:
    def __init__(self):
        pass

    def return_best_model_uri(self):
        try:
            manager = ConfigurationManager()
            model_pred_config = manager.get_model_prediction_config()
            model_pred_obj = ModelPrediction(config=model_pred_config)
            best_model_uri = model_pred_obj.predict_best_model_uri()
            return best_model_uri
        except Exception as e:
            logger.info(f"Exception: {e}")
            raise CustomException(e, sys)
        
        
