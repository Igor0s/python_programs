import tkinter
import random


def create_text(counter):
    #creates text with random colour and text
    for i in range(counter):
        canvas.create_text(random.randint(5,950), random.randint(5, 80), text= random.choice(colours), tags= "text", fill= random.choice(colours), anchor= "nw", font = "Arial 20 bold italic")

def movement(canvas, text, speed):
    #global speed
    canvas.move(text, 0, speed)
    canvas.update()
    canvas.after(1)

def delete_text(event):
    #delete_text gets text, fill atributes of text and if they are matching, deletes the text
    global score_counter, miss_counter
    x, y = event.x, event.y
    x1 = x-10
    y1 = y-10
    x2 = x+10
    y2 = y+10
    
    item = canvas.find_overlapping(x1, y1, x2, y2)
    if item:     
        text = canvas.itemcget(item, 'text')
        color = canvas.itemcget(item, 'fill')
        if text == color:        
            canvas.delete(item)
            score_counter += 3
            miss_counter = 0
            canvas.delete("score")
            canvas.create_text(500,900, text= f"Score: {score_counter}", tags = "score", fill= "white", anchor= "n", font = "Arial 20 bold italic" )
        elif text != color:
            canvas.delete(item)
            score_counter -= 2
            miss_counter += 1
            canvas.delete("score")
            canvas.create_text(500,900, text= f"Score: {score_counter}", tags = "score", fill= "white", anchor= "n", font = "Arial 20 bold italic" )               
        else:
            miss_counter += 1
    print(miss_counter)
    
def animate(speed, counter):   
    y_cord = 0   
    create_text(counter)
    while y_cord < 700:        
        movement(canvas, "text", speed)
        y_cord += speed
    canvas.delete("text")
    window.after(50, animate)
        

HEIGHT = 1000
WIDTH = 1000
colours = ["red", "green", "black", "blue", "gold", "orange", "purple", "grey", "brown", "pink"]
counter = 5
speed = 1
score_counter = 0
miss_counter = 0
game_over = 1

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=WIDTH, height=HEIGHT, bg = "white")
canvas.pack()

canvas.bind('<Button-1>', delete_text)
canvas.create_rectangle(0,800, 1000,1000, fill="black")

#game loop
while game_over == 1:
    if counter < 15:
        animate(speed, counter)
        counter += 1
        speed += 0.2
        if miss_counter >= 5:
            canvas.delete("all")
            canvas.create_text(500,300, text= f"GAME OVER", fill= "blue", anchor= "n", font = "Arial 20 bold italic" )
            canvas.create_text(500,700, text= f"Score: {score_counter}",  fill= "blue", anchor= "n", font = "Arial 20 bold italic" )
            game_over = 0
    else:
        animate(speed, counter)
        if miss_counter >= 5:
            canvas.delete("all")
            canvas.create_text(500,300, text= f"GAME OVER", fill= "blue", anchor= "n", font = "Arial 20 bold italic" )
            canvas.create_text(500,700, text= f"Score: {score_counter}",  fill= "blue", anchor= "n", font = "Arial 20 bold italic" )
            game_over = 0

window.mainloop()



