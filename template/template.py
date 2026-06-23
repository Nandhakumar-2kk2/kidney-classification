from pathlib import Path



# Path("..") / "kidney classification"   last second path 





PROJECT_NAME = Path("..") / "kidney classification"





folders = [

    "data/raw",

    "data/processed",

    "data/external",

    "notebooks",

    "logs",

    "artifacts",

    "experiments",

    "models",

    "tests",

    "reports/figures",

    "reports/tables",

    "src/components",

    "src/pipeline",

    "src/exception",

    "src/logger",

    "src/utils",

    "src/config",

    "src/entity",

]



files = [

    "README.md",

    "requirements.txt",

    ".gitignore",

    "setup.py",

    "main.py",

    "params.yaml",

    "dvc.yaml",



    "src/__init__.py",



    "src/components/__init__.py",

    "src/components/data_ingestion.py",

    "src/components/data_validation.py",

    "src/components/data_transformation.py",

    "src/components/model_trainer.py",

    "src/components/model_evaluation.py",



    "src/pipeline/__init__.py",

    "src/pipeline/train_pipeline.py",

    "src/pipeline/predict_pipeline.py",



    "src/exception/__init__.py",

    "src/exception/custom_exception.py",



    "src/logger/__init__.py",

    "src/logger/logging.py",



    "src/utils/__init__.py",

    "src/utils/helper.py",



    "src/config/__init__.py",

    "src/config/configuration.py",



    "src/entity/__init__.py",

    "src/entity/config_entity.py",



    "tests/test_data.py",

    "tests/test_model.py"

]



project_path = Path(PROJECT_NAME)



# Create folders

for folder in folders:

    (project_path / folder).mkdir(parents=True, exist_ok=True)



# Create files

for file in files:

    file_path = project_path / file

    file_path.parent.mkdir(parents=True, exist_ok=True)



    if not file_path.exists():

        file_path.touch()



print(f"Project '{PROJECT_NAME}' created successfully!")



