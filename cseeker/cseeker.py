#!/usr/bin/env python3
import requests, time, sys, os


RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m" 
CYAN   = "\033[96m"
WHITE  = "\033[97m"
PURPLE = "\033[95m"
RESET  = "\033[0m"

def clear():
    os.system("clear")

def banner():
  
    print(BLUE + """
  ░█▀▀░█▀█░█░█░▀█▀░█▀▀░█░█░█▀▀░█▀▄
  ░█░░░█▀▀░█▀█░░█░░▀▀█░█▀█░█▀▀░█▀▄
  ░▀▀▀░▀░░░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀ 2.3.5
    """ + RESET)

def request(url):
    try:

        return requests.get("http://" + url, timeout=5)
    except:
        return None

def loading(text):
    for i in range(6):
        sys.stdout.write("\r" + BLUE + text + "." * i + RESET)
        sys.stdout.flush()
        time.sleep(0.4)
    print()

def start_scanner():
    while True: 
        clear()
        banner()
        
       
        print(BLUE + " [" + WHITE + "::" + BLUE + "]" + YELLOW + " C-Seeker Sub-Menu " + BLUE + "[" + WHITE + "::" + BLUE + "] \n" + RESET)
        print(RED + " [" + WHITE + "01" + RED + "]" + YELLOW + " Discover Files (Directories)")
        print(RED + " [" + WHITE + "02" + RED + "]" + YELLOW + " Discover Subdomains")
        print(RED + " [" + WHITE + "03" + RED + "]" + YELLOW + " Full Website Report")
        print(RED + " [" + WHITE + "00" + RED + "]" + YELLOW + " Back to Main Menu (Cphisher)")

        choice = input(RED + "\n [-] Select an option : " + RESET)

        if choice == "01":
            clear()
            banner()
            targets_url = input(YELLOW + '[+] Enter Target URL (e.g., google.com): ' + RESET)
            loading("[*] Searching for Directories")
            try:
             
                with open("/home/sayyaf/Desktop/project/file.txt") as wordlists_file:
                    for line in wordlists_file:
                        word = line.strip()
                        tests_url = targets_url + "/" + word
                        if request(tests_url):
                            print(GREEN + "[+] Found: " + WHITE + "http://" + tests_url + RESET)
            except FileNotFoundError:
                print(RED + "[-] Error: file.txt not found in /project/ folder!" + RESET)
            input(CYAN + "\n[*] Press Enter to go back..." + RESET)

        elif choice == "02":
            clear()
            banner()
            target_url = input(YELLOW + '[+] Enter Domain (e.g., google.com): ' + RESET)
            loading("[*] Searching for Subdomains")
            try:
                with open("/home/sayyaf/Desktop/project/subdomain.txt") as wordlist_file:
                    for line in wordlist_file:
                        word = line.strip() 
                        test_url = word + "." + target_url
                        if request(test_url):
                            print(GREEN + "[+] Subdomain: " + WHITE + "http://" + test_url + RESET)
            except FileNotFoundError:
                print(RED + "[-] Error: subdomain.txt not found!" + RESET)
            input(CYAN + "\n[*] Press Enter to go back..." + RESET)

        elif choice == "03":
            clear()
            banner()
            targets3_url = input(YELLOW + '[+] Enter URL for Report: ' + RESET)
            loading("[*] Analysing Server Response")
            res = request(targets3_url)
            if res:
                print(GREEN + f"[+] Status: Online | Code: {res.status_code}" + RESET)
            else:
                print(RED + "[-] Target Offline or Unreachable." + RESET)
            input(CYAN + "\n[*] Press Enter to go back..." + RESET)

        elif choice == "00":
         
            print(BLUE + "\n[*] Returning to Cphisher..." + RESET)
            time.sleep(0.8)
            break 

        else:
            print(RED + "[-] Invalid selection!" + RESET)
            time.sleep(1)
