import json
from pathlib import Path


def load_json(path: Path) -> list[dict]:
    """

    :param path:
    :return:
    """
    with open(path, encoding='utf-8') as file:
        return json.load(file)
import json
from pathlib import Path


def load_json(path: Path) -> list[dict]:
    """

    :param path:
    :return:
    """
    with open(path, encoding='utf-8') as file:
        return json.load(file)
