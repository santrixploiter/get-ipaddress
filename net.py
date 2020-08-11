import os
import time
os.system('clear')
import socket
import pyfiglet
print("\33[36;1m")
ascii_banner = pyfiglet.figlet_format("IP Address")
print(ascii_banner)
print ("\tby SantriXploiter")
print ("\33[32;1mMasukan Url, Contoh (israel.com)")
print ("\33[36;1m")
#Take the server name
host = (input("Url : "))
time.sleep(1)
print("mencari...")
time.sleep(3)
try:
  #know the ip address of the website
  addr = socket.gethostbyname(host)
  print("Sudah Ketemu!")
  time.sleep(1)
  print(f"\33[36;1mIP Web (", host, ")",f"\33[31;1m {addr}")
  print("\33[37;1m")
except socket.gaierror:
  print("\33[31;1mWebsite Tidam Ditemukan :)")
  print("\33[37;1m")
