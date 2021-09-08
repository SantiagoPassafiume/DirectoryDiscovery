def measure_file(file):
    f = open(file, "r")
    nonempty_lines = [line.strip("\n") for line in f if line != "\n"]
    line_count = len(nonempty_lines)
    f.close()
    return line_count
