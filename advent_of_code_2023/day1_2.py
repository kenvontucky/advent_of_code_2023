import pathlib
import sys

NUMBERS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def load_input(data_path):
    data = []
    with open(data_path, "r") as reader:
        data = reader.readlines()
    return data


def numerify(entry, order=0):
    if order == -1:
        entry = entry[::-1]

    copy_str = entry
    for index, letter in enumerate(entry):
        for value, key in enumerate(NUMBERS):
            if order == -1:
                key = key[::-1]

            is_number_str = entry[index : index + len(key)]
            if is_number_str in key and len(is_number_str) >= 3:
                copy_str = copy_str.replace(key, str(value))
    if order == -1:
        copy_str = copy_str[::-1]
    return copy_str


def map_str_2_number(data):
    res = []
    for item in data:
        copy_str = f"{numerify(item, 0)}{numerify(item, -1)}"
        res.append(copy_str)
    return res


def check_calibration(data):
    numbers = []
    for x in data:
        if x.isnumeric():
            numbers.append(x)
    if len(numbers) == 1:
        return int(f"{numbers[0]}{numbers[0]}")
    elif len(numbers) > 1:
        return int(f"{numbers[0]}{numbers[-1]}")


def trebuchet(data):
    r = []
    for item in data:
        r.append(check_calibration(item))
    return r


def save_output(data):
    with open("output/day_two.txt", "w") as writer:
        for item in data:
            writer.write(f"{item}\n")


def calculate_output(data):
    print(sum(data))


if __name__ == "__main__":
    for path in sys.argv[1:]:
        data = load_input(path)
        clean_data = map_str_2_number(data)
        ouput_data = trebuchet(clean_data)
        save_output(ouput_data)
        calculate_output(ouput_data)
