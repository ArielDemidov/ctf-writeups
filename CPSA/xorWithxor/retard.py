import re
import struct


def xor(data, key): 
    return bytearray(a^b for a, b in zip(*map(bytearray, [data, key]))) 


FILE = './xor-with-xor.bin'
regex = re.compile(rb'CSA{.+}')


with open(FILE, 'rb') as f:
    data = f.read()

key = b'xor' * 231202 + b'xo'
with open('xored.zip', 'wb') as f:
    f.write(xor(data, key))