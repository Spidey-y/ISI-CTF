#!/usr/bin/env python3

from time import sleep
import os
from sys import exit

flag = os.environ.get('FLAG', 'flag{not_flag}')

def wrong():
    f = open("wrong.txt", "r")
    print(f.read())
    f.close()
    exit()


def correct():
    f = open("correct.txt", "r")
    print(f.read())
    f.close()
    exit()


if __name__ == '__main__':
    f = open("welcome.txt", "r")
    print(f.read())
    f.close()
    while True:
        print("Please input the flag: ")
        s = input()
        for i, c in enumerate(s):
            if c != flag[i]:
                wrong()
            else:
                sleep(0.5)
        correct()
