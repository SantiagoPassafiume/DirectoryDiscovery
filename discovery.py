from colorama import Fore

from my_request import my_request
from saving import saving
from open_file import open_file


def discovery(wordlist, url, save):
    file = open_file(wordlist)
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
