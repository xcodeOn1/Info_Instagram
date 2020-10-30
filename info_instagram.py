# -*- coding:utf -8 -*-
import requests
import time as mm
import sys as n
import optparse
parser = optparse.OptionParser()
parser.add_option("-u", "--user",dest="user", help="Check username info")
(options, arguments) = parser.parse_args()
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m' # gray
def slow(M): ## By Twitter : @Matrix0700
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 100)
def slow1(M): ## By Twitter : @Matrix0700
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 1000)
slow( R + '''
  _____        __          _____           _                                  
  \_   \_ __  / _| ___     \_   \_ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___  
   / /\/ '_ \| |_ / _ \     / /\/ '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \ 
/\/ /_ | | | |  _| (_) | /\/ /_ | | | \__ \ || (_| | (_| | | | (_| | | | | | |
\____/ |_| |_|_|  \___/  \____/ |_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_|
                                                    |___/                                                                                                                                              
''')
slow( C + '''
──▄█████████████████████████▄──
▄█▀░█░█░█░░░░░░░░░░░░░░░░░░░▀█▄
█░░░█░█░█░░░░░░░░░░░░░░█████░░█
█░░░█░█░█░░░░░░░░░░░░░░█████░░█
█░░░█░█░█░░░░░░░░░░░░░░█████░░█
█░░░░░░░░░▄▄▄█████▄▄▄░░░░░░░░░█
███████████▀▀░░░░░▀▀███████████
█░░░░░░░██░░▄█████▄░░██░░░░░░░█
█░░░░░░░██░██▀░░░▀██░██░░░░░░░█
█░░░░░░░██░██░░░░░██░██░░░░░░░█
█░░░░░░░██░██▄░░░▄██░██░░░░░░░█
█░░░░░░░██▄░▀█████▀░▄██░░░░░░░█
█░░░░░░░░▀██▄▄░░░▄▄██▀░░░░░░░░█
█░░░░░░░░░░▀▀█████▀▀░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀
──▀█████████████████████████▀──
─────── By Xcode & @xcodeon1─────────
''')
print(W +"-"*58)
user = options.user
url = "https://i.instagram.com:443/api/v1/users/lookup/"
cookies = {"mid": "XOSINgABAAG1IDmaral3noOozrK0rrNSbPuSbzHq"}
headers = {"Connection": "close", "X-IG-Connection-Type": "WIFI", "X-IG-Capabilities": "3R4=",
           "Accept-Language": "ar-AE",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
           "User-Agent": "Instagram 99.4.0 S3od_al3nzi (Dmaral3noOoz)",
           "Accept-Encoding": "gzip, deflate"}
data = {"signed_body": "35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{\"q\":\"%s\"}" % user }
re = requests.post(url, headers=headers, cookies=cookies, data=data)
info = re.json()
# print(info)
print(W + "Username :"  + G + options.user)
if info['email_sent'] ==  False :
     print( W + "Email_Sent :" + R + " False")
else:
    print( W + "Sms_Sent :" +G + "True")
if info['sms_sent'] ==  False :
     print( W + "sms :" + R + " False")
else:
    print( W + "sms :" +G + "True")
def emailPhoneIsuue(info):
    try:
        if info['obfuscated_email']:
            print(W + "His Phone Email Is: " + G + info['obfuscated_email'])
        else:
            print("oh")
    except KeyError:
        'obfuscated_email'
    pass

    try:
        if info['obfuscated_phone']:
            print(W + "His Phone number Is: " + G + info['obfuscated_phone'])
        else:
            print("oh")
    except KeyError:
        'obfuscated_phone'
    pass
emailPhoneIsuue(info)
print(W + "-"*58)
print("\n")
