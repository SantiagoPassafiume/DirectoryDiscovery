from measure_file import measure_file
import discovery as d
import concurrent.futures
from divide_file import dividing
import time


start = time.perf_counter()

target_url = input("[+] Enter Target URL (With Protocol): ")
wordlist = input("[+] Enter Wordlist: ")
save_to_file = input("[+] Do you want to save the output to a file? (yes/no): ")
threads = int(input("[+] How many threads do you want to use?: "))


dict = dividing(wordlist, measure_file(wordlist) / threads)

with concurrent.futures.ThreadPoolExecutor() as executor:
    count = 0
    for _ in range(0, threads):
        executor.submit(d.discovery, dict[f"dir{count}"], target_url, save_to_file)
        count += 1

finish = time.perf_counter()

print(len(wordlist))
print(f"Finished in {finish-start, 2} second(s)")
