import pathlib
import sys


def load_input(data_path):
    data = []
    with open(data_path, "r") as reader:
        data = reader.readlines()
    return data


def game_number(game):
    return game.split(":")[0].split(" ")[1]


def game_check(game):
    cube_set = game.split(":")[1].split(";")

    red_amount = 0
    green_amount = 0
    blue_amount = 0

    for entry in cube_set:
        draft = entry.split(", ")
        for cube in draft:
            cube_detail = cube.split(" ")
            color = cube_detail[1]
            amount = cube_detail[0]

            if color == "red":
                red_amount += int(amount)
            elif color == "green":
                green_amount += int(amount)
            elif color == "blue":
                blue_amount += int(amount)

    if red_amount >= 12 or green_amount >= 13 or blue_amount >= 14:
        return False
    return True


def game_check_alt(game):
    cube_set = game.split(":")[1].split(";")

    for entry in cube_set:
        draft = entry.split(", ")
        for cube in draft:
            cube_detail = cube.split(" ")
            color = cube_detail[1]
            amount = cube_detail[0]

            if color == "red" and int(amount) > 12:
                return False
            elif color == "green" and int(amount) > 13:
                return False
            elif color == "blue" and int(amount) > 14:
                return False
    return True


def core(data):
    possible_games = []
    for game in data:
        number = game_number(game)
        if game_check_alt(game):
            possible_games.append(int(number))
    return possible_games


def save_output(data):
    with open("output/day_two.txt", "w") as writer:
        for item in data:
            writer.write(f"{item}\n")


def calculate_output(data):
    return sum(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        data = load_input(path)
        ouput_data = core(data)
        save_output(ouput_data)
        final_sum = calculate_output(ouput_data)
        print(final_sum)
