import concurrent.futures
from utility import *
import time


start = time.perf_counter()

target_url = input("[+] Enter Target URL (With Protocol): ")
wordlist = input("[+] Enter Wordlist: ")


dict = dividing(wordlist, 1000)

with concurrent.futures.ThreadPoolExecutor() as executor:
    for count in range(0, 5):
        executor.submit(discovery, dict[f"dir{count}"], target_url)

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")
