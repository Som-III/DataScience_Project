import os
from pathlib import Path
import sys
from src.DataSc_project.logger import logger
from src.DataSc_project.exceptions import (CustomException)
from src.DataSc_project.components.data_transformation import (DataTransformation)
from src.DataSc_project.config import (ConfigurationManager)

STAGE_NAME = "Data transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        manager = ConfigurationManager()
        data_transformation_config = manager.get_data_transformation_config()
        data_transformation_obj = DataTransformation(config=data_transformation_config)
        raw_filepath = data_transformation_config.raw_file_path
        data_transformation_obj.data_preprocess(raw_filepath)
        transfromed_filepath = data_transformation_config.local_data_file
        if os.path.exists(Path(transfromed_filepath)):
            data_transformation_obj.train_test_split(transfromed_filepath)
        
        
if __name__ == '__main__':
    try:
        logger.info(f"\n\n\n>>>>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        logger.info(f">>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<\n\nx=====x")
    except Exception as e:
        logger.exception(e)
        raise CustomException(e,sys)