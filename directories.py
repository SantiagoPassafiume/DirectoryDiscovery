import requests
from colorama import Fore


def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


def discovery(wordlist, url):
    try:
        file = open(wordlist, "r")
    except FileNotFoundError:
        print("File could not be found.")
    else:
        for line in file:
            directory = line.strip()
            full_url = f"{url}/{directory}"
            response = request(full_url)
            if response:
                print(f"{Fore.GREEN}[+] /{directory} - [{response.status_code}]")


target_url = input("[+] Enter Target URL (With Protocol): ")
file_name = input("[+] Enter Wordlist: ")

discovery(file_name, target_url)
