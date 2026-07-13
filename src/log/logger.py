import logging
import os
from datetime import datetime
from pathlib import Path

# Create Logs Directory
LOG_DIR = "logs"
Path(LOG_DIR).mkdir(exist_ok=True)

# Log File Name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Full Log Path
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Logging Configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)