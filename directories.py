import requests


def request(url):
    try:
        return requests.get(f"http://{url}")
    except requests.exceptions.ConnectionError:
        pass


target_url = input("[+] Enter Target URL: ")
file_name = input("[+] Enter Wordlist: ")

try:
    file = open(file_name, "r")
except FileNotFoundError:
    print("File could not be found.")
else:
    for line in file:
        directory = line.strip()
        full_url = f"{target_url}/{directory}"
        response = request(full_url)
        if response:
            print(f"[+] /{directory} - [{response.status_code}]")
