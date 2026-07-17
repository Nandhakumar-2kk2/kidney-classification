from src.config.configuration import ConfigurationManager
from src.components.model_training import Training
from src.log.logger import logger
from src.exception.custom_exception import CustomException
import sys

STAGE_NAME="Model Training"


class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        training_config = config.get_prepare_base_model_config()

        train_ = Training(config=training_config)
        train_.get_base_model()
        train_.train_valid_genrator()
        train_.train()


if __name__=="__main__":
    try:
        logger.info(f'>>>>> stage {STAGE_NAME} started <<<<')
        obj=ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")

    except Exception as e:
        logger.exception(e)
        CustomException(e,sys)