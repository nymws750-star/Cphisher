#!/usr/bin/env python3
import os
import time

# =========================
# COLORS (تنسيق الألوان)
# =========================
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
CYAN   = "\033[96m"
WHITE  = "\033[97m"
RESET  = "\033[0m"

def start_mac_changer():
    # 1. مسح الشاشة
    os.system("clear")
    
    # 2. طباعة الواجهة (Banner)
    print(BLUE + """
  ░█▄█░█▀█░█▀▀░░░█▀▀░█░█░█▀█░█▀█░█▀▀░█▀▀░█▀▄
  ░█░█░█▀█░█░░░░░█░░░█▀█░█▀█░█░█░█░█░█▀▀░█▀▄
  ░▀░▀░▀░▀░▀▀▀░░░▀▀▀░▀░▀░▀░▀░▀░▀░▀▀▀░▀▀▀░▀░▀ 2.1.0
    """ + RESET)
    
    print(CYAN + "    " + "━" * 55 + RESET)
    print(YELLOW + "    [*] Mode   : Hardware Address Spoofing (MAC)" + RESET)
    print(WHITE +  "    [*] Author : Eng-Cybersecurity" + RESET)
    print(CYAN + "    " + "━" * 55 + RESET)

    # 3. طلب البيانات من المستخدم
    print(GREEN + "\n    [+] Enter Configuration Details:" + RESET)
    
    interface = input(CYAN + "    ├───( " + WHITE + "Interface Name" + CYAN + " )─> " + RESET)
    new_mac   = input(CYAN + "    └───( " + WHITE + "New MAC Address" + CYAN + " )─> " + RESET)

    # التأكد من عدم ترك الحقول فارغة
    if not interface or not new_mac:
        print(RED + "\n    [!] Error: Interface or MAC cannot be empty!" + RESET)
        time.sleep(2)
        return

    print(YELLOW + "\n    [*] Attempting to change MAC address..." + RESET)
    time.sleep(1.5)

    # 4. تنفيذ أوامر تغيير الـ MAC
    # ملاحظة: تم توجيه المخرجات لـ /dev/null لإخفاء رسائل النظام المزعجة
    try:
        # إيقاف كرت الشبكة
        os.system(f"sudo ifconfig {interface} down > /dev/null 2>&1")
        
        # تغيير العنوان الفيزيائي
        change_result = os.system(f"sudo ifconfig {interface} hw ether {new_mac} > /dev/null 2>&1")
        
        # إعادة تشغيل كرت الشبكة
        os.system(f"sudo ifconfig {interface} up > /dev/null 2>&1")

        if change_result == 0:
            print(GREEN + "\n    [✔] Success: Identity Spoofed Successfully!" + RESET)
            print(WHITE + f"    [+] Interface : {interface}" + RESET)
            print(WHITE + f"    [+] New MAC   : {new_mac}" + RESET)
        else:
            print(RED + "\n    [!] Failed: Please check the interface name or MAC format." + RESET)

    except Exception as e:
        print(RED + f"\n    [!] Unexpected Error: {e}" + RESET)

    print(CYAN + "\n    " + "━" * 55 + RESET)
    input(YELLOW + "    Press [Enter] to return to Main Menu..." + RESET)

# تشغيل الأداة مباشرة إذا تم فتح الملف بشكل مستقل
if __name__ == "__main__":
    start_mac_changer()
