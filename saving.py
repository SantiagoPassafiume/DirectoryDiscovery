def saving(input):
    with open("discovery.txt", "a") as file:
        file.write(f"{input}\n")
