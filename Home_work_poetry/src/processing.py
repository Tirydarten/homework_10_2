def filter_by_state(dict_for_search: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и опционально значение для ключа state ('по умолчанию'EXECUTED') и
    возвращает новый список словарей,у которых ключ state соответствует указанному значению"""
    new_dicts = []
    for i in range(len(dict_for_search)):
        if dict_for_search[i]["state"] == state:
            new_dicts.append(dict_for_search[i])
    return new_dicts


my_dict = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 41428829, "state": "EXECUTED", "date": "2020-05-02T18:35:29.512364"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

results = filter_by_state(my_dict)


def sort_by_date(new_dicts: list, sort_reverse: bool = True) -> list:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — сортировка по убыванию, т. е. сначала самые последние операции)"""
    sorted_date = sorted(new_dicts, key=lambda new_dict: new_dict["date"], reverse=sort_reverse)
    return sorted_date


fix_result = sort_by_date(results)
print(f"отсортировано по 'state' и 'date', {fix_result}")
