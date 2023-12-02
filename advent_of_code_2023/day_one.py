import pathlib
import sys


def load_input(data_path):
    data = []
    with open(data_path, "r") as reader:
        data = reader.readlines()
    return data


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
    with open("day_one_output.txt", "w") as writer:
        for item in data:
            writer.write(f"{item}\n")


def calculate_output(data):
    print(sum(data))


if __name__ == "__main__":
    for path in sys.argv[1:]:
        data = load_input(path)
        ouput_data = trebuchet(data)
        save_output(ouput_data)
        calculate_output(ouput_data)
