from src.DataSc_project.constants import *
from src.DataSc_project.utils.helpers import read_yaml, create_directories
from src.DataSc_project.entity.config_entity import (DataIngestionConfig,
                                            
                                            DataTransformationConfig
                                     
                                            )
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
    

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config: Dict[str,Any] = self.config['data_transformation']

        create_directories([Path(config["root_dir"])])
        create_directories([Path(config["train_test_split"])])

        data_transformation_config = DataTransformationConfig(
            root_dir=Path(config['root_dir']),
            train_test_split = Path(config['train_test_split']),
            raw_file_path = Path(config['raw_file_path']),
            local_data_file=Path(config['local_data_file']),
            train_path=Path(config['train_path']),
            test_path=Path(config['test_path'])
        )

        return data_transformation_config
