import json


def write_order_to_json(item, quantity, price, buyer, date):
    FILE_PATH = './task_files/orders.json'
    dict_to_json = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    }

    with open(FILE_PATH, 'w') as f_n:
        json.dump(dict_to_json, f_n, sort_keys=True, indent=4)


write_order_to_json('phone', 1, 58000, 'Alexandr', '19.02.2021')