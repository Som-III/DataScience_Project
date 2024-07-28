from dataclasses import dataclass
from pathlib import Path


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

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict

