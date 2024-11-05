import pytest


@pytest.fixture
def new_string_card():
    return "Visa Gold 5999414228426353"


@pytest.fixture
def card_num_trace():
    card_num = "Visa Gold 5999414228426353"
    card_num_is_digit = card_num[-16:].isdigit()
    return card_num_is_digit


@pytest.fixture
def mask_card_duration():
    card = "Visa Gold 5999414228426353"
    card_is_digit = card[-16:].isdigit()
    if card_is_digit:
        len_card = len(card[-16:])
        return len_card



@pytest.fixture
def data_various_state(state):
    if state == "EXECUTED":
        dict_data = [
            {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        ]
    elif state == "FALL":
        dict_data = [
            {"id": 594226727, "state": "FALL", "date": "2019-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "FALL", "date": "2020-10-14T08:21:33.419441"},
            {"id": 594226727, "state": "FALL", "date": "2021-09-12T21:27:25.241689"},
        ]
    elif state == "CANCELED":
        dict_data = [
            {"id": 594226727, "state": "CANCELED", "date": "2022-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2023-10-14T08:21:33.419441"},
            {"id": 594226727, "state": "CANCELED", "date": "2025-09-12T21:27:25.241689"},
        ]
    return dict_data


@pytest.fixture
def list_my_dict():
    list_my_dict = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 41428829, "state": "EXECUTED", "date": "2020-05-02T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    return list_my_dict


@pytest.fixture
def list_my_dict_reverse_yes():
    my_dict_reverse = [
        {"id": 41428829, "state": "EXECUTED", "date": "2020-05-02T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    return my_dict_reverse


@pytest.fixture
def list_my_dict_reverse_no():
    my_dict_reverse = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2020-05-02T18:35:29.512364"},
    ]
    return my_dict_reverse


@pytest.fixture
def incorrect_type_dates_examination():
    dict_incorrect_type_exam = [
        {"id": 41428829, "state": "EXECUTED", "date": "31st of February, 2023T18:35:30.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "31-02-2023T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2023-02T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "31.02.2023T08:21:33.419441"},
        {"id": 939719570, "state": "EXECUTED", "date": "2023/02/31T02:08:58.425572"},
    ]
    return dict_incorrect_type_exam
