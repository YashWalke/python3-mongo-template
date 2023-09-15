import json
import logging
from logging.config import dictConfig
from pathlib import Path

import sys
from typing import Dict

config_dir: Path = Path(__file__).parent.parent / "configs"

try:
    print("Reading config...")
    with open(config_dir / "logging.json", "r") as f:
        logging_config: Dict[str, object] = json.load(f)
    print("Logging config read.")
except FileNotFoundError:
    print("Logging config not found.")
    sys.exit(1)

dictConfig(logging_config)

logger: logging.Logger = logging.getLogger("main")

# Add logic here
