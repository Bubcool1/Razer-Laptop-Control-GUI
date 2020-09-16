from dearpygui.dearpygui import *
import os

# Global Variable Declaration
global EffectPrefix
global function
global one
global two
EffectPrefix = "razer-cli write effect "

# Screen clearing Function
def ScreenClear():
    delete_item("Static Colour Picker")
    delete_item("Static Colour")

    delete_item("Static Gradient Picker")
    delete_item("Static Colour 1")
    delete_item("Static Colour 2")

    delete_item("Wave Gradient Picker")
    delete_item("Wave Colour 1")
    delete_item("Wave Colour 1")
    
    delete_item("Breathing Colour Picker")
    delete_item("Breathing Colour")


def print_me(sender, data):
    print(get_value("Colour 1"))
    colour1 = get_value("Colour 1")
    colour2 = get_value("Colour 2")

    redone = " " + str(colour1[0])
    greenone = " " + str(colour1[1])
    blueone = " " + str(colour1[2])

    one = redone + greenone + blueone

    redtwo = " " + str(colour2[0])
    greentwo = " " + str(colour2[1])
    bluetwo = " " + str(colour2[2])

    two = redtwo + greentwo + bluetwo

    # if str(UsrInput.lower()) == "static":
    #     function = "static_gradient"
    # else:
    #     function = "wave_gradient"

    Fullcommand = prefix + function + one + two
    print(Fullcommand)
    os.system(Fullcommand)
    print("Command Run")


def StaticPage(sender, data):
    # delete_item("MainWindow", True) # Clear Screen
    ScreenClear()
    add_text("Static Colour Picker")

    add_color_picker4("Static Colour", width=500, callback=StaticPageBack)
    # add_button("Save2", callback=print_me)
    end()

def StaticPageBack(sender, data):
    colour1 = get_value("Static Colour") # Clear Screen

    redOne = " " + str(colour1[0])
    greenOne = " " + str(colour1[1])
    blueOne = " " + str(colour1[2])

    one = redOne + greenOne + blueOne

    function = 'static'

    Fullcommand = EffectPrefix + function + one
    print(Fullcommand)
    os.system(Fullcommand)

def StaticGradient(sender, data):
    # delete_item("MainWindow", True) # Clear Screen
    ScreenClear()
    add_text("Static Gradient Picker")

    add_color_picker4("Static Colour 1", width=500, callback=StaticGradientBack)
    add_same_line(spacing=10)
    add_color_picker4("Static Colour 2", width=500, callback=StaticGradientBack)

def StaticGradientBack(sender, data):
    colour1 = get_value("Static Colour 1")
    colour2 = get_value("Static Colour 2")

    redOne = " " + str(colour1[0])
    greenOne = " " + str(colour1[1])
    blueOne = " " + str(colour1[2])

    one = redOne + greenOne + blueOne

    redTwo = " " + str(colour2[0])
    greenTwo = " " + str(colour2[1])
    blueTwo = " " + str(colour2[2])

    two = redTwo + greenTwo + blueTwo

    function = 'static_gradient'

    Fullcommand = EffectPrefix + function + one + two
    print(Fullcommand)
    os.system(Fullcommand)

def WaveGradient(sender, data):
    # delete_item("MainWindow", True) # Clear Screen
    ScreenClear()
    add_text("Wave Gradient Picker")
    
    add_color_picker4("Wave Colour 1", width=500, callback=WaveGradientBack)
    add_same_line(spacing=10)
    add_color_picker4("Wave Colour 2", width=500, callback=WaveGradientBack)

def WaveGradientBack(sender, data):
    colour1 = get_value("Wave Colour 1")
    colour2 = get_value("Wave Colour 2")

    redOne = " " + str(colour1[0])
    greenOne = " " + str(colour1[1])
    blueOne = " " + str(colour1[2])

    one = redOne + greenOne + blueOne

    redTwo = " " + str(colour2[0])
    greenTwo = " " + str(colour2[1])
    blueTwo = " " + str(colour2[2])

    two = redTwo + greenTwo + blueTwo

    function = 'wave_gradient'

    Fullcommand = EffectPrefix + function + one + two
    print(Fullcommand)
    os.system(Fullcommand)

def BreathingSingle(sender, data):
    # delete_item("MainWindow", True) # Clear Screen
    ScreenClear()
    add_text("Breathing Colour Picker")

    add_color_picker4("Breathing Colour", width=500, callback=BreathingSingleBack)
    # add_button("Save2", callback=print_me)
    end()

def BreathingSingleBack(sender, data):
    colour1 = get_value("Breathing Colour") # Clear Screen

    redOne = " " + str(colour1[0])
    greenOne = " " + str(colour1[1])
    blueOne = " " + str(colour1[2])

    one = redOne + greenOne + blueOne

    function = 'breathing_single'

    Fullcommand = EffectPrefix + function + one
    print(Fullcommand)
    os.system(Fullcommand)


# Menubar
add_menu_bar("Main Menu")
add_menu("Effects")
add_menu_item("Static", callback=StaticPage)
add_menu_item("Static Gradient", callback=StaticGradient)
add_menu_item("Wave Gradient", callback=WaveGradient)
add_menu_item("Breathing Single", callback=BreathingSingle)
end()


# add_input_text("Static or wave")

# add_color_picker4("Colour 1", width=500, callback=print_me)
# add_same_line(spacing=10)
# add_color_picker4("Colour 2", width=500, callback=print_me)

# add_button("Save", callback=print_me)


start_dearpygui()
