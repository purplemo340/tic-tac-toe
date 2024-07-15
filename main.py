#imports

from tkinter import *
import math
global player
global game_arr
global arr
global buttons

window=Tk()
window.title('Tic Tac Toe')
window.config(padx=50, pady=50, height=200, width=200)

arr=['X', 'O']
score_dict={'X':0, 'O':0}
player = 0
def game():
    global game_arr
    buttons_arr=[]
    game_arr = board()
    for x in range(9):
        button=Button(height=0, width=5, font=24, command= lambda place=x:switch(place))
        buttons_arr.append(button)
        buttons_arr[x].grid(column=int(x/3), row=x%3)
    return buttons_arr
def board():
    array = [[str(x*3), str((x*3)+1), str((x*3)+2)] for x in range(0,3)]

    return array

def win(arr):
    for x in range(3):
        if all(y == arr[x][0] for y in arr[x]):
            return True
        if all(arr[y][x] == arr[0][x] for y in range(3)):
            return True
    if all(arr[y][y] == arr[0][0] for y in range(3)):
        return True
    if all(arr[y][(2-y)] == arr[0][2] for y in range(3)):
        return True
    return False



def switch(x):
    global player
    global game_arr


   # arr1=[top_left, top_middle, top_right]
    if player==0:

        game_arr[int(x/3)][x%3] = f'{arr[player]}'

        buttons[x].config(text=f"{arr[player]}")
        winner = win(game_arr)
        if winner==True:
            score_dict['X'] += 1
            end(player)

        player=1
    else:
        game_arr[int(x / 3)][x % 3] = f'{arr[player]}'

        buttons[x].config(text=f"{arr[player]}")
        winner=win(game_arr)
        if winner==True:
            score_dict['O'] += 1
            end(player)
        player=0
def end(winner):
    score.config(text=f"X: {score_dict['X']}\t O: {score_dict['O']}")

    for button in buttons:
        button.destroy()

    congrats.config(text=f"Congrats!: {arr[winner]}")
    congrats.grid(column=0,row=0)

    con.grid(column=0, row=1)
def next_game():
    global buttons
    con.destroy()
    congrats.destroy()
    buttons=game()

score = Label(text=f"X: {score_dict['X']}\t O: {score_dict['O']}")
score.grid(row=3, column=0, columnspan=3)

buttons=game()
con=Button(text="Continue", command=next_game)
congrats=Label()
window.mainloop()
