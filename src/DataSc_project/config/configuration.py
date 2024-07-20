from src.DataSc_project.constants import *
from src.DataSc_project.utils.helpers import read_yaml, create_directories
from src.DataSc_project.entity.config_entity import (DataIngestionConfig,
                                            DataValidationConfig,
                                            DataTransformationConfig,
                                            ModelTrainerConfig,
                                            ModelEvaluationConfig)
from typing import Dict, Any


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        create_directories([Path(self.config['artifacts_root'])])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config: Dict[str,Any] = self.config['data_ingestion']

        create_directories([Path(config['root_dir'])])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config['root_dir']),
            local_data_file=Path(config['local_data_file'])
            
        )

        return data_ingestion_config
    

