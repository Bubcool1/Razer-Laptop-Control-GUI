from dearpygui.dearpygui import *
import os

# def save_callback(sender, data):
#     prefix = "razer-cli write effect "


#     redone = " " + str(get_value("Red 1"))
#     greenone = " " + str(get_value("Green 1"))
#     blueone = " " + str(get_value("Blue 1"))

#     one = redone + greenone + blueone

#     redtwo = " " + str(get_value("Red 2"))
#     greentwo = " " + str(get_value("Green 2"))
#     bluetwo = " " + str(get_value("Blue 2"))

#     two = redtwo + greentwo + bluetwo


#     UsrInput = get_value("Static or wave")
#     # print(UsrInput)
#     # UsrInput = str(UsrInput).lower()
#     # print(UsrInput)

#     if str(UsrInput.lower()) == "static":
#         function = "static_gradient"
#     else:
#         function = "wave_gradient"

# Fullcommand = prefix + function + one + two
# print(Fullcommand)
# os.system(Fullcommand)
# print("Command Run")

def print_me(sender, data):
    print(get_value("Colour 1"))

    UsrInput = get_value("Static or wave")
    prefix = "razer-cli write effect "
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

    if str(UsrInput.lower()) == "static":
        function = "static_gradient"
    else:
        function = "wave_gradient"

    Fullcommand = prefix + function + one + two
    print(Fullcommand)
    os.system(Fullcommand)
    print("Command Run")


os.system("python -V")

add_input_text("Static or wave")

# add_text("First Colours")
# add_slider_int("Red 1", default_value=0, min_value=0, max_value=255,)
# add_slider_int("Green 1", default_value=0, min_value=0, max_value=255,)
# add_slider_int("Blue 1", default_value=0, min_value=0, max_value=255,)

# add_text("Second Colours")
# add_slider_int("Red 2", default_value=0, min_value=0, max_value=255, )
# add_slider_int("Green 2", default_value=0, min_value=0, max_value=255,)
# add_slider_int("Blue 2", default_value=0, min_value=0, max_value=255,)


add_color_picker4("Colour 1", width=500, callback=print_me)
add_color_picker4("Colour 2", width=500, callback=print_me)
add_button("Save", callback=print_me)

start_dearpygui()
