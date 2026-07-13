from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
import yaml
from pathlib import Path
import os
from src.log.logger import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Returns:
        ConfigBox: YAML content wrapped in ConfigBox.
    """

    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)

            print(f"YAML file loaded successfully: {path_to_yaml}")

            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("YAML file is empty.")







def create_directories(path_to_directories: list, verbose= True):
    """
    Create directories if they don't already exist.

    Args:
        path_to_directories: List of directory paths.
        verbose: Whether to log directory creation.
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)

        if verbose:
            logger.info(f"Created directory at: {path}")