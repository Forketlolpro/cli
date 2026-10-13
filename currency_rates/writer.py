import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def writer_into_file(text: str, file_name: str) -> None:
    path = Path(file_name)
    with path.open("w", encoding="utf-8") as file:
        file.write(text)
