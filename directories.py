import requests
from colorama import Fore


def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


def saving(input):
    with open("discovery.txt", "a") as file:
        file.write(f"{input}\n")


def discovery(wordlist, url, save):
    try:
        file = open(wordlist, "r")
    except FileNotFoundError:
        print("File could not be found.")
    else:
        try:
            for line in file:
                directory = line.strip()
                full_url = f"{url}/{directory}"
                response = request(full_url)
                if response:
                    dir = f"/{directory} - [{response.status_code}]"
                    print(f"{Fore.GREEN}[+] {dir}")
                    if save.lower() == "yes":
                        saving(dir)
        except KeyboardInterrupt:
            print(f"{Fore.CYAN}The Execution Was Interrupted.")


target_url = input("[+] Enter Target URL (With Protocol): ")
file_name = input("[+] Enter Wordlist: ")
save_to_file = input("Do you want to save the output to a file? (yes/no): ")


discovery(file_name, target_url, save_to_file)
