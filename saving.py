def saving(input, name):
    """Saves whatever it receives into a file called 'discovery.txt'"""
    with open(name, "a") as file:
        file.write(f"{input}\n")
