import discovery as d
import concurrent.futures
from divide_file import dividing
import time


start = time.perf_counter()

target_url = input("[+] Enter Target URL (With Protocol): ")
wordlist = input("[+] Enter Wordlist: ")
save_to_file = input("[+] Do you want to save the output to a file? (yes/no): ")
# if save_to_file.lower() == "yes":
#     output_file = input(
#         '[+] Please enter the name of the output file (default="discovery.txt"): '
#     )


# if output_file:
#     d.discovery(wordlist, target_url, save_to_file, output_file)
# else:
#     d.discovery(wordlist, target_url, save_to_file)

# threads = int(input("How many threads do you want to use?: "))

dividing(wordlist, 1000, "list")

with concurrent.futures.ThreadPoolExecutor() as executor:
    count = 0
    for _ in range(0, 5):
        executor.submit(d.discovery, f"list{count}.txt", target_url, save_to_file)
        count += 1

finish = time.perf_counter()

print(f"Finished in {finish-start, 2} second(s)")
