import tkinter
from PIL import Image, ImageDraw


HEIGHT = 1020
WIDTH = 1020
counter = 0
x_beg = 0
y_beg = 0

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=WIDTH, height=HEIGHT, bg = "white")
canvas.pack()

def field():
    x = 10
    y = 10
    for i in range(11):
        canvas.create_line(x,y ,x,HEIGHT-10 )
        x += 100       
    x = 10
    y = 10
    for i in range(11):
        canvas.create_line(x,y ,WIDTH-10,y )
        y += 100

def x_cord(coordinates):
    #functoin x_cord calculates x-coordinate of top left corner of the square used had clicked
    x = coordinates.x
    if x < WIDTH-10 and x > 10:
        while x % 100 != 0:
            x -= 1
        return x
    else:
        return -1 #means that user clicked outside of field
    
def y_cord(coordinates):
    #functoin y_cord calculates y-coordinate of top left corner of the square used had clicked
    y = coordinates.y
    if y < HEIGHT-10 and y > 10:
        while y % 100 != 0:
            y -= 1
        return y
    else:
        return -1 #means that user clicked outside of field

def level(event):   
    global x, y, counter, x_beg, y_beg
    x = x_cord(event)
    y = y_cord(event)
    print(f"x_beg={x_beg}, y_beg={y_beg}")
    print(f"coordinates: {x, y}")
    #check if user clicked inside of the field
    if x == -1 or y == -1:
        canvas.create_rectangle(x_beg+10, y_beg+10, x_beg+110, y_beg+110, fill="white")
        counter = 0
        x_beg = 0
        y_beg = 0
        pass
    else:
        if counter == 0:
            canvas.create_rectangle(x+10,y+10 , x+110,y+110, fill="blue")
            x_beg = x
            y_beg = y
            counter += 1
            
        elif counter == 1:
            #check if the new square is in the same row
            if x == x_beg or y == y_beg:       
                #down
                if y > y_beg:
                    canvas.create_rectangle(x_beg+10, y_beg+10 , x+110,y+110, fill="blue")
                #up
                elif y < y_beg:
                    canvas.create_rectangle(x+10, y+10 , x_beg+110,y_beg+110, fill="blue")
                #left
                elif x < x_beg:
                    canvas.create_rectangle(x+10, y+10 , x_beg+110,y_beg+110, fill="blue")
                #right
                elif x > x_beg:
                    canvas.create_rectangle(x_beg+10, y_beg+10 , x+110,y+110, fill="blue")
            else:
                canvas.create_rectangle(x_beg+10, y_beg+10, x_beg+110, y_beg+110, fill="white")
            counter = 0
            
'''
def export_to_png():
    ps_file = "canvas_image.ps"
    canvas.postscript(file=ps_file, colormode="color")
    img = Image.open(ps_file)
    img.save("canvas_image.png", format="png")
    print("Image exported to canvas_image.png")
'''

field()
canvas.bind('<Button-1>', level)

'''
export_button = tkinter.Button(window, text="Export to PNG", command=export_to_png)
export_button.pack()
'''

window.mainloop()