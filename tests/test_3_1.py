from advent_of_code_2023.day3_1 import core, calculate_output


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
        "..........",
        "........$1",
    ]
    possible_games = core(data)

    assert sum(possible_games) == 4362


def test_bottom_left_single():
    data = [
        "...",
        "1$.",
    ]
    possible_games = core(data)

    assert sum(possible_games) == 1


def test_bottom_right_single():
    data = [
        "...",
        ".$1",
    ]
    possible_games = core(data)

    assert sum(possible_games) == 1


def test_bottom_right_eol():
    data = [
        ".....\n",
        ".$939\n",
        ".....\n",
    ]
    possible_games = core(data)

    assert sum(possible_games) == 939


def test_bottom_left():
    data = [
        "....",
        "21$.",
    ]
    possible_games = core(data)

    assert sum(possible_games) == 21


def test_bottom_right():
    data = [
        "....",
        ".$21",
    ]
    possible_games = core(data)

    assert sum(possible_games) == 21


def test_left():
    data = [
        "21$.",
        "....",
    ]
    possible_games = core(data)

    assert sum(possible_games) == 21


def test_top_right():
    data = [
        ".$21",
        "....",
    ]
    possible_games = core(data)

    assert sum(possible_games) == 21


def test_top_top_right():
    data = [
        ".45.",
        ".$21",
        "....",
    ]
    possible_games = core(data)

    assert sum(possible_games) == 66


def test_diag():
    data = [
        ".1.2.",
        "..%..",
        ".3.4.",
    ]
    possible_games = core(data)

    assert sum(possible_games) == 10


def test_complete():
    data = [
        ".45.",
        "4$21",
        "23..",
    ]
    possible_games = core(data)

    assert sum(possible_games) == 93
