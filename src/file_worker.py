import os

from src import csv_support, json_support

def create_files(params: dict[str, list[tuple[str, str]]], csv: bool, json: bool) -> None:
    for el in params.items():
        month = el[0]
        for day, daytime in el[1]:
            path = os.path.join(os.getcwd(), month, day, daytime)

            if csv:
                csv_support.write_csv(path)
            if json:
                json_support.write_json(path)



def read_files(params: dict[str, list[tuple[str, str]]], csv: bool, json: bool) -> int:
    result: int = 0

    for el in params.items():
        month = el[0]
        for day, daytime in el[1]:
            path = os.path.join(os.getcwd(), month, day, daytime)

            if csv:
                result = result + csv_support.read_csv(path)
            if json:
                result = result + json_support.read_json(path)

    return result
