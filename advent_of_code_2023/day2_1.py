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

    for entry in cube_set:
        draft = entry.split(", ")
        for cube in draft:
            amount, color = cube.split()

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
        if game_check(game):
            possible_games.append(int(number))
    return possible_games


def save_output(data):
    with open("output/2_1.txt", "w") as writer:
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
