from dataclasses import dataclass
from pathlib import Path
from typing import Dict


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    local_data_file:Path
    

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    train_test_split: Path
    raw_file_path: Path
    local_data_file: Path
    train_path: Path
    test_path: Path

    
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    target_column: str

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    metric_file_name: Path
    mlflow_uri: str
    target_column: str
    model_paths: Dict[str, Path]

