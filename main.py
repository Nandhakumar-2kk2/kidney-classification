from src.pipeline.stage_01_data_ingestion import DataIngestionTrainigPipeline
from src.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.log.logger import logger

STAGE_NAME="Data Ingestion Stage"


try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<')
    obj=DataIngestionTrainigPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Prepare Base Model"

try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<')
    obj=PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")

except Exception as e:
    logger.exception(e)
    raise e