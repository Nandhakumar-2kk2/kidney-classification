from pathlib import Path

from src.constants import CONFIG_FILE_PATH
from src.entity.config_entity import DataIngestionConfig,PrepareModelConfig
from src.utils.helper import read_yaml,create_directories


class ConfigurationManager:
    def __init__(
        self,
        config_filepath: Path = CONFIG_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)

        create_directories([self.config.artifacts_root])
        

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        config = self.config.data_ingestion

        create_directories([config.root_dir])                    

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_url=config.source_url,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir),
        )

        return data_ingestion_config
    
    def get_prepare_base_model_config(self) -> PrepareModelConfig:
        
        config=self.config.prepare_base_model

        create_directories([config.root_dir])

        prepare_base_model_config= PrepareModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size= self.param.IMAGE_SIZE,
            params_include_top= self.param.INCLUDE_TOP,
            params_classes= self.param.CLASSES,
            params_weights=self.param.WEIGHTS,
            params_learning_rate= self.param.LEARNING_RATE


    )
        return prepare_base_model_config