# DoS_attacker
# DoS Attacker – Basit Çok Thread'li GET İsteği Aracı

Bu araç, test/etik güvenlik çalışmaları için hedefe çoklu `GET` istekleri göndermenizi sağlar.

>  **UYARI:** Bu yazılım sadece eğitim, test ve izinli güvenlik analizleri içindir. İzinsiz kullanımlar Türk Ceza Kanunu'na göre suçtur.
# indirmek için
> git clone https://github.com/canyilmaz959/DoS_Attacker.git

---

## Gereksinimler

**Python 3 yüklü olmalıdır.**  
Ayrıca şu ek paketlerin kurulması gerekir:

### Linux için:

sudo apt update
sudo apt install python3 python3-pip -y
pip3 install colorama requests


### Termux için:

pkg update
pkg install python -y
pip install colorama requests


> Bazı cihazlarda `python3` yerine `python` olarak çalıştırmak gerekebilir. Termux'ta genellikle `python` komutu yeterlidir.

---

## Kullanım

Script’i çalıştırmak için:

Dosyanın indirildiği dizine gidip

python3 DoS_attacker.py

Ya da bazı cihazlarda:

python DoS_attacker.py

---

## Özellikler

- Sürekli GET isteği gönderme
- Süreli veya miktarlı saldırılar
- Thread sayısı belirleme
- Proxy desteği

---

##  Yasal Uyarı

Bu yazılım yalnızca eğitim, test ve etik siber güvenlik amaçlıdır.
Geliştirici, izinsiz veya kötüye kullanım durumlarında hiçbir sorumluluk kabul etmez.

