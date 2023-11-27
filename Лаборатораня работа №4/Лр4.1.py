# TODO решите задачу
import json


def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    all_ = 0
    for item in data:
        point = item.get('score', 0)
        weg = item.get('weight', 0)
        item = point * weg
        all_ += item
    return round(all_, 3)


print(task())
