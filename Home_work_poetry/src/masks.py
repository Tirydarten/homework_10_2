def get_mask_card_number(number: str) -> str:
    """Функция принимает строку и возвращает маски карты"""
    new_string_card = f"{number[0:4]} {number[4:6]}** **** {number[12:]}"
    return new_string_card


def get_mask_account(number: str) -> str:
    """Функция принимает строку и возвращает маски счёта"""
    new_string_account = f"**{number[-4:]}"
    return new_string_account
