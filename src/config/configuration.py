from pathlib import Path

from src.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from src.entity.config_entity import (DataIngestionConfig,PrepareModelConfig,TrainingModelConfig)
from src.utils.helper import read_yaml,create_directories


class ConfigurationManager:
    def __init__(
        self,
        config_filepath: Path = CONFIG_FILE_PATH,
        params_filepath: Path = PARAMS_FILE_PATH
    
    ):
        self.config = read_yaml(config_filepath)
        self.params= read_yaml(params_filepath)

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
            params_image_size= self.params.IMAGE_SIZE,
            params_include_top= self.params.INCLUDE_TOP,
            params_classes= self.params.CLASSES,
            params_weights=self.params.WEIGHTS,
            params_learning_rate= self.params.LEARNING_RATE


    )
        return prepare_base_model_config
    



    def get_training_model_config(self) -> TrainingModelConfig:
        training=self.config.training
        prepase_config=self.config.prepare_base_model
        params=self.params
        training_data=os.path.join(self.config.data_ingestion.unzip_dir,"kidney tumor")

        create_directories([training.root_dir])

        training_model_config=TrainingModelConfig(
            root_dir=Path(training.root_dir),
            training_model_path=Path(training.training_model_path),
            updated_base_model_path=Path(prepase_config.updated_base_model_path),
            training_data=Path(training_data),
            params_epochs = params.EPOCHS,
            params_batch_size= params.BATCH_SIZE,
            params_is_augmentation= params.AUGMENTATION,
            params_image_size= params.IMAGE_SIZE,
            params_learning_rate=params.LEARNING_RATE

        )

        return training_model_config

