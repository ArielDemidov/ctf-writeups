import socket
import binascii
import struct


def xor(data, key): 
    return bytearray(a^b for a, b in zip(*map(bytearray, [data, key]))) 

msg1 = b'\x5a\x01\xfe\xdd\x74\x9c\x2e'
msg2 = b'\x5a\x2c\xd2\x33\x1f\xa9\x0b\xb9\x6a'
msg3 = bytes.fromhex("5a010001c0a8ad0a005074f2be19")

msg4 = "GET / HTTP/1.1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36\r\nHost: 172.0.115.223\r\nAccept-Language: en-us\r\nConnection: Keep-Alive\r\n\r\n"

msg4 = msg4.encode()
# 5a 67 a6 f1 93             f4 76 98 64
# 5a 67 e5 a2 d2            49 b5 90 15

# 5a 2c 91 60 5e         14 c8 b1 1b
# 5a 2c d2 33 1f                a9 0b b9 6a


sock = socket.socket()
sock.connect(("52.28.255.56", 1080))
#52.28.255.56
#172.0.115.223

sock.send(msg1)
a = bytes.fromhex(sock.recv(1024).hex()[:-8])
b = a[0].to_bytes(1, 'big') + a[2].to_bytes(1, 'big') + xor(a[3:], b'\x43\x53\x41')
b += binascii.crc32(b).to_bytes(4, 'big')
sock.send(b)

sock.send(msg3)
print(sock.recv(1024))

sock.send(msg4)
print(sock.recv(1024).decode())