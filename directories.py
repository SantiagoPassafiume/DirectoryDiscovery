import discovery as d


target_url = input("[+] Enter Target URL (With Protocol): ")
file_name = input("[+] Enter Wordlist: ")
save_to_file = input("Do you want to save the output to a file? (yes/no): ")

d.discovery(file_name, target_url, save_to_file)
