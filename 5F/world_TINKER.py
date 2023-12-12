from tkinter import *
import random

window = Tk()
HEIGHT = 1000
WIDTH = 1000
canvas = Canvas(window , height=HEIGHT , width=WIDTH , bg = "light blue")
canvas.pack()


def hill():
    colours = f'#00{random.randint(50, 255):02x}00' 
    peak = random.randint(HEIGHT/2, HEIGHT-100)
    y = random.randint(HEIGHT-300, HEIGHT)
    x = 0
    print(f"peak: {peak}, y: {y}")
    
    while x <= WIDTH:
        if y >= peak:
            canvas.create_polygon(x,y , x+10,y , x+10,HEIGHT , x,HEIGHT, fill=colours)
            y -= random.randint(0,5)
            x+=5
        else:
            while x<= WIDTH:
                canvas.create_polygon(x,y , x+10,y , x+10,HEIGHT , x,HEIGHT, fill=colours)
                y += random.randint(0,5)
                x+=5


    
for i in range(10):
    hill()

window.mainloop()