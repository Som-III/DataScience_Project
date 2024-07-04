from DataSc_project.logger import logger
from src.DataSc_project.constants import CONFIG_FILE_PATH  
from src.DataSc_project.exceptions import CustomException
import sys
from src.DataSc_project.utils.helpers import read_yaml


    

if __name__ == "__main__":

        config = read_yaml(CONFIG_FILE_PATH)
        print(config['data_ingestion']['root_dir'])
        