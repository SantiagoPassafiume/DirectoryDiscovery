def open_file(wordlist):
    try:
        file = open(wordlist, "r")
    except FileNotFoundError:
        print("File could not be found.")
    return file
