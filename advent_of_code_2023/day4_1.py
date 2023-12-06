import sys


def load_input(data_path):
    data = []
    with open(data_path, "r") as reader:
        data = reader.readlines()
    return data


def core(data):
    r = []
    for card in data:
        numbers = card.split(":")
        length = len(
            set(numbers[1].split("|")[0].split())
            & set(numbers[1].split("|")[1].split())
        )
        if length > 2:
            r.append(2 ** (length - 1))
        else:
            r.append(length)
    return r


def calculate_output(data):
    return sum(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        data = load_input(path)
        ouput_data = core(data)
        final_sum = calculate_output(ouput_data)
        print(final_sum)
