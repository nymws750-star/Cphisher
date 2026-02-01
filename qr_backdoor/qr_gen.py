#!/usr/bin/env python3
import os
import time
import requests # مكتبةRequests متوفرة افتراضياً في أغلب الأنظمة

# الألوان المتناسقة
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
PURPLE = "\033[95m"
CYAN   = "\033[96m"
WHITE  = "\033[97m"
RESET  = "\033[0m"

def start_qr_attack(): # تأكد أن الاسم مطابق لما تستدعيه في Cphisher.py
    os.system("clear")
    print(RED + """
    █▀▀█ █▀▀█ ░░ ░█▀▀█ █▀▀█ █▀▀ █░█ ░░ ▀█▀ █▀▀█ █▀▀ █░█ █▀▀ █▀▀█
    █░░█ █▄▄▀ ▀▀ ░█▄▄█ █░░█ █░░ █▀▄ ▀▀ ░█░ █▄▄█ █░░ █▀▄ █▀▀ █▄▄▀
    ▀▀▀█ ▀░▀▀ ░░ ░█░░█ █▀▀▀ ▀▀▀ ▀░▀ ░░ ▄█▄ ▀░░▀ ▀▀▀ ▀░▀ ▀▀▀ ▀░▀▀
    """ + RESET)
    print(CYAN + "    " + "━" * 55 + RESET)
    print(YELLOW + "    [*] Mode: QR-Code Payload Injection (API Mode)" + RESET)
    print(WHITE + "    [*] Status: System Online" + RESET)
    
    # طلب الرابط
    target_url = input(CYAN + "\n    [+] Enter URL to encode in QR: " + RESET)
    
    if not target_url:
        print(RED + "    [!] URL cannot be empty!" + RESET)
        time.sleep(2)
        return

    print(GREEN + "    [*] Requesting QR from Server..." + RESET)
    
    # استخدام API خارجي لتوليد الباركود لتفادي مشاكل Pip
    api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={target_url}"
    
    try:
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            img_name = "target_qr.png"
            # حفظ الصورة داخل مجلد الأداة
            with open(img_name, "wb") as f:
                f.write(response.content)
            
            print(BLUE + f"    [+] QR Code saved successfully as: {img_name}" + RESET)
            print(YELLOW + "    [!] Opening QR Image... Send this to victim!" + RESET)
            
            # محاولة فتح الصورة
            os.system(f"xdg-open {img_name} > /dev/null 2>&1 &")
        else:
            print(RED + "    [!] Server returned an error. Please try again." + RESET)
    except Exception as e:
        print(RED + f"    [!] Connection Error: {e}" + RESET)
        print(YELLOW + "    [!] Make sure your internet connection is stable." + RESET)

    print(RED + "\n    [00] Back to Menu" + RESET)
    input(CYAN + "    └───> Press Enter to return..." + RESET)
