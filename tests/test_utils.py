from src.classes import Operation
from src.utils import get_executed_operations


def test_get_executed_operations():
    operations = [
        {
            "state": "EXECUTED",
        },
        {
            "state": "EXECUTED",
        },
        {
            "state": "asdfgh",
        },
        {},
    ]

    expected_operations = [
        {
            "state": "EXECUTED",
        },
        {
            "state": "EXECUTED",
        },
    ]

    assert get_executed_operations(operations) == expected_operations

def test_get_operation_instances():
    op = Operation(
        date="2019-07-03T18:35:29.512364",
        pk=41428829,
        state="EXECUTED",
        amount="8221.37",
        currency_name="USD",
        description="Перевод организации",
        to="Счет 35383033474447895560",
        from_="MasterCard 7158300734726758",
    )

    assert op.from_ == "MasterCard 7158 30** **** 6758"
    assert op.to == "Счет **5560"
    assert op.convert_payment_date() == "03.07.2019"
    assert str(op) == (
            "03.07.2019 Перевод организации\n"
            "MasterCard 7158 30** **** 6758 -> Счет **5560\n"
            "8221.37 USD\n"
    )

    assert op.convert_payment_data("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"

def test_get_operation_instances_if_from_None():
    op = Operation(
        date="2019-07-03T18:35:29.512364",
        pk=41428829,
        state="EXECUTED",
        amount="8221.37",
        currency_name="USD",
        description="Перевод организации",
        to="Счет 35383033474447895560",
        from_=None,
    )

    assert op.from_ == ""
