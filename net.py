#python 3.7.1

import socket

#Take the server name
host = str(input("Masukan Nama Web:"))

try:
  #know the ip address of the website
  addr = socket.gethostbyname(host)
  print(f"IP ADDRESS : {addr}")
  
except socket.gaierror:
  print("The website does not exits!")