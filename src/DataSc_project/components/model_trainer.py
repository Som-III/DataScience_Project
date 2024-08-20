import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor
import xgboost as xgb
from DataSc_project.entity.config_entity import (ModelTrainerConfig)
from DataSc_project.logger import (logger)
from DataSc_project.exceptions import (CustomException)
from pathlib import Path
import sys



class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        self.train_data = pd.read_csv(self.config.train_data_path)
        self.test_data = pd.read_csv(self.config.test_data_path)
        print("Train data columns:", self.train_data.columns)
        print("Test data columns:", self.test_data.columns)
        print("Test data columns:", self.config.target_column)
        self.X_train = self.train_data.drop([str(self.config.target_column)], axis=1)
        self.X_test = self.test_data.drop([str(self.config.target_column)], axis=1)
        self.y_train = self.train_data[[str(self.config.target_column)]]
        self.y_test = self.test_data[[str(self.config.target_column)]]
        
    def train_linear_regression(self):
        try:
            model_path = Path(self.config.root_dir) / 'linear_regression_model.joblib'
            if not model_path.exists():
                model = LinearRegression()
                model.fit(self.X_train, self.y_train)
                joblib.dump(model, model_path)
                logger.info(f"model created at {model_path}")
            else:
                logger.info(f"model already exists at {model_path}")
        except Exception as e:
            logger.info(f"Exception: {e}")
            raise CustomException(e, sys)

    def train_ridge(self):
        try:
            model_path = Path(self.config.root_dir) / 'ridge_model.joblib'
            if not model_path.exists():
                model = Ridge(alpha=0.1)
                model.fit(self.X_train, self.y_train)
                joblib.dump(model, model_path)
                logger.info(f"model created at {model_path}")
            else:
                logger.info(f"model already exists at {model_path}")
        except Exception as e:
            logger.info(f"Exception: {e}")
            raise CustomException(e, sys)

    def train_lasso(self):
        try:
            model_path = Path(self.config.root_dir) / 'lasso_model.joblib'
            if not model_path.exists():
                model = Lasso(alpha=0.1)
                model.fit(self.X_train, self.y_train)
                joblib.dump(model, model_path)
                logger.info(f"model created at {model_path}")
            else:
                logger.info(f"model already exists at {model_path}")
        except Exception as e:
            logger.info(f"Exception: {e}")
            raise CustomException(e, sys)

    def train_elastinet(self):
        try:
            model_path = Path(self.config.root_dir) / 'elasticnet_model.joblib'
            if not model_path.exists():
                model = ElasticNet(alpha=0.1, l1_ratio=0.2)
                model.fit(self.X_train, self.y_train)
                joblib.dump(model, model_path)
                logger.info(f"model created at {model_path}")
            else:
                logger.info(f"model already exists at {model_path}")
        except Exception as e:
            logger.info(f"Exception: {e}")
            raise CustomException(e, sys)

    def train_decision_tree(self):
        try:
            model_path = Path(self.config.root_dir) / 'decision_tree_model.joblib'
            if not model_path.exists():
                model = DecisionTreeRegressor()
                model.fit(self.X_train, self.y_train)
                joblib.dump(model, model_path)
                logger.info(f"model created at {model_path}")
            else:
                logger.info(f"model already exists at {model_path}")
        except Exception as e:
            logger.info(f"Exception: {e}")
            raise CustomException(e, sys)

    def train_gradient_boosting(self):
        try:
            model_path = Path(self.config.root_dir) / 'gradient_boosting_model.joblib'
            if not model_path.exists():
                model = GradientBoostingRegressor()
                model.fit(self.X_train, self.y_train)
                joblib.dump(model, model_path)
                logger.info(f"model created at {model_path}")
            else:
                logger.info(f"model already exists at {model_path}")
        except Exception as e:
            logger.info(f"Exception: {e}")
            raise CustomException(e, sys)

    def train_xgboost(self):
        try:
            model_path = Path(self.config.root_dir) / 'xgboost_model.joblib'
            if not model_path.exists():
                model = xgb.XGBRegressor()
                model.fit(self.X_train, self.y_train)
                joblib.dump(model, model_path)
                logger.info(f"model created at {model_path}")
            else:
                logger.info(f"model already exists at {model_path}")
        except Exception as e:
            logger.info(f"Exception: {e}")
            raise CustomException(e, sys)
    
        
    
