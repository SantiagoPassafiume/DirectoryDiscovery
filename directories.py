import discovery as d
import concurrent.futures


target_url = input("[+] Enter Target URL (With Protocol): ")
file_name = input("[+] Enter Wordlist: ")
save_to_file = input("[+] Do you want to save the output to a file? (yes/no): ")
if save_to_file.lower() == "yes":
    output_file = input(
        '[+] Please enter the name of the output file (default="discovery.txt"): '
    )


# if output_file:
#     d.discovery(file_name, target_url, save_to_file, output_file)
# else:
#     d.discovery(file_name, target_url, save_to_file)

with concurrent.futures.ThreadPoolExecutor() as executor:
    for _ in range(10):
        executor.submit(d.discovery, file_name, target_url, save_to_file, output_file)
