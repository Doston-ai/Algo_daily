import socket

# Serverning IP adresi va u uchun port 
host = '127.0.0.1'
port = 8888

# Создаем сокет, протоколы IP va TCP protokollar uchun socket yaratamiz
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# IP-adres va portni socketga bog'laymiz (bind) 
s.bind((host, port))
# Ulanishni kutamiz
s.listen(5)
print(f"Server ishlayapti, IP {host}, port {port}.")
print("Ulanishni kutyapman...")
# Ждем подключения клиента
conn, addr = s.accept()
print(f"Klient ulandi {addr}")
# Klient ulangandan so'ng, cheksiz tsiklda undan 
# keladigan xabarlarni qabul qilishni boshlaymiz
while True:
    #  1024 baytni qabul qilamiz
    data = conn.recv(1024)
    # Agar xabar bo'sh bo'lsa, cheksiz tsikldan chiqamiz    
    if not data: 
        break
    # Qabul qilingan xabarni klietnga qaytarib yuboramiz
    print(f"Klientdan qabul qilingan xabar:")
    print(data)
    print("klientga qaytarib yuborildi!")
    conn.sendall(data)
# Ulanishni tugallaymiz (yopamiz)
conn.close()
print("Xizmat tugadi...")
s.close()

