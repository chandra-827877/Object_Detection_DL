import os
from box.exceptions import BoxValueError # type: ignore
import yaml # type: ignore
from detectionClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: str) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.
    
    Args:
        path_to_yaml (str): Path to the YAML file.
        
    Returns:
        ConfigBox: Contents of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def save_json(path: str, data: dict) -> None:
    """
    Saves a dictionary as a JSON file.
    
    Args:
        path (str): Path to save the JSON file.
        data (dict): Data to be saved in the JSON file.
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)

    logger.info(f"JSON file {path} saved successfully.")

def decodeImage(imagestring, fileName):
    imgdata = base64.b64decode(imagestring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImage(croppedImagePath):
    with open(croppedImagePath, "rb") as imageFile:
        encoded_string = base64.b64encode(imageFile.read())
        return encoded_string