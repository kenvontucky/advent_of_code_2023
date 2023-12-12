import sys


def load_input(data_path):
    data = []
    with open(data_path, "r") as reader:
        data = reader.readlines()
    return data


def core(data):
    almanac = {}

    seeds = None
    stsm = False
    stfm = False

    for line in data:
        line = line.strip()
        if line.startswith("seeds"):
            seeds = line.split(":")[1].split()
            seeds.sort()
            for seed in seeds:
                almanac.update(
                    {
                        int(seed): {
                            "soil": None,
                            "fertilizer": None,
                            "water": None,
                            "light": None,
                            "temperature": None,
                            "humidity": None,
                            "location": None,
                        }
                    }
                )

        # seed to soil
        if line.startswith("seed-to-soil map"):
            stsm = True
            continue

        if stsm and line != "":
            d = line.split()
            seeds_tmp = list(range(int(d[1]), int(d[1]) + int(d[2])))
            soil_tmp = [int(d[0]) + x for x in range(len(seeds_tmp))]
            for index, seed in enumerate(seeds_tmp):
                if not almanac.get(seed):
                    almanac.update(
                        {
                            seed: {
                                "soil": None,
                                "fertilizer": None,
                                "water": None,
                                "light": None,
                                "temperature": None,
                                "humidity": None,
                                "location": None,
                            }
                        }
                    )
                almanac[seed].update({"soil": soil_tmp[index]})
        else:
            stsm = False

        # soil to fertilizer
        if line.startswith("soil-to-fertilizer map"):
            stfm = True
            continue

        if stfm and line != "":
            d = line.split()
            soil_tmp = list(range(int(d[1]), int(d[1]) + int(d[2])))
            fert_tmp = [int(d[0]) + x for x in range(len(soil_tmp))]
            for index, soil in enumerate(soil_tmp):
                seeds = list(filter(lambda x: almanac[x]["soil"] == soil, almanac))
                for seed in seeds:
                    if not almanac.get(seed):
                        almanac.update(
                            {
                                seed: {
                                    "soil": None,
                                    "fertilizer": None,
                                    "water": None,
                                    "light": None,
                                    "temperature": None,
                                    "humidity": None,
                                    "location": None,
                                }
                            }
                        )
                    almanac[seed].update({"fertilizer": fert_tmp[index]})
        else:
            stfm = False

    return data


def calculate_output(data):
    return sum(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        data = load_input(path)
        ouput_data = core(data)
        final_sum = calculate_output(ouput_data)
        print(final_sum)
