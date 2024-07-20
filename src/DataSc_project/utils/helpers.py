import os
import yaml
from src.DataSc_project.logger import logger
import json
import joblib
from pathlib import Path
from src.DataSc_project.exceptions import CustomException
import sys
from typing import Dict, Any




def read_yaml(path_to_yaml: Path) -> Dict[str, Any]:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: If the YAML file is empty.
        Exception: For other exceptions.

    Returns:
        dict: dictonary of yaml.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            if not content:
                raise ValueError("YAML file is empty.")
            logger.info(f"ingestion YAML file: {path_to_yaml} loaded successfully")
            return content
    except Exception as e:
        logger.info(f"Exception: {e}")
        raise CustomException(e, sys)   



    
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")




def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")




def load_json(path: Path) -> dict:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        dict: data as dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return content
#########check load json return



def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
