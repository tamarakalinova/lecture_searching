import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if field not in data:
        return None

    return data[field]


def linear_search(sequence, target_num):
    positions = []
    count = 0

    for i, value in enumerate(sequence):
        if value == target_num:
            positions.append(i+1)
            count += 1

    return {"Positions": positions, "Count": count}

def main():
    file_name = "sequential.json"

    sequential_data = read_data(file_name, field="unordered_numbers")
    print(f"Data: {sequential_data}")

    target_num = 5
    result = linear_search(sequential_data, target_num)

    print("Výsledky vyhledávání:")
    print(f"Pozice: {result['Positions']}")
    print(f"Počet: {result['Count']}")

if __name__ == '__main__':
    main()