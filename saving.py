def saving(input):
    """Saves whatever it receives into a file called 'discovery.txt'"""
    with open("discovery.txt", "a") as file:
        file.write(f"{input}\n")
