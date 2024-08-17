import json
from pathlib import Path

from src.classes import Operation


def load_json(path: Path) -> list[dict]:
    """
    открываем файл  .json
    :param path:
    :return:
    """
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def get_executed_operations(operations:list[dict]) -> list[dict]:
    """
    выбираем выполненные операции
    :param operations:
    :param operation:
    :return:
    """
    return [
        operation
        for operation in operations
        if operation.get("state") == "EXECUTED"
    ]


def get_operation_instances(operations:list[dict]) -> list[Operation]:
    """
    создаем экзкмпляры класса
    :param operations:
    :return:
    """
    operation_instances = []
    for operation in operations:
        operation_amount = operation["operationAmount"]
        op = Operation(
            pk=operation["id"],
            state=operation["state"],
            amount=operation_amount["amount"],
            currency_name=operation_amount["currency"]["name"],
            date=operation["date"],
            description=operation["description"],
            to=operation["to"],
            from_=operation.get("from"),
        )
        operation_instances.append(op)
    return operation_instances


def sort_operations_by_date(operations:list[Operation]) -> list[Operation]:
    """
    сортировка по убыванию
    :return:
    """
    return sorted(operations, reverse = True)
