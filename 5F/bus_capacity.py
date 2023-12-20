import tkinter

def bus_stops_names(bus_stops):
    x = 20
    y = 20
    for i in range(len(bus_stops)):
        canvas.create_text(x, y, text = bus_stops[i], anchor = "nw")
        y += 50

def bus_capacity_bar(event):
    global state, x, y, current_capacity
    if state < len(passg_in):
        current_capacity += passg_in[state]-passg_out[state] #number of passangers in bus    
        bar_width = (current_capacity/bus_capacity)*200 #lenght of bar
        canvas.create_rectangle(170, y, 370,y+20)    
        if bar_width < 200:
            canvas.create_rectangle(170, y, 170 + bar_width, y + 20, fill="green")
        else:
            canvas.create_rectangle(x + 150, y, x + 150 + bar_width, y + 20, fill="red")
        state+=1
        y+=50
    else:
        exit()


        
with open("C:\\SCHOOL\\programing\\5.F\\bus.txt",encoding = "utf-8") as input_file:
    file = input_file.readlines()
    data = []
    bus_stops = []
    passg_in = []
    passg_out = []
    #erase "\n" from end 
    for item in file:
        data.append(item[:-1])        
    bus_capacity = int(data.pop(0))
    #extract bus stops names, passangers in and out
    for item in data:
        item = item.split(" ")
        passg_in.append(int(item[0]))
        passg_out.append(int(item[1]))
        stops = ""
        for i in item:
            if i.isalpha():
                stops += f" {i}"       
        bus_stops.append(stops)
        
        if "" in bus_stops:
            bus_stops.remove("")   

HEIGHT = len(bus_stops)*50
WIDTH = 500
x = 20
y = 20
state = 0 #nuber of passangers in bus
current_capacity = 0

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=WIDTH, height=HEIGHT, bg = "white")
canvas.pack()

bus_stops_names(bus_stops)
canvas.bind('<Button-1>', bus_capacity_bar)

window.mainloop()