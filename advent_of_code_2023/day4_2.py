import sys


def load_input(data_path):
    data = []
    with open(data_path, "r") as reader:
        data = reader.readlines()
    return data


def core(data):
    r = len(data)
    for index, card in enumerate(data):
        numbers = card.split(":")
        length = len(
            set(numbers[1].split("|")[0].split())
            & set(numbers[1].split("|")[1].split())
        )
        r += length
        card_number = int(numbers[0].split()[1])

        for j in range(1, length + 1):
            tmp = card_number + j
            data.append(data[tmp - 1])

    return r


def calculate_output(data):
    return sum(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        data = load_input(path)
        ouput_data = core(data)
        print(ouput_data)
