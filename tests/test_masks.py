import pytest
from src.masks import get_mask_card_number, get_mask_account


"""Тестирование модуль masks. Функция get_mask_card_number"""


def test_mask_card_func(new_string_card: str):
    """Тест-функция правильного маскирования номера карты,
     замена символов на '** ****'
     #'Visa Gold 5999414228426353' -> ** **** 6353"""
    assert get_mask_card_number(new_string_card) == "** **** 6353"
    assert get_mask_card_number("Visa Platinum 7000792289606361") == "** **** 6361"
    assert get_mask_card_number("Visa 7000792289606362") == "** **** 6362"


@pytest.mark.parametrize('number, number_card', [("Visa Gold 5999414228426553", "** **** 6553"),
                                                 ("Visa Classic 5999414228416354", "** **** 6354"),
                                                 ("Visa Premium 5999414228476356", "** **** 6356")])
def test_get_mask_card_number_2(number, number_card):
    """Тест-функция через параметризацию правильного маскирования номера карты,
         замена символов на '** ****'
         #'Visa Gold 5999414228426353' -> ** **** 6353"""
    assert get_mask_card_number(number) == number_card


@pytest.mark.parametrize('input_card_num', ["Visa Gold 59994142",
                                            "Visa Classic 59994142284263128888",
                                            "Visa Premium 0"])
def test_mask_card_format(input_card_num: str, expected='Неверный формат номера карты'):
    """Проверка работы функции на различных входных форматах номеров
     карт, включая граничные случаи и нестандартные длины номеров"""
    assert get_mask_card_number(input_card_num) == expected


def test_mask_card_num_trace(card_num_trace: str):
    """Тест-функция проверки цифрового следа номера карты
    #"Visa Gold 5999414228426353 - > int (5999414228426353)"""
    assert card_num_trace is True


def test_mask_card_duration(mask_card_duration: str):
    """Тест-функция проверки количества цифр в номере карты
    #"Visa Gold 5999414228426353 -> 5999414228426353 (len(card[-16:])"""
    assert mask_card_duration == 16


@pytest.mark.parametrize('number', ["Visa Gold 5999414228426553",
                                    "Visa Classic 5999414228416354",
                                    "Visa Premium 5999414228476356",
                                    ])
def test_mask_card_number(number, num_isdigit=True, len_num=21, expected: int = 16):
    assert number[-16:].isdigit() is num_isdigit
    assert len(number) > len_num
    assert len(number[-16:]) == expected


@pytest.mark.parametrize('empty_card_numb', [1, True, 0.1, 500, -1, 3.14, None])
def test_get_mask_card_empty(empty_card_numb, expected="Ошибка типа данных"):
    """Проверка, что функция корректно обрабатывает входные строки,
     где отсутствует номер карт"""
    assert get_mask_card_number(empty_card_numb) == expected

def test_get_mask_card_empty_2():
    assert get_mask_card_number([]) == 'Ошибка типа данных'
    assert get_mask_card_number(0) == 'Ошибка типа данных'
    assert get_mask_card_number(" ") == 'Неверный формат номера карты'
    assert get_mask_card_number("Visa") == 'Неверный формат номера карты'


def test_get_mask_account():
    """Функция get_mask_account.
    Тестирование правильности маскирования номера счета"""
    assert get_mask_account("Счет 73654108430135874305") == "**4305"
    assert get_mask_account("Счет 73654108430135885503") == "**5503"


@pytest.mark.parametrize('new_string_account',
                         ("Счет 7365410843013581228", "Счет 73654108430188877678888"))
def test_get_mask_account_format(new_string_account, expected='Ошибка в номере счета карты'):
    """Проверка работы функции на различных входных форматах номеров карт,
     включая граничные случаи и нестандартные длины номер"""
    assert get_mask_account(new_string_account) == expected

@pytest.mark.parametrize('empty_account_numb', [1, True, 0.1, 500, -1, 3.14, None])
def test_get_mask_account_empty(empty_account_numb, expected_account="Ошибка типа данных"):
    """Проверка, что функция корректно обрабатывает входные строки,
     где отсутствует номер счета"""
    assert get_mask_account(empty_account_numb) == expected_account


def test_get_mask_account_empty_2(expected='Ошибка типа данных'):
    """Проверка, что функция корректно обрабатывает входные строки,
         где отсутствует номер счета"""
    assert get_mask_account(0) == expected
    assert get_mask_account([]) == expected


