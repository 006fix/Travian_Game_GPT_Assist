
import os
from datetime import datetime

# Base directory for outputs (inside repo)
BASE_OUTPUT_DIR = os.path.join(os.getcwd(), "sim_output")

ECONOMY_CONFIG_DIR = os.path.join(BASE_OUTPUT_DIR, "economy_configs")
RUN_LOGS_DIR = os.path.join(BASE_OUTPUT_DIR, "run_logs")
TEMP_DATA_DIR = os.path.join(BASE_OUTPUT_DIR, "temp_data")
INFRASTRUCTURE_CONFIG_DIR = os.path.join(BASE_OUTPUT_DIR, "infrastructure_configs")

for folder in [BASE_OUTPUT_DIR, ECONOMY_CONFIG_DIR, RUN_LOGS_DIR, TEMP_DATA_DIR, INFRASTRUCTURE_CONFIG_DIR]:
    os.makedirs(folder, exist_ok=True)

def get_timestamped_run_dir():
"""Create and return a new folder for a specific simulation run."""
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
path = os.path.join(RUN_LOGS_DIR, f"run_{timestamp}")
os.makedirs(path, exist_ok=True)
return path

def get_field_json_path(field_name):
    return os.path.join(ECONOMY_CONFIG_DIR, f"{field_name}.json")

def get_building_json_path(field_name):
    return os.path.join(INFRASTRUCTURE_CONFIG_DIR, f"{field_name}.json")

