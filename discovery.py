from colorama import Fore

from my_request import my_request
from saving import saving


def discovery(wordlist, url, save, output="discovery.txt"):
    try:
        for item in wordlist:
            directory = item
            full_url = f"{url}/{directory}"
            response = my_request(full_url)
            if response:
                dir = f"/{directory} - [{response.status_code}]"
                print(f"{Fore.GREEN}[+] {dir}")
                if save.lower() == "yes":
                    saving(dir, output)
    except KeyboardInterrupt:
        print(f"{Fore.CYAN}The Execution Was Interrupted.")
