import src.processing
from src.widget import get_new_data, mask_account_card

print(mask_account_card("Visa Gold 5999414228426353"))

print(mask_account_card("Счет 73654108430135874305"))

print(get_new_data("2018-07-11T02:26:18.671407"))

src.processing.sort_by_date(
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 41428829, "state": "EXECUTED", "date": "2020-05-02T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
)
