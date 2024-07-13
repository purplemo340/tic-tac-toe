#imports

from tkinter import *
import math
global player
global game_arr

player = 0
def board():
    arr = [[str(x*3), str((x*3)+1), str((x*3)+2)] for x in range(0,3)]

    return arr

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

def switch(x):
    global player
    global game_arr
    print(x)
    arr=['x', 'o']
   # arr1=[top_left, top_middle, top_right]
    if player==0:

        game_arr[int(x/3)][x%3] = f'{arr[player]}'

        buttons[x].config(text=f"{arr[player]}")
        winner = win(game_arr, arr[player])
        if winner==True:
            end(player)
        player=1
    else:

        buttons[x].config(text=f"{arr[player]}")
        winner=win(game_arr, arr[player])
        if winner==True:
            end(player)
        player=0
def end(winner):
    for buttton in buttons:
        buttton.destroy()

    congrats=Label(text= f"Congrats player:{winner}")
    congrats.grid(column=0,row=0)
game_arr=board()

window=Tk()
window.title('Tic Tac Toe')
window.config(padx=50, pady=50, height=200, width=200)
buttons=[]
for x in range(9):
    button=Button(height=0, width=5, font=24, command= lambda place=x:switch(place))
    buttons.append(button)
    buttons[x].grid(column=int(x/3), row=x%3)

window.mainloop()
