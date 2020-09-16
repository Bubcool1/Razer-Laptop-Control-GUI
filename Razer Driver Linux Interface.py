from dearpygui.dearpygui import *
import os

# Global Variable Declaration
global EffectPrefix
global function
global one
global two
EffectPrefix = "razer-cli write effect "


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
    delete_item("MainWindow", True)    
    add_color_picker4("Static Colour", width=500, callback=StaticPageBack)
    add_same_line(spacing=10)
    # add_button("Save2", callback=print_me)
    end()

def StaticPageBack(sender, data):
    colour1 = get_value("Static Colour") # Clear Screen

    redone = " " + str(colour1[0])
    greenone = " " + str(colour1[1])
    blueone = " " + str(colour1[2])

    one = redOne + greenOne + blueOne

    function = 'static'

    Fullcommand = EffectPrefix + function + one
    print(Fullcommand)
    os.system(Fullcommand)

def StaticGradient(sender, data):
    delete_item("MainWindow", True) # Clear Screen
    add_color_picker4("Static Colour 1", width=500, callback=StaticGradientBack)
    add_same_line(spacing=10)
    add_color_picker4("Static Colour 2", width=500, callback=StaticGradientBack)

def StaticGradientBack(sender, data):
    colour1 = get_value("Static Colour 1")
    colour2 = get_value("Static Colour 1")

    redone = " " + str(colour1[0])
    greenone = " " + str(colour1[1])
    blueone = " " + str(colour1[2])

    one = redOne + greenOne + blueOne

    redTwo = " " + str(colour1[0])
    greenTwo = " " + str(colour1[1])
    blueTwo = " " + str(colour1[2])

    two = redTwo + greenTwo + blueTwo

    function = 'static'

    Fullcommand = EffectPrefix + function + one + two
    print(Fullcommand)
    os.system(Fullcommand)


# Menubar
add_menu_bar("Main Menu")
add_menu("Effects")
add_menu_item("Static", callback=StaticPage)
add_menu_item("Static Gradient", callback=StaticGradient)
add_menu_item("Wave Gradient")
add_menu_item("Breathing Single")
end()


# add_input_text("Static or wave")

# add_color_picker4("Colour 1", width=500, callback=print_me)
# add_same_line(spacing=10)
# add_color_picker4("Colour 2", width=500, callback=print_me)

# add_button("Save", callback=print_me)


start_dearpygui()
