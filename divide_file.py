# def write_to_file(filename, data):
#     with open(filename, "a") as file:
#         file.write(data)


def dividing(filename, line_count=10000):
    f = open(filename, "r")
    count = 0
    dir_count = 0
    dict = {"dir0": []}

    for line in f:
        if count == line_count:
            count = 0
            dir_count += 1
            dict[f"dir{dir_count}"] = []
        else:
            count += 1
            dict[f"dir{dir_count}"].append(line.strip())
    return dict


# def create_file(filename):
#     with open(filename, "a") as file:
#         pass
