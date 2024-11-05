import pytest

from src.masks import get_mask_card_number
from src.widget import get_date, mask_account_card


@pytest.mark.parametrize('new_string, expected',
                [("Счет 73654108430135874305", "Счет **4305"),
                ("Счет 73654108430135879456", "Счет **9456"),
                ("Счет 73654108430188877678", "Счет **7678"),
                ("Visa Gold 5999414228426553", "Visa Gold 5999 41 ** **** 6553"),
                ("Visa Premium 5988824238457663", "Visa Premium 5988 82 ** **** 7663"),
                ("Visa 5972124238468773", "Visa 5972 12 ** **** 8773"),
                ("Master Card 4279014508319635", "Master Card 4279 01 ** **** 9635")
                ])
def test_mask_account_card_1(new_string, expected):
    """Тесты для проверки, что функция корректно распознает
    и применяет нужный тип маскировки в зависимости от
    типа входных данных (карта или счет).
    Параметризованные тесты с разными типами карт и счетов
    для проверки универсальности функции
    Счет 73654108430135874305 -> Счет **4305
    Visa Gold 5988824238457663 -> Visa Gold 5988 82 ** **** 663"""
    assert mask_account_card(new_string) == expected


@pytest.mark.parametrize("number_card, expected_card, number_account, expected_account",
                         [("Visa Gold 5999414228426553", "Visa Gold 5999 41 ** **** 6553",
                           "Счет 73654108430135879456", "Счет **9456")])
def test_mask_account_card(number_card, expected_card, number_account, expected_account,
                           error_numb="Visa Gold" "59994142284226553",
                           error_expected='Ошибка данных'):
    assert mask_account_card(number_card) == expected_card
    assert mask_account_card(number_account) == expected_account
    assert mask_account_card(error_numb) == error_expected


def test_get_date():
    """Тестирование правильности преобразования даты.
    Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата"""
    assert get_date("2018.07-11T02:26:18.671407") == "Неверный формат входящей даты"
    assert get_date("2018.07-11T02:26:18.67") == "Ошибка типа данных"
    assert get_date("2018-07-11T02:26:18.671407") == "11.07.2018"


@pytest.mark.parametrize('input_data', ["2018/07-11T02:26:18.671407", "2018.07-11T02:26:18.671407"])
def test_get_date_is_wrong_date(input_data):
    """Проверка работы функции на различных входных форматах даты,
     включая граничные случаи и нестандартные строки с датами."""
    assert get_date(input_data) == 'Неверный формат входящей даты'


@pytest.mark.parametrize('input_data_type', ["31st of February, 2023",  "2023-02",  "31.02.23", "31.02.2023",
                                             [], "26:18.671407", "Hello" ])
def test_get_date_is_wrong_type(input_data_type):
    """Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата"""
    assert get_date(input_data_type) == 'Ошибка типа данных'

