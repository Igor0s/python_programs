import tkinter
import random

def squares():
    # function field creates visual interference of game,
    #appends coordinates of each card in list coords
    x = 40
    y = 40
    number = 0
    for i in range(4):
        for i in range(4):
            canvas.create_rectangle(x,y, x+100, y+100, fill = "Grey")
            square.append(number)
            coords.append([x,y])
            number += 1
            x += 125
        y += 125
        x = 40
        
def choose_square(event):
    #function choose_square finds coordinates, index and value of square which has user clicked and stores them
    #in variables x1/2,y1/2 , index_sq1/2 , first_sq/second_sq
    global first_sq, second_sq, counter, x1, x2, y1, y2, score, index_sq1, index_sq2

    for i in range(16):
        if event.x in range(coords[i][0], coords[i][0] + 100) and event.y in range(coords[i][1], coords[i][1] + 100):
            if counter == 0:
                first_sq = values[i]
                x1, y1 = coords[i]
                index_sq1 = square[i]
                #reveales card which user has clicked on
                canvas.create_rectangle(x1, y1, x1 + 100, y1 + 100, fill="white")
                canvas.create_text(x1 + 50, y1 + 50, text=str(values[i]))
            elif counter == 1:
                second_sq = values[i]
                x2, y2 = coords[i]
                index_sq2 = square[i]
                #reveales card which user has clicked on
                canvas.create_rectangle(x2, y2, x2 + 100, y2 + 100, fill="white")
                canvas.create_text(x2 + 50, y2 + 50, text=str(values[i]))
                counter = 2
    
    if counter >= 2:
        window.after(500, check_match)
    else:
        counter += 1

def check_match():
    global first_sq, second_sq, counter, x1, x2, y1, y2, score, index_sq1, index_sq2
    
    #check if 2 revealed cards are matching
    if first_sq == second_sq and index_sq1 != index_sq2:
        score += 1
        canvas.delete('score')
        canvas.create_text(WIDTH/2,10, text= f'SCORE: {score}/{len(values)//2}', tags = 'score', anchor= 'n', font = "Arial 15 bold italic")
    elif x2 == 0:
        canvas.create_rectangle(x1, y1, x1 + 100, y1 + 100, fill="grey")
    elif x1 == 0:
        canvas.create_rectangle(x2, y2, x2 + 100, y2 + 100, fill="grey")
    else:
        canvas.create_rectangle(x1, y1, x1 + 100, y1 + 100, fill="grey")
        canvas.create_rectangle(x2, y2, x2 + 100, y2 + 100, fill="grey")
    counter = 0

    if score == 8:
        canvas.delete('all')
        canvas.create_text(WIDTH/2, HEIGHT/2 , text= f'SCORE: {score}', anchor= 'n', font = "Arial 30 bold italic")
        canvas.create_text(WIDTH/2, HEIGHT/2-100 , text= f'WIN', anchor= 'n', font = "Arial 30 bold italic")
        

HEIGHT = 550
WIDTH = 550
coords = []
values = []
square = []
first_sq = 0
second_sq = 0
index_sq1 = 0
index_sq2 = 0
counter = 0
x1 = 0
x2 = 0
y1 = 0
y2 = 0
score = 0

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=WIDTH, height=HEIGHT, bg = "white")
canvas.pack()

for i in range(8):
    values.append(i)
    values.append(i)
random.shuffle(values)

squares()
canvas.bind('<Button-1>', choose_square)
canvas.create_text(WIDTH/2,10, text= f'SCORE: {score}/{len(values)//2}', tags = 'score', anchor= 'n', font = "Arial 15 bold italic")

window.mainloop()

