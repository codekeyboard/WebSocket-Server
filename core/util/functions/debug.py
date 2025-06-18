import os, sys
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(ROOT_DIR) if ROOT_DIR not in sys.path else None

from datetime import datetime
from core.util.functions.config import config

# Get current timestamp parts
now = datetime.now()
hour_dir = now.strftime("%Y-%m-%d--%H-00-logs")  # Hourly folder name
log_file = now.strftime("%Y-%m-%d--%H-%M-%S") + "-debug.log"  # Filename with full timestamp

# Create full path: logs/<hour_dir>/<log_file>
LOG_DIR = os.path.join(ROOT_DIR, "logs", hour_dir)
DEBUG_FILE = os.path.join(LOG_DIR, log_file)

# Ensure the hourly log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

def debug(*args, **kwargs):
    """Custom debug function to log messages if debug mode is enabled."""
    if config("debug", False):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"[{timestamp}] " + " ".join(map(str, args))
        with open(DEBUG_FILE, "a", encoding='utf-8') as f:
            print(message, **kwargs, file=f)
