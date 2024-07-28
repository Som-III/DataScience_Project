import os
import sys
import urllib.request as request
from src.DataSc_project.logger import logger
from src.DataSc_project.utils.helpers import get_size
from src.DataSc_project.exceptions import (CustomException)
from pathlib import Path
from src.DataSc_project.entity.config_entity import (DataTransformationConfig)
import pandas as pd
from sklearn.model_selection import train_test_split

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.HAC = ['HeartIssues', 'AnyTransplants', 'CancerHistory']
    def data_preprocess(self,filepath:Path):
        try:
            df = pd.read_csv(f"../../../{str(filepath)}")
            logger.info("raw file is being transformed")
            df = df.drop(columns=['CustomerID', 'Name'])
            df['DATE'] = df['DATE'].apply(lambda x: int(x.split('/')[2]))
            for i in self.HAC:
                df[i] = df[i].map({'No': 0, 'Yes': 1})
            df['Smoker'] = df['Smoker'].map({'No': 0, 'yes': 1})
            tier_mapping = {'tier - 1': 1, 'tier - 2': 2, 'tier - 3': 3}
            df['HospitalTier'] = df['HospitalTier'].map(tier_mapping)
            df['CityTier'] = df['CityTier'].map(tier_mapping)
            df['StateID'] = df['StateID'].str.lstrip('R').astype(int)
            logger.info("transformation complete")
            if not os.path.exists(Path(self.config.local_data_file)):                                               
                df.to_csv(Path(self.config.local_data_file),index=False,header=True)                                
                logger.info(f"csv file created at:{self.config.root_dir} with name {self.config.local_data_file} ") 
            else:
                logger.info(f"file already exists of size: {get_size(Path(self.config.local_data_file))}")          
            
        except Exception as e:
            logger.info(f"Exception: {e}")
            raise CustomException(e, sys) 
        
    def train_test_split(self, filepath:Path):
        try:
            df = pd.read_csv(f"../../../{str(filepath)}")
            train_set,test_set = train_test_split(df,test_size=0.25,random_state=42)
            if not (os.path.exists(Path(self.config.train_path)) and os.path.exists(Path(self.config.test_path))):                                                                              
                train_set.to_csv(Path(self.config.train_path),index=False,header=True)
                logger.info(f"train file created at:{self.config.train_test_split} with name {self.config.train_path} ")
                test_set.to_csv(Path(self.config.test_path),index=False,header=True)
                logger.info(f"test file created at:{self.config.train_test_split} with name {self.config.test_path} ")
                
            else:
                logger.info(f"train file already exists of size: {get_size(Path(self.config.train_path))}")
                logger.info(f"train file already exists of size: {get_size(Path(self.config.test_path))}")
        except Exception as e:
            logger.info(f"Exception: {e}")
            raise CustomException(e, sys) 