import sys
from DataSc_project.logger import logger
from DataSc_project.exceptions import (CustomException)
from DataSc_project.components.model_evaluation import  (ModelEvaluation)
from DataSc_project.config import (ConfigurationManager)

STAGE_NAME = "Model Evaluation stage"


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        manager = ConfigurationManager()
        model_eval_config = manager.get_model_evaluation_config()
        model_eval_obj = ModelEvaluation(config=model_eval_config)
        best_model, all_scores = model_eval_obj.compare_models()
        model_eval_obj.register_best_model(best_model_name=best_model)
        print(all_scores)
        logger.info(all_scores)




if __name__ == '__main__':
    try:
        logger.info(f"\n\n\n>>>>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<\n\nx=====x")
    except Exception as e:
        logger.exception(e)
        raise CustomException(e,sys)

