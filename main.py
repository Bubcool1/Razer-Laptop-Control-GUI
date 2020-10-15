import tkinter as tkinter
from tkinter.ttk import *
import os
import tkcolorpicker 

global color

# master = Tk() 

class MyFirstGUI(tkinter.Toplevel):
    def __init__(self, master):
        self.master = master
        master.title("Menu")
        master.geometry("200x250")

        self.label = tkinter.Label(master, text="Razer-Laptop-Control GUI", padx=21, pady=10)
        self.label.pack()

        self.static_button = tkinter.Button(master, text="Static Colour", command=self.static, padx=21, pady=10)
        self.static_button.pack()

        self.static_button = tkinter.Button(master, text="Static Gradient", command=self.staticGradient, padx=16, pady=10)
        self.static_button.pack()

        self.static_button = tkinter.Button(master, text="Wave Gradient", command=self.waveGradient, padx=16, pady=10)
        self.static_button.pack()

        self.static_button = tkinter.Button(master, text="Breathing Single", command=self.breathingSingle, padx=11, pady=10)
        self.static_button.pack()

        self.close_button = tkinter.Button(master, text="Quit All", command=master.quit, padx=37, pady=10, background='#C50A0B', foreground='white')
        self.close_button.pack()        

    def static(self):
        color = str(tkcolorpicker.askcolor((0, 0, 0)))

        color = color.split(",", 2)

        red = color[0]
        red = red.split("((", 1)
        red = red[1]
        # print(red)
        green = color[1]
        green = green.split(" ", 1)
        green = green[1]
        # print(green)
        blue = color[2]
        blue = blue.split(")", 1)
        blue = blue[0]
        blue = blue.split(" ", 1)
        blue = blue[1]
        # print(blue)
        os.system('clear && razer-cli write effect ' + "static" + ' ' + red + ' ' + green + ' ' + blue)

    def breathingSingle(self):
        breathingSingleWindow = tkinter.Toplevel(root)
        breathingSingleWindow.title("Breathing Single")
        global color

        color = str(tkcolorpicker.askcolor((0, 0, 0), breathingSingleWindow))

        color = color.split(",", 2)

        red = color[0]
        red = red.split("((", 1)
        red = red[1]
        # print(red)
        green = color[1]
        green = green.split(" ", 1)
        green = green[1]
        # print(green)
        blue = color[2]
        blue = blue.split(")", 1)
        blue = blue[0]
        blue = blue.split(" ", 1)
        blue = blue[1]
        # print(blue)
        color = ' ' + red + ' ' + green + ' ' + blue + ' '

        self.timeSlider1 = tkinter.Scale(breathingSingleWindow, from_=0, to=200, orient=tkinter.HORIZONTAL)
        self.timeSlider1.pack()

        self.static_button = tkinter.Button(breathingSingleWindow, text="Submit", command=self.breathingBack)
        self.static_button.pack()

        self.close_button = tkinter.Button(breathingSingleWindow, text="Quit All", command=breathingSingleWindow.quit)
        self.close_button.pack()

    def breathingBack(self):
        Duration = int(self.timeSlider1.get())
        os.system('clear && razer-cli write effect ' + "breathing_single" + color + str(Duration))
    
    def waveGradient(self):
        color1 = str(tkcolorpicker.askcolor((0, 0, 0), title=("Wave Gradient Colour 1")))
        color1 = color1.split(",", 2)

        red = color1[0]
        red = red.split("((", 1)
        red = red[1]
        # print(red)
        green = color1[1]
        green = green.split(" ", 1)
        green = green[1]
        # print(green)
        blue = color1[2]
        blue = blue.split(")", 1)
        blue = blue[0]
        blue = blue.split(" ", 1)
        blue = blue[1]
        # print(blue)
        color1 = ' ' + red + ' ' + green + ' ' + blue + ' '

        color2 = str(tkcolorpicker.askcolor((0, 0, 0), title=("Wave Gradient Colour 2")))

        color2 = color2.split(",", 2)

        red = color2[0]
        red = red.split("((", 1)
        red = red[1]
        # print(red)
        green = color2[1]
        green = green.split(" ", 1)
        green = green[1]
        # print(green)
        blue = color2[2]
        blue = blue.split(")", 1)
        blue = blue[0]
        blue = blue.split(" ", 1)
        blue = blue[1]
        # print(blue)
        color2 = red + ' ' + green + ' ' + blue

        os.system('razer-cli write effect ' + "wave_gradient" + color1 + color2)

    def staticGradient(self):
        color1 = str(tkcolorpicker.askcolor((0, 0, 0), title=("Static Gradient Colour 1")))
        color1 = color1.split(",", 2)

        red = color1[0]
        red = red.split("((", 1)
        red = red[1]
        # print(red)
        green = color1[1]
        green = green.split(" ", 1)
        green = green[1]
        # print(green)
        blue = color1[2]
        blue = blue.split(")", 1)
        blue = blue[0]
        blue = blue.split(" ", 1)
        blue = blue[1]
        # print(blue)
        color1 = ' ' + red + ' ' + green + ' ' + blue + ' '

        color2 = str(tkcolorpicker.askcolor((0, 0, 0), title=("Static Gradient Colour 2")))

        color2 = color2.split(",", 2)

        red = color2[0]
        red = red.split("((", 1)
        red = red[1]
        # print(red)
        green = color2[1]
        green = green.split(" ", 1)
        green = green[1]
        # print(green)
        blue = color2[2]
        blue = blue.split(")", 1)
        blue = blue[0]
        blue = blue.split(" ", 1)
        blue = blue[1]
        # print(blue)
        color2 = red + ' ' + green + ' ' + blue

        os.system('razer-cli write effect ' + "static_gradient" + color1 + color2)


root = tkinter.Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
