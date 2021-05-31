import socket
import time

sock = socket.socket()
letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def rec(password, index, reconnect):
    if reconnect:
        global sock
        sock = socket.socket()
        sock.connect(("challenges.ctfd.io", 30440))
        sock.recv(4096)
        sock.send(b'1\n')
        sock.recv(2048)
    if len(password) >= 624:
        return password
    # if index <= 0:
    #     index = 10
    if index >= 10:
        index = 0
    for c in password:
        sock.send(str(c+'\n').encode())
        sock.recv(2048)
    sock.send(str(letters[index]+'\n').encode())
    print(letters[index])
    result = sock.recv(2048)
    print(result)
    if b"Enter" in result:
        password += letters[index]
        print("Password: " + password)
        return rec(password, 0, False)
    else:
        sock.close()
        return rec(password, index+1, True)

def main():
    index_letters = 0 # 0
    password = "1058463025"
    # password = ""
    reconnect = True

    test = rec(password, index_letters, reconnect)
    print(test)

if __name__ == '__main__':
    main()


# Enter digit number 10
# 5
# You have limited resources on guessing mode
# bye bye :)