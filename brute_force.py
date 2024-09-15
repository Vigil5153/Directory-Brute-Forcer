import requests
import time
import sys
import os

def directory_brute_force(url, wordlist):
    # Check if the wordlist file exists
    if not os.path.exists(wordlist):
        print(f"[!] Error: Wordlist file '{wordlist}' not found.")
        return

    with open(wordlist, 'r') as file:
        directories = file.readlines()

    if not directories:
        print(f"[!] Error: Wordlist '{wordlist}' is empty.")
        return
    
    found_directories = []

    print(f"\nStarting directory brute force on: {url}")
    
    for idx, directory in enumerate(directories, start=1):
        directory = directory.strip()
        full_url = f"{url}/{directory}"

        # loading animation
        sys.stdout.write(f"\rAnalyzing directory {idx}...")
        sys.stdout.flush()

        try:
            response = requests.get(full_url, timeout=5, verify=True)

            if response.status_code == 200:
                found_directories.append(full_url)

        except requests.exceptions.ConnectTimeout:
            print(f"\n[!] Connection timed out while trying to access {full_url}. Skipping...")

        except requests.exceptions.SSLError:
            print(f"\n[!] SSL error encountered with {full_url}. Skipping...")

        except requests.exceptions.ConnectionError:
            print(f"\n[!] Connection error occurred while trying to access {full_url}. Skipping...")

        except requests.exceptions.InvalidURL:
            print(f"\n[!] Invalid URL: {full_url}. Skipping...")

        except requests.exceptions.RequestException as e:
            print(f"\n[!] Request error: {e}. Skipping {full_url}...")

        time.sleep(0.1)  # small delay to simulate loading
    
    sys.stdout.write("\n\n[+] Scan complete!\n")
    if found_directories:
        print("[+] Found directories:")
        for directory in found_directories:
            print(f"[+] {directory}")
    else:
        print("[-] No directories found or directories are hidden or protected.")

if __name__ == "__main__":
    print('''
    ===========================================
           Directory Brute Forcer v1.0
    ===========================================
    A tool for brute-forcing directories on a
    target URL using a customizable wordlist.
    -------------------------------------------
    ''')

    target_url = input("Enter the target URL (e.g., http://example.com): ")
    wordlist_path = input("Enter the path to your wordlist (default: wordlist.txt): ") or 'wordlist.txt'
    directory_brute_force(target_url, wordlist_path)
    print("[+] Job complete.")
