#!/usr/bin/env python3

import os
from binascii import hexlify


def xor(a, b):
    return bytes([ord(x) ^ y for x, y in zip(a, b)])


flag = os.environ.get('FLAG', 'flag{not_flag_}')
key = os.urandom(len(flag))
encrypted_message = xor(flag, key)
f = open("welcome2.txt", "r")
print(f.read())
f.close()

print("we all have secrets here's mine:", hexlify(encrypted_message), "\n")
while True:
    try:
        plaintext = input(
            "Enter your secret and i'll hide it for u (or 'q' to quit): ")
        if plaintext == 'q':
            break
        plaintext = plaintext + "A"*(len(flag)-len(plaintext) % len(flag))
        encrypted_text = xor(plaintext, key)
        print("secret:", hexlify(encrypted_text), "\n")
    except Exception as e:
        print("You broke me -_-")
        break
