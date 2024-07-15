#imports

from tkinter import *
import math
global player
global game_arr
global arr
global buttons
global congrats
buttons=[]
window = Tk()
window.title('Tic Tac Toe')
window.config(padx=50, pady=50, height=200, width=200)

arr = ['X', 'O']
score_dict = {'X': 0, 'O': 0}
player = 0


def game():
    global game_arr
    global buttons
    buttons = []

    game_arr = board()

    score.grid(row=3, column=0, columnspan=3)
    for x in range(9):
        button = Button(window, height=2,  width=5, font=24, command=lambda place=x: switch(place))
        buttons.append(button)
        buttons[x].grid(column=int(x/3), row=x % 3)
    return buttons
def board():
    array = [[str(x*3), str((x*3)+1), str((x*3)+2)] for x in range(0, 3)]

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
        if winner:
            score_dict['X'] += 1
            end(player)

        player = 1
    else:
        game_arr[int(x / 3)][x % 3] = f'{arr[player]}'

        buttons[x].config(text=f"{arr[player]}")
        winner = win(game_arr)
        if winner:
            score_dict['O'] += 1

            end(player)
        player = 0


def end(winner):
    global buttons
    global congrats
    score.config(text=f"X: {score_dict['X']}\t O: {score_dict['O']}")

    for button in buttons:
        button.config(text="")
        button.grid_forget()


    congrats=Label(text=f"Congrats!: {arr[winner]}")
    congrats.grid(column=0, row=0)

    con.grid(column=0, row=1)
def next_game():
    global congrats
    global buttons
    global game_arr

    game_arr=board()
    con.grid_forget()
    congrats.grid_forget()
    for x in range(9):

        buttons[x].grid(column=int(x/3), row=x % 3)


score = Label(text=f"X: {score_dict['X']}\t O: {score_dict['O']}")


buttons = game()
con=Button(text="Continue", command=next_game)


window.mainloop()
