from advent_of_code_2023.day3_2 import core


def test_core():
    data = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]
    possible_games = core(data)

    assert sum(possible_games) == 467835
