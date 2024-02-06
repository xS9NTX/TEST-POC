import requests
import time
from colorama import Fore, Back, Style
import os 


print(Fore.GREEN +"S9NTX XMPRPC.PHP Hunter V2")
time.sleep(4)
os.system("clear")
print(Fore.GREEN +"Start!    ▄︻デ══━一💥")
print("    ")
print("    ")

def add_xmlrpc_to_fixed_sites():
    with open('domain.txt', 'r') as file:
        sites = file.read().splitlines()

    for site in sites:
        url = site.rstrip('/') + '/xmlrpc.php'
        try:
            response = requests.get(url, timeout=1)
            if response.status_code == 405:
                with open('saved.txt', 'a') as file:
                    file.write(url + '\n')
                print(Fore.GREEN + "XMPRPC.PHP BULUNDU!" + "  ▄︻デ══━一💥  "f"{url} başarıyla kaydedildi.")
            else:
                print(Fore.RED + "Başarısız İStek" + " 🔪  " f"{url} bulunamadı.")
        except (requests.exceptions.RequestException, requests.exceptions.Timeout) as e:
            print(Fore.RED + "Başarısız İStek" + " 🔪  " f"{url} ile bağlantı hatası oluştu veya zaman aşımına uğradı: {e}")
     
          

add_xmlrpc_to_fixed_sites()
