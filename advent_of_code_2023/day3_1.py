import sys


def load_input(data_path):
    data = []
    with open(data_path, "r") as reader:
        data = reader.readlines()
    return data


def top(row, index, data):
    if row != 0:
        c = data[row - 1][index]
        l = data[row - 1][:index].split(".")[-1]
        r = data[row - 1][index:].split(".")[0]
        return l + r


def top_right(row, index, data):
    if row != 0 and index < len(data[row]) - 1:
        c = data[row - 1][index + 1]
        l = data[row - 1][: index + 1].split(".")[-1]
        r = data[row - 1][index + 1 :].split(".")[0]
        return l + r


def right(row, index, data):
    if index < len(data[0]) - 1:
        return data[row][index + 1 :].split(".")[0]


def right_bottom(row, index, data):
    if row < (len(data) - 1) and index < len(data[0]) - 1:
        c = data[row + 1][index + 1]
        l = data[row + 1][: index + 1].split(".")[-1]
        r = data[row + 1][index + 1 :].split(".")[0]
        return l + r


def bottom(row, index, data):
    if row < (len(data) - 1):
        c = data[row + 1][index]
        l = data[row + 1][:index].split(".")[-1]
        r = data[row + 1][index:].split(".")[0]
        return l + r


def bottom_left(row, index, data):
    if row < (len(data) - 1) and index > 0:
        c = data[row + 1][index - 1]
        l = data[row + 1][: index - 1].split(".")[-1]
        r = data[row + 1][index - 1 :].split(".")[0]
        return l + r


def left(row, index, data):
    if index > 0:
        return data[row][:index].split(".")[-1]


def left_top(row, index, data):
    if row != 0 and index > 0:
        c = data[row][index]
        l = data[row][:index].split(".")[-1]
        r = data[row][index:].split(".")[0]
        return l + r


def core(data):
    r = []
    row = 0
    for entry in data:
        top_layer = []
        middle_layer = []
        lower_layer = []
        for index, value in enumerate(entry):
            if value.isnumeric() or value == ".":
                continue

            number = top(row, index, data)
            if number is not None and number.isnumeric():
                top_layer.append(int(number))

            number = top_right(row, index, data)
            if number is not None and number.isnumeric():
                top_layer.append(int(number))

            number = right(row, index, data)
            if number is not None and number.isnumeric():
                middle_layer.append(int(number))

            number = right_bottom(row, index, data)
            if number is not None and number.isnumeric():
                lower_layer.append(int(number))

            number = bottom(row, index, data)
            if number is not None and number.isnumeric():
                lower_layer.append(int(number))

            number = bottom_left(row, index, data)
            if number is not None and number.isnumeric():
                lower_layer.append(int(number))

            number = left(row, index, data)
            if number is not None and number.isnumeric():
                middle_layer.append(int(number))

            number = left_top(row, index, data)
            if number is not None and number.isnumeric():
                top_layer.append(int(number))

        r = r + list(set(top_layer)) + list(set(middle_layer)) + list(set(lower_layer))
        row += 1
    return r


def calculate_output(data):
    return sum(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        data = load_input(path)
        ouput_data = core(data)
        final_sum = calculate_output(ouput_data)
        print(final_sum)
