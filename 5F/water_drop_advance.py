'''
I am sorry that the button is not working but as a compensation I added a rising level of water
Hope its enough
'''

import tkinter

HEIGHT = 500
WIDTH = 500
x=250
y=400
ball_radius = 10
ball_radius = 10
size_x = 0
size_y = 0
size_y_up = 0
counter_drops = 0
counter = 0

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=WIDTH, height=HEIGHT, bg = "white")
canvas.pack()

def circle(canvas, ball):
    global speed
    canvas.move(ball, 0, speed)
    canvas.update()
    speed += 0.03
    canvas.after(3)
    
def petri_dish():
    canvas.create_oval(100,290, 400,390)#horny kruh
    canvas.create_oval(100,340, 400,440)#dolny kruh
    canvas.create_line(100,340, 100,390)
    canvas.create_line(400,340, 400,390)

def pause(counter):
    counter += 1
    
button = tkinter.Button(window, text = "pause", command = pause)
button.pack()

for drop in range(20):   
    petri_dish()
    canvas.create_text(250, 20, text = f"Number of drops: {counter_drops}", anchor = "n")
    if 340-size_y_up > 290:
        if 225-size_x < 100:
            
            x,y = WIDTH//2, HEIGHT//5
            ball = canvas.create_oval(x,y, x + ball_radius, y + ball_radius, fill='#9393ff')
            speed = 1.4
            for i in range(100):
                circle(canvas, ball)
            
            #canvas.delete('all')
            canvas.create_oval(100,340-size_y_up, 400,440-size_y_up, fill='#9393ff')
            #size_x += 25
            size_y_up += 2
            counter_drops += 1
        else:       
            x,y = WIDTH//2, HEIGHT//5
            ball = canvas.create_oval(x,y, x + ball_radius, y + ball_radius, fill='#9393ff')
            speed = 1.4
            for i in range(100):
                circle(canvas, ball)
            
            canvas.delete('all')
            canvas.create_oval(225-size_x,390-size_y, 275+size_x,390+size_y, fill='#9393ff')
            size_x += 25
            size_y += 10
            counter_drops += 1
    petri_dish()

        
        
        
window.mainloop()

