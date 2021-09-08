def write_to_file(filename, data):
    with open(filename, "a") as file:
        file.write(data)


def dividing(filename, line_count=10000, name_of_chunks="list"):
    f = open(filename, "r")
    count = 0
    file_count = 0
    final_name = f"{name_of_chunks}{file_count}.txt"
    create_file(final_name)
    for line in f:
        if count == line_count:
            count = 0
            file_count += 1
            print(f"FILE COUNT IS {file_count}")
            final_name = f"{name_of_chunks}{file_count}.txt"
            create_file(final_name)
        else:
            count += 1
            write_to_file(final_name, line)


def create_file(filename):
    with open(filename, "a") as file:
        pass
