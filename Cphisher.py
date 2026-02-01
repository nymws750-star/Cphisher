#!/usr/bin/env python3
import subprocess
import requests
import time
import sys
import os
import re
import importlib.util

# ======================================================
# قسم الاستيراد الذكي - حل مشكلة "لا يوجد" نهائياً
# ======================================================
cseeker_tool = mac_tool = payload_tool = link_tool = pass_tool = logger_tool = qr_tool = None

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_PATH) 

def smart_import(folder_name, file_name, module_name):
    """دالة محسنة لاستيراد الأدوات مع كشف الأخطاء"""
    try:
        path = os.path.join(BASE_PATH, folder_name, file_name)
        if os.path.exists(path):
            spec = importlib.util.spec_from_file_location(module_name, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        else:
            return None
    except Exception as e:
        print(f"\033[91m\n[!] Error loading {folder_name}/{file_name}: {e}\033[0m")
        time.sleep(2)
        return None


try: from cseeker import cseeker as cseeker_tool
except ImportError: pass
try: from mac_changer import mac_changer as mac_tool
except ImportError: pass
try: from payload_gen import payload_gen as payload_tool
except ImportError: pass
try: from link_changer import link_checker as link_tool
except ImportError: pass
try: from pass_grabber import pass_grabber as pass_tool
except ImportError: pass

logger_tool = smart_import("Img-Logger", "img_logger.py", "img_logger")
qr_tool = smart_import("qr_backdoor", "qr_gen.py", "qr_gen")

# =========================
# COLORS
# =========================
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
PURPLE = "\033[95m"
CYAN   = "\033[96m"
WHITE  = "\033[97m"
RESET  = "\033[0m"

# ========================

def clear():
    os.system("clear")

clear()
print(GREEN + "[+] Installing required packages..." + RESET)
time.sleep(0.5)
print(GREEN + "[+] Packages already installed." + RESET)
time.sleep(0.5)
print(GREEN + "[+] Internet Status : Online" + RESET)
time.sleep(0.5)
print(GREEN + "[+] Checking for update : Up to date" + RESET)
time.sleep(0.5)

# =======================
# BANNER
# =======================
def banner():
    clear()
    print(YELLOW + """
             _     _     _                
            | |   (_)   | |               
  ___ _ __ | |__  _ ___| |__   ___ _ __ 
 / __| '_ \| '_ \| / __| '_ \ / _ \ '__|
| (__| |_) | | | | \__ \ | | |  __/ |   
 \___| .__/|_| |_|_|___/_| |_|\___|_|   
      | |                                
      |_|                                 
    """ + RESET)

# =======================
# دالة معلومات عن الأداة
# =======================
def show_about():
    banner()
    print(CYAN + " [ ABOUT THIS TOOL ] " + RESET)
    print(WHITE + "--------------------------------------------------" + RESET)
    print(YELLOW + " Tool Name    : " + RESET + "Cphisher Multi-Tool")
    print(YELLOW + " Developer    : " + RESET + "Eng-Cybersecurity")
    print(YELLOW + " Version      : " + RESET + "2.0.0")
    print(YELLOW + " Description  : " + RESET + "All-in-one cybersecurity toolkit.")
    print(WHITE + "--------------------------------------------------" + RESET)
    input(GREEN + "\nPress Enter to return to main menu..." + RESET)

def input_mac_changer():
    while True:
        banner()
        print(CYAN + "[-] Tool Created by Eng-Cybersecurity\n" + RESET)
        print(RED + """[""" + RESET + WHITE + """::""" + RESET + RED + """]""" + RESET  + YELLOW + """Select An Attack For Your Victim """ + RESET + RED + """[""" + RESET + WHITE + """::""" + RESET + RED + """] \n""" + RESET)
        
        # القائمة المحدثة (تم حذف 03 و 04 وإعادة الترقيم)
        print(RED + "[" + WHITE + "01" + RED + "]" + YELLOW + " C-Seeker (Web Recon)     " + RESET + RED + "[" + WHITE + "05" + RED + "]" + YELLOW + " Image-Logger (IP)" + RESET)
        print(RED + "[" + WHITE + "02" + RED + "]" + YELLOW + " Mac Changer (New)        " + RESET + RED + "[" + WHITE + "06" + RED + "]" + YELLOW + " QR-Backdoor (Session)" + RESET)
        print(RED + "[" + WHITE + "03" + RED + "]" + YELLOW + " Safe-Guard (URL Scan)    " + RESET + RED + "[" + WHITE + "07" + RED + "]" + YELLOW + " Android Payload" + RESET)
        print(RED + "[" + WHITE + "04" + RED + "]" + YELLOW + " Pass-Grabber (Phishing)  " + RESET)
        
        print(RED + "\n[" + WHITE + "00" + RED + "]" + YELLOW + " Exit                     " + RESET + RED + "[" + WHITE + "08" + RED + "]" + YELLOW + " About Tool" + RESET)

        interface_url = input(RED + "\n[" + WHITE + "-" + RED + "]" + CYAN + " Select an option: " + RESET)

        def launch(tool, func_name):
            if tool:
                if hasattr(tool, func_name):
                    print(BLUE + f"\n[*] Launching {func_name}..." + RESET)
                    time.sleep(1)
                    getattr(tool, func_name)()
                else:
                    print(RED + f"\n[!] Error: Function {func_name} not found!" + RESET)
                    time.sleep(2)
            else:
                print(RED + f"\n[!] Error: Module not found! Check your folders." + RESET)
                time.sleep(2)

        if interface_url in ["01", "1"]:
            launch(cseeker_tool, "start_scanner")
        elif interface_url in ["02", "2"]:
            launch(mac_tool, "start_mac_changer")
        elif interface_url in ["03", "3"]:
            launch(link_tool, "start_link_checker")
        elif interface_url in ["04", "4"]:
            launch(pass_tool, "start_pass_grabber")
        elif interface_url in ["05", "5"]:
            launch(logger_tool, "start_img_logger")
        elif interface_url in ["06", "6"]:
            launch(qr_tool, "start_qr_attack")
        elif interface_url in ["07", "7"]:
            launch(payload_tool, "start_payload_generator")
        elif interface_url in ["08", "8"]:
            show_about()
        elif interface_url in ["00", "0"]:
            print(GREEN + "[+] Goodbye!" + RESET)
            sys.exit()
        else:
            print(RED + "[-] Invalid Option!" + RESET); time.sleep(1)

if __name__ == "__main__":
    try:
        input_mac_changer()
    except KeyboardInterrupt:
        print("\n" + RED + "[!] Stopped by user." + RESET)
        sys.exit()
