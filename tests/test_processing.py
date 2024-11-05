import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("test_dict_for_search, expected", [([
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 41428829, "state": "EXECUTED", "date": "2020-05-02T18:35:29.512364"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
],
[
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 41428829, 'state': 'EXECUTED',  'date': '2020-05-02T18:35:29.512364'}])])
def test_filter_by_state(test_dict_for_search, expected):
    """Тестирование фильтрации списка словарей по заданному статусу state"""
    assert filter_by_state(test_dict_for_search) == expected


@pytest.mark.parametrize("test_dict_for_search", [([
    {"id": 594226727, "state": "-", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "FALL", "date": "2018-09-12T21:27:25.241689"},
])])
def test_filter_by_state_empty_executed(test_dict_for_search):
    """Проверка работы функции при отсутствии словарей с указанным статусом state в списке"""
    assert filter_by_state(test_dict_for_search) == []


@pytest.mark.parametrize("test_dict_for_search, state", [([
    {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
], "EXECUTED"),
([
    {"id": 594226727, "state": "FALL", "date": "2019-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "FALL", "date": "2020-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "FALL", "date": "2021-09-12T21:27:25.241689"},
], "FALL"),
([
    {"id": 594226727, "state": "CANCELED", "date": "2022-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2023-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2025-09-12T21:27:25.241689"},
], "CANCELED"),
])
def test_filter_by_state_various_state(test_dict_for_search, state, data_various_state):
    """Параметризация тестов для различных возможных значений статуса state"""
    assert filter_by_state(test_dict_for_search, state=state) == data_various_state


def test_sort_by_date_true(list_my_dict, list_my_dict_reverse_yes, revers=True):
    """Тестирование сортировки списка словарей по датам в порядке убывания."""
    assert sort_by_date(list_my_dict, sort_reverse=revers) == list_my_dict_reverse_yes


def test_sort_by_date_false(list_my_dict, list_my_dict_reverse_no, revers=False):
    """Тестирование сортировки списка словарей по датам в порядке возрастания."""
    assert sort_by_date(list_my_dict, sort_reverse=revers) == list_my_dict_reverse_no


def test_list_my_dict_same_dates(list_my_dict, list_my_dict_reverse_no, revers=False):
    """Проверка корректности сортировки при одинаковых датах."""
    assert sort_by_date(list_my_dict, sort_reverse=revers) == list_my_dict_reverse_no


def test_incorrect_type_dates_examination(incorrect_type_dates_examination, expected="Неверный формат даты"):
    """Тесты на работу функции с некорректными или нестандартными форматами дат."""
    assert sort_by_date(incorrect_type_dates_examination) == expected


