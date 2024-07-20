from DataSc_project.logger import logger
from src.DataSc_project.constants import CONFIG_FILE_PATH  
from src.DataSc_project.exceptions import CustomException
import sys
from src.DataSc_project.utils.helpers import read_yaml
import os
from pathlib import Path



    

if __name__ == "__main__":
        try:
          config = read_yaml(CONFIG_FILE_PATH)
          print(Path(config['data_ingestion']['local_data_file']))
          
        except Exception as e:
                raise CustomException(e,sys) from e
        
        