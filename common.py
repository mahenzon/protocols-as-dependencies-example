import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def configure_logging(level: int = logging.INFO) -> None:
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="%(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
        # format="[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
    )
