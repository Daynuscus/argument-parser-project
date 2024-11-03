import random
import json

def read_json(path):
    with open(path, 'r') as file:
        data = json.load(file)  
    return data


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

if __name__ == "__main__":
    print('XD')
    write_json("testing.json")
    print(read_json("testing.json"))
    print('XD')



























































