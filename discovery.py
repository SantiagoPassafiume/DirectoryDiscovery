from colorama import Fore

from my_request import my_request
from saving import saving


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
                response = my_request(full_url)
                if response:
                    dir = f"/{directory} - [{response.status_code}]"
                    print(f"{Fore.GREEN}[+] {dir}")
                    if save.lower() == "yes":
                        saving(dir)
        except KeyboardInterrupt:
            print(f"{Fore.CYAN}The Execution Was Interrupted.")
