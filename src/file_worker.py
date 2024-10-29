# wszystko można poprawić w razie konieczności

import os


def create_files(params: dict[str, list[tuple[str, str]]], csv: bool, json: bool) -> None:
    for el in params.items():
        m = el[0]

        for d,p in el[1]:
            path = os.path.join(os.getcwd(), m, d, p)

            if csv:
                csv_worker.write(path)
            if json:
                json_worker.write(path)



def read_files(params: dict[str, list[tuple[str, str]]], csv: bool, json: bool) -> tuple[int, int]:
    csv_result: int = 0
    json_result: int = 0

    for el in params.items():
        m = el[0]
        for d,p in el[1]:
            path = os.path.join(os.getcwd(), m, d, p)

            if csv:
                csv_result = csv_result + csv_worker.read(path)
            if json:
                json_result = json_result + json_worker.read(path)

    return csv_result, json_result
