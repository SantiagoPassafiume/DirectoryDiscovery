from colorama import Fore

from my_request import my_request
from saving import saving
from open_file import open_file


def discovery(wordlist, url, save, output="discovery.txt"):
    """
    It receives 3 arguments (a wordlist, an URL and a save option).
    First it calls the "open_file" function and tries to open the wordlist, if it fails then the execution
    is stopped.

    If the wordlist is found, then it proceeds to generate requests through the "my_request" function.

    If the requests are sucessful, it means that the directory exists, so it outputs it (and saves it to a file if the option was specified).

    If at any point the Keyboard it's interrupted, it raises an exception and prints a message.
    """
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
                    saving(dir, output)
    except KeyboardInterrupt:
        print(f"{Fore.CYAN}The Execution Was Interrupted.")
