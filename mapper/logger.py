import logging
import logging.handlers
import os

logging.basicConfig(filename='cloud-mapper.log',level=logging.INFO,format="%(asctime)s [%(levelname)s] - %(message)s")
logger = logging.getLogger(__name__)

LOG_FILE = 'cloud-mapper.log'
LOG_MAX_BYTES = 5 * 1024 * 1024 # 5 MB
LOG_BACKUP_COUNT = 3
LOG_FORMAT = "%(asctime)s [%(levelname)s] - %(message)s"

def setup_logging(level = logging.INFO):
    pass