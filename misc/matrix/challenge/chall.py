#!/usr/bin/env python3

import random as rnd
from sys import exit
import os
from inputimeout import inputimeout


def display_matrix(matrix):
    print("\ta\tb\tc\td\te\tf\tg\th")
    for i in range(0,8):
        print(str(i+1)+"\t"+"\t".join([str(j) for j in matrix[i]]))


def generate_matrix():
    matrix = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],]  
    index_y = "abcdefgh"
    index_x = "12345678"
    result = []
    for i in range(rnd.choice(range(4,20))):
        x = rnd.randint(0,7) 
        y = rnd.randint(0,7)
        if matrix[x][y] == 0:
            matrix[x][y] = 1
            result.append(index_x[x]+index_y[y])
    return matrix, result

Flag = os.environ.get("FLAG", "FLAG{this_is_a_fake_flag}")
print("Welcome to your first programming challenge\nthe goal is to determine the index of value 1 inside a given 8x8 matrix\nif you solve 100, i'll give you a flag, but you only have 5 sec for each matrix or you lose\ninput format ex: 2d,3e,3b,7h\ngood luck :)\n\n")
score = 0
goal = 100
while score<goal:
    m,r = generate_matrix()
    display_matrix(m)
    try:
        ans = inputimeout(prompt="\nyour answer: ",timeout=5).split(',')
    except:
        print("Too slow :P")
        exit()
    try:
        res = all([i in ans for i in r])
    except:
        print("you broke the game -_-")
        exit()
    if not res:
        print("you loose :P")
        exit()
    print("ding ding ding!! correct :)\n")
    score += 1
if score == goal:
    print("Congratualions :D here's your flag: "+Flag)        


