r = "\033[91m" #red
g = "\033[92m" #green
y = "\033[93m" #yellow
c = "\033[96m" #cyan
p = "\033[95m" #pink
w = "\033[37m" #white
b = "\033[94m" #blue
#Project 2023 - HENZX
#			Do not modify this script - HENZX ( SUNSHINE )
import phonenumbers as number
from phonenumbers import geocoder, carrier, timezone
import sys
import os
import time
import colorama
import random
from time import sleep
from colorama import Fore, Back, Style
#start
os.system('clear')
os.system("xdg-open https://youtube.com/channel/UCENRlq6-MUjG99znHBeojPg")
time.sleep (1)
os.system('toilet -f mono12 Tracer')
banner='''
[ Note ]   : Modify will break the code, that will be an error.
[ Version] : 1.0
[ Author ] : Sunshine
'''
print(banner)
print("Tracer - working project")

text = input("$ Tracer 1.0 > ")
konv = number.parse(text)

tracer = geocoder.description_for_number(konv, "id")
isp = carrier.name_for_number(konv, "id")
timezone = timezone.time_zones_for_number(konv)

print("Country : ", tracer)
print("ISP Number -- DFGB : ", isp)
print("timezone number : ", timezone)

#geolocation -- Not mine
sleep (1)
print("")
banner = """
[]--------Locator--------[]
     Modified by HenzX
     Author : Sunshine ( HenzX )
[]-----------------------[]
""".format(y,y,y,y,y,w,w,r,p,b,c,w,w,r,p,b,c,w,w,r,p,b,c,w,w)

print(banner)

try:
	while True:
		text = input(w+"\n["+y+"?"+w+"]"+y+" Enter IP target: ")

		if text == "":
			print(w+"["+r+"!"+w+"]"+r+" Enter the valid IP!")
			break

		scan = geocoder.ipinfo(teks)

		print(w+"\n["+g+"+"+w+"]"+g+" Address          "+w+": ", scan.address)
		print(w+"["+g+"+"+w+"]"+g+" City            "+w+": ", scan.city)
		print(w+"["+g+"+"+w+"]"+g+" Country          "+w+": ", scan.country)
		print(w+"["+g+"+"+w+"]"+g+" Hostname        "+w+": ", scan.hostname)
		print(w+"["+g+"+"+w+"]"+g+" IP address      "+w+": ", scan.ip)
		print(w+"["+g+"+"+w+"]"+g+" Latitude        "+w+": ", scan.lat)
		print(w+"["+g+"+"+w+"]"+g+" Longitude       "+w+": ", scan.lng)
		print(w+"["+g+"+"+w+"]"+g+" IP Valid        "+w+": ", scan.ok)
		print(w+"["+g+"+"+w+"]"+g+" ASN/ISP/ORG     "+w+": ", scan.org)
		print(w+"["+g+"+"+w+"]"+g+" Code ZIP/Postal "+w+": ", scan.postal)

		ulang = str(input(w+"["+y+"?"+w+"]"+y+" Repeat? [Y/n] "))

		#Tanya user mau ulang apa gk
		if ulang == "Y":
			continue
		else:
			print(w+"["+g+"+"+w+"]"+g+" Ok")
			break

#Jika user memaksa keluar dengan CTRL + C
except KeyboardInterrupt:
	print(w+"["+g+"+"+w+"]"+g+"Bye-bye\n"+w+"["+g+"+"+w+"]"+g+"Thanks for using")
# component like colorama its used for 1.1 update
# 1.1 Update with accurate location -- coming soon in March / 17
sleep (5)
os.system('clear')
def text(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
text('Contact for.education.mode@gmail.com for any requests or other.')
text('Thank you for using our services. -- HenzX ')
