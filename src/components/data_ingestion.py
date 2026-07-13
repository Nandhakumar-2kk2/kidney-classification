from src.entity.config_entity import DataIngestionConfig
import os
import sys
from src.log.logger import logger
from src.exception.custom_exception import CustomException
import gdown
import zipfile



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self) ->str:

        try:
            dataset_url=self.config.source_url
            zip_download_dir=self.config.local_data_file
            os.makedirs("artifacts/data_ingestion",exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir} ")

            file_id=dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?id="
            gdown.download(prefix + file_id, str(zip_download_dir))

        except Exception as e:
            raise CustomException(e,sys)
        


    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)





