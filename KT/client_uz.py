import socket

# Ulanish kerak bo'lgan Serverning adresi va port 
server_host = '127.0.0.1'
server_port = 8888

#  IP va TCP protokollar uchun soket yaratamiz 
s = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM)
# Serverga ulanish
s.connect((server_host, server_port))
# Serverga xabar yuboramiz
a = input("Xabarni yozing")
s.sendall(a)
# ПServerdan javob olamiz
data = s.recv(1024)
# Soketni yopamiz
s.close()
# Serverdan olingan xabarni chop qilamiz
print('Serverdan qabul qilingan xabar:', data)
