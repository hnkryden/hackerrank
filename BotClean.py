#!/usr/bin/python

# Head ends here
import sys
if len(sys.argv) > 1:
    sys.stdin = open(sys.argv[1], "r")

def displayPathtoPrincess(pathR,pathC):
    if  pathR <0:
        print('UP')
        return (-1,0)
    elif pathR >0:
        print('DOWN')
        return (1,0)
    elif pathC > 0:
        print('RIGHT')
        return (0,1)
    elif pathC < 0:
        print('LEFT')
        return (0,-1)
    else:
        return (0,0)


def next_move(botX, botY, board,rows):
    distance = 100
    bestI = botX
    bestJ = botY
    for i in range(rows):
        for j in range(rows):
            if board[i][j] == 'd':
                distTmp = abs(botX - i) + abs(botY - j)
                #print(distance,i,j)
                if (distTmp < distance):
                    distance = distTmp
                    bestI = i
                    bestJ = j
                    
      
    if (distance==0):
        print("CLEAN")
        board[botX][botY]='c'
        newpos=(0,0)
    else:
        newpos = displayPathtoPrincess(bestI-botX,bestJ-botY)
    return botX + newpos[0],botY + newpos[1]

    #print("DOWN")




if __name__ == "__main__":
    rows = 5
    pos = [int(i) for i in input().strip().split()]

    board = [[j for j in input().strip()] for i in range(rows)]
   

    botX = 0
    botY = 0
    for i in range(30):
        #for i in range(rows):
        #    print(board[i])
        #print(botX,botY)
        #board[botX][botY]='b'
        botX, botY = next_move(botX, botY, board,rows)
       

