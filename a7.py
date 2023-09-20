import struct
import time
import sys
import random
import serial
from tkinter import *
from tkinter import ttk

status="";
iter=0; iter2=0; iter_absolutefirst=0
xsteps=0;ysteps=0;x=0;y=0;iterator=0;

#the location increment is the increment per keystroke displayed on the top. the increment display is the increment in pixels on the canvas. timebetweensteps is really small because since we're moving in microns, we have to move a lot of microns; they should move fast af.
incrementx_location=0; incrementy_location=0;
incrementx_display=0; incrementy_display=0; minimumtravel_display=0.03; minimumtravel_location=25; timebetweensteps=0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001;

#the highest value of x,y and the lowest value of x, y. The tool has to stay within (start_x, start_y) and (limit_x, limit_y)
limit_x=220000; limit_y=280000;
start_x=0; start_y=0;

#origin_status="Start"

#locations of all buttons typed here for convenience so we can just change them here and don't have to look for the buttons to change their location
Offbutton_location_x=495; Offbutton_location_y=0
Onbutton_location_x=495; Onbutton_location_y=0
controltoolyourselfprompt_location_x=550; controltoolyourselfprompt_location_y=80
enterlocationprompt_location_x=390; enterlocationprompt_location_y=80
Frequency_and_duty_cycle_entry_button_location_x=390; Frequency_and_duty_cycle_entry_button_location_y=130
Voltage_and_current_button_location_x=390; Voltage_and_current_button_location_y=180
fill_button_location_x=390; fill_button_location_y=230
spark_button_location_x=390; spark_button_location_y=280
drain_button_location_x=390; drain_button_location_y=320
toollocationscreen_x=25; toollocationscreen_y=250
detect_x=50;detect_y=570
proceed_x=210; proceed_y=570

status=""                           #Is the machine starting or stopping
status_location=""                  #Is the location being entered at the starting of the machine or is it being entered via a button during operation
status_frequency_and_duty_cycle=""
status_drain=""
status_power=""
status_fill=""
status_spark=""

Voltage=0; Current=0; Frequency_value=0; Duty_cycle_value=0

#Establishing serial communication from this program to Arduino.

stepper_data1=serial.Serial('COM7',baudrate=9600)
#stepper_data2=serial.Serial('COM8',baudrate=9600)

def pressure_value():
    for x in range(10):
      print(random.randint(1.8,2.1))

def flowrate_value():
    flowrate=0.0;
    flowrate=random.uniform(1.8,2.1)

def temperature_value():
    for x in range(10):
      print(random.randint(1,9))

toolclearance=0
def readup():
    global toolclearance
    while stepper_data1.in_waiting:
        print("taking")
        if toolclearance!=5:
            input=stepper_data1.read()
            returningback=input.decode("ascii")
            if returningback!="5":
                print(returningback)
            if returningback=="5":
                print("YES")
                toolclearance=5
                #tool_touched()
                break; return
        time.sleep(0.5)

#This delay of a few seconds right after establishing serial communication is very important because as soon as python program is run, the arduino resets and any data sent by python during this resetting is lost; thus, we'd better wait a few seconds and then start sending serial data.
time.sleep(2)

#function that converts stepper motor's steps to linear movement
def steppertoscrew():
    global x; global y;
    x=25*xsteps; y=25*ysteps;

#function that converts linear movement to stepper motor's steps
def screwtostepper():
    global xsteps; global ysteps;
    xsteps=x/25; ysteps=y/25;

#Starting the GUI display
window = Tk()
window.title("μ Electric Discharge Machine")
window.geometry("1024x768+0+0")
window.configure(background="#262626")
xLocation = StringVar(); yLocation = StringVar();

def drive_the_rails_to_users_location():
    #if greenlightformovement==1:   DELETE THIS LINE, not the 2 below it, or delete this comment.
    print(xsteps, "have been turned by x stepper and ",ysteps,"have been turned by the y stepper")
    print("The tool is at ",x," ",y)


                                            #   DISPLAYING REAL TIME LOCATION OF TOOL (TOP)

def currentlocationliveupdates():
    global currentlocationcoordinates
    global Voltage
    global Current
    global Frequency_value
    global Duty_cycle_value
    #currentlocationcoordinates.place_forget()
    currentlocationcoordinates=Label(window, text=(x,",",y,"μm"),bg="#262626", fg="white", font=("montserrat",14,"normal"))
    currentlocationcoordinates.place_forget()
    currentlocationcoordinates.place(x=125,y=25)
    currentvoltageandcurrent=Label(window, text=(Voltage,"V", ",", Current, "Amp"),bg="#262626", fg="white", font=("montserrat",14,"normal"))
    currentvoltageandcurrent.place(x=125,y=50)
    currentfrequencyanddutycycle=Label(window, text=(Frequency_value,"Hz", ",", Duty_cycle_value, "%"),bg="#262626", fg="white", font=("montserrat",14,"normal"))
    currentfrequencyanddutycycle.place(x=125,y=75)
    #currentlocationtext.place_forget()
    #currentlocationtext.place(x=125,y=50)

currentlocationliveupdates()

Tool_location=PhotoImage(file="location_icon.gif")
Tool_location_properties=Label(window,image=Tool_location,bg="#262626")
Tool_location_button=Button(window,image=Tool_location,bg="#262626",highlightthickness=0,bd=0,command=currentlocationliveupdates)
Tool_location_button.place(x=35,y=25)

                                            #   DISPLAYING REAL TIME LOCATION OF TOOL (BOTTOM)

                                                    #   FEEDBACK SCHEMATIC (BOTTOM)

#An image of the EDM schematic
schematic_image_file=PhotoImage(file="schematic.gif")
schematic_image=Label (window, image=schematic_image_file, bg="#262626")
schematic_image.place(x=525,y=40)

level_tank_1=Label (window,text=("Level"),bg="#262626",fg="white",font=("montserrat",7,"normal"))
level_tank_1_value=Label (window,text=("12", "cm"),bg="#262626",fg="white",font=("montserrat",9,"normal"))

level_tank_2=Label (window,text=("Level"),bg="#262626",fg="white",font=("montserrat",7,"normal"))
level_tank_2_value=Label (window,text=("12", "cm"),bg="#262626",fg="white",font=("montserrat",9,"normal"))

temperatature_text=Label (window,text=("Temperature"),bg="#262626",fg="white",font=("montserrat",7,"normal"))
#the verticle temperature bar
s = ttk.Style()         #this whole "s" thing simply changes the color of the bar, it's green by default, I wanted red.
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
temperaturebar=ttk.Progressbar(window, style="red.Horizontal.TProgressbar", orient='vertical', length=100, mode='determinate', value=20)

pump_1_pressure=Label(window, text=("Pressure "),bg="#262626",fg="white",font=("montserrat",7,"normal"))
pump_1_pressure_value=Label(window, text=("5", "Pa"),bg="#262626",fg="white",font=("montserrat",9,"normal"))

pump_2_pressure=Label(window, text=("Pressure "),bg="#262626",fg="white",font=("montserrat",7,"normal"))
pump_2_pressure_value=Label(window, text=("5", "Pa"),bg="#262626",fg="white",font=("montserrat",9,"normal"))

tank_1_pressure=Label(window, text=("Pressure "),bg="#262626",fg="white",font=("montserrat",7,"normal"))
tank_1_pressure_value=Label(window, text=("5", "Pa"),bg="#262626",fg="white",font=("montserrat",9,"normal"))

tank_1_temperature=Label(window, text=("Temperature "),bg="#262626",fg="white",font=("montserrat",7,"normal"))
tank_1_temperature_value=Label(window, text=("5", "C"),bg="#262626",fg="white",font=("montserrat",9,"normal"))

tool_temperature=Label(window, text=("Temperature "),bg="#262626",fg="white",font=("montserrat",7,"normal"))
tool_temperature_value=Label(window, text=("5", "C"),bg="#262626",fg="white",font=("montserrat",9,"normal"))

tool_flow_rate=Label(window, text=("Flow "),bg="#262626",fg="white",font=("montserrat",7,"normal"))
tool_flow_rate_value=Label(window, text=("0.1", "m3/s"),bg="#262626",fg="white",font=("montserrat",9,"normal"))

tool_flow_rate.place(x=757,y=65)
tool_flow_rate_value.place(x=750,y=85)

tool_temperature.place(x=813,y=65)
tool_temperature_value.place(x=828,y=85)

tank_1_temperature.place(x=865,y=276)
tank_1_temperature_value.place(x=885,y=295)

tank_1_pressure.place(x=654,y=276)
tank_1_pressure_value.place(x=656,y=295)

level_tank_1.place(x=660,y=210)
level_tank_1_value.place(x=655,y=225)

level_tank_2.place(x=660,y=585)
level_tank_2_value.place(x=655,y=600)

temperatature_text.place(x=945,y=345)
temperaturebar.place(x=965,y=365)

pump_1_pressure.place(x=555,y=430)
pump_1_pressure_value.place(x=555,y=445)

pump_2_pressure.place(x=855,y=450)
pump_2_pressure_value.place(x=855,y=465)

                                                #   FEEDBACK SCHEMATIC (BOTTOM)
def limitswitchreturningdata():
    while stepper_data1.in_waiting:
        input=stepper_data1.readline()
        returningback=input.decode("ascii")
        print(returningback)
        #time.sleep(1)
                                            #   KEYBOARD LOCATION ENTRY SYSTEM (TOP)

#function that registers keystrokes
def keystrokelocation(event):
    global userx;
    global x; global y;
    global incrementx_location; global incrementy_location;
    global minimumtravel_location
    global incrementx_display; global incrementy_display;
    global minimumtravel_display;
    incrementx_display=0; incrementy_display=0;             #These are set to 0 right after you press a jey so that the next time, only your next key governs the motion of the tool on the screen.
    incrementx_location=0; incrementy_location=0;
    timedelayaftersendingdata=1; timedelayinreceivingloop=0.75;

    Delimiter_Comma=","

    if event.char == event.keysym:
        msg = 'Normal Key %r' % event.char
    elif len(event.char) == 1:
        msg = 'Punctuation Key %r (%r)' % (event.keysym, event.char)
    else:
        msg = 'Special Key %r' % event.keysym
    toollocationscreen.place_forget()
    print(msg)

    if msg=="Special Key 'Right'":
        if x<limit_x:
            textright=("you're moving the tool to right side")
            print(textright)
            incrementx_display=+minimumtravel_display
            incrementx_location=+minimumtravel_location
            currentlocationcoordinates.place_forget()
            #incrementx=+minimumtravel
            Thetask="keyboardentry"; x_stepper_right="r"
            #lengths of all strings:
            lengthThetask=len(Thetask); lengthx_stepper_right=len(x_stepper_right); lengthDelimiter_Comma=len(Delimiter_Comma)
            #lengths are in integers by default, converting them to strings
            lengthThetaskstring=str(lengthThetask); lengthx_stepper_rightstring=str(lengthx_stepper_right); lengthDelimiter_Commastring=str(lengthDelimiter_Comma);
            #joining the lengths of all the data to be sent with "s" in between, stringpackingsize is like 16s3s1s3s1s4s1s (just an example). the variable contains the data regarding the size of the strings that are being combined by struct and then sent to arduino
            stringpackingsize=lengthThetaskstring+"s"+lengthDelimiter_Commastring+"s"+lengthx_stepper_rightstring+"s"
            send_string_Frequency_and_Duty_command=struct.pack(stringpackingsize, Thetask.encode('UTF-8'), Delimiter_Comma.encode('UTF-8'), x_stepper_right.encode('UTF-8'))
            stepper_data1.write(send_string_Frequency_and_Duty_command)
            #stepper_data2.write(send_string_Frequency_and_Duty_command)
            #time.sleep(timedelayaftersendingdata)
            while stepper_data1.in_waiting:
                input=stepper_data1.readline()
                returningback=input.decode("ascii")
                print(returningback)
            #    time.sleep(timedelayinreceivingloop)
        controltool()

    if msg=="Special Key 'Left'":
        if x>start_x:
            print("you're moving the tool to left side")
            incrementx_display=-minimumtravel_display
            incrementx_location=-minimumtravel_location
            currentlocationcoordinates.place_forget()
            """
            x_stepper_left='l'
            x_stepper_left_ecnode=x_stepper_left.encode()
            stepper_data.write(x_stepper_left_ecnode)
            print(x_stepper_left_ecnode)
            """
            Thetask="keyboardentry"; x_stepper_left="l"
            #lengths of all strings:
            lengthThetask=len(Thetask); lengthx_stepper_left=len(x_stepper_left); lengthDelimiter_Comma=len(Delimiter_Comma)
            #lengths are in integers by default, converting them to strings
            lengthThetaskstring=str(lengthThetask); lengthx_stepper_leftstring=str(lengthx_stepper_left); lengthDelimiter_Commastring=str(lengthDelimiter_Comma);
            #joining the lengths of all the data to be sent with "s" in between, stringpackingsize is like 16s3s1s3s1s4s1s (just an example). the variable contains the data regarding the size of the strings that are being combined by struct and then sent to arduino
            stringpackingsize=lengthThetaskstring+"s"+lengthDelimiter_Commastring+"s"+lengthx_stepper_leftstring+"s"
            send_string_Frequency_and_Duty_command=struct.pack(stringpackingsize, Thetask.encode('UTF-8'), Delimiter_Comma.encode('UTF-8'), x_stepper_left.encode('UTF-8'))
            stepper_data1.write(send_string_Frequency_and_Duty_command)
            #stepper_data2.write(send_string_Frequency_and_Duty_command)
            #time.sleep(timedelayaftersendingdata)
            while stepper_data1.in_waiting:
                input=stepper_data1.readline()
                returningback=input.decode("ascii")
                print(returningback)
            #    time.sleep(timedelayinreceivingloop)
        controltool()

    if msg=="Special Key 'Up'":
        if y>start_y:
            print("you're moving the tool to top side")
            incrementy_display=-minimumtravel_display
            incrementy_location=-minimumtravel_location
            currentlocationcoordinates.place_forget()
            #Sending the stepper to take a step to move the power screw right
            # incrementx=+minimumtravel
            Thetask="keyboardentry"; x_stepper_up="u"
            #lengths of all strings:
            lengthThetask=len(Thetask); lengthx_stepper_up=len(x_stepper_up); lengthDelimiter_Comma=len(Delimiter_Comma)
            #lengths are in integers by default, converting them to strings
            lengthThetaskstring=str(lengthThetask); lengthx_stepper_upstring=str(lengthx_stepper_up); lengthDelimiter_Commastring=str(lengthDelimiter_Comma);
            #joining the lengths of all the data to be sent with "s" in between, stringpackingsize is like 16s3s1s3s1s4s1s (just an example). the variable contains the data regarding the size of the strings that are being combined by struct and then sent to arduino
            stringpackingsize=lengthThetaskstring+"s"+lengthDelimiter_Commastring+"s"+lengthx_stepper_upstring+"s"
            send_string_Frequency_and_Duty_command=struct.pack(stringpackingsize, Thetask.encode('UTF-8'), Delimiter_Comma.encode('UTF-8'), x_stepper_up.encode('UTF-8'))
            stepper_data1.write(send_string_Frequency_and_Duty_command)
            #stepper_data1.write(send_string_Frequency_and_Duty_command)
            #time.sleep(timedelayaftersendingdata)
            while stepper_data1.in_waiting:
                input=stepper_data1.readline()
                returningback=input.decode("ascii")
                print(returningback)
            #    time.sleep(timedelayinreceivingloop)
        controltool()

    if msg=="Special Key 'Down'":
        if y<limit_y:
            print("you're moving the tool to bottom side")
            incrementy_display=+minimumtravel_display;
            incrementy_location=+minimumtravel_location;
            currentlocationcoordinates.place_forget()
            # incrementx=+minimumtravel
            Thetask="keyboardentry"; x_stepper_down="d"
            #lengths of all strings:
            lengthThetask=len(Thetask); lengthx_stepper_down=len(x_stepper_down); lengthDelimiter_Comma=len(Delimiter_Comma)
            #lengths are in integers by default, converting them to strings
            lengthThetaskstring=str(lengthThetask); lengthx_stepper_downstring=str(lengthx_stepper_down); lengthDelimiter_Commastring=str(lengthDelimiter_Comma);
            #joining the lengths of all the data to be sent with "s" in between, stringpackingsize is like 16s3s1s3s1s4s1s (just an example). the variable contains the data regarding the size of the strings that are being combined by struct and then sent to arduino
            stringpackingsize=lengthThetaskstring+"s"+lengthDelimiter_Commastring+"s"+lengthx_stepper_downstring+"s"
            send_string_Frequency_and_Duty_command=struct.pack(stringpackingsize, Thetask.encode('UTF-8'), Delimiter_Comma.encode('UTF-8'), x_stepper_down.encode('UTF-8'))
            stepper_data1.write(send_string_Frequency_and_Duty_command)
            #stepper_data2.write(send_string_Frequency_and_Duty_command)
            #time.sleep(timedelayaftersendingdata)
            while stepper_data1.in_waiting:
                input=stepper_data1.readline()
                returningback=input.decode("ascii")
                print(returningback)
            #    time.sleep(timedelayinreceivingloop)
        controltool()
    if msg=="Special Key 'z'":
        if y<limit_y:
            print("you're moving the tool to bottom side")
            incrementy_display=+minimumtravel_display;
            incrementy_location=+minimumtravel_location;
            currentlocationcoordinates.place_forget()
            # incrementx=+minimumtravel
            Thetask="keyboardentry"; x_stepper_down="z"
            #lengths of all strings:
            lengthThetask=len(Thetask); lengthx_stepper_down=len(x_stepper_down); lengthDelimiter_Comma=len(Delimiter_Comma)
            #lengths are in integers by default, converting them to strings
            lengthThetaskstring=str(lengthThetask); lengthx_stepper_downstring=str(lengthx_stepper_down); lengthDelimiter_Commastring=str(lengthDelimiter_Comma);
            #joining the lengths of all the data to be sent with "s" in between, stringpackingsize is like 16s3s1s3s1s4s1s (just an example). the variable contains the data regarding the size of the strings that are being combined by struct and then sent to arduino
            stringpackingsize=lengthThetaskstring+"s"+lengthDelimiter_Commastring+"s"+lengthx_stepper_downstring+"s"
            send_string_Frequency_and_Duty_command=struct.pack(stringpackingsize, Thetask.encode('UTF-8'), Delimiter_Comma.encode('UTF-8'), x_stepper_down.encode('UTF-8'))
            stepper_data1.write(send_string_Frequency_and_Duty_command)
            #stepper_data2.write(send_string_Frequency_and_Duty_command)
            #time.sleep(timedelayaftersendingdata)
            while stepper_data1.in_waiting:
                input=stepper_data1.readline()
                returningback=input.decode("ascii")
                print(returningback)
            #    time.sleep(timedelayinreceivingloop)
        controltool()
        if msg=="Special Key 'a'":
            if y<limit_y:
                print("you're moving the tool to bottom side")
                incrementy_display=+minimumtravel_display;
                incrementy_location=+minimumtravel_location;
                currentlocationcoordinates.place_forget()
                # incrementx=+minimumtravel
                Thetask="keyboardentry"; x_stepper_down="a"
                #lengths of all strings:
                lengthThetask=len(Thetask); lengthx_stepper_down=len(x_stepper_down); lengthDelimiter_Comma=len(Delimiter_Comma)
                #lengths are in integers by default, converting them to strings
                lengthThetaskstring=str(lengthThetask); lengthx_stepper_downstring=str(lengthx_stepper_down); lengthDelimiter_Commastring=str(lengthDelimiter_Comma);
                #joining the lengths of all the data to be sent with "s" in between, stringpackingsize is like 16s3s1s3s1s4s1s (just an example). the variable contains the data regarding the size of the strings that are being combined by struct and then sent to arduino
                stringpackingsize=lengthThetaskstring+"s"+lengthDelimiter_Commastring+"s"+lengthx_stepper_downstring+"s"
                send_string_Frequency_and_Duty_command=struct.pack(stringpackingsize, Thetask.encode('UTF-8'), Delimiter_Comma.encode('UTF-8'), x_stepper_down.encode('UTF-8'))
                stepper_data1.write(send_string_Frequency_and_Duty_command)
                #stepper_data2.write(send_string_Frequency_and_Duty_command)
                #time.sleep(timedelayaftersendingdata)
                while stepper_data1.in_waiting:
                    input=stepper_data1.readline()
                    returningback=input.decode("ascii")
                    print(returningback)
                #    time.sleep(timedelayinreceivingloop)
            controltool()
    if event.keysym=="Return":
        print("you done?")
        sys.exit(0)

def stopcontrolling():
    global currentlocationcoordinates;
    controltoolyourselfpressed.place_forget()                       #since the "controlling tool" button is no longer needed, it is hidden
    controltoolyourselfprompt.place(x=controltoolyourselfprompt_location_x,y=controltoolyourselfprompt_location_y)                     #the "control tool" prompt is displayed again
    #bind_id=window.bind_all('<Key>', keystrokelocation)             #defined here just so that it can be unbinded again in case it hasn't been defined already. which happens when limit is reached by entering location(no bind_id defined) and then we try to control the tool.
    window.unbind('<Key>', bind_id)                                 #because of this line, when the controltoolyourselfpressed is pressed, the keystroke function is unbinded or terminated, window.unbind and bind_id=window.bind_all together, contained in two functions, act as prompts governing whether the keystrokes are recorded or not.
    toollocationscreen.place_forget()                               #the canvas on which the tool movement is shown is hidden

def controltool():
    global bind_id;
    global x; global y;
    global currentlocationcoordinates;
    #currentlocationcoordinates.place_forget()                       #if you entered location manually before, the coordinates it left must be forgotten first
    """if x==limit_x and y==limit_y:
        print("fuck off")
        stopcontrolling()"""
    if y>=limit_y:
        print("y reached")
        #window.unbind('<Key>', bind_id)
    if x>=limit_x:
        print("x reached")
        #window.unbind('<Key>', bind_id)
    if x<=limit_x or y<=limit_y:
        if x<limit_x or x==limit_x:
            x=x+incrementx_location
            #currentlocationcoordinates.place_forget()
            toollocationscreen.place(x=toollocationscreen_x,y=toollocationscreen_y)
            toollocationscreen.move(toolcircle, incrementx_display, 0)
        if y<limit_y or y==limit_y:
            y=y+incrementy_location
            #currentlocationcoordinates.place_forget()
            toollocationscreen.place(x=toollocationscreen_x,y=toollocationscreen_y)
            toollocationscreen.move(toolcircle, 0, incrementy_display)
        bind_id=window.bind_all('<Key>', keystrokelocation) #the keystroke function is called and equated to a variable because when we want to uncall this function with a button prompt, we need to enter the variable, bind_id, in the unbind's argument.
        controltoolyourselfprompt.place_forget()
        controltoolyourselfpressed.place(x=controltoolyourselfprompt_location_x,y=controltoolyourselfprompt_location_y)
    print("x and y are: ", x, y)
    currentlocationcoordinates.place_forget()
    currentlocationliveupdates()


    #drive_the_rails_to_users_location()    comment is temporary, i need this line

#The prompt that enters the location
#aftertypinglocationpressthis=Button(window,text="ENTER", font=("montserrat",8,"normal"), width=5, bg="yellow",fg="black",command=enterlocation)

#The button that's shown while you are controlling the tool
Controlling_tool=PhotoImage(file="controlling_tool.gif")
Controlling_tool_properties=Label(window,image=Controlling_tool,bg="#262626")
controltoolyourselfpressed=Button(window,image=Controlling_tool,bg="#262626",highlightthickness=0,bd=0,command=stopcontrolling)

#The button already on the screen. When you press it, you start controlling the tool with keyboard.
Control_tool_yourself_button=PhotoImage(file="control_tool.gif")
Control_tool_yourself_button_properties=Label(window,image=Control_tool_yourself_button,bg="#262626")
controltoolyourselfprompt=Button(window,image=Control_tool_yourself_button, bg="#262626",highlightthickness=0,bd=0,command=controltool)
controltoolyourselfprompt.place(x=controltoolyourselfprompt_location_x,y=controltoolyourselfprompt_location_y)

                                            #   KEYBOARD LOCATION ENTRY SYSTEM (BOTTOM)
controltoolyourselfprompt
controltoolyourselfpressed
controltoolyourselfprompt.place(x=550,y=80)
                                            #   MANUAL LOCATION ENTRY SYSTEM (TOP)
def get_it_moving():
    global xLocation; global yLocation
    #global userx; global usery
    global directionx; global directiony
    global initialuserx; global initialusery
    Delimiter_Comma=","; Thetask="getthetoolmoving"
    global delta_x; global delta_y
    userx=0; usery=0;
    iter=0
    userx=delta_x/25; usery=delta_y/25              #these are the steps to be turned for moving userx and usery
    print("userx and usery are", userx, usery)
    userxstring=str(userx); userystring=str(usery)
    timedelayaftersendingdata=2; timedelayinreceivingloop=0.25;
    #lengths of all strings:
    lengthThetask=len(Thetask); lengthuserx=len(userxstring); lengthusery=len(userystring); lengthDelimiter_Comma=len(Delimiter_Comma); lengthdirectionx=len(directionx); lengthdirectiony=len(directiony);
    #lengths are in integers by default, converting them to strings
    lengthThetaskstring=str(lengthThetask); lengthuserxstring=str(lengthuserx); lengthuserystring=str(lengthusery); lengthDelimiter_Commastring=str(lengthDelimiter_Comma);  lengthdirectionxstring=str(lengthdirectionx); lengthdirectionystring=str(lengthdirectiony);
    #joining the lengths of all the data to be sent with "s" in between, stringpackingsize is like 16s3s1s3s1s4s1s (just an example). the variable contains the data regarding the size of the strings that are being combined by struct and then sent to arduino
    stringpackingsize=lengthThetaskstring+"s"+lengthDelimiter_Commastring+"s"+lengthuserxstring+"s"+lengthDelimiter_Commastring+"s"+lengthdirectionxstring+"s"+lengthDelimiter_Commastring+"s"+lengthuserystring+"s"+lengthDelimiter_Commastring+"s"+lengthdirectionystring+"s"+lengthDelimiter_Commastring+"s"
    #b=struct.pack('3s', String.encode('UTF-8'))
    send_string_location=struct.pack(stringpackingsize, Thetask.encode('UTF-8'), Delimiter_Comma.encode('UTF-8'), userxstring.encode('UTF-8'), Delimiter_Comma.encode('UTF-8'), directionx.encode('UTF-8'), Delimiter_Comma.encode('UTF-8'), userystring.encode('UTF-8'), Delimiter_Comma.encode('UTF-8'), directiony.encode('UTF-8'), Delimiter_Comma.encode('UTF-8'))
    print(send_string_location)
    stepper_data1.write(send_string_location);
    #stepper_data2.write(send_string_location);
    time.sleep(timedelayaftersendingdata)
    while stepper_data1.in_waiting:
        input=stepper_data1.readline()
        returningback=input.decode("ascii")
        print(returningback)
        time.sleep(timedelayinreceivingloop)


#6. When the user submits the location by pressing enter, this function removes the prompts opened by the last function and resets the screen to the time when location wasn't entered manually, but, more importantly, it converts user's location into integers and calculates the steps for each motor needed to get to that location. It then returns to the original function run when the user had decided to enter location manually, this function is now ready to send this data (steps needed) to a function that actually drives the stepper motors.

#function finds out the steps needed by the stepper to move to the entered location
def displaythetoolmovingtoatoalocationenteredbyuser():
    global userx; global usery;
    global incrementx_display; global incrementy_display
    global minimumtravel_display; global minimumtravel_location
    incrementx_display=minimumtravel_display; incrementy_display=minimumtravel_display
    incrementx_location=minimumtravel_location; incrementy_location=minimumtravel_location
    global x; global y
    global timebetweensteps
    #displayed_x=x; displayed_y=y
    toollocationscreen.place(x=toollocationscreen_x,y=toollocationscreen_y)
    while (x!=userx):
        if x<userx:
            x=x+incrementx_location
            toollocationscreen.move(toolcircle, incrementx_display, 0)
            #time.sleep(timebetweensteps)
        if x>userx:
            x=x-incrementx_location;
            toollocationscreen.move(toolcircle, -incrementx_display, 0)
            #time.sleep(timebetweensteps)
        window.update()
        #limitswitchreturningdata()
        #print (x)
        #print("nigga I'm moving in x bitch")
        if x==userx:
            break
    while (y!=usery):
        if y<usery:
            y=y+incrementx_location
            toollocationscreen.move(toolcircle, 0, incrementy_display)
            #time.sleep(timebetweensteps)
        if y>usery:
            y=y-incrementx_location;
            toollocationscreen.move(toolcircle, 0, -incrementy_display)
            #time.sleep(timebetweensteps)
        window.update()
        #limitswitchreturningdata()
        #print (y)
        #print("nigga I'm moving in y daym")
        if y==usery:
            break
    while(x==userx) & (y==usery):
        time.sleep(2)
        toollocationscreen.place_forget()
        window.update()
        #print("Go to sleep bitch")
        #limitswitchreturningdata()
        break
    return

#5. this function receives the values entered by the user and displays the tool moving to another location
def enterlocation():
    global userx; global usery
    global initialuserx; global initialusery
    global userxsteps; global userysteps
    global directionx; global directiony
    global iter; global iter2; global iter_absolutefirst
    global delta_x; global delta_y
    global status_location
    userx=int(xLocation.get()); usery=int(yLocation.get())
    if userx<=limit_x and usery<=limit_y:
        if iter==0 and iter2==0:
            if iter_absolutefirst==0:
                initialuserx=userx; initialusery=usery
                if userx>0:
                    directionx="fwd"
                    delta_x=userx-0
                if userx<0:
                    directionx="rev"
                    delta_x=userx-0
                if userx==0:
                    directionx="non"
                    delta_x=0
                if usery>0:
                    directiony="fwd"
                    delta_y=usery-0
                if usery<0:
                    directiony="rev"
                    delta_y=usery-0
                if usery==0:
                    directiony="non"
                    delta_y=0
                print("absolute first iteration", directionx, directiony)

            if iter_absolutefirst==1:
                #initialuserx=userx; initialusery=usery
                if userx>initialuserx:
                    directionx="fwd"
                    delta_x=userx-initialuserx
                    #userx=userx-initialuserx
                if userx<initialuserx:
                    directionx="rev"
                    delta_x=initialuserx-userx
                if userx==initialuserx:
                    directionx="non"
                    delta_x=0
                if usery>initialusery:
                    lengthdirectiony="fwd"
                    delta_y=usery-initialusery
                if usery<initialusery:
                    directiony="rev"
                    delta_y=initialusery-usery
                if usery==initialusery:
                    directiony="non"
                    delta_y=0
                initialuserx=userx; initialusery=usery
                print("third iteration", delta_x, directionx, delta_y , directiony)
            #print("first iteration", directionx, directiony)
            iter2=1

        if iter==1 and iter2==1:
        #if iter2==1:
            #initialuserx=userx; initialusery=usery
            if userx>initialuserx:
                directionx="fwd"
                delta_x=userx-initialuserx
                #userx=userx-initialuserx
            if userx<initialuserx:
                directionx="rev"
                delta_x=initialuserx-userx
            if userx==initialuserx:
                directionx="non"
                delta_x=0
            if usery>initialusery:
                directiony="fwd"
                delta_y=usery-initialusery
            if usery<initialusery:
                directiony="rev"
                delta_y=initialusery-usery
            if usery==initialusery:
                directiony="non"
                delta_y=0
            initialuserx=userx; initialusery=usery
            print("second iteration", delta_x, directionx, delta_y , directiony)
            iter2=0
            #print (directionx, userx, initialuserx)

        #iter_absolutefirst (iter=0, iter2=0, iter3=0) runs only once, only when you enter the location for the first time, that's why when iter_absolutefirst is executed, your entered value is compared with 0,0
        #after iter_absolutefirst has executed, its value is changed to 1 (it has to be zero to execute) so it won't be executed again.
        #iter_absolutefirst saves whatever value you entered as initialuserx and initialusery for further use.
        #iter_2 (iter=1, iter2=1) runs when you enter the location for the 2nd time, it is compared with the previous location you entered (saved as initialuserx and initialusery in iter_absolutefirst) to determine whether your x and y are increasing, decreasing or staying same, resultantly determining the direction of power screw and the direction of the stepper motor
        #after iter2 has run, it saves the value you just entered as initialuserx and initialusery
        #the if conditions reset iter and iter2 from 1 back to 0. but iter_absolutefirst is kept at 1 so when you enter location again, the condition that runs is (iter=0, iter2=0, iter3=1)
        #it works just like second iteration, comparing values from last iteration to determine direction
        #the code keeps switching b/w third iteration (iter=0, iter2=0, iter3=1) and second iteration (iter=1, iter2=1)

        if iter2==0 and iter==1:
            iter=0

        if iter2==1 and iter==0:
            iter=1
        iter_absolutefirst=1

        print("The tool should move to ", userx, ",", usery)
        userxsteps=userx/25; userysteps=usery/25;
        print("The steps for that are ", userxsteps, "for x stepper and ", userysteps, "for the y stepper!")

        enteringlocationprompt.place_forget()
        enterlocationinx.place_forget()
        enterlocationiny.place_forget()
        enterlocationtext.place_forget()
        aftertypinglocationpressthis.place_forget()
        if status_location=="button":                                #This prompt, or button, needs to be displayed only and only when this function was called because of a button prompt and not in the initial code which prompts location entry by default
            enterlocationprompt.place(x=390,y=80)
        displaythetoolmovingtoatoalocationenteredbyuser()

        get_it_moving()
    currentlocationcoordinates.place_forget()
    currentlocationliveupdates()
    enterlocationprompt.place(x=enterlocationprompt_location_x,y=enterlocationprompt_location_y)


#funcion that prompts user to enter location
def receivelocationfromuser():                      #4. This function displays the empty boxes for x and y coordinates and a button to be pressed when user wants to submit these coordinates
    enterlocationprompt.place_forget()              # Hide the prompt "Enter location" when it is clicked
    aftertypinglocationpressthis.place(x=295,y=140)
    enteringlocationprompt.place(x=enterlocationprompt_location_x,y=enterlocationprompt_location_y)        # Place a new prompt "Entering location" in its placeenteringlocationprompt.place()
    enterlocationinx.place(x=200,y=140)
    enterlocationiny.place(x=240,y=140)
    enterlocationtext.place(x=25,y=140)

enterlocationinx=Entry(window,textvariable=xLocation,width=7,bg="white")
enterlocationiny=Entry(window,textvariable=yLocation,width=7,bg="white")
enterlocationtext=Label (window, text="Enter Location (μm): ", bg="#262626", fg="white",font=("montserrat",10,"normal"))

def cancelenteringlocation():
    enteringlocationprompt.place_forget()           #When it is pressed, hide the "entering location" prompt
    enterlocationprompt.place(x=enterlocationprompt_location_x,y=enterlocationprompt_location_y)           #replace it with the "enter location" prompt
    enterlocationinx.place_forget()
    enterlocationiny.place_forget()
    enterlocationtext.place_forget()
    aftertypinglocationpressthis.place_forget()
    toollocationscreen.place_forget()

# function that commands the tool to move to the location entered by the user
def userenteredlocation():                          #2. When button is pressed, this function starts runnings
    global status_power
    status_location="button"
    receivelocationfromuser()                       #3. The first thing this function does is running another function that is configured to receive location from the user
    drive_the_rails_to_users_location()

aftertypinglocationpressthis=Button(window,text="ENTER", font=("montserrat",8,"normal"), width=5, bg="yellow",fg="black",command=enterlocation)

entering_location_button=PhotoImage(file="entering.gif")
entering_location_button_properties=Label(window,image=entering_location_button,bg="#262626")
enteringlocationprompt=Button(window,image=entering_location_button,bg="#262626",highlightthickness=0,bd=0,command=cancelenteringlocation)

#1. The prompt to enter location manually is displayed on the screen right from the beginning
enter_location_button=PhotoImage(file="enter_location.gif")
enter_location_button_properties=Label(window,image=enter_location_button,bg="#262626")
enterlocationprompt=Button(window,image=enter_location_button,bg="#262626",highlightthickness=0,bd=0,command=userenteredlocation)
enterlocationprompt.place(x=enterlocationprompt_location_x,y=enterlocationprompt_location_y)

                                            #   MANUAL LOCATION ENTRY SYSTEM (BOTTOM)

                                                # FREQUENCY AND DUTY CYCLE ENTRY

def send_frequency_and_duty_cycle_to_arduino():
    global Frequency_command; global Duty_cycle_command;
    Delimiter_Comma=","
    Thetask="frequency&duty"
    timedelayaftersendingdata=1; timedelayinreceivingloop=0.25;

    #lengths of all strings:
    lengthThetask=len(Thetask); lengthFrequency_command=len(Frequency_command); lengthDuty_cycle_command=len(Duty_cycle_command); lengthDelimiter_Comma=len(Delimiter_Comma)

    #lengths are in integers by default, converting them to strings
    lengthThetaskstring=str(lengthThetask); lengthFrequency_commandstring=str(lengthFrequency_command); lengthDuty_cycle_commandstring=str(lengthDuty_cycle_command); lengthDelimiter_Commastring=str(lengthDelimiter_Comma);

    #joining the lengths of all the data to be sent with "s" in between, stringpackingsize is like 16s3s1s3s1s4s1s (just an example). the variable contains the data regarding the size of the strings that are being combined by struct and then sent to arduino
    stringpackingsize=lengthThetaskstring+"s"+lengthDelimiter_Commastring+"s"+lengthFrequency_commandstring+"s"+lengthDelimiter_Commastring+"s"+lengthDuty_cycle_commandstring+"s"

    send_string_Frequency_and_Duty_command=struct.pack(stringpackingsize, Thetask.encode('UTF-8'), Delimiter_Comma.encode('UTF-8'),Frequency_command.encode('UTF-8'), Delimiter_Comma.encode('UTF-8'), Duty_cycle_command.encode('UTF-8'))
    #stepper_data1.write(send_string_Frequency_and_Duty_command);
    stepper_data2.write(send_string_Frequency_and_Duty_command);
    time.sleep(timedelayaftersendingdata)

    while stepper_data2.in_waiting:
        input=stepper_data2.readline()
        returningback=input.decode("ascii")
        print(returningback)
        time.sleep(timedelayinreceivingloop)

def convert_frequency_and_duty_cycle_into_commands():
    global enteredfrequency; global entereddutycycle
    global Frequency_value; global Duty_cycle_value
    global Frequency_command; global Duty_cycle_command
    Frequency_value=int(enteredfrequency.get()); Duty_cycle_value=int(entereddutycycle.get())
    Frequency_value=str(Frequency_value); Duty_cycle_value=str(Duty_cycle_value)
    characters_in_Duty_cycle_value=len(Duty_cycle_value)
    currentlocationliveupdates()
    if characters_in_Duty_cycle_value==1:
        Duty_cycle_command="D"+"0"+"0"+Duty_cycle_value
    if characters_in_Duty_cycle_value==2:
        Duty_cycle_command="D"+"0"+Duty_cycle_value
    if characters_in_Duty_cycle_value==3:
        Duty_cycle_command="D"+Duty_cycle_value
    #print(Duty_cycle_command)
    characters_in_Frequency_value=len(Frequency_value)
    if characters_in_Frequency_value==1:
        Frequency_command="F"+"00"+Frequency_value
    if characters_in_Frequency_value==2:
        Frequency_command="F"+"0"+Frequency_value
    if characters_in_Frequency_value==3:
        Frequency_command="F"+Frequency_value
    if characters_in_Frequency_value==4:
        first_digit_kiloHerts=Frequency_value[0]
        last_3_digits_kiloHerts=Frequency_value[1:]
        after_2_decimals=last_3_digits_kiloHerts[:-1]
        Frequency_command="F"+first_digit_kiloHerts+"."+after_2_decimals
    #print(Frequency_command)
    send_frequency_and_duty_cycle_to_arduino()

def frequency_and_duty_cycle_entry():
    Frequency_and_duty_cycle_entry_button.place_forget()
    Entering_Frequency_and_duty_cycle_button.place(x=390,y=130)
    frequencytext.place(x=25,y=200)
    enterfrequency.place(x=200,y=200)
    dutycycletext.place(x=25,y=225)
    enterdutycycle.place(x=200,y=225)
    aftertypingfrequencyanddutycyclepressthis.place(x=264,y=200)

def cancel_frequency_and_duty_cycle_entry():
    frequencytext.place_forget()
    enterfrequency.place_forget()
    dutycycletext.place_forget()
    enterdutycycle.place_forget()
    aftertypingfrequencyanddutycyclepressthis.place_forget()
    Entering_Frequency_and_duty_cycle_button.place_forget()
    Frequency_and_duty_cycle_entry_button.place(x=390,y=130)

def entered_frequency_and_duty_cycle():
    cancel_frequency_and_duty_cycle_entry()
    convert_frequency_and_duty_cycle_into_commands()

enteredfrequency=StringVar(); entereddutycycle=StringVar()
enterfrequency=Entry(window,textvariable=enteredfrequency,width=7,bg="white")
frequencytext=Label(window, text="Frequency (Hz): ",bg="#262626",fg="white",font=("montserrat",10,"normal"))
enterdutycycle=Entry(window,textvariable=entereddutycycle,width=7,bg="white")
dutycycletext=Label(window, text="Duty cycle (%): ",bg="#262626",fg="white",font=("montserrat",10,"normal"))
aftertypingfrequencyanddutycyclepressthis=Button(window,text="ENTER", font=("montserrat",8,"normal"), width=5, height=3, bg="yellow",fg="black",command=entered_frequency_and_duty_cycle)

Frequency_and_duty_cycle_entry_image=PhotoImage(file="frequencyandduty.gif")
Frequency_and_duty_cycle_entry_image_properties=Label(window, image=Frequency_and_duty_cycle_entry_image, bg="#262626")
Frequency_and_duty_cycle_entry_button=Button(window, image=Frequency_and_duty_cycle_entry_image, highlightthickness=0,bd=0,bg="white",command=frequency_and_duty_cycle_entry)

Entering_Frequency_and_duty_cycle_image=PhotoImage(file="enteringfrequencyandduty.gif")
Entering_Frequency_and_duty_cycle_image_properties=Label(window, image=Entering_Frequency_and_duty_cycle_image, bg="#262626")
Entering_Frequency_and_duty_cycle_button=Button(window, image=Entering_Frequency_and_duty_cycle_image, highlightthickness=0,bd=0,bg="white",command=cancel_frequency_and_duty_cycle_entry)

                                                # FREQUENCY AND DUTY CYCLE ENTRY

#The canvas on the GUI that displays the tool's location, as a red dot, on the GUI.
toollocationscreen=Canvas(window,width=300,height=381)
toolcircle=toollocationscreen.create_oval(0,0,10,10,fill="red")


                                                            #POWER SUPPLY

def fifty_Volt():
    #Tell the program that the voltage is 50 V
    global Voltage
    Voltage=50
    #Hide other voltage buttons
    eighty_Volt_Button.place_forget()
    onehundredten_Volt_Button.place_forget()
    #display the "back" button that allows you to go back and pick 80 V or 110 V
    backbutton_fifty_Volt.place(x=245,y=250)
    #display all the currents available for 50 V
    fifty_Volt_Currents_available.place(x=25,y=275)
    pointfive_Amp_Button.place(x=200,y=275)
    one_Amp_Button.place(x=245,y=275)
    two_Amp_Button.place(x=290,y=275)
    three_Amp_Button.place(x=335,y=275)
    four_Amp_Button.place(x=380,y=275)

def eighty_Volt():
    #Tell the program that the voltage is 80 V
    global Voltage
    Voltage=80
    #Hide other voltage buttons
    fifty_Volt_Button.place_forget()
    onehundredten_Volt_Button.place_forget()
    #We hide the 80 V button and place it again at the location where 50 V used to be
    eighty_Volt_Button.place_forget()
    eighty_Volt_Button.place(x=200,y=250)
    #display the "back" button that allows you to go back and pick 50 V or 110 V
    backbutton_eighty_Volt.place(x=245,y=250)
    #display all the currents available for 50 V
    eighty_Volt_Currents_available.place(x=25,y=275)
    onepointfive_Amp_Button.place(x=200,y=275)
    twopointfive_Amp_Button.place(x=245,y=275)
    three_Amp_Button.place(x=290,y=275)
    fourpointfive_Amp_Button.place(x=335,y=275)
    five_Amp_Button.place(x=380,y=275)
    six_Amp_Button.place(x=425,y=275)
    seven_Amp_Button.place(x=470,y=275)

def onehundredten_Volt():
    #Tell the program that the voltage is 110 V
    global Voltage
    Voltage=110
    #Hide other voltage buttons
    fifty_Volt_Button.place_forget()
    eighty_Volt_Button.place_forget()
    #We hide the 110 V button and place it again at the location where 50 V used to be
    onehundredten_Volt_Button.place_forget()
    onehundredten_Volt_Button.place(x=200,y=250)
    #display the "back" button that allows you to go back and pick 50 V or 80 V
    backbutton_onehundredten_Volt.place(x=245,y=250)
    #display all the currents available for 110 V
    onehundredten_Volt_Currents_available.place(x=25,y=275)
    one_Amp_Button.place(x=200,y=275)
    twopointfive_Amp_Button.place(x=245,y=275)
    threepointfive_Amp_Button.place(x=290,y=275)
    five_Amp_Button.place(x=335,y=275)
    six_Amp_Button.place(x=380,y=275)
    sevenpointfive_Amp_Button.place(x=425,y=275)

def send_power_to_arduino():
    global Voltage; global Current
    Delimiter_Comma=","
    Thetask="Voltage&Current"
    timedelayaftersendingdata=2; timedelayinreceivingloop=0.5;
    Voltage=str(Voltage); Current=str(Current)
    #lengths of all strings:
    lengthThetask=len(Thetask); lengthVoltage=len(Voltage); lengthCurrent=len(Current); lengthDelimiter_Comma=len(Delimiter_Comma)

    #lengths are in integers by default, converting them to strings
    lengthThetaskstring=str(lengthThetask); lengthVoltagestring=str(lengthVoltage); lengthCurrentstring=str(lengthCurrent); lengthDelimiter_Commastring=str(lengthDelimiter_Comma);

    #joining the lengths of all the data to be sent with "s" in between, stringpackingsize is like 16s3s1s3s1s4s1s (just an example). the variable contains the data regarding the size of the strings that are being combined by struct and then sent to arduino
    stringpackingsize=lengthThetaskstring+"s"+lengthDelimiter_Commastring+"s"+lengthVoltagestring+"s"+lengthDelimiter_Commastring+"s"+lengthCurrentstring+"s"

    send_Voltage_and_Current_command=struct.pack(stringpackingsize, Thetask.encode('UTF-8'), Delimiter_Comma.encode('UTF-8'),Voltage.encode('UTF-8'), Delimiter_Comma.encode('UTF-8'), Current.encode('UTF-8'))
    #stepper_data1.write(send_Voltage_and_Current_command);
    stepper_data2.write(send_Voltage_and_Current_command);
    time.sleep(timedelayaftersendingdata)

    while stepper_data2.in_waiting:
        input=stepper_data2.readline()
        returningback=input.decode("ascii")
        print(returningback)
        time.sleep(timedelayinreceivingloop)

def hide_all_voltages_and_currents():
    #Removing any current prompts
    pointfive_Amp_Button.place_forget()
    one_Amp_Button.place_forget()
    onepointfive_Amp_Button.place_forget()
    two_Amp_Button.place_forget()
    twopointfive_Amp_Button.place_forget()
    three_Amp_Button.place_forget()
    threepointfive_Amp_Button.place_forget()
    four_Amp_Button.place_forget()
    fourpointfive_Amp_Button.place_forget()
    five_Amp_Button.place_forget()
    six_Amp_Button.place_forget()
    seven_Amp_Button.place_forget()
    sevenpointfive_Amp_Button.place_forget()
    #Removing the current selection prompt labels
    fifty_Volt_Currents_available.place_forget()
    eighty_Volt_Currents_available.place_forget()
    onehundredten_Volt_Currents_available.place_forget()
    #Removing Voltage buttons because we need to place them again at positions such that they are simultaneously visible. Otherwise, each button is at the same position after selecting voltage (x=175,y=250)
    fifty_Volt_Button.place_forget()
    eighty_Volt_Button.place_forget()
    onehundredten_Volt_Button.place_forget()
    #Removing the "Back" prompts
    backbutton_fifty_Volt.place_forget()
    backbutton_eighty_Volt.place_forget()
    backbutton_onehundredten_Volt.place_forget()
    #Placing Voltages at their default positions. This is what is shown at starting screen. All the lines above are in this function so that when back button is pressed, everything is removed just to be placed again as done below:

def cancelenteringvoltageandcurent():
    hide_all_voltages_and_currents()
    Enter_voltage.place_forget()
    entering_Voltage_and_current_button.place_forget()
    Voltage_and_current_button.place(x=Voltage_and_current_button_location_x,y=Voltage_and_current_button_location_y)

def enter_power():
    global status_power
    #Removing any current prompts
    hide_all_voltages_and_currents()
    Enter_voltage.place(x=25,y=250)
    fifty_Volt_Button.place(x=200,y=250)
    eighty_Volt_Button.place(x=245,y=250)
    onehundredten_Volt_Button.place(x=290,y=250)
    #entering_Voltage_and_current_button.place(x=390,y=180)
    currentlocationliveupdates()

def enter_power_via_button():
    enter_power()
    Voltage_and_current_button.place_forget()
    entering_Voltage_and_current_button.place(x=Voltage_and_current_button_location_x, y=Voltage_and_current_button_location_y)

Enter_voltage=Label (window,text=("Select voltage:"),bg="#262626",fg="white",font=("montserrat",10,"normal"))

backbutton_fifty_Volt=Button(window,
text="Back", font=("montserrat",8,"normal"), width=24, bg="orange",fg="black",command=enter_power)
fifty_Volt_Button=Button(window,text="50 V", font=("montserrat",8,"normal"), width=5, bg="yellow",fg="black",command=fifty_Volt)
fifty_Volt_Currents_available=Label (window,text=("Currents for 50 V:"),bg="#262626",fg="white",font=("montserrat",10,"normal"))
#the possible currents for 50 V are 0.5, 1, 2, 3, 4

backbutton_eighty_Volt=Button(window,text="Back", font=("montserrat",8,"normal"), width=37, bg="orange",fg="black",command=enter_power)
eighty_Volt_Button=Button(window,text="80 V", font=("montserrat",8,"normal"), width=5, bg="yellow",fg="black",command=eighty_Volt)
eighty_Volt_Currents_available=Label (window,text=("Currents for 80 V:"),bg="#262626",fg="white",font=("montserrat",10,"normal"))
#the possible currents for 80 V are 1.5, 2.5, 3, 4.5, 5, 6, 7

backbutton_onehundredten_Volt=Button(window,text="Back", font=("montserrat",8,"normal"), width=31, bg="orange",fg="black",command=enter_power)
onehundredten_Volt_Button=Button(window,text="110 V", font=("montserrat",8,"normal"), width=5, bg="yellow",fg="black",command=onehundredten_Volt)
onehundredten_Volt_Currents_available=Label (window,text=("Currents for 110 V:"),bg="#262626",fg="white",font=("montserrat",10,"normal"))
#the possible currents for 110 V are 1, 2.5, 3.5, 5, 6, 7.5

entering_Voltage_and_current_button_image=PhotoImage(file="enteringvoltageandcurrent.gif")
entering_Voltage_and_current_button_image_properties=Label(window,image=entering_Voltage_and_current_button_image, bg="#262626")
entering_Voltage_and_current_button=Button(window,image=entering_Voltage_and_current_button_image,highlightthickness=0,bd=0,bg="#262626",command=cancelenteringvoltageandcurent)

Voltage_and_current_button_image=PhotoImage(file="voltageandcurrent.gif")
Voltage_and_current_button_image_properties=Label(window,image=Voltage_and_current_button_image, bg="#262626")
Voltage_and_current_button=Button(window,image=Voltage_and_current_button_image,highlightthickness=0,bd=0,bg="#262626",command=enter_power_via_button)


def pointfive_Amp():
    global Current
    Current=0.5
    #print("Voltage & Current", Voltage, Current)
    currentlocationliveupdates()
    if status_power == "button":
        send_power_to_arduino()

def one_Amp():
    global Current; global status_power;
    Current=1
    #print("Voltage & Current", Voltage, Current)
    currentlocationliveupdates()
    if status_power == "button":
        send_power_to_arduino()

def onepointfive_Amp():
    global Current; global status_power;
    Current=1.5
    #print("Voltage & Current", Voltage, Current)
    currentlocationliveupdates()
    if status_power == "button":
        send_power_to_arduino()

def two_Amp():
    global Current; global status_power;
    Current=2
    #print("Voltage & Current", Voltage, Current)
    currentlocationliveupdates()
    if status_power == "button":
        send_power_to_arduino()

def twopointfive_Amp():
    global Current; global status_power;
    Current=2.5
    #print("Voltage & Current", Voltage, Current)
    currentlocationliveupdates()
    if status_power == "button":
        send_power_to_arduino()

def three_Amp():
    global Current; global status_power;
    Current=3
    #print("Voltage & Current", Voltage, Current)
    currentlocationliveupdates()
    if status_power == "button":
        send_power_to_arduino()

def threepointfive_Amp():
    global Current; global _power;
    Current=3.5
    #print("Voltage & Current", Voltage, Current)
    currentlocationliveupdates()
    if _power == "button":
        send_power_to_arduino()

def four_Amp():
    global Current; global _power;
    Current=4
    #print("Voltage & Current", Voltage, Current)
    currentlocationliveupdates()
    if _power == "button":
        send_power_to_arduino()

def fourpointfive_Amp():
    global Current; global _power;
    Current=4.5
    #print("Voltage & Current", Voltage, Current)
    currentlocationliveupdates()
    if _power == "button":
        send_power_to_arduino()

def five_Amp():
    global Current; global _power;
    Current=5
    #print("Voltage & Current", Voltage, Current)
    currentlocationliveupdates()
    if status_power == "button":
        send_power_to_arduino()

def six_Amp():
    global Current; global status_power;
    Current=6
    #print("Voltage & Current", Voltage, Current)
    currentlocationliveupdates()
    if status_power == "button":
        send_power_to_arduino()

def seven_Amp():
    global Current; global status_power;
    Current=7
    #print("Voltage & Current", Voltage, Current)
    currentlocationliveupdates()
    if status_power == "button":
        send_power_to_arduino()

def sevenpointfive_Amp():
    global Current; global status_power;
    Current=7.5
    #print("Voltage & Current", Voltage, Current)
    currentlocationliveupdates()
    if status_power == "button":
        send_power_to_arduino()

#All currents:
pointfive_Amp_Button=Button(window,text="0.5 A", font=("montserrat",8,"normal"), width=5, bg="yellow",fg="black",command=pointfive_Amp)
one_Amp_Button=Button(window,text="1 A", font=("montserrat",8,"normal"), width=5, bg="yellow",fg="black",command=one_Amp)
onepointfive_Amp_Button=Button(window,text="1.5 A", font=("montserrat",8,"normal"), width=5, bg="yellow",fg="black",command=onepointfive_Amp)
two_Amp_Button=Button(window,text="2 A", font=("montserrat",8,"normal"), width=5, bg="yellow",fg="black",command=two_Amp)
twopointfive_Amp_Button=Button(window,text="2.5 A", font=("montserrat",8,"normal"), width=5, bg="yellow",fg="black",command=twopointfive_Amp)
three_Amp_Button=Button(window,text="3 A", font=("montserrat",8,"normal"), width=5, bg="yellow",fg="black",command=three_Amp)
threepointfive_Amp_Button=Button(window,text="3.5 A", font=("montserrat",8,"normal"), width=5, bg="yellow",fg="black",command=threepointfive_Amp)
four_Amp_Button=Button(window,text="4 A", font=("montserrat",8,"normal"), width=5, bg="yellow",fg="black",command=four_Amp)
fourpointfive_Amp_Button=Button(window,text="4.5 A", font=("montserrat",8,"normal"), width=5, bg="yellow",fg="black",command=fourpointfive_Amp)
five_Amp_Button=Button(window,text="5 A", font=("montserrat",8,"normal"), width=5, bg="yellow",fg="black",command=five_Amp)
six_Amp_Button=Button(window,text="6 A", font=("montserrat",8,"normal"), width=5, bg="yellow",fg="black",command=six_Amp)
seven_Amp_Button=Button(window,text="7 A", font=("montserrat",8,"normal"), width=5, bg="yellow",fg="black",command=seven_Amp)
sevenpointfive_Amp_Button=Button(window,text="7.5 A", font=("montserrat",8,"normal"), width=5, bg="yellow",fg="black",command=sevenpointfive_Amp)

                                                                    # POWER SUPPLY

                                                                        # DRAIN (TOP)


def send_drain_command_to_arduino():
    Thetask="Drain,"
    timedelayaftersendingdata=2; timedelayinreceivingloop=0.5;
    #lengths of all strings:
    lengthThetask=len(Thetask)
    #lengths are in integers by default, converting them to strings
    lengthThetaskstring=str(lengthThetask)
    #joining the lengths of all the data to be sent with "s" in between, stringpackingsize is like 16s3s1s3s1s4s1s (just an example). the variable contains the data regarding the size of the strings that are being combined by struct and then sent to arduino
    stringpackingsize=lengthThetaskstring+"s"
    send_drain_command=struct.pack(stringpackingsize, Thetask.encode('UTF-8'))
    #stepper_data1.write(send_drain_command);

    stepper_data2.write(send_drain_command);
    time.sleep(timedelayaftersendingdata)
    while stepper_data2.in_waiting:
        input=stepper_data2.readline()
        returningback=input.decode("ascii")
        print(returningback)
        time.sleep(timedelayinreceivingloop)

def drain():
    drain_button.place_forget()
    stop_draining_button.place(x=drain_button_location_x, y=drain_button_location_y)
    send_drain_command_to_arduino()

drain_image=PhotoImage(file="drain.gif")
drain_image_properties=Label(window, image=drain_image, bg="#262626")
drain_button=Button(window, image=drain_image, highlightthickness=0,bd=0,bg="white",command=drain)

def send_stopdraining_command_to_arduino():
    Thetask="Stopdraining"
    timedelayaftersendingdata=2; timedelayinreceivingloop=0.5;
    #lengths of all strings:
    lengthThetask=len(Thetask)
    #lengths are in integers by default, converting them to strings
    lengthThetaskstring=str(lengthThetask)
    #joining the lengths of all the data to be sent with "s" in between, stringpackingsize is like 16s3s1s3s1s4s1s (just an example). the variable contains the data regarding the size of the strings that are being combined by struct and then sent to arduino
    stringpackingsize=lengthThetaskstring+"s"
    send_drain_command=struct.pack(stringpackingsize, Thetask.encode('UTF-8'))
    #stepper_data1.write(send_drain_command);
    stepper_data2.write(send_drain_command);
    time.sleep(timedelayaftersendingdata)
    while stepper_data2.in_waiting:
        input=stepper_data2.readline()
        returningback=input.decode("ascii")
        print(returningback)
        time.sleep(timedelayinreceivingloop)

def stopdraining():
    stop_draining_button.place_forget()
    drain_button.place(x=drain_button_location_x, y=drain_button_location_y)
    send_stopdrain_command_to_arduino()

stop_draining_image=PhotoImage(file="draining.gif")
stop_draining_image_properties=Label(window, image=stop_draining_image, bg="#262626")
stop_draining_button=Button(window, image=stop_draining_image, highlightthickness=0,bd=0,bg="white",command=stopdraining)

                                                                # DRAIN (BOTTOM)

                                                                # FILL (TOP)

def send_fill_command_to_arduino():
    Thetask="Fill"
    timedelayaftersendingdata=2; timedelayinreceivingloop=0.5;
    #lengths of all strings:
    lengthThetask=len(Thetask)
    #lengths are in integers by default, converting them to strings
    lengthThetaskstring=str(lengthThetask)
    #joining the lengths of all the data to be sent with "s" in between, stringpackingsize is like 16s3s1s3s1s4s1s (just an example). the variable contains the data regarding the size of the strings that are being combined by struct and then sent to arduino
    stringpackingsize=lengthThetaskstring+"s"
    send_drain_command=struct.pack(stringpackingsize, Thetask.encode('UTF-8'))
    #stepper_data1.write(send_drain_command);
    stepper_data2.write(send_drain_command);
    time.sleep(timedelayaftersendingdata)
    while stepper_data2.in_waiting:
        input=stepper_data2.readline()
        returningback=input.decode("ascii")
        print(returningback)
        time.sleep(timedelayinreceivingloop)

def fill():
    fill_button.place_forget()
    stop_filling_button.place(x=fill_button_location_x,  y=fill_button_location_y)
    send_fill_command_to_arduino()

fill_image=PhotoImage(file="fill.gif")
fill_image_properties=Label(window, image=fill_image, bg="#262626")
fill_button=Button(window, image=fill_image, highlightthickness=0,bd=0,bg="white",command=fill)

def send_stopfilling_command_to_arduino():
    Thetask="Stopfilling"
    timedelayaftersendingdata=2; timedelayinreceivingloop=0.5;
    #lengths of all strings:
    lengthThetask=len(Thetask)
    #lengths are in integers by default, converting them to strings
    lengthThetaskstring=str(lengthThetask)
    #joining the lengths of all the data to be sent with "s" in between, stringpackingsize is like 16s3s1s3s1s4s1s (just an example). the variable contains the data regarding the size of the strings that are being combined by struct and then sent to arduino
    stringpackingsize=lengthThetaskstring+"s"
    send_drain_command=struct.pack(stringpackingsize, Thetask.encode('UTF-8'))
    #stepper_data1.write(send_drain_command);
    stepper_data2.write(send_drain_command);
    time.sleep(timedelayaftersendingdata)
    while stepper_data2.in_waiting:
        input=stepper_data2.readline()
        returningback=input.decode("ascii")
        print(returningback)
        time.sleep(timedelayinreceivingloop)

def stopfilling():
    stop_filling_button.place_forget()
    fill_button.place(x=fill_button_location_x,y=fill_button_location_y)
    send_stopfilling_command_to_arduino()

stop_filling_image=PhotoImage(file="filling.gif")
stop_filling_image_properties=Label(window, image=stop_filling_image, bg="#262626")
stop_filling_button=Button(window, image=stop_filling_image, highlightthickness=0,bd=0,bg="white",command=stopfilling)

                                                                # FILL (BOTTOM)

                                                                # FLUSHING (TOP)

flush_image=PhotoImage(file="flush.gif")
flush_image_properties=Label(window, image=flush_image, bg="#262626")
flush_button=Button(window, image=flush_image, highlightthickness=0,bd=0,bg="white",command=stopfilling)

                                                                # FLUSHING (BOTTOM)

                                                                # SPARKING (TOP)
def send_spark_command_to_arduino():
    Thetask="Spark"
    timedelayaftersendingdata=2; timedelayinreceivingloop=0.5;
    #lengths of all strings:
    lengthThetask=len(Thetask)
    #lengths are in integers by default, converting them to strings
    lengthThetaskstring=str(lengthThetask)
    #joining the lengths of all the data to be sent with "s" in between, stringpackingsize is like 16s3s1s3s1s4s1s (just an example). the variable contains the data regarding the size of the strings that are being combined by struct and then sent to arduino
    stringpackingsize=lengthThetaskstring+"s"
    send_drain_command=struct.pack(stringpackingsize, Thetask.encode('UTF-8'))
    stepper_data2.write(send_drain_command);
    stepper_data1.write(send_drain_command);
    time.sleep(timedelayaftersendingdata)
    while stepper_data1.in_waiting:
        input=stepper_data1.readline()
        returningback=input.decode("ascii")
        print(returningback)
        time.sleep(timedelayinreceivingloop)

def spark():
    spark_button.place_forget()
    sparking_button.place(x=spark_button_location_x, y=spark_button_location_y)
    send_spark_command_to_arduino()

spark_image=PhotoImage(file="spark.gif")
spark_image_properties=Label(window, image=spark_image, bg="#262626")
spark_button=Button(window, image=spark_image, highlightthickness=0,bd=0,bg="white",command=spark)

def send_stop_sparking_command_to_arduino():
    Thetask="Stopsparking"
    timedelayaftersendingdata=2; timedelayinreceivingloop=0.5;
    #lengths of all strings:
    lengthThetask=len(Thetask)
    #lengths are in integers by default, converting them to strings
    lengthThetaskstring=str(lengthThetask)
    #joining the lengths of all the data to be sent with "s" in between, stringpackingsize is like 16s3s1s3s1s4s1s (just an example). the variable contains the data regarding the size of the strings that are being combined by struct and then sent to arduino
    stringpackingsize=lengthThetaskstring+"s"
    send_drain_command=struct.pack(stringpackingsize, Thetask.encode('UTF-8'))
    stepper_data1.write(send_drain_command);
    stepper_data2.write(send_drain_command);
    time.sleep(timedelayaftersendingdata)
    while stepper_data1.in_waiting:
        input=stepper_data1.readline()
        returningback=input.decode("ascii")
        print(returningback)
        time.sleep(timedelayinreceivingloop)

def stop_sparking():
    sparking_button.place_forget()
    spark_button.place(x=spark_button_location_x, y=spark_button_location_y)
    send_stop_sparking_command_to_arduino()

sparking_image=PhotoImage(file="sparking.gif")
sparking_image_properties=Label(window, image=sparking_image, bg="#262626")
sparking_button=Button(window, image=sparking_image, highlightthickness=0,bd=0,bg="white",command=stop_sparking)

                                                                    # SPARKING (BOTTOM)

                                                                # CHECKING TOOL FOR SPARKING (TOP)
def tool_touched():
    checking_tool_button.place_forget()
    proceed_after_checking_tool_button.place(x=proceed_x, y=proceed_y)

def send_detect_command_to_arduino():
    Thetask="Detect"
    timedelayaftersendingdata=2; timedelayinreceivingloop=0.5;
    #lengths of all strings:
    lengthThetask=len(Thetask)
    #lengths are in integers by default, converting them to strings
    lengthThetaskstring=str(lengthThetask)
    #joining the lengths of all the data to be sent with "s" in between, stringpackingsize is like 16s3s1s3s1s4s1s (just an example). the variable contains the data regarding the size of the strings that are being combined by struct and then sent to arduino
    stringpackingsize=lengthThetaskstring+"s"
    send_detect_command=struct.pack("6s", "Detect".encode('UTF-8'))
    stepper_data1.write(send_detect_command);
    #get it back on
    stepper_data2.write(send_detect_command);
    time.sleep(timedelayaftersendingdata)
    print("sentdetect")

    """global toolclearance; global iterator
    while iterator<10:
        print(iterator, "iterator")
        if toolclearance!=5:
            print("not clear")
            print("toolclearance",toolclearance)
            readup()
        if toolclearance==5:
            print("clear")
            print("toolclearance",toolclearance)
            toolclearance=1;
            tool_touched()
            break;return
        if iterator==3:
            iterator=0
            break
        time.sleep(1)
        iterator=iterator+1"""

def detect():
    global toolclearance
    toolclearance=0
    print("toolclearance",toolclearance)
    print("detect is being sent")
    check_tool_button.place_forget()
    checking_tool_button.place(x=detect_x,y=detect_y)
    send_detect_command_to_arduino()

def start_detecting():
    check_tool_button.place(x=detect_x,y=detect_y)

check_tool_image=PhotoImage(file="detect.gif")
check_tool_image_properties=Label(window, image=check_tool_image, bg="#262626")
check_tool_button=Button(window, image=check_tool_image, highlightthickness=0,bd=0,bg="white",command=detect)


def stop_detecting():
    checking_tool_button.place_forget()
    check_tool_button.place(x=detect_x,y=detect_y)

checking_tool_image=PhotoImage(file="checkingtool.gif")
checking_tool_image_properties=Label(window, image=checking_tool_image, bg="#262626")
checking_tool_button=Button(window, image=checking_tool_image, highlightthickness=0,bd=0,bg="white",command=stop_detecting)

                                                                # CHECKING TOOL FOR SPARKING (TOP)


                                                            #   START, TURN ON AND TURN OFF (TOP)

#This function displays the ON button and turns the EDM on
def turniton():
    global clearance
    if clearance=="yes": #this clearance is granted only when you enter initial perimeters and enter them. without this clearance (without entering initial perimeters), you can't turn the machine on.
        print("turned on")
        proceed_after_checking_tool_button.place(x=proceed_x, y=proceed_y)
        Offbutton.place_forget()
        Onbutton.place(x=Onbutton_location_x,  y=Onbutton_location_y)
        startbutton.place_forget()
        controltoolyourselfprompt.place(x=controltoolyourselfprompt_location_x,y=controltoolyourselfprompt_location_y)
        enterlocationprompt.place(x=enterlocationprompt_location_x,y=enterlocationprompt_location_y)
        Frequency_and_duty_cycle_entry_button.place(x=Frequency_and_duty_cycle_entry_button_location_x,   y=Frequency_and_duty_cycle_entry_button_location_y)
        Voltage_and_current_button.place(x=Voltage_and_current_button_location_x,y=Voltage_and_current_button_location_y)
        fill_button.place(x=fill_button_location_x,y=fill_button_location_y)
        spark_button.place(x=spark_button_location_x,y=spark_button_location_y)
        drain_button.place_forget()
        #proceed_after_checking_tool_button.place_forget()
        forget_initial_perimeters()

def initial_location_entry():
    enterlocationinx.place(x=200,y=140)
    enterlocationiny.place(x=240,y=140)
    enterlocationtext.place(x=25,y=140)
    originbutton.place(x=200,y=110)
    centerbutton.place(x=250,y=110)
    #aftertypinglocationpressthis.place(x=295,y=140)

def move_tool_to_center():
    currentlocationcoordinates.place_forget()
    global xLocation; global yLocation
    #global userx; global usery
    global directionx; global directiony
    global initialuserx; global initialusery
    Delimiter_Comma=","; Thetask="getthetoolmoving"
    global delta_x; global delta_y
    userx=0; usery=0;
    iter=0
    userx=delta_x/25; usery=delta_y/25              #these are the steps to be turned for moving userx and usery
    print("userx and usery are", userx, usery)
    userxstring=str(userx); userystring=str(usery)
    timedelayaftersendingdata=2; timedelayinreceivingloop=0.25;
    #lengths of all strings:
    lengthThetask=len(Thetask); lengthuserx=len(userxstring); lengthusery=len(userystring); lengthDelimiter_Comma=len(Delimiter_Comma); lengthdirectionx=len(directionx); lengthdirectiony=len(directiony);
    #lengths are in integers by default, converting them to strings
    lengthThetaskstring=str(lengthThetask); lengthuserxstring=str(lengthuserx); lengthuserystring=str(lengthusery); lengthDelimiter_Commastring=str(lengthDelimiter_Comma);  lengthdirectionxstring=str(lengthdirectionx); lengthdirectionystring=str(lengthdirectiony);
    #joining the lengths of all the data to be sent with "s" in between, stringpackingsize is like 16s3s1s3s1s4s1s (just an example). the variable contains the data regarding the size of the strings that are being combined by struct and then sent to arduino
    stringpackingsize=lengthThetaskstring+"s"+lengthDelimiter_Commastring+"s"+lengthuserxstring+"s"+lengthDelimiter_Commastring+"s"+lengthdirectionxstring+"s"+lengthDelimiter_Commastring+"s"+lengthuserystring+"s"+lengthDelimiter_Commastring+"s"+lengthdirectionystring+"s"+lengthDelimiter_Commastring+"s"
    #b=struct.pack('3s', String.encode('UTF-8'))
    send_string_location=struct.pack(stringpackingsize, Thetask.encode('UTF-8'), Delimiter_Comma.encode('UTF-8'), userxstring.encode('UTF-8'), Delimiter_Comma.encode('UTF-8'), directionx.encode('UTF-8'), Delimiter_Comma.encode('UTF-8'), userystring.encode('UTF-8'), Delimiter_Comma.encode('UTF-8'), directiony.encode('UTF-8'), Delimiter_Comma.encode('UTF-8'))
    print(send_string_location)
    stepper_data1.write(send_string_location);
    #stepper_data2.write(send_string_location);
    time.sleep(timedelayaftersendingdata)
    while stepper_data1.in_waiting:
        input=stepper_data1.readline()
        returningback=input.decode("ascii")
        print(returningback)
        time.sleep(timedelayinreceivingloop)

def center_location_processing():
    currentlocationcoordinates.place_forget()
    global userx; global usery
    global initialuserx; global initialusery
    global userxsteps; global userysteps
    global directionx; global directiony
    global iter; global iter2; global iter_absolutefirst
    global delta_x; global delta_y
    global status_location

    if userx<=limit_x and usery<=limit_y:
        if iter==0 and iter2==0:
            if iter_absolutefirst==0:
                initialuserx=userx; initialusery=usery
                if userx>0:
                    directionx="fwd"
                    delta_x=userx-0
                if userx<0:
                    directionx="rev"
                    delta_x=userx-0
                if userx==0:
                    directionx="non"
                    delta_x=0
                if usery>0:
                    directiony="fwd"
                    delta_y=usery-0
                if usery<0:
                    directiony="rev"
                    delta_y=usery-0
                if usery==0:
                    directiony="non"
                    delta_y=0
                print("absolute first iteration", directionx, directiony)

            if iter_absolutefirst==1:
                #initialuserx=userx; initialusery=usery
                if userx>initialuserx:
                    directionx="fwd"
                    delta_x=userx-initialuserx
                    #userx=userx-initialuserx
                if userx<initialuserx:
                    directionx="rev"
                    delta_x=initialuserx-userx
                if userx==initialuserx:
                    directionx="non"
                    delta_x=0
                if usery>initialusery:
                    lengthdirectiony="fwd"
                    delta_y=usery-initialusery
                if usery<initialusery:
                    directiony="rev"
                    delta_y=initialusery-usery
                if usery==initialusery:
                    directiony="non"
                    delta_y=0
                initialuserx=userx; initialusery=usery
                print("third iteration", delta_x, directionx, delta_y , directiony)
            #print("first iteration", directionx, directiony)
            iter2=1

        if iter==1 and iter2==1:
        #if iter2==1:
            #initialuserx=userx; initialusery=usery
            if userx>initialuserx:
                directionx="fwd"
                delta_x=userx-initialuserx
                #userx=userx-initialuserx
            if userx<initialuserx:
                directionx="rev"
                delta_x=initialuserx-userx
            if userx==initialuserx:
                directionx="non"
                delta_x=0
            if usery>initialusery:
                directiony="fwd"
                delta_y=usery-initialusery
            if usery<initialusery:
                directiony="rev"
                delta_y=initialusery-usery
            if usery==initialusery:
                directiony="non"
                delta_y=0
            initialuserx=userx; initialusery=usery
            print("second iteration", delta_x, directionx, delta_y , directiony)
            iter2=0
            #print (directionx, userx, initialuserx)

        #iter_absolutefirst (iter=0, iter2=0, iter3=0) runs only once, only when you enter the location for the first time, that's why when iter_absolutefirst is executed, your entered value is compared with 0,0
        #after iter_absolutefirst has executed, its value is changed to 1 (it has to be zero to execute) so it won't be executed again.
        #iter_absolutefirst saves whatever value you entered as initialuserx and initialusery for further use.
        #iter_2 (iter=1, iter2=1) runs when you enter the location for the 2nd time, it is compared with the previous location you entered (saved as initialuserx and initialusery in iter_absolutefirst) to determine whether your x and y are increasing, decreasing or staying same, resultantly determining the direction of power screw and the direction of the stepper motor
        #after iter2 has run, it saves the value you just entered as initialuserx and initialusery
        #the if conditions reset iter and iter2 from 1 back to 0. but iter_absolutefirst is kept at 1 so when you enter location again, the condition that runs is (iter=0, iter2=0, iter3=1)
        #it works just like second iteration, comparing values from last iteration to determine direction
        #the code keeps switching b/w third iteration (iter=0, iter2=0, iter3=1) and second iteration (iter=1, iter2=1)
        if iter2==0 and iter==1:
            iter=0
        if iter2==1 and iter==0:
            iter=1
        iter_absolutefirst=1
        print("The tool should move to ", userx, ",", usery)
        userxsteps=userx/25; userysteps=usery/25;
        print("The steps for that are ", userxsteps, "for x stepper and ", userysteps, "for the y stepper!")
        displaythetoolmovingtoatoalocationenteredbyuser()
        currentlocationcoordinates.place_forget()
        get_it_moving()
    currentlocationcoordinates.place_forget()
    currentlocationliveupdates()

def center():
    global x; global y;
    global userx; global usery; global initialuserx; global initialusery

    currentlocationcoordinates.place_forget()
    #displaythetoolmovingtoatoalocationenteredbyuser() function operates by making displayed x and y approach userx and usery.
    #so we set userx and usery as 0 and call this function so that whatever value of x exists would reach userx on the canvas.
    #When displaythetoolmovingtoatoalocationenteredbyuser() finishes and returns to this function, x and y have already reached 0 and x and y are equal to 0,
    #so when the next functition currentlocationliveupdates() is called, it displays x and y as 0 microns
    userx=110000; usery=140000; #initialuserx=110000; initialusery=140000
    displaythetoolmovingtoatoalocationenteredbyuser()
    center_location_processing()
    currentlocationliveupdates()
    #move_tool_to_center()

def move_tool_to_origin():
    Thetask="Origin"
    timedelayaftersendingdata=2; timedelayinreceivingloop=0.5;
    #lengths of all strings:
    lengthThetask=len(Thetask)
    #lengths are in integers by default, converting them to strings
    lengthThetaskstring=str(lengthThetask)
    #joining the lengths of all the data to be sent with "s" in between, stringpackingsize is like 16s3s1s3s1s4s1s (just an example). the variable contains the data regarding the size of the strings that are being combined by struct and then sent to arduino
    stringpackingsize=lengthThetaskstring+"s"
    send_drain_command=struct.pack(stringpackingsize, Thetask.encode('UTF-8'))
    stepper_data1.write(send_drain_command);
    #stepper_data2.write(send_drain_command);
    time.sleep(timedelayaftersendingdata)
    while stepper_data1.in_waiting:
        input=stepper_data1.readline()
        returningback=input.decode("ascii")
        print(returningback)
        time.sleep(timedelayinreceivingloop)

def origin():
    global x; global y;
    global userx; global usery; global initialuserx; global initialusery
    currentlocationcoordinates.place_forget()
    #displaythetoolmovingtoatoalocationenteredbyuser() function operates by making displayed x and y approach userx and usery.
    #so we set userx and usery as 0 and call this function so that whatever value of x exists would reach userx on the canvas.
    #When displaythetoolmovingtoatoalocationenteredbyuser() finishes and returns to this function, x and y have already reached 0 and x and y are equal to 0,
    #so when the next functition currentlocationliveupdates() is called, it displays x and y as 0 microns
    userx=0; usery=0
    initialuserx=0; initialusery=0
    displaythetoolmovingtoatoalocationenteredbyuser()
    currentlocationliveupdates()
    move_tool_to_origin()

originbutton=Button(window,text="Origin", font=("montserrat",8,"bold"), width=5, bg="yellow",fg="black",command=origin)
centerbutton=Button(window,text="Center", font=("montserrat",8,"bold"), width=5, bg="yellow",fg="black",command=center)

def initial_frequency_and_duty_cycle_entry():
    frequencytext.place(x=25,y=200)
    enterfrequency.place(x=200,y=200)
    dutycycletext.place(x=25,y=225)
    enterdutycycle.place(x=200,y=225)
    #aftertypingfrequencyanddutycyclepressthis.place(x=264,y=200)

def forget_initial_perimeters():
    enterlocationinx.place_forget()
    enterlocationiny.place_forget()
    enterlocationtext.place_forget()
    frequencytext.place_forget()
    enterfrequency.place_forget()
    dutycycletext.place_forget()
    enterdutycycle.place_forget()
    hide_all_voltages_and_currents()
    Enter_voltage.place_forget()
    enter_initial_perimeters.place_forget()

def get_initial_perimeters():
    initial_location_entry()
    initial_frequency_and_duty_cycle_entry()
    enter_power()
    enter_initial_perimeters.place(x=26,y=300)

def send_status_command():
    global status;
    Thetask=status
    timedelayaftersendingdata=2; timedelayinreceivingloop=0.5;
    #lengths of all strings:
    lengthThetask=len(Thetask);
    #lengths are in integers by default, converting them to strings
    lengthThetaskstring=str(lengthThetask);
    #joining the lengths of all the data to be sent with "s" in between, stringpackingsize is like 16s3s1s3s1s4s1s (just an example). the variable contains the data regarding the size of the strings that are being combined by struct and then sent to arduino
    stringpackingsize=lengthThetaskstring+"s"
    send_status_command=struct.pack(stringpackingsize, Thetask.encode('UTF-8'))
    stepper_data1.write(send_status_command);
    #get it back on - SEND AND GET FROM BOTH 1 AND 2
    stepper_data2.write(send_status_command);
    time.sleep(timedelayaftersendingdata)
    while stepper_data1.in_waiting:
        input=stepper_data1.readline()
        returningback=input.decode("ascii")
        print(returningback)
        time.sleep(timedelayinreceivingloop)

def send_power_and_start_after_proceed_is_confirmed():
    global status; global clearance
    #proceed_after_checking_tool_button.place_forget()
    convert_frequency_and_duty_cycle_into_commands()
    send_power_to_arduino()
    #time.sleep(5)
    forget_initial_perimeters()
    send_status_command()
    #send_status_command()
    turniton()

proceed_after_checking_tool_image=PhotoImage(file="proceedaftercheckingtool.gif")
proceed_after_checking_tool_image_properties=Label(window, image=proceed_after_checking_tool_image, bg="#262626")
proceed_after_checking_tool_button=Button(window, image=proceed_after_checking_tool_image, highlightthickness=0,bd=0,bg="white",command=send_power_and_start_after_proceed_is_confirmed)

def send_initial_perimeters():
    global status; global clearance
    status="Start"; #origin_status="Start"
    status_power="Startingpower"
    #the purpose of clearance is to ensure that the "ON" button can't be displayed or the machine can't be started without entering initial perimeters. right when you hit enter with initial perimeters, this clearance is granted and you can now turn the machine on.
    clearance="yes"
    #send_status_command()
    forget_initial_perimeters()
    enterlocation()
    start_detecting()

enter_initial_perimeters=Button(window,text="Enter initial perimeters", font=("montserrat",9,"bold"), width=38, bg="yellow",fg="black",command=send_initial_perimeters)

#This function displays the OFF button and turns the EDM off
def turnitoff():                                           #function that turns the EDM OFF
    print("turned off")
    global status;
    status="Stop"
    #origin()
    proceed_after_checking_tool_button.place(x=proceed_x, y=proceed_y)
    Onbutton.place_forget()
    Offbutton.place(x=Offbutton_location_x,y=Offbutton_location_y)
    startbutton.place_forget()
    controltoolyourselfprompt.place_forget()
    enterlocationprompt.place_forget()
    Frequency_and_duty_cycle_entry_button.place_forget()
    Voltage_and_current_button.place_forget()
    fill_button.place_forget()
    spark_button.place_forget()
    #send_status_command()
    get_initial_perimeters()
    #origin()
    #check_tool_button.place(detect_x,detect_y)
    drain_button.place(x=drain_button_location_x, y=drain_button_location_y)

#These are custom images used as buttons. highlightthickness=0 is important aesthetically because it removes the outline stroke around the button.
On_button_image=PhotoImage(file="on_button.gif")
On_button_properties=Label(window,image=On_button_image,bg="#262626")
Onbutton=Button(window,image=On_button_image,highlightthickness=0,bd=0,bg="#262626",command=turnitoff)

Off_button_image=PhotoImage(file="off_button.gif")
Off_button_properties=Label(window,image=Off_button_image, bg="#262626")
Offbutton=Button(window,image=Off_button_image,highlightthickness=0,bd=0,bg="#262626",command=turniton)

Start_button_image=PhotoImage(file="start_button.gif")
Start_button_image_properties=Label(window, image=Start_button_image, bg="#262626")
startbutton=Button(window, image=Start_button_image, highlightthickness=0,bd=0,bg="white",command=turnitoff)
startbutton.place(x=0,y=0)

"""
def readitup():
    stepper_data.write(b'1');
    time.sleep(0.5)

    while stepper_data.in_waiting:
        input=stepper_data.readline()
        returningback=input.decode("UTF-8")
        print(returningback)
        time.sleep(0.25)
readitup()
"""

                                                        #   START, TURN ON AND TURN OFF (BOTTOM)

window.mainloop()
