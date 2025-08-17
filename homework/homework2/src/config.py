
import sys, os
print("Python version:", sys.version)
print("Interpreter path:", sys.executable)

try:
    import numpy as np
    from dotenv import load_dotenv
    print("Imports OK")
except Exception as e:
    print("Import error:", e)
    raise

from pathlib import Path

def load_env() -> None:
    load_dotenv()
    print(".env loaded (if present)")

# src/config.py (inline demo)
from typing import Optional

def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(name, default)

CONFIG_DIR = Path(__file__).resolve().parent # current: homework2/src 
PROJECT_ROOT = CONFIG_DIR.parent
DATA_DIR = PROJECT_ROOT / "data"
print("PROJECT_ROOT:", PROJECT_ROOT)
print("DATA_DIR:", DATA_DIR)

api_key_present = get_key("API_KEY") is not None
data_dir_env = get_key("DATA_DIR", str(DATA_DIR))
print("API_KEY present:", api_key_present)
print("DATA_DIR from env:", data_dir_env)

if not Path(data_dir_env).is_absolute():
    data_dir_env = DATA_DIR 

# Ensure data directory exists (non-destructive)
Path(data_dir_env).mkdir(parents=True, exist_ok=True)
print("Ensured data directory exists.")
