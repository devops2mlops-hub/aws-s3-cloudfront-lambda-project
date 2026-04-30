import logging
import time
import os

LOG_DIR = "/var/log/myapp"
LOG_FILE = os.path.join(LOG_DIR, "app.log")

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

while True:
    logging.info("Application running - generating logs...")
    time.sleep(2)
