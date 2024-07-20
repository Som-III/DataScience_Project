import os
import sys
import urllib.request as request
from src.DataSc_project.logger import logger
from src.DataSc_project.utils.helpers import get_size
from src.DataSc_project.exceptions import (CustomException)
from pathlib import Path
from src.DataSc_project.entity.config_entity import (DataIngestionConfig)
from dotenv import load_dotenv,find_dotenv
import pymysql
import pandas as pd

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config
        load_dotenv(find_dotenv())
        self.host = os.getenv("host")
        self.user = os.getenv("user")
        self.password = os.getenv("password")
        self.db = os.getenv("db")
        
    def connect_db(self) -> pymysql.connections.Connection:
        
        logger.info("Connecting to database")
        try:
            mydb = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                db=self.db
            )
            logger.info("connection established: ",mydb)
            return mydb
         
        except Exception as e:
            logger.info(f"Exception: {e}")
            raise CustomException(e, sys) 
        
        
    def load_data(self,mydb: pymysql.connections.Connection):
        try:
            if not os.path.exists(Path(self.config['data_ingestion']['local_data_file'])):
                df = pd.read_sql_query('SELECT * FROM insurance_t',mydb)
                df.to_csv(Path(self.config['data_ingestion']['local_data_file']),index=False,header=True)
                logger.info(f"csv file created at:{self.config['data_ingestion']['root_dir']} with name {self.config['data_ingestion']['local_data_file']} ")
                
            else:
                logger.info(f"file already exists of size: {get_size(Path(self.config['data_ingestion']['local_data_file']))}")
        except Exception as e:
            logger.info(f"Exception: {e}")
            raise CustomException(e, sys) 