import requests
from colorama import Fore


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


def saving(input, name):
    """Saves whatever it receives into a file called 'discovery.txt'"""
    with open(name, "a") as file:
        file.write(f"{input}\n")


def my_request(url):
    """
    It tries to do a get request to the URL received.
    If it fails, it raises an exception and passes.
    """
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


def discovery(wordlist, url):
    try:
        for item in wordlist:
            directory = item
            full_url = f"{url}/{directory}"
            response = my_request(full_url)
            if response:
                dir = f"/{directory} - [{response.status_code}]"
                print(f"{Fore.GREEN}[+] {dir}")
                saving(dir, "discovery.txt")
    except KeyboardInterrupt:
        print(f"{Fore.CYAN}The Execution Was Interrupted.")


def measure_file(file):
    f = open(file, "r")
    nonempty_lines = [line.strip("\n") for line in f if line != "\n"]
    line_count = len(nonempty_lines)
    f.close()
    return line_count
