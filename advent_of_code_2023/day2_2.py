import sys


def load_input(data_path):
    data = []
    with open(data_path, "r") as reader:
        data = reader.readlines()
    return data


def game_number(game):
    return game.split(":")[0].split(" ")[1]


def game_power_of_set(game):
    cube_set = game.split(":")[1].split(";")

    cube_ref = {"red": 0, "green": 0, "blue": 0}

    for entry in cube_set:
        draft = entry.split(", ")
        for cube in draft:
            amount, color = cube.split()

            if color == "red":
                cube_ref["red"] = max(int(amount), cube_ref["red"])
            elif color == "green":
                cube_ref["green"] = max(int(amount), cube_ref["green"])
            elif color == "blue":
                cube_ref["blue"] = max(int(amount), cube_ref["blue"])
    return cube_ref["red"] * cube_ref["green"] * cube_ref["blue"]


def core(data):
    r = []
    for game in data:
        r.append(game_power_of_set(game))
    return r


def save_output(data):
    with open("output/2_2.txt", "w") as writer:
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
