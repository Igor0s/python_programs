import tkinter
import time 

HEIGHT = 500
WIDTH = 500
x=250
y=400
ball_radius = 10
ball_radius = 10
size_x = 0
size_y = 0
counter_drops = 0
counter = 0

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=WIDTH, height=HEIGHT, bg = "white")
canvas.pack()

def circle(canvas, ball):
    #movement of drop in canvas
    global speed
    canvas.move(ball, 0, speed)
    canvas.update()
    speed += 0.03
    canvas.after(3)
    
def petri_dish():
    #creates a petri dish in canvas
    canvas.create_oval(100,290, 400,390)#horny kruh
    canvas.create_oval(100,340, 400,440)#dolny kruh
    canvas.create_line(100,340, 100,390)
    canvas.create_line(400,340, 400,390)

def pause():
    global counter
    counter += 1
    
    
button = tkinter.Button(window, text = "pause", command = pause)
button.pack()

for i in range(10): 
    petri_dish()
    canvas.create_text(WIDTH/2, 20, text = f"Number of drops: {counter_drops}", anchor = "n", font="Times 20 italic bold")
    #check if petri dish is full
    if (WIDTH/2-25)-size_x < 100:
        canvas.create_text(WIDTH/2, HEIGHT-50, text = f"Petri dish is full.", anchor = "n", font="Times 20 italic bold")
    else:
        #check if button was pressed, else continue animation
        if counter%2 == 0:
            x,y = WIDTH//2, HEIGHT//5
            ball = canvas.create_oval(x,y, x + ball_radius, y + ball_radius, fill='#9393ff')
            speed = 1.4
            for i in range(100):
                circle(canvas, ball)
            
            canvas.delete('all')
            canvas.create_oval((WIDTH/2-25)-size_x, (HEIGHT-110)-size_y, (WIDTH/2+25)+size_x, (HEIGHT-110)+size_y, fill='#9393ff')
            size_x += 25
            size_y += 10
            counter_drops += 1
        else:
            canvas.create_text(WIDTH/2, HEIGHT-50, text = f"drops are paused", anchor = "n", font="Times 20 italic bold")
            pause()
    print(counter)
'''
I appologize that the button is not working properly, I spent hours trying to figure out how to resume the animation again.
Unfortunately with no result.

'''

        
        
        
window.mainloop()
