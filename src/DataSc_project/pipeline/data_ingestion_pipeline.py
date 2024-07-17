import os
import sys
from src.DataSc_project.logger import logger
from src.DataSc_project.exceptions import (CustomException)
from src.DataSc_project.components.data_ingestion import (DataIngestion)
from src.DataSc_project.config import (ConfigurationManager)

STAGE_NAME = "Data Ingestion stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        manager = ConfigurationManager()
        data_ingestion_configurations = manager.get_data_ingestion_config()
        data_ingestion_obj = DataIngestion(config=data_ingestion_configurations)
        mydb = data_ingestion_obj.connect_db()
        data_ingestion_obj.load_data(mydb)
        

if __name__ == '__main__':
    try:
        logger.info(f">>> stage {STAGE_NAME} started <<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>> stage {STAGE_NAME} completed <<<<<\n\nx=====x")
    except Exception as e:
        logger.exception(e)
        raise CustomException(e,sys)
