#!/usr/bin/python
import sys
def displayPathtoPrincess(pathR,pathC):
    if pathR <0:
        print('UP')
    elif pathR >0:
        print('DOWN')
    elif pathC > 0:
        print('LEFT')
    elif pathC < 0:
        print('RIGHT')

#print all the moves here
import sys


#print(sys.argv)

if len(sys.argv) > 1:
    #print(sys.argv[1])
    sys.stdin = open(sys.argv[1], "r")


m = int(input())
bot = input()
#print(bot)

grid = [] 
for i in range(0, m):
    c = input().strip()
    grid.append(c)
    if 'm' in c:
        cm = c.find('m')
        rm = i
    if 'p' in c:
        cp = c.find('p')
        rp = i

pathR = rp - rm
pathC = cm - cp

#print(pathR,pathC)
displayPathtoPrincess(pathR,pathC)

