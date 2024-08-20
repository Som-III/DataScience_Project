import sys
from DataSc_project.logger import logger
from DataSc_project.exceptions import (CustomException)
from DataSc_project.components.model_trainer import (ModelTrainer)
from DataSc_project.config import (ConfigurationManager)


STAGE_NAME = "Model Training stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        manager = ConfigurationManager()
        model_train_config = manager.get_model_trainer_config()
        model_train_object = ModelTrainer(config=model_train_config)
        model_train_object.train_linear_regression()
        model_train_object.train_ridge()
        model_train_object.train_lasso()
        model_train_object.train_elastinet()
        model_train_object.train_decision_tree()
        model_train_object.train_gradient_boosting()
        model_train_object.train_xgboost()




if __name__ == '__main__':
    try:
        logger.info(f"\n\n\n>>>>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<\n\nx=====x")
    except Exception as e:
        logger.exception(e)
        raise CustomException(e,sys)