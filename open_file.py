def open_file(wordlist):
    """
    Opens a file.
    If the file is not found, it raises an exception and prints a message.
    Otherwise it returns the opent file.
    """
    try:
        file = open(wordlist, "r")
    except FileNotFoundError:
        print("File could not be found.")
    return file
