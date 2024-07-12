#imports

from tkinter import *
window=Tk()
window.title('Tic Tac Toe')
#TODO: Create visual display for users

def board():
    arr = [[str(x*3), str((x*3)+1), str((x*3)+2)] for x in range(0,3)]
    print(arr)
    for x in range (3):
        print(f"\t|\t|\t")
        if x!=2:
            print("-------------")
    return arr
def game(arr):
    for x in range (3):
        print(f"\t{arr[x][0]}|\t{arr[x][1]}|\t{arr[x][2]}")
        if x!=2:
            print("-------------")
    #return arr
def player_1(player1, player2):
    dec = input(f"{player1}: Choose the number space that you would like to mark")
    dec = int(dec)
    row = dec / 3
    col = dec % 3
    if arr[int(row)][int(col)] != f'{player2}':
        arr[int(row)][int(col)] = f'{player1}'
    else:
        print("Wrong move")
    game(arr)
    return arr


def player_2(player2, player1):
    dec = input(f"{player2}: Choose the number space that you would like to mark")
    dec = int(dec)
    row = dec / 3
    col = dec % 3
    if arr[int(row)][int(col)] != f'{player1}':
        arr[int(row)][int(col)] = f'{player2}'
    else:
        print("Wrong move")
    game(arr)
    return arr


# TODO: Keep track of a win
def win(arr, player):
    sold = 0
    for x in range(3):
        soly=0
        solx = 0

        for y in range(3):
            if arr[x][y]==player:
                soly+=1
                if soly==3:
                    return True
                if x==0 and y==2:
                    sold+=1
                    print(sold)
            if arr[y][x]==player:
                solx+=1
                if solx==3:
                    return True
                if y==0 and x==2:
                    sold+=1
                    print('hi')
            if arr[x][y] == player and x == y :
                sold+=1
                print('y')
            if sold==3:
                return True

                break

        # soly = 0
        # for y in x:
        #     if y==f"{player}":
        #         soly+=1
        #         print(y.isdigit())
        #     if soly==3:
        #         return True
    return False


arr=board()
# TODO: Take users input
player1=input("Player 1 ( x or o): ")
player2=input("Player 2 ( x or o): ")

# TODO: Alternate between each player
y=0
while(y<=9):
    arr=player_1(player1, player2)

    winner1=win(arr, player1)
    print(winner1)
    if winner1==True:
        print(f"Congratulations {player1}!")
        break
    arr= player_2(player2, player1)

    winner2 = win(arr, player2)
    if winner2==True:
        print(f"Congratulations {player2}!")
        break
    y+=2

