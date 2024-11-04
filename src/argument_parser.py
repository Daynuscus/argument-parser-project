import argparse
import csv
import json
import os
import random
from enum import IntEnum

class Week:
    class EnumWeek(IntEnum):
        pn = 0
        wt = 1
        śr = 2
        cz = 3
        pt = 4
        sb = 5
        nd = 6
        
    week = ['pn', 'wt', 'śr', 'cz', 'pt', 'sb', 'nd']
    week_full = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']

def en_list(string: str) -> list[str]:
    return [i.strip() for i in string[1:-1].replace('"',"").split(',')]

def expand(fro: str, to: str) -> list[str]:

    start = Week.EnumWeek[fro]
    end = Week.EnumWeek[to]
    if start <= end:
        return Week.week[start:end + 1]
    else:
        return Week.week[start:] + Week.week[:end + 1]


def unpack(daytime: str):
    if daytime in Week.week:
        return Week.week_full[Week.EnumWeek[daytime]]
        
    return 'wieczorem' if daytime == 'w' else 'rano'


def create_files(params: dict[str, list[tuple[str, str]]], csv_flag: bool, json_flag: bool) -> None:
    for el in params.items():
        month = el[0]
        for day, daytime in el[1]:
            path = os.path.join(os.getcwd(), month, day)
            if not os.path.exists(path):
                os.makedirs(path)
            path = os.path.join(path, daytime)

            if csv_flag:
                write_csv(path)
            if json_flag:
                write_json(path)



def read_files(params: dict[str, list[tuple[str, str]]], csv_flag: bool, json_flag: bool) -> int:
    result: int = 0

    for el in params.items():
        month = el[0]
        for day, daytime in el[1]:
            path = os.path.join(os.getcwd(), month, day)
            if not os.path.exists(path):
                os.makedirs(path)
            path = os.path.join(path, daytime)

            if csv_flag:
                result = result + read_csv(path)
            if json_flag:
                result = result + read_json(path)

    return result



def parse() -> tuple[dict, bool, bool, bool]:
    parser = argparse.ArgumentParser(description = "Project Management Tool")

    # Positional arguments
    parser.add_argument('month_list')
    parser.add_argument('week_list')
    parser.add_argument('daytime_list')

    # Optional flags
    parser.add_argument('-t', action = 'store_true')
    parser.add_argument('-c', action = 'store_true')
    parser.add_argument('-j', action = 'store_true')

    # For testing purposes
    args = parser.parse_args(['[styczeń, luty]', '[pn-śr, pt-sb]', '[r, w, w]', '-t', '-c', '-j'])

    month_list = en_list(args.month_list)
    week_list = en_list(args.week_list)
    daytime_list = en_list(args.daytime_list)

    paths: dict[str, list[tuple[str, str]]] = {}
    daytime_index: int = 0
    for idx, month in enumerate(month_list):

        if idx < len(week_list):
            week_entries = week_list[idx]
        else:
            week_entries = week_list[-1]  # Use the last entry if not enough entries

        days = []
        entry = week_entries.strip()
        if '-' in entry:
            fr, to = entry.split('-')
            days.extend(expand(fr, to))
        else:
            days.append(entry)

        times = []
        for day in days:
            daytime = unpack(daytime_list[daytime_index]) if daytime_index < len(daytime_list) else 'rano'
            daytime_index += 1

            times.append((unpack(day), daytime))

        paths[month] = times  

    return (paths, args.t, args.c, args.j)


def read_csv(path):
    with open(path, 'r') as plik:
        dane = csv.DictReader(plik, delimiter=';')
        for row in dane:
            if row['Model'] == 'A':
                return int(row['Czas'][0:-1])
            else:
                return 0
    return


def write_csv(path):
    model = ord('A') + random.randint(0, 2)
    model = chr(model)
    wynik = str(random.randint(0, 1000))
    czas = str(random.randint(0, 1000)) + 's'

    data = [
        ['Model', 'Wynik', 'Czas'],
        [model, wynik, czas]
    ]

    with open(path, 'w', newline='') as plik:
        dane = csv.writer(plik, delimiter=';')
        dane.writerows(data)
    return


def read_json(path):
    with open(path, 'r') as file:
        data = json.load(file)
    if(data["Model"] == 'A'):
        wynik = data["Czas"]
        wynik = wynik[0:-1]
        wynik = int(wynik)
        return wynik
    else:
        return 0


def write_json(path):
    model = ord('A') + random.randint(0, 2)
    model = chr(model)
    wynik = str(random.randint(0, 1000))
    czas = str(random.randint(0, 1000)) + 's'

    data = {
        "Model": model,
        "Wynik": wynik,
        "Czas": czas
    }

    with open(path, 'w') as file:
        json.dump(data, file)

    return


def main() -> None:
    paths: dict[str, list[tuple[str, str]]] 
    t_flag: bool
    csv_flag: bool
    json_flag: bool


    paths, t_flag, csv_flag, json_flag = parse()

    


if __name__ == '__main__':
    main()
