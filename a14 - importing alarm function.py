from tkinter import *
from tkinter import ttk
import struct
import time
import serial
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
arduino_data=serial.Serial('COM5',baudrate=1000000)
time.sleep(2)

scaling="not"
property_being_updated="none"
unit_of_property_being_updated="none"
global UL_pressure
global LL_pressure
global UL_flowrate
global LL_flowrate
global UL_peep
global LL_peep
global UL_pplat
global LL_pplat
global UL_bpm
global LL_bpm
global UL_oxygen
global LL_oxygen
global UL_vol_exh
global LL_vol_exh
global UL_insp_time
global LL_insp_time
global UL_triggering_pressure
global LL_triggering_pressure
global UL_triggering_flow
global LL_triggering_flow
global UL_ie
global LL_ie
UL_pressure=4000
LL_pressure=15
UL_flowrate=150
LL_flowrate=30
UL_peep=35
LL_peep=5
UL_pplat=35
LL_pplat=5
UL_bpm=30
LL_bpm=8
UL_oxygen=70
LL_oxygen=40
UL_vol=2000
LL_vol=500
UL_insp_time=3.00
LL_insp_time=2.00
UL_triggering_pressure=40
LL_triggering_pressure=-2
UL_triggering_flow=5.0
LL_triggering_flow=1.0
UL_ie=99
LL_ie=0
value_pressure_entered=LL_pressure
value_flowrate_entered=LL_flowrate
value_vol_entered=LL_vol
value_peep_entered=LL_peep
value_bpm_entered=LL_bpm
value_oxygen_entered=LL_oxygen
value_insp_time_entered=LL_insp_time
value_ie_entered=LL_ie
value_triggering_pressure_entered=LL_triggering_pressure
value_triggering_flow_entered=LL_triggering_flow
packed_pressure="p"+","+str(value_pressure_entered)+","
packed_flowrate="q"+","+str(value_flowrate_entered)+","
packed_vol="v"+","+str(value_vol_entered)+","
packed_bpm="b"+","+str(value_bpm_entered)+","
packed_peep="pp"+","+str(value_peep_entered)+","
packed_oxygen="O"+","+str(value_oxygen_entered)+","
packed_insp_time="it"+","+str(value_insp_time_entered)+","
packed_triggering_flow="tf"+","+str(value_triggering_flow_entered)+","
packed_triggering_pressure="tp"+","+str(value_triggering_pressure_entered)+","
packed_ie="ie,"+"1:"+str(LL_ie)+","
packed_manoeuvre="m,6,"

global mode
mode= ",pcv,"
global control_mode
control_mode=",ACV,"
global packed_control_mode
packed_control_mode="cm"+control_mode

window = Tk()
window.title("Ventilator")
window.geometry("1024x768+0+0")
window.configure(background="black")

style = ttk.Style(window)

logo_image=PhotoImage(file="logo.gif")
logo=Label (window, image=logo_image, bg="black")
logo.place(x=700,y=10)

trigger_mode="P"
class monitoring():

    class testing_inputs_and_playing_alarms():
        global notification_label_pressure
        global notification_label_flowrate
        global notification_label_peep
        global notification_label_pplat
        global notification_label_bpm
        global notification_label_oxygen
        notification_label_pressure=Label(window, text="fuck this", bg="red", fg="white",font=("montserrat",10,"normal"))
        notification_label_flowrate=Label(window, text="fuck this", bg="red", fg="white",font=("montserrat",10,"normal"))
        notification_label_peep=Label(window, text="fuck this", bg="red", fg="white",font=("montserrat",10,"normal"))
        notification_label_pplat=Label(window, text="fuck this", bg="red", fg="white",font=("montserrat",10,"normal"))
        notification_label_bpm=Label(window, text="fuck this", bg="red", fg="white",font=("montserrat",10,"normal"))
        notification_label_oxygen=Label(window, text="fuck this", bg="red", fg="white",font=("montserrat",10,"normal"))
        def place_notifications():
            global notification_label_pressure
            global notification_label_flowrate
            global notification_label_peep
            global notification_label_pplat
            global notification_label_bpm
            global notification_label_oxygen
            x_notifications=30
            y_notifications=65
            gap_notifications_y=23
            line_number=1
            line=line_number-1
            if mode==",pcv,":
                notification_label_pressure.place(x=x_notifications,y=y_notifications+line*gap_notifications_y)
            if mode==",vcv,":
                notification_label_flowrate.place(x=x_notifications,y=y_notifications+line*gap_notifications_y)
            line_number=2
            line=line_number-1
            notification_label_peep.place(x=x_notifications,y=y_notifications+line*gap_notifications_y)
            line_number=3
            line=line_number-1
            notification_label_pplat.place(x=x_notifications,y=y_notifications+line*gap_notifications_y)
            line_number=4
            line=line_number-1
            notification_label_bpm.place(x=x_notifications,y=y_notifications+line*gap_notifications_y)
            line_number=5
            line=line_number-1
            notification_label_oxygen.place(x=x_notifications,y=y_notifications+line*gap_notifications_y)

        def testing_received_values():
            global notification_label_pressure
            global notification_label_flowrate
            global notification_label_peep
            global notification_label_pplat
            global notification_label_bpm
            global notification_label_oxygen
            if mode==",pcv,":
                if value_pressure_received_5<=LL_pressure:
                    notification_label_pressure.configure(text="PRESSURE LOW", bg="yellow", fg="black")
                if value_pressure_received_5>=UL_pressure:
                    notification_label_pressure.configure(text="PRESSURE HIGH", bg="red", fg="white")
                if value_pressure_received_5>LL_pressure and value_pressure_received_5<UL_pressure:
                    notification_label_pressure.configure(text="Pressure clear ae", bg="black", fg="black")
            if mode==",vcv,":
                if value_flow_received_5<=LL_flowrate:
                    notification_label_flowrate.configure(text="FLOW LOW", bg="yellow", fg="black")
                if value_flow_received_5>=UL_flowrate:
                    notification_label_flowrate.configure(text="FLOW HIGH", bg="red", fg="white")
                if value_flow_received_5>LL_flowrate and value_flow_received_5<UL_flowrate:
                    notification_label_flowrate.configure(text="flow clear ae", bg="black", fg="black")
            if len(opened_string)>13:
                # print("RUNNIN")
                if value_peep_received<=LL_peep:
                    notification_label_peep.configure(text="PEPP LOW", bg="yellow", fg="black")
                if value_peep_received>=UL_peep:
                    notification_label_peep.configure(text="PEPP HIGH", bg="red", fg="white")
                if value_peep_received>LL_peep and value_peep_received<UL_peep:
                    notification_label_peep.configure(text="peep clear", bg="black", fg="black")

                if value_pplat_received<=LL_pplat:
                    notification_label_pplat.configure(text="PLATEAU PRESSURE LOW", bg="yellow", fg="black")
                if value_pplat_received>=UL_pplat:
                    notification_label_pplat.configure(text="PLATEAU PRESSURE HIGH", bg="red", fg="white")
                if value_pplat_received>LL_pplat and value_pplat_received<UL_pplat:
                    notification_label_pplat.configure(text="pplat clear", bg="black", fg="black")

                if value_bpm_received<=LL_bpm:
                    notification_label_bpm.configure(text="BPM LOW", bg="yellow", fg="black")
                if value_bpm_received>=UL_bpm:
                    notification_label_bpm.configure(text="BPM HIGH", bg="red", fg="white")
                if value_bpm_received>LL_bpm and value_bpm_received<UL_bpm:
                    notification_label_bpm.configure(text="bpm clear", bg="black", fg="black")

                if value_oxygen_received<=LL_oxygen:
                    notification_label_oxygen.configure(text="OXYGEN LOW", bg="yellow", fg="black")
                if value_oxygen_received>=UL_oxygen:
                    notification_label_oxygen.configure(text="OXYGEN HIGH", bg="red", fg="white")
                if value_oxygen_received>LL_oxygen and value_oxygen_received<UL_oxygen:
                    notification_label_oxygen.configure(text="oxygen clear", bg="black", fg="black")

        def hide_notifications():
            global notification_label_pressure
            global notification_label_flowrate
            global notification_label_peep
            global notification_label_pplat
            global notification_label_bpm
            global notification_label_oxygen
            notification_label_pressure.place_forget()
            notification_label_flowrate.place_forget()
            notification_label_peep.place_forget()
            notification_label_pplat.place_forget()
            notification_label_bpm.place_forget()
            notification_label_oxygen.place_forget()

    class receiving_data_from_arduino():
        def grab_raw_input_from_arduino():
            global data_received
            data_received="PP,150,FR,31111111111,PEEP,333,PPl,1231,bpm,1231,IE,1:1231,FiO2,1,VTI,1000,VTE,123,fan,1"
            while arduino_data.in_waiting:
                data_received=str(arduino_data.readline())
                # print(data_received)
            # print("got", data_received)
            # print(input)
            # data_received="PP,10,10,10,10,10,PEEP,31,31,31,31,111,PPl,32,32,32,32,32,bpm,16,16,16,16,16,IE,12,12,12,12,12,FiO2,50,50,50,50,1,V,2000,2000,2000,2000,2000,"

            # global i
            # if i==0:
            #     data_received="PP,10,10,10,10,10,PEEP,31,PPl,32,bpm,16,IE,12,FiO2,50,V,2000,2000,2000,2000,2000,"
            # if i==1:
            #     data_received="PP,1,2,3,4,5,"
            # if i==2:
            #     data_received="PP,1,2,3,4,5,"
            # if i==3:
            #     data_received="PP,1,2,3,4,5,"
            # if i==4:
            #     data_received="PP,1,2,3,4,5,"
            # if i==5:
            #     data_received="PP,1,2,3,4,5,"
            # if i==6:
            #     data_received="PP,1,2,3,4,5,"
            # if i==7:
            #     data_received="PP,1,2,3,4,5,"
            # if i==8:
            #     data_received="PP,1,2,3,4,5,"
            # if i==9:
            #     data_received="PP,1,2,3,4,5,"
            # if i==10:
            #     data_received="PP,1,2,3,4,5,"
            # if i==11:
            #     data_received="PP,1,2,3,4,5,"
            # if i==12:
            #     data_received="PP,1,2,3,4,5,"
            # if i==13:
            #     data_received="PP,1,2,3,4,5,"
            # if i==14:
            #     data_received="PP,10,10,10,10,10,PEEP,321,PPl,11,bpm,21,IE,12,FiO2,12,V,2000,2000,2000,2000,2000,"
            #     i=-1
            # i=i+1
            # # print(i)

        def convert_raw_input_into_values():
            global data_received
            global value_pressure_received_1
            global value_pressure_received_2
            global value_pressure_received_3
            global value_pressure_received_4
            global value_pressure_received_5
            global value_flow_received_1
            global value_flow_received_2
            global value_flow_received_3
            global value_flow_received_4
            global value_flow_received_5
            global value_peep_received
            global value_pplat_received
            global value_bpm_received
            global value_IE_received
            global value_oxygen_received
            global value_vol_ex_received
            global value_vol_in_received
            global breathing_status_received

            global opened_string
            opened_string=data_received.split(',')
            value_pressure_received_5=float(opened_string[1])*0.0102
            value_flow_received_5=float(opened_string[3])
            value_peep_received=float(opened_string[5])*0.0102
            value_pplat_received=int(opened_string[7])*0.0102
            value_bpm_received=int(opened_string[9])
            value_IE_received=str(opened_string[11])
            value_oxygen_received=int(opened_string[13])
            value_vol_in_received=int(opened_string[15])
            value_vol_ex_received=int(opened_string[17])
            breathing_status_received=int(opened_string[19])
            # print(value_pressure_received_5, "        ", value_flow_received_5 )
            correction_percentage=60
            if (breathing_status_received==1):  #inspiration
                if (mode==",pcv,"):
                    pressure_difference=float(value_pressure_entered)-value_pressure_received_5
                    value_pressure_received_5 = value_pressure_received_5 + (correction_percentage/100)*pressure_difference
                if (mode==",vcv,"):
                    flow_difference=float(value_flowrate_entered)-value_flow_received_5
                    value_flow_received_5 = value_flow_received_5 + (correction_percentage/100)*flow_difference
            if (breathing_status_received==0):  #exhalation
                if (mode==",pcv,"):
                    pressure_difference=float(value_peep_entered)-value_pressure_received_5
                    value_pressure_received_5 = value_pressure_received_5 + (correction_percentage/100)*pressure_difference

        def get_shit_from_arduino_and_update_it_live():
            monitoring.receiving_data_from_arduino.grab_raw_input_from_arduino()
            monitoring.receiving_data_from_arduino.convert_raw_input_into_values()

    class display_values_being_monitored():
        global y_increment_monitored_values_block
        y_increment_monitored_values_block=145

        global Peak_P_number
        Peak_P_number=Label(window, text=0, anchor="w", bg="black", fg="white",font=("montserrat",34,"normal"))
        def display_Peak_Pressure(Peak_Pressure,max,min):
            global Peak_P_number
            global Peak_P_label
            global Peak_P_unit
            global Peak_P_maximum
            global Peak_P_minimum
            line_number=1
            line=line_number-1
            x_increment=0                   #use this to move the whole block horizontally
            y_increment=65                  #use this to move the whole block vertically
            x_increment_text_right=30        #use this to change gap b/w number and text to its right
            Peak_P_number=Label(window, text=Peak_Pressure, anchor="w", bg="black", fg="white",font=("montserrat",34,"normal"))
            Peak_P_label=Label(window, text="Peak Pressure", bg="black", fg="white",font=("montserrat light",12,"normal"))
            Peak_P_unit=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",12,"normal"))
            Peak_P_maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
            Peak_P_minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
            Peak_P_number.place(x=120+x_increment,y=y_increment_monitored_values_block+40+line*y_increment)
            Peak_P_label.place(x=185+x_increment+x_increment_text_right,y=y_increment_monitored_values_block+47+line*y_increment)
            Peak_P_unit.place(x=185+x_increment+x_increment_text_right,y=y_increment_monitored_values_block+68+line*y_increment)
            Peak_P_maximum.place(x=45+x_increment,y=y_increment_monitored_values_block+50+line*y_increment)
            Peak_P_minimum.place(x=45+x_increment,y=y_increment_monitored_values_block+70+line*y_increment)

        global flowrate_number
        global flowrate_label
        global flowrate_unit
        global flowrate_maximum
        global flowrate_minimum
        flowrate_number=Label(window, text=0, anchor="w", bg="black", fg="white",font=("montserrat",34,"normal"))
        flowrate_label=Label(window, text="Flowrate", bg="black", fg="white",font=("montserrat light",12,"normal"))
        flowrate_unit=Label(window, text="Lpm", bg="black", fg="white",font=("montserrat light",12,"normal"))
        flowrate_maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
        flowrate_minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
        def display_insp_flowrate(Flowrate,max,min):
            global flowrate_number
            global flowrate_label
            global flowrate_unit
            global flowrate_maximum
            global flowrate_minimum
            line_number=1
            line=line_number-1
            x_increment=0                   #use this to move the whole block horizontally
            y_increment=65                  #use this to move the whole block vertically
            x_increment_text_right=30        #use this to change gap b/w number and text to its right
            flowrate_number=Label(window, text=Flowrate, anchor="w", bg="black", fg="white",font=("montserrat",34,"normal"))
            flowrate_label=Label(window, text="Flowrate", bg="black", fg="white",font=("montserrat light",12,"normal"))
            flowrate_unit=Label(window, text="Lpm", bg="black", fg="white",font=("montserrat light",12,"normal"))
            flowrate_maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
            flowrate_minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
            flowrate_number.place(x=120+x_increment,y=y_increment_monitored_values_block+40+line*y_increment)
            flowrate_label.place(x=185+x_increment+x_increment_text_right,y=y_increment_monitored_values_block+47+line*y_increment)
            flowrate_unit.place(x=185+x_increment+x_increment_text_right,y=y_increment_monitored_values_block+68+line*y_increment)
            flowrate_maximum.place(x=45+x_increment,y=y_increment_monitored_values_block+50+line*y_increment)
            flowrate_minimum.place(x=45+x_increment,y=y_increment_monitored_values_block+70+line*y_increment)

        def display_PEEP(PEEP,max,min):
            global PEEP_number
            global PEEP_label
            global PEEP_unit
            global PEEP_maximum
            global PEEP_minimum
            line_number=2
            line=line_number-1
            x_increment=0
            y_increment=65
            x_increment_text_right=30        #use this to change gap b/w number and text to its right
            PEEP_number=Label(window, text=PEEP, anchor="e", bg="black", fg="white",font=("montserrat",34,"normal"))
            PEEP_label=Label(window, text="PEEP", bg="black", fg="white",font=("montserrat light",12,"normal"))
            PEEP_unit=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",12,"normal"))
            PEEP_maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
            PEEP_minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
            PEEP_number.place(x=120+x_increment,y=y_increment_monitored_values_block+40+line*y_increment)
            PEEP_label.place(x=185+x_increment+x_increment_text_right,y=y_increment_monitored_values_block+47+line*y_increment)
            PEEP_unit.place(x=185+x_increment+x_increment_text_right,y=y_increment_monitored_values_block+68+line*y_increment)
            PEEP_maximum.place(x=45+x_increment,y=y_increment_monitored_values_block+50+line*y_increment)
            PEEP_minimum.place(x=45+x_increment,y=y_increment_monitored_values_block+70+line*y_increment)

        def display_P_plat(P_plat,max,min):
            global P_plat_number
            global P_plat_label
            global P_plat_unit
            global P_plat_maximum
            global P_plat_minimum
            line_number=3
            line=line_number-1
            x_increment=0
            y_increment=65
            x_increment_text_right=30        #use this to change gap b/w number and text to its right
            P_plat_number=Label(window, text=P_plat, anchor="e", bg="black", fg="white",font=("montserrat",34,"normal"))
            P_plat_label=Label(window, text="P.Plateau", bg="black", fg="white",font=("montserrat light",12,"normal"))
            P_plat_unit=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",12,"normal"))
            P_plat_maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
            P_plat_minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
            P_plat_number.place(x=120+x_increment,y=y_increment_monitored_values_block+40+line*y_increment)
            P_plat_label.place(x=185+x_increment+x_increment_text_right,y=y_increment_monitored_values_block+47+line*y_increment)
            P_plat_unit.place(x=185+x_increment+x_increment_text_right,y=y_increment_monitored_values_block+68+line*y_increment)
            P_plat_maximum.place(x=45+x_increment,y=y_increment_monitored_values_block+50+line*y_increment)
            P_plat_minimum.place(x=45+x_increment,y=y_increment_monitored_values_block+70+line*y_increment)

        def display_BPM(BPM,max,min):
            global BPM_number
            global BPM_label
            global BPM_unit
            global BPM_maximum
            global BPM_minimum
            line_number=4
            line=line_number-1
            x_increment=0
            y_increment=65
            x_increment_text_right=30        #use this to change gap b/w number and text to its right
            BPM_number=Label(window, text=BPM, anchor="e", bg="black", fg="white",font=("montserrat",34,"normal"))
            BPM_label=Label(window, text="BPM", bg="black", fg="white",font=("montserrat light",12,"normal"))
            BPM_maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
            BPM_minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
            BPM_number.place(x=120+x_increment,y=y_increment_monitored_values_block+40+line*y_increment)
            BPM_label.place(x=185+x_increment+x_increment_text_right,y=y_increment_monitored_values_block+47+line*y_increment)
            BPM_maximum.place(x=45+x_increment,y=y_increment_monitored_values_block+50+line*y_increment)
            BPM_minimum.place(x=45+x_increment,y=y_increment_monitored_values_block+70+line*y_increment)

        def display_VTE(VTE,max,min):
            global VTE_number
            global VTE_label
            global VTE_unit
            global VTE_maximum
            global VTE_minimum
            line_number=5
            line=line_number-1
            x_increment=0
            y_increment=65
            x_increment_text_right=30
            VTE_number=Label(window, text=VTE, anchor="e", bg="black", fg="white",font=("montserrat",34,"normal"))
            VTE_label=Label(window, text="VTE", bg="black", fg="white",font=("montserrat light",12,"normal"))
            VTE_unit=Label(window, text="mL", bg="black", fg="white",font=("montserrat light",12,"normal"))
            VTE_maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
            VTE_minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
            VTE_number.place(x=90+x_increment,y=y_increment_monitored_values_block+40+line*y_increment)
            VTE_label.place(x=185+x_increment+x_increment_text_right, y=y_increment_monitored_values_block+47+line*y_increment)
            VTE_unit.place(x=185+x_increment+x_increment_text_right, y=y_increment_monitored_values_block+68+line*y_increment)
            VTE_maximum.place(x=45+x_increment,y=y_increment_monitored_values_block+50+line*y_increment)
            VTE_minimum.place(x=45+x_increment,y=y_increment_monitored_values_block+70+line*y_increment)

        def display_VTI(VTI,max,min):
            global VTI_number
            global VTI_label
            global VTI_unit
            global VTI_maximum
            global VTI_minimum
            line_number=6
            line=line_number-1
            x_increment=0
            y_increment=65
            x_increment_text_right=30
            VTI_number=Label(window, text=VTI, anchor="e", bg="black", fg="white",font=("montserrat",34,"normal"))
            VTI_label=Label(window, text="VTI", bg="black", fg="white",font=("montserrat light",12,"normal"))
            VTI_unit=Label(window, text="mL", bg="black", fg="white",font=("montserrat light",12,"normal"))
            VTI_maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
            VTI_minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
            VTI_number.place(x=90+x_increment,y=y_increment_monitored_values_block+40+line*y_increment)
            VTI_label.place(x=185+x_increment+x_increment_text_right, y=y_increment_monitored_values_block+47+line*y_increment)
            VTI_unit.place(x=185+x_increment+x_increment_text_right, y=y_increment_monitored_values_block+68+line*y_increment)
            VTI_maximum.place(x=45+x_increment,y=y_increment_monitored_values_block+50+line*y_increment)
            VTI_minimum.place(x=45+x_increment,y=y_increment_monitored_values_block+70+line*y_increment)

        def display_IE(IE,max,min):
            global IE_number
            global IE_label
            global IE_unit
            global IE_maximum
            global IE_minimum
            line_number=7
            line=line_number-1
            x_increment=0
            y_increment=65
            x_increment_text_right=30        #use this to change gap b/w number and text to its right
            IE_number=Label(window, text="1:"+str(IE), anchor="e", bg="black", fg="white",font=("montserrat",34,"normal"))
            IE_label=Label(window, text="IE Ratio", bg="black", fg="white",font=("montserrat light",12,"normal"))
            IE_maximum=Label(window, text="1:"+str(max), bg="black", fg="white",font=("montserrat light",10,"normal"))
            IE_minimum=Label(window, text="1:"+str(min), bg="black", fg="white",font=("montserrat light",10,"normal"))
            IE_number.place(x=120+x_increment,y=y_increment_monitored_values_block+40+line*y_increment)
            IE_label.place(x=185+x_increment+x_increment_text_right,y=y_increment_monitored_values_block+47+line*y_increment)
            IE_maximum.place(x=45+x_increment,y=y_increment_monitored_values_block+50+line*y_increment)
            IE_minimum.place(x=45+x_increment,y=y_increment_monitored_values_block+70+line*y_increment)

        def display_FiO2(FiO2,max,min):
            global FiO2_number
            global FiO2_label
            global FiO2_unit
            global FiO2_maximum
            global FiO2_minimum
            line_number=8
            line=line_number-1
            x_increment=0
            y_increment=65
            x_increment_text_right=30
            FiO2_number=Label(window, text=FiO2, anchor="e", bg="black", fg="white",font=("montserrat",34,"normal"))
            FiO2_label=Label(window, text="FiO2", bg="black", fg="white",font=("montserrat light",12,"normal"))
            FiO2_unit=Label(window, text="%", bg="black", fg="white",font=("montserrat light",12,"normal"))
            FiO2_maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
            FiO2_minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
            FiO2_number.place(x=120+x_increment,y=y_increment_monitored_values_block+40+line*y_increment)
            FiO2_label.place(x=185+x_increment+x_increment_text_right,y=y_increment_monitored_values_block+47+line*y_increment)
            FiO2_unit.place(x=185+x_increment+x_increment_text_right,y=y_increment_monitored_values_block+68+line*y_increment)
            FiO2_maximum.place(x=45+x_increment,y=y_increment_monitored_values_block+50+line*y_increment)
            FiO2_minimum.place(x=45+x_increment,y=y_increment_monitored_values_block+70+line*y_increment)

        def display_breathing_status(breathing_status,max,min):
            global breathing_status_number
            global breathing_status_label
            global breathing_status_unit
            global breathing_status_maximum
            global breathing_status_minimum
            line_number=9
            line=line_number-1
            x_increment=0; y_increment=65
            breathing_status_number=Label(window, text=breathing_status, bg="black", fg="white",font=("montserrat",34,"normal"))
            breathing_status_label=Label(window, text="breathing", bg="black", fg="white",font=("montserrat light",12,"normal"))
            breathing_status_unit=Label(window, text="sec", bg="black", fg="white",font=("montserrat light",12,"normal"))
            breathing_status_maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
            breathing_status_minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
            breathing_status_number.place(x=120+x_increment,y=y_increment_monitored_values_block+40+line*y_increment)
            breathing_status_label.place(x=185,y=y_increment_monitored_values_block+47+line*y_increment)
            breathing_status_unit.place(x=185+x_increment,y=y_increment_monitored_values_block+68+line*y_increment)
            breathing_status_maximum.place(x=45+x_increment,y=y_increment_monitored_values_block+50+line*y_increment)
            breathing_status_minimum.place(x=45+x_increment,y=y_increment_monitored_values_block+70+line*y_increment)

        def display_monitored_values_label():
            global display_monitored_values_image_label
            global display_monitored_values_image
            display_monitored_values_image=PhotoImage(file="monitored values image.gif")
            display_monitored_values_image_label=Label (window, image=display_monitored_values_image, bg="black")
            display_monitored_values_image_label.place(x=25,y=30)

        def configure_monitored_values():
            global Peak_P_number
            global flowrate_number
            global PEEP_number
            global P_plat_number
            global BPM_number
            global VTE_number
            global VTI_number
            global IE_number
            global FiO2_number
            global insp_time_number
            if mode==",pcv,":
                Peak_P_number.configure(text=int(value_pressure_received_5))
            if mode==",vcv,":
                flowrate_number.configure(text=int(value_flow_received_5))
            PEEP_number.configure(text=int(value_peep_received))
            P_plat_number.configure(text=int(value_pplat_received))
            BPM_number.configure(text=int(value_bpm_received))
            VTE_number.configure(text=int(value_vol_ex_received))
            VTI_number.configure(text=int(value_vol_in_received))
            IE_number.configure(text=str(value_IE_received))
            FiO2_number.configure(text=value_pressure_received_5)
            # insp_time_number.configure(text=value_insp_received_5)
            global breathing_status_number
            breathing_status_number.configure(text=breathing_status_received)

        def display_monitored_values():
            monitoring.display_values_being_monitored.display_monitored_values_label()
            if mode==",pcv,":
                monitoring.display_values_being_monitored.display_Peak_Pressure(value_pressure_received_5,32,2)
            if mode==",vcv,":
                monitoring.display_values_being_monitored.display_insp_flowrate(value_flow_received_5,32,2)
            monitoring.display_values_being_monitored.display_PEEP(value_peep_received,1.5,1.25)
            monitoring.display_values_being_monitored.display_P_plat(value_pplat_received,1.5,1.25)
            monitoring.display_values_being_monitored.display_BPM(value_bpm_received,32,2)
            monitoring.display_values_being_monitored.display_VTE(value_vol_ex_received,1400,500)
            monitoring.display_values_being_monitored.display_VTI(value_vol_in_received,1400,500)
            monitoring.display_values_being_monitored.display_IE(str("1:"+str(value_IE_received)),1.5,1.25)
            monitoring.display_values_being_monitored.display_FiO2(value_oxygen_received,1.5,1.25)
            monitoring.display_values_being_monitored.display_breathing_status(breathing_status_received,1.5,1.25)

        def hide_monitored_values():
            global Peak_P_number
            global Peak_P_label
            global Peak_P_unit
            global Peak_P_maximum
            global Peak_P_minimum
            Peak_P_number.place_forget()
            Peak_P_label.place_forget()
            Peak_P_unit.place_forget()
            Peak_P_maximum.place_forget()
            Peak_P_minimum.place_forget()
            global flowrate_number
            global flowrate_label
            global flowrate_unit
            global flowrate_maximum
            global flowrate_minimum
            flowrate_number.place_forget()
            flowrate_label.place_forget()
            flowrate_unit.place_forget()
            flowrate_maximum.place_forget()
            flowrate_minimum.place_forget()
            # if mode==",pcv,":
            #     global Peak_P_number
            #     global Peak_P_label
            #     global Peak_P_unit
            #     global Peak_P_maximum
            #     global Peak_P_minimum
            #     Peak_P_number.place_forget()
            #     Peak_P_label.place_forget()
            #     Peak_P_unit.place_forget()
            #     Peak_P_maximum.place_forget()
            #     Peak_P_minimum.place_forget()
            # if mode==",vcv,":
            #     global flowrate_number
            #     global flowrate_label
            #     global flowrate_unit
            #     global flowrate_maximum
            #     global flowrate_minimum
            #     flowrate_number.place_forget()
            #     flowrate_label.place_forget()
            #     flowrate_unit.place_forget()
            #     flowrate_maximum.place_forget()
            #     flowrate_minimum.place_forget()
            global BPM_number
            global BPM_label
            global BPM_unit
            global BPM_maximum
            global BPM_minimum
            BPM_number.place_forget()
            BPM_label.place_forget()
            BPM_maximum.place_forget()
            BPM_minimum.place_forget()
            global VTE_number
            global VTE_label
            global VTE_unit
            global VTE_maximum
            global VTE_minimum
            VTE_number.place_forget()
            VTE_label.place_forget()
            VTE_unit.place_forget()
            VTE_maximum.place_forget()
            VTE_minimum.place_forget()
            global VTI_number
            global VTI_label
            global VTI_unit
            global VTI_maximum
            global VTI_minimum
            VTI_number.place_forget()
            VTI_label.place_forget()
            VTI_unit.place_forget()
            VTI_maximum.place_forget()
            VTI_minimum.place_forget()
            global IE_number
            global IE_label
            global IE_unit
            global IE_maximum
            global IE_minimum
            IE_number.place_forget()
            IE_label.place_forget()
            IE_maximum.place_forget()
            IE_minimum.place_forget()
            global FiO2_number
            global FiO2_label
            global FiO2_unit
            global FiO2_maximum
            global FiO2_minimum
            FiO2_number.place_forget()
            FiO2_label.place_forget()
            FiO2_unit.place_forget()
            FiO2_maximum.place_forget()
            FiO2_minimum.place_forget()
            global PEEP_number
            global PEEP_label
            global PEEP_unit
            global PEEP_maximum
            global PEEP_minimum
            PEEP_number.place_forget()
            PEEP_label.place_forget()
            PEEP_unit.place_forget()
            PEEP_maximum.place_forget()
            PEEP_minimum.place_forget()
            global P_plat_number
            global P_plat_label
            global P_plat_unit
            global P_plat_maximum
            global P_plat_minimum
            P_plat_number.place_forget()
            P_plat_label.place_forget()
            P_plat_unit.place_forget()
            P_plat_maximum.place_forget()
            P_plat_minimum.place_forget()
            global display_monitored_values_image_label
            display_monitored_values_image_label.place_forget()

    class graphs():
        plt.rcParams.update({'font.size': 10})
        text_color = 'white'
        plt.rcParams['text.color'] = text_color
        plt.rcParams['axes.labelcolor'] = text_color
        plt.rcParams['xtick.color'] = text_color
        plt.rcParams['ytick.color'] = text_color
        global x_data_pressure
        global y_data_pressure
        global y_val_pressure
        global starting_time_pressure
        global time_interval_pressure
        global total_time_pressure
        global data_points_pressure
        global animation_loop_counter_pressure
        global array_character_number_being_printed_pressure
        global data_points_in_one_array_pressure_pressure
        x_data_pressure = np.array([0])
        y_data_pressure = np.array([0])
        starting_time_pressure=0
        time_interval_pressure=0.03
        total_time_pressure=10
        data_points_pressure=total_time_pressure/time_interval_pressure
        animation_loop_counter_pressure=0
        def animation_frame_pressure(i):
            global time_interval_pressure
            global starting_time_pressure
            global y_val_pressure
            global x_data_pressure
            global y_data_pressure
            global animation_loop_counter_pressure
            global array_character_number_being_printed_pressure
            starting_time_pressure=starting_time_pressure+time_interval_pressure
            if animation_loop_counter_pressure<data_points_pressure:
                x_data_pressure=np.append(x_data_pressure,[starting_time_pressure])
                y_data_pressure=np.append(y_data_pressure,[value_pressure_received_5])
            if animation_loop_counter_pressure>=data_points_pressure:
                y_data_pressure=np.append(y_data_pressure,[value_pressure_received_5])
                y_data_pressure=np.delete(y_data_pressure,0)
            line_pressure.set_xdata(x_data_pressure)
            line_pressure.set_ydata(y_data_pressure)
            animation_loop_counter_pressure=animation_loop_counter_pressure+1
            return line_pressure,
        global line_pressure
        fig_pressure=Figure(figsize=(9,2.3), dpi=100)
        ax_pressure = fig_pressure.add_subplot(111)
        ax_pressure.set_facecolor('xkcd:black')   #background color
        fig_pressure.patch.set_facecolor('xkcd:black')
        ax_pressure.set_xlim(0, total_time_pressure)
        ax_pressure.set_ylim(-5, 50)
        line_pressure, = ax_pressure.plot(0, 0, color='white')
        graph_pressure = FigureCanvasTkAgg(fig_pressure, master=window)
        canvas_pressure=graph_pressure.get_tk_widget()
        animation_pressure = FuncAnimation(fig_pressure, func=animation_frame_pressure, frames=1000, interval=time_interval_pressure*1000)

        global x_data_flow
        global y_data_flow
        global y_val_flow
        global starting_time_flow
        global time_interval_flow
        global total_time_flow
        global data_points_flow
        global animation_loop_counter_flow
        global array_character_number_being_printed_flow
        x_data_flow = np.array([0])
        y_data_flow = np.array([0])
        starting_time_flow=0
        time_interval_flow=0.03
        total_time_flow=10
        data_points_flow=total_time_flow/time_interval_flow
        animation_loop_counter_flow=0
        def animation_frame_flow(i):
            global time_interval_flow
            global starting_time_flow
            global y_val_flow
            global x_data_flow
            global y_data_flow
            global animation_loop_counter_flow
            global array_character_number_being_printed_flow
            starting_time_flow=starting_time_flow+time_interval_flow
            if animation_loop_counter_flow<data_points_flow:
                x_data_flow=np.append(x_data_flow,[starting_time_flow])
                y_data_flow=np.append(y_data_flow,[value_flow_received_5])
            if animation_loop_counter_flow>=data_points_flow:
                y_data_flow=np.append(y_data_flow,[value_flow_received_5])
                y_data_flow=np.delete(y_data_flow,0)
            line_flow.set_xdata(x_data_flow)
            line_flow.set_ydata(y_data_flow)
            animation_loop_counter_flow=animation_loop_counter_flow+1
            return line_flow,
        global line_flow
        fig_flow=Figure(figsize=(9,2.3), dpi=100)
        ax_flow = fig_flow.add_subplot(111)
        ax_flow.set_facecolor('xkcd:black')   #background color
        fig_flow.patch.set_facecolor('xkcd:black')
        ax_flow.set_xlim(0, total_time_flow)
        ax_flow.set_ylim(-100, 100)
        line_flow, = ax_flow.plot(0, 0, color='white')
        graph_flow = FigureCanvasTkAgg(fig_flow, master=window)
        canvas_flow=graph_flow.get_tk_widget()
        animation2 = FuncAnimation(fig_flow, func=animation_frame_flow, frames=1000, interval=time_interval_flow*1000)

        def display_graphs():
            global value_flow_received
            value_flow_received=10
            monitoring.graphs.canvas_pressure.place(x=300,y=130)
            monitoring.graphs.canvas_flow.place(x=300,y=380)

        def hide_graphs():
            monitoring.graphs.canvas_pressure.place_forget()
            monitoring.graphs.canvas_flow.place_forget()

    def start_monitoring():
        monitoring.testing_inputs_and_playing_alarms.place_notifications()
        monitoring.graphs.display_graphs()
        monitoring.receiving_data_from_arduino.get_shit_from_arduino_and_update_it_live()
        monitoring.testing_inputs_and_playing_alarms.testing_received_values()
        monitoring.display_values_being_monitored.display_monitored_values()
        monitoring.live_updates()

    def live_updates():
        global testing_time_start
        monitoring.receiving_data_from_arduino.get_shit_from_arduino_and_update_it_live()
        monitoring.testing_inputs_and_playing_alarms.testing_received_values()
        monitoring.display_values_being_monitored.configure_monitored_values()
        if testing_time_start==testing_time_end:                            #once testing is finished, reset testime time and use this if condition to ensure that live_update stops running. Or it'll be receiving and updating values in back end and that can fuck shit up
            monitoring.stop_monitoring()
            testing_time_start=0
            return()
        if testing_time_start<testing_time_end:
            window.after(30,monitoring.live_updates)

    def stop_monitoring():
        monitoring.graphs.hide_graphs()
        monitoring.display_values_being_monitored.hide_monitored_values()
        monitoring.testing_inputs_and_playing_alarms.hide_notifications()
global pressure_UA
global pressure_LA
global flowrate_UA
global flowrate_LA
global peep_UA
global peep_LA
global bpm_UA
global bpm_LA
global oxygen_UA
global oxygen_LA
global vol_UA
global vol_LA

pressure_UA = UL_pressure
pressure_LA = LL_pressure
flowrate_UA = UL_flowrate
flowrate_LA = LL_flowrate
peep_UA = UL_peep
peep_LA = LL_peep
bpm_UA = UL_bpm
bpm_LA = LL_bpm
oxygen_UA = UL_oxygen
oxygen_LA = LL_oxygen
vol_UA = UL_vol
vol_LA = LL_vol
"""CLASS: ALARM/START"""
class alarm_scales():
    global CustomScale_pressure_UA
    global CustomScale_pressure_LA
    global CustomScale_flowrate_UA
    global CustomScale_flowrate_LA
    global CustomScale_bpm_UA
    global CustomScale_bpm_LA
    global CustomScale_peep_UA
    global CustomScale_peep_LA
    global CustomScale_vol_UA
    global CustomScale_vol_LA
    global CustomScale_oxygen_UA
    global CustomScale_oxygen_LA
    class CustomScale_pressure_UA(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'pressure_UA.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global pressure_UA
            if scaling=="yes":
                if scale_location_status=="centered":
                    global alarm_scale_pressure_value_UA
                    alarm_scale_pressure_value_UA.place_forget()
                    pressure_UA=format(int(self.variable.get()))
                    alarm_scale_pressure_value_UA=Label(window, text=str(pressure_UA), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    alarm_scale_pressure_value_UA.place(x=scale_value_pressure_entered_location_x_UA,y=scale_value_pressure_entered_location_y_UA, anchor = CENTER)
    class CustomScale_pressure_LA(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'pressure_LA.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global pressure_LA
            if scaling=="yes":
                if scale_location_status=="centered":
                    global alarm_scale_pressure_value_LA
                    alarm_scale_pressure_value_LA.place_forget()
                    pressure_LA=format(int(self.variable.get()))
                    alarm_scale_pressure_value_LA=Label(window, text=str(pressure_LA), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    alarm_scale_pressure_value_LA.place(x=scale_value_pressure_entered_location_x_LA,y=scale_value_pressure_entered_location_y_LA, anchor = CENTER)

    class CustomScale_flowrate_UA(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'flowrate_UA.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global flowrate_UA
            if scaling=="yes":
                if scale_location_status=="centered":
                    global alarm_scale_flowrate_value_UA
                    alarm_scale_flowrate_value_UA.place_forget()
                    flowrate_UA=format(int(self.variable.get()))
                    alarm_scale_flowrate_value_UA=Label(window, text=str(flowrate_UA), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    alarm_scale_flowrate_value_UA.place(x=scale_value_flowrate_entered_location_x_UA,y=scale_value_flowrate_entered_location_y_UA, anchor = CENTER)

    class CustomScale_flowrate_LA(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'flowrate_LA.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global flowrate_LA
            if scaling=="yes":
                if scale_location_status=="centered":
                    global alarm_scale_flowrate_value_LA
                    alarm_scale_flowrate_value_LA.place_forget()
                    flowrate_LA=format(int(self.variable.get()))
                    alarm_scale_flowrate_value_LA=Label(window, text=str(flowrate_LA), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    alarm_scale_flowrate_value_LA.place(x=scale_value_flowrate_entered_location_x_LA,y=scale_value_flowrate_entered_location_y_LA, anchor = CENTER)

    class CustomScale_peep_UA(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'peep_UA.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global peep_UA
            if scaling=="yes":
                if scale_location_status=="centered":
                    global alarm_scale_peep_value_UA
                    alarm_scale_peep_value_UA.place_forget()
                    peep_UA=format(int(self.variable.get()))
                    alarm_scale_peep_value_UA=Label(window, text=str(peep_UA), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    alarm_scale_peep_value_UA.place(x=scale_value_peep_entered_location_x_UA,y=scale_value_peep_entered_location_y_UA, anchor = CENTER)

    class CustomScale_peep_LA(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'peep_LA.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global peep_LA
            if scaling=="yes":
                if scale_location_status=="centered":
                    global alarm_scale_peep_value_LA
                    alarm_scale_peep_value_LA.place_forget()
                    peep_LA=format(int(self.variable.get()))
                    alarm_scale_peep_value_LA=Label(window, text=str(peep_LA), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    alarm_scale_peep_value_LA.place(x=scale_value_peep_entered_location_x_LA,y=scale_value_peep_entered_location_y_LA, anchor = CENTER)

    class CustomScale_bpm_UA(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'bpm_UA.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global bpm_UA
            if scaling=="yes":
                if scale_location_status=="centered":
                    global alarm_scale_bpm_value_UA
                    alarm_scale_bpm_value_UA.place_forget()
                    bpm_UA=format(int(self.variable.get()))
                    alarm_scale_bpm_value_UA=Label(window, text=str(bpm_UA), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    alarm_scale_bpm_value_UA.place(x=scale_value_bpm_entered_location_x_UA,y=scale_value_bpm_entered_location_y_UA, anchor = CENTER)

    class CustomScale_bpm_LA(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'bpm_LA.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global bpm_LA
            if scaling=="yes":
                if scale_location_status=="centered":
                    global alarm_scale_bpm_value_LA
                    alarm_scale_bpm_value_LA.place_forget()
                    bpm_LA=format(int(self.variable.get()))
                    alarm_scale_bpm_value_LA=Label(window, text=str(bpm_LA), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    alarm_scale_bpm_value_LA.place(x=scale_value_bpm_entered_location_x_LA,y=scale_value_bpm_entered_location_y_LA, anchor = CENTER)

    class CustomScale_vol_UA(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'vol_UA.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global vol_UA
            if scaling=="yes":
                if scale_location_status=="centered":
                    global alarm_scale_vol_value_UA
                    alarm_scale_vol_value_UA.place_forget()
                    vol_UA=format(int(self.variable.get()))
                    alarm_scale_vol_value_UA=Label(window, text=str(vol_UA), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    alarm_scale_vol_value_UA.place(x=scale_value_vol_entered_location_x_UA,y=scale_value_vol_entered_location_y_UA, anchor = CENTER)

    class CustomScale_vol_LA(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'vol_LA.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global vol_LA
            if scaling=="yes":
                if scale_location_status=="centered":
                    global alarm_scale_vol_value_LA
                    alarm_scale_vol_value_LA.place_forget()
                    vol_LA=format(int(self.variable.get()))
                    alarm_scale_vol_value_LA=Label(window, text=str(vol_LA), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    alarm_scale_vol_value_LA.place(x=scale_value_vol_entered_location_x_LA,y=scale_value_vol_entered_location_y_LA, anchor = CENTER)

    class CustomScale_oxygen_UA(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'oxygen_UA.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global oxygen_UA
            if scaling=="yes":
                if scale_location_status=="centered":
                    global alarm_scale_oxygen_value_UA
                    alarm_scale_oxygen_value_UA.place_forget()
                    oxygen_UA=format(int(self.variable.get()))
                    alarm_scale_oxygen_value_UA=Label(window, text=str(oxygen_UA), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    alarm_scale_oxygen_value_UA.place(x=scale_value_oxygen_entered_location_x_UA,y=scale_value_oxygen_entered_location_y_UA, anchor = CENTER)

    class CustomScale_oxygen_LA(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'oxygen_LA.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global oxygen_LA
            if scaling=="yes":
                if scale_location_status=="centered":
                    global alarm_scale_oxygen_value_LA
                    alarm_scale_oxygen_value_LA.place_forget()
                    oxygen_LA=format(int(self.variable.get()))
                    alarm_scale_oxygen_value_LA=Label(window, text=str(oxygen_LA), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    alarm_scale_oxygen_value_LA.place(x=scale_value_oxygen_entered_location_x_LA,y=scale_value_oxygen_entered_location_y_LA, anchor = CENTER)

    def create_alarm_bar_and_slider():
        global alarm_img_trough
        global alarm_img_slider
        alarm_img_trough = PhotoImage(file="alarm_bar.gif")
        alarm_img_slider = PhotoImage(file="startup_slider.gif")
    create_alarm_bar_and_slider()

    def create_scale_styles_for_alarm():
        # create scale elements
        string_alarm_trough='pressure_UA.Horizontal.Scale.trough'
        string_alarm_slider='pressure_UA.Horizontal.Scale.slider'
        style.element_create(string_alarm_trough, 'image', alarm_img_trough)
        style.element_create(string_alarm_slider, 'image', alarm_img_slider)
        style.layout('pressure_UA.Horizontal.TScale',[(string_alarm_trough, {'sticky': 'ns'}),
                    (string_alarm_slider, {'side': 'left', 'sticky': '','children': [('pressure_UA.Horizontal.Scale.label', {'sticky': ''})]})])
        # create scale elements
        string_alarm_trough='pressure_LA.Horizontal.Scale.trough'
        string_alarm_slider='pressure_LA.Horizontal.Scale.slider'
        style.element_create(string_alarm_trough, 'image', alarm_img_trough)
        style.element_create(string_alarm_slider, 'image', alarm_img_slider)
        style.layout('pressure_LA.Horizontal.TScale',[(string_alarm_trough, {'sticky': 'ns'}),
                    (string_alarm_slider, {'side': 'left', 'sticky': '','children': [('pressure_LA.Horizontal.Scale.label', {'sticky': ''})]})])
        # create scale elements
        string_alarm_trough='flowrate_UA.Horizontal.Scale.trough'
        string_alarm_slider='flowrate_UA.Horizontal.Scale.slider'
        style.element_create(string_alarm_trough, 'image', alarm_img_trough)
        style.element_create(string_alarm_slider, 'image', alarm_img_slider)
        style.layout('flowrate_UA.Horizontal.TScale',[(string_alarm_trough, {'sticky': 'ns'}),
                    (string_alarm_slider, {'side': 'left', 'sticky': '','children': [('flowrate_UA.Horizontal.Scale.label', {'sticky': ''})]})])
        # create scale elements
        string_alarm_trough='flowrate_LA.Horizontal.Scale.trough'
        string_alarm_slider='flowrate_LA.Horizontal.Scale.slider'
        style.element_create(string_alarm_trough, 'image', alarm_img_trough)
        style.element_create(string_alarm_slider, 'image', alarm_img_slider)
        style.layout('flowrate_LA.Horizontal.TScale',[(string_alarm_trough, {'sticky': 'ns'}),
                    (string_alarm_slider, {'side': 'left', 'sticky': '','children': [('flowrate_LA.Horizontal.Scale.label', {'sticky': ''})]})])
        # create scale elements
        string_alarm_trough='peep_UA.Horizontal.Scale.trough'
        string_alarm_slider='peep_UA.Horizontal.Scale.slider'
        style.element_create(string_alarm_trough, 'image', alarm_img_trough)
        style.element_create(string_alarm_slider, 'image', alarm_img_slider)
        style.layout('peep_UA.Horizontal.TScale',[(string_alarm_trough, {'sticky': 'ns'}),
                    (string_alarm_slider, {'side': 'left', 'sticky': '','children': [('peep_UA.Horizontal.Scale.label', {'sticky': ''})]})])
        # create scale elements
        string_alarm_trough='peep_LA.Horizontal.Scale.trough'
        string_alarm_slider='peep_LA.Horizontal.Scale.slider'
        style.element_create(string_alarm_trough, 'image', alarm_img_trough)
        style.element_create(string_alarm_slider, 'image', alarm_img_slider)
        style.layout('peep_LA.Horizontal.TScale',[(string_alarm_trough, {'sticky': 'ns'}),
                    (string_alarm_slider, {'side': 'left', 'sticky': '','children': [('peep_LA.Horizontal.Scale.label', {'sticky': ''})]})])
        # create scale elements
        string_alarm_trough='oxygen_UA.Horizontal.Scale.trough'
        string_alarm_slider='oxygen_UA.Horizontal.Scale.slider'
        style.element_create(string_alarm_trough, 'image', alarm_img_trough)
        style.element_create(string_alarm_slider, 'image', alarm_img_slider)
        style.layout('oxygen_UA.Horizontal.TScale',[(string_alarm_trough, {'sticky': 'ns'}),
                    (string_alarm_slider, {'side': 'left', 'sticky': '','children': [('oxygen_UA.Horizontal.Scale.label', {'sticky': ''})]})])
        # create scale elements
        string_alarm_trough='oxygen_LA.Horizontal.Scale.trough'
        string_alarm_slider='oxygen_LA.Horizontal.Scale.slider'
        style.element_create(string_alarm_trough, 'image', alarm_img_trough)
        style.element_create(string_alarm_slider, 'image', alarm_img_slider)
        style.layout('oxygen_LA.Horizontal.TScale',[(string_alarm_trough, {'sticky': 'ns'}),
                    (string_alarm_slider, {'side': 'left', 'sticky': '','children': [('oxygen_LA.Horizontal.Scale.label', {'sticky': ''})]})])
        # create scale elements
        string_alarm_trough='bpm_UA.Horizontal.Scale.trough'
        string_alarm_slider='bpm_UA.Horizontal.Scale.slider'
        style.element_create(string_alarm_trough, 'image', alarm_img_trough)
        style.element_create(string_alarm_slider, 'image', alarm_img_slider)
        style.layout('bpm_UA.Horizontal.TScale',[(string_alarm_trough, {'sticky': 'ns'}),
                    (string_alarm_slider, {'side': 'left', 'sticky': '','children': [('bpm_UA.Horizontal.Scale.label', {'sticky': ''})]})])
        # create scale elements
        string_alarm_trough='bpm_LA.Horizontal.Scale.trough'
        string_alarm_slider='bpm_LA.Horizontal.Scale.slider'
        style.element_create(string_alarm_trough, 'image', alarm_img_trough)
        style.element_create(string_alarm_slider, 'image', alarm_img_slider)
        style.layout('bpm_LA.Horizontal.TScale',[(string_alarm_trough, {'sticky': 'ns'}),
                    (string_alarm_slider, {'side': 'left', 'sticky': '','children': [('bpm_LA.Horizontal.Scale.label', {'sticky': ''})]})])
        # create scale elements
        string_startup_trough='vol_UA.Horizontal.Scale.trough'
        string_startup_slider='vol_UA.Horizontal.Scale.slider'
        style.element_create(string_startup_trough, 'image', alarm_img_trough)
        style.element_create(string_startup_slider, 'image', alarm_img_slider)
        style.layout('vol_UA.Horizontal.TScale',[(string_startup_trough, {'sticky': 'ns'}),
                    (string_startup_slider, {'side': 'left', 'sticky': '','children': [('vol_UA.Horizontal.Scale.label', {'sticky': ''})]})])
        # create scale elements
        string_startup_trough='vol_LA.Horizontal.Scale.trough'
        string_startup_slider='vol_LA.Horizontal.Scale.slider'
        style.element_create(string_startup_trough, 'image', alarm_img_trough)
        style.element_create(string_startup_slider, 'image', alarm_img_slider)
        style.layout('vol_LA.Horizontal.TScale',[(string_startup_trough, {'sticky': 'ns'}),
                    (string_startup_slider, {'side': 'left', 'sticky': '','children': [('vol_LA.Horizontal.Scale.label', {'sticky': ''})]})])
    create_scale_styles_for_alarm()

    def create_alarm_scales():
        global scale_alarm_pressure_UA
        global scale_alarm_pressure_LA
        global scale_alarm_flowrate_UA
        global scale_alarm_flowrate_LA
        global scale_alarm_bpm_UA
        global scale_alarm_bpm_LA
        global scale_alarm_peep_UA
        global scale_alarm_peep_LA
        global scale_alarm_vol_UA
        global scale_alarm_vol_LA
        global scale_alarm_oxygen_UA
        global scale_alarm_oxygen_LA
        scale_alarm_pressure_UA = CustomScale_pressure_UA(window, from_=LL_pressure, to=UL_pressure)
        scale_alarm_pressure_LA = CustomScale_pressure_LA(window, from_=LL_pressure, to=UL_pressure)
        scale_alarm_flowrate_UA = CustomScale_flowrate_UA(window, from_=LL_flowrate, to=UL_flowrate)
        scale_alarm_flowrate_LA = CustomScale_flowrate_LA(window, from_=LL_flowrate, to=UL_flowrate)
        scale_alarm_bpm_UA = CustomScale_bpm_UA(window, from_=LL_bpm, to=UL_bpm)
        scale_alarm_bpm_LA = CustomScale_bpm_LA(window, from_=LL_bpm, to=UL_bpm)
        scale_alarm_peep_UA = CustomScale_peep_UA(window, from_=LL_peep, to=UL_peep)
        scale_alarm_peep_LA = CustomScale_peep_LA(window, from_=LL_peep, to=UL_peep)
        scale_alarm_vol_UA = CustomScale_vol_UA(window, from_=LL_vol, to=UL_vol)
        scale_alarm_vol_LA = CustomScale_vol_LA(window, from_=LL_vol, to=UL_vol)
        scale_alarm_oxygen_UA = CustomScale_oxygen_UA(window, from_=LL_oxygen, to=UL_oxygen)
        scale_alarm_oxygen_LA = CustomScale_oxygen_LA(window, from_=LL_oxygen, to=UL_oxygen)
    create_alarm_scales()
    global scale_value_pressure_entered_location_x_UA
    global scale_value_pressure_entered_location_y_UA
    global scale_value_pressure_entered_location_x_UA
    global scale_value_pressure_entered_location_y_UA
    global scale_value_flowrate_entered_location_x_UA
    global scale_value_flowrate_entered_location_y_UA
    global scale_value_peep_entered_location_x_UA
    global scale_value_peep_entered_location_y_UA
    global scale_value_bpm_entered_location_x_UA
    global scale_value_bpm_entered_location_y_UA
    global scale_value_vol_entered_location_x_UA
    global scale_value_vol_entered_location_y_UA
    global scale_value_oxygen_entered_location_x_UA
    global scale_value_oxygen_entered_location_y_UA
    global scale_value_pressure_entered_location_x_LA
    global scale_value_pressure_entered_location_y_LA
    global scale_value_pressure_entered_location_x_LA
    global scale_value_pressure_entered_location_y_LA
    global scale_value_flowrate_entered_location_x_LA
    global scale_value_flowrate_entered_location_y_LA
    global scale_value_peep_entered_location_x_LA
    global scale_value_peep_entered_location_y_LA
    global scale_value_bpm_entered_location_x_LA
    global scale_value_bpm_entered_location_y_LA
    global scale_value_vol_entered_location_x_LA
    global scale_value_vol_entered_location_y_LA
    global scale_value_oxygen_entered_location_x_LA
    global scale_value_oxygen_entered_location_y_LA
    scale_value_pressure_entered_location_x_UA = 0
    scale_value_pressure_entered_location_y_UA = 0
    scale_value_pressure_entered_location_x_UA = 0
    scale_value_pressure_entered_location_y_UA = 0
    scale_value_flowrate_entered_location_x_UA = 0
    scale_value_flowrate_entered_location_y_UA = 0
    scale_value_peep_entered_location_x_UA = 0
    scale_value_peep_entered_location_y_UA = 0
    scale_value_bpm_entered_location_x_UA = 0
    scale_value_bpm_entered_location_y_UA = 0
    scale_value_vol_entered_location_x_UA = 0
    scale_value_vol_entered_location_y_UA = 0
    scale_value_oxygen_entered_location_x_UA = 0
    scale_value_oxygen_entered_location_y_UA = 0
    scale_value_pressure_entered_location_x_LA = 0
    scale_value_pressure_entered_location_y_LA = 0
    scale_value_pressure_entered_location_x_LA = 0
    scale_value_pressure_entered_location_y_LA = 0
    scale_value_flowrate_entered_location_x_LA = 0
    scale_value_flowrate_entered_location_y_LA = 0
    scale_value_peep_entered_location_x_LA = 0
    scale_value_peep_entered_location_y_LA = 0
    scale_value_bpm_entered_location_x_LA = 0
    scale_value_bpm_entered_location_y_LA = 0
    scale_value_vol_entered_location_x_LA = 0
    scale_value_vol_entered_location_y_LA = 0

    def place_alarm_scales():
        global scale_value_pressure_entered_location_x_UA
        global scale_value_pressure_entered_location_y_UA
        global scale_value_pressure_entered_location_x_UA
        global scale_value_pressure_entered_location_y_UA
        global scale_value_flowrate_entered_location_x_UA
        global scale_value_flowrate_entered_location_y_UA
        global scale_value_peep_entered_location_x_UA
        global scale_value_peep_entered_location_y_UA
        global scale_value_bpm_entered_location_x_UA
        global scale_value_bpm_entered_location_y_UA
        global scale_value_vol_entered_location_x_UA
        global scale_value_vol_entered_location_y_UA
        global scale_value_oxygen_entered_location_x_UA
        global scale_value_oxygen_entered_location_y_UA
        global scale_value_pressure_entered_location_x_LA
        global scale_value_pressure_entered_location_y_LA
        global scale_value_pressure_entered_location_x_LA
        global scale_value_pressure_entered_location_y_LA
        global scale_value_flowrate_entered_location_x_LA
        global scale_value_flowrate_entered_location_y_LA
        global scale_value_peep_entered_location_x_LA
        global scale_value_peep_entered_location_y_LA
        global scale_value_bpm_entered_location_x_LA
        global scale_value_bpm_entered_location_y_LA
        global scale_value_vol_entered_location_x_LA
        global scale_value_vol_entered_location_y_LA
        global scale_value_oxygen_entered_location_x_LA
        global scale_value_oxygen_entered_location_y_LA
        global property_p_insp_UA
        global unit_p_insp_left_UA
        global property_p_insp_LA
        global unit_p_insp_left_LA
        global scale_alarm_pressure_UA
        global scale_alarm_pressure_LA
        global alarm_scale_pressure_value_UA
        global alarm_scale_pressure_value_LA
        global p_scale_unit_label_UA
        global p_scale_unit_label_LA
        global property_flowrate_UA
        global unit_flowrate_left_UA
        global property_flowrate_LA
        global unit_flowrate_left_LA
        global scale_alarm_flowrate_UA
        global scale_alarm_flowrate_LA
        global alarm_scale_flowrate_value_UA
        global alarm_scale_flowrate_value_LA
        global flowrate_scale_unit_label_UA
        global flowrate_scale_unit_label_LA
        global property_peep_UA
        global unit_peep_UA
        global property_peep_LA
        global unit_peep_LA
        global scale_alarm_peep_UA
        global scale_alarm_peep_LA
        global alarm_scale_peep_value_UA
        global alarm_scale_peep_value_LA
        global peep_scale_unit_label_UA
        global peep_scale_unit_label_LA
        global property_bpm_UA
        global property_bpm_LA
        global scale_alarm_bpm_UA
        global scale_alarm_bpm_LA
        global alarm_scale_bpm_value_UA
        global alarm_scale_bpm_value_LA
        global property_vol_UA
        global unit_vol_left_UA
        global property_vol_LA
        global unit_vol_left_LA
        global scale_alarm_vol_UA
        global scale_alarm_vol_LA
        global alarm_scale_vol_value_UA
        global alarm_scale_vol_value_LA
        global vol_scale_unit_label_UA
        global vol_scale_unit_label_LA
        global property_oxygen_UA
        global unit_oxygen_left_UA
        global property_oxygen_LA
        global unit_oxygen_left_LA
        global scale_alarm_oxygen_UA
        global scale_alarm_oxygen_LA
        global alarm_scale_oxygen_value_UA
        global alarm_scale_oxygen_value_LA
        global oxygen_scale_unit_label_UA
        global oxygen_scale_unit_label_LA
        global scaling
        scaling="yes"
        global property_being_updated
        global scale_location_status
        scale_location_status="centered"
        y_increment_entire_block=85      # change this to move everything up or down
        line_1_y=50+y_increment_entire_block
        y_increment=125                   #gap b/w lines
        y_unit_increment=35              #gap b/w property and unit
        y_scale_increment=-1             #gap b/w everything else and the scale. Use this to move just the scales up and down
        y_display_increment=10            # gap b/w scale and displayed values
        line_1_x=50                     # x location of line no.1. Since all labels are inclined verticaly. All have the same x_location. Change this to move everything horizontally
        x_increment=0                    # use this to change things horizontally rather than editing the value of line_1_x
        x_increment_UL=750                    # use this to change things horizontally rather than editing the value of line_1_x
        x_scale_increment=175            # gap b/w left label and scale
        x_display_increment=625          # gap b/w scale and the display to the right side of the scale
        global pressure_UA
        global pressure_LA
        global scale_value_pressure_entered_location_x
        global scale_value_pressure_entered_location_y
        global flowrate_UA
        global flowrate_LA
        global scale_value_flowrate_entered_location_x
        global scale_value_flowrate_entered_location_y
        line_no=1
        line=line_no-1
        if mode==",pcv,":
            property_p_insp_UA=Label(window, text="Pressure UL", bg="black", fg="white",font=("montserrat",18,"normal"))
            unit_p_insp_left_UA=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
            property_p_insp_UA.place(x=line_1_x+x_increment_UL,y=line_1_y+line*y_increment)
            unit_p_insp_left_UA.place(x=line_1_x+x_increment_UL,y=line_1_y+line*y_increment+y_unit_increment)
            scale_alarm_pressure_UA.place(x=line_1_x+x_increment_UL+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
            alarm_scale_pressure_value_UA=Label(window, text=pressure_UA, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
            p_scale_unit_label_UA=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
            scale_value_pressure_entered_location_x_UA=line_1_x+x_increment_UL+x_display_increment
            scale_value_pressure_entered_location_y_UA=line_1_y+line*y_increment+y_display_increment
            alarm_scale_pressure_value_UA.place(x=scale_value_pressure_entered_location_x_UA,y=scale_value_pressure_entered_location_y_UA, anchor = CENTER)
            p_scale_unit_label_UA.place(x=line_1_x+x_increment_UL+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)
            # line_no=1
            # line=line_no-1
            property_p_insp_LA=Label(window, text="Pressure LL", bg="black", fg="white",font=("montserrat",18,"normal"))
            unit_p_insp_left_LA=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
            property_p_insp_LA.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
            unit_p_insp_left_LA.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
            scale_alarm_pressure_LA.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
            alarm_scale_pressure_value_LA=Label(window, text=pressure_LA, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
            p_scale_unit_label_LA=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
            scale_value_pressure_entered_location_x_LA=line_1_x+x_increment+x_display_increment
            scale_value_pressure_entered_location_y_LA=line_1_y+line*y_increment+y_display_increment
            alarm_scale_pressure_value_LA.place(x=scale_value_pressure_entered_location_x_LA,y=scale_value_pressure_entered_location_y_LA, anchor = CENTER)
            p_scale_unit_label_LA.place(x=line_1_x+x_increment+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)
        if mode==",vcv,":
            property_flowrate_UA=Label(window, text="Flowrate UL", bg="black", fg="white",font=("montserrat",18,"normal"))
            unit_flowrate_left_UA=Label(window, text="Lpm", bg="black", fg="white",font=("montserrat light",9,"normal"))
            property_flowrate_UA.place(x=line_1_x+x_increment_UL,y=line_1_y+line*y_increment)
            unit_flowrate_left_UA.place(x=line_1_x+x_increment_UL,y=line_1_y+line*y_increment+y_unit_increment)
            scale_alarm_flowrate_UA.place(x=line_1_x+x_increment_UL+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
            alarm_scale_flowrate_value_UA=Label(window, text=flowrate_UA, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
            flowrate_scale_unit_label_UA=Label(window, text="Lpm", bg="black", fg="white",font=("montserrat light",9,"normal"))
            scale_value_flowrate_entered_location_x_UA=line_1_x+x_increment_UL+x_display_increment
            scale_value_flowrate_entered_location_y_UA=line_1_y+line*y_increment+y_display_increment
            alarm_scale_flowrate_value_UA.place(x=scale_value_flowrate_entered_location_x_UA,y=scale_value_flowrate_entered_location_y_UA, anchor = CENTER)
            flowrate_scale_unit_label_UA.place(x=line_1_x+x_increment_UL+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)
            # line_no=2
            # line=line_no-1
            property_flowrate_LA=Label(window, text="Flowrate LL", bg="black", fg="white",font=("montserrat",18,"normal"))
            unit_flowrate_left_LA=Label(window, text="Lpm", bg="black", fg="white",font=("montserrat light",9,"normal"))
            property_flowrate_LA.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
            unit_flowrate_left_LA.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
            scale_alarm_flowrate_LA.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
            alarm_scale_flowrate_value_LA=Label(window, text=flowrate_LA, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
            flowrate_scale_unit_label_LA=Label(window, text="Lpm", bg="black", fg="white",font=("montserrat light",9,"normal"))
            scale_value_flowrate_entered_location_x_LA=line_1_x+x_increment+x_display_increment
            scale_value_flowrate_entered_location_y_LA=line_1_y+line*y_increment+y_display_increment
            alarm_scale_flowrate_value_LA.place(x=scale_value_flowrate_entered_location_x_LA,y=scale_value_flowrate_entered_location_y_LA, anchor = CENTER)
            flowrate_scale_unit_label_LA.place(x=line_1_x+x_increment+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)
        global peep_UA
        global peep_LA
        global scale_value_peep_entered_location_x
        global scale_value_peep_entered_location_y
        line_no=2
        line=line_no-1
        property_peep_UA=Label(window, text="PEEP UL", bg="black", fg="white",font=("montserrat",18,"normal"))
        unit_peep_UA=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
        property_peep_UA.place(x=line_1_x+x_increment_UL,y=line_1_y+line*y_increment)
        unit_peep_UA.place(x=line_1_x+x_increment_UL,y=line_1_y+line*y_increment+y_unit_increment)
        scale_alarm_peep_UA.place(x=line_1_x+x_increment_UL+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
        alarm_scale_peep_value_UA=Label(window, text=peep_UA, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        peep_scale_unit_label_UA=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_value_peep_entered_location_x_UA=line_1_x+x_increment_UL+x_display_increment
        scale_value_peep_entered_location_y_UA=line_1_y+line*y_increment+y_display_increment
        alarm_scale_peep_value_UA.place(x=scale_value_peep_entered_location_x_UA,y=scale_value_peep_entered_location_y_UA, anchor = CENTER)
        peep_scale_unit_label_UA.place(x=line_1_x+x_increment_UL+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)
        # line_no=4
        # line=line_no-1
        property_peep_LA=Label(window, text="PEEP LL ", bg="black", fg="white",font=("montserrat",18,"normal"))
        unit_peep_LA=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
        property_peep_LA.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        unit_peep_LA.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
        scale_alarm_peep_LA.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
        alarm_scale_peep_value_LA=Label(window, text=peep_LA, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        peep_scale_unit_label_LA=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_value_peep_entered_location_x_LA=line_1_x+x_increment+x_display_increment
        scale_value_peep_entered_location_y_LA=line_1_y+line*y_increment+y_display_increment
        alarm_scale_peep_value_LA.place(x=scale_value_peep_entered_location_x_LA,y=scale_value_peep_entered_location_y_LA, anchor = CENTER)
        peep_scale_unit_label_LA.place(x=line_1_x+x_increment+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)
        global bpm_UA
        global bpm_LA
        global scale_value_bpm_entered_location_x
        global scale_value_bpm_entered_location_y
        line_no=3
        line=line_no-1
        property_bpm_UA=Label(window, text="BPM UL", bg="black", fg="white",font=("montserrat",18,"normal"))
        property_bpm_UA.place(x=line_1_x+x_increment_UL,y=line_1_y+line*y_increment)
        scale_alarm_bpm_UA.place(x=line_1_x+x_increment_UL+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
        alarm_scale_bpm_value_UA=Label(window, text=bpm_UA, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        scale_value_bpm_entered_location_x_UA=line_1_x+x_increment_UL+x_display_increment
        scale_value_bpm_entered_location_y_UA=line_1_y+line*y_increment+y_display_increment
        alarm_scale_bpm_value_UA.place(x=scale_value_bpm_entered_location_x_UA,y=scale_value_bpm_entered_location_y_UA, anchor = CENTER)
        # line_no=6
        # line=line_no-1
        property_bpm_LA=Label(window, text="BPM LL", bg="black", fg="white",font=("montserrat",18,"normal"))
        property_bpm_LA.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        scale_alarm_bpm_LA.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
        alarm_scale_bpm_value_LA=Label(window, text=bpm_LA, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        scale_value_bpm_entered_location_x_LA=line_1_x+x_increment+x_display_increment
        scale_value_bpm_entered_location_y_LA=line_1_y+line*y_increment+y_display_increment
        alarm_scale_bpm_value_LA.place(x=scale_value_bpm_entered_location_x_LA,y=scale_value_bpm_entered_location_y_LA, anchor = CENTER)
        global oxygen_UA
        global oxygen_LA
        global scale_value_oxygen_entered_location_x
        global scale_value_oxygen_entered_location_y
        line_no=4
        line=line_no-1
        property_oxygen_UA=Label(window, text="FiO2 UL", bg="black", fg="white",font=("montserrat",18,"normal"))
        unit_oxygen_left_UA=Label(window, text="%", bg="black", fg="white",font=("montserrat light",9,"normal"))
        property_oxygen_UA.place(x=line_1_x+x_increment_UL,y=line_1_y+line*y_increment)
        unit_oxygen_left_UA.place(x=line_1_x+x_increment_UL,y=line_1_y+line*y_increment+y_unit_increment)
        scale_alarm_oxygen_UA.place(x=line_1_x+x_increment_UL+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
        alarm_scale_oxygen_value_UA=Label(window, text=oxygen_UA, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        oxygen_scale_unit_label_UA=Label(window, text="%", bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_value_oxygen_entered_location_x_UA=line_1_x+x_increment_UL+x_display_increment
        scale_value_oxygen_entered_location_y_UA=line_1_y+line*y_increment+y_display_increment
        alarm_scale_oxygen_value_UA.place(x=scale_value_oxygen_entered_location_x_UA,y=scale_value_oxygen_entered_location_y_UA, anchor = CENTER)
        oxygen_scale_unit_label_UA.place(x=line_1_x+x_increment_UL+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)
        # line_no=8
        # line=line_no-1
        property_oxygen_LA=Label(window, text="FiO2 LL", bg="black", fg="white",font=("montserrat",18,"normal"))
        unit_oxygen_left_LA=Label(window, text="%", bg="black", fg="white",font=("montserrat light",9,"normal"))
        property_oxygen_LA.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        unit_oxygen_left_LA.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
        scale_alarm_oxygen_LA.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
        alarm_scale_oxygen_value_LA=Label(window, text=oxygen_LA, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        oxygen_scale_unit_label_LA=Label(window, text="%", bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_value_oxygen_entered_location_x_LA=line_1_x+x_increment+x_display_increment
        scale_value_oxygen_entered_location_y_LA=line_1_y+line*y_increment+y_display_increment
        alarm_scale_oxygen_value_LA.place(x=scale_value_oxygen_entered_location_x_LA,y=scale_value_oxygen_entered_location_y_LA, anchor = CENTER)
        oxygen_scale_unit_label_LA.place(x=line_1_x+x_increment+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)
        global vol_UA
        global vol_LA
        global scale_value_vol_entered_location_x
        global scale_value_vol_entered_location_y
        if mode==",vcv,":
            line_no=5
            line=line_no-1
            property_vol_UA=Label(window, text="Volume UL", bg="black", fg="white",font=("montserrat",18,"normal"))
            unit_vol_left_UA=Label(window, text="mL", bg="black", fg="white",font=("montserrat light",9,"normal"))
            property_vol_UA.place(x=line_1_x+x_increment_UL,y=line_1_y+line*y_increment)
            unit_vol_left_UA.place(x=line_1_x+x_increment_UL,y=line_1_y+line*y_increment+y_unit_increment)
            scale_alarm_vol_UA.place(x=line_1_x+x_increment_UL+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
            alarm_scale_vol_value_UA=Label(window, text=vol_UA, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
            vol_scale_unit_label_UA=Label(window, text="mL", bg="black", fg="white",font=("montserrat light",9,"normal"))
            scale_value_vol_entered_location_x_UA=line_1_x+x_increment_UL+x_display_increment
            scale_value_vol_entered_location_y_UA=line_1_y+line*y_increment+y_display_increment
            alarm_scale_vol_value_UA.place(x=scale_value_vol_entered_location_x_UA,y=scale_value_vol_entered_location_y_UA, anchor = CENTER)
            vol_scale_unit_label_UA.place(x=line_1_x+x_increment_UL+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)
            # line_no=10
            # line=line_no-1
            property_vol_LA=Label(window, text="Volume LL", bg="black", fg="white",font=("montserrat",18,"normal"))
            unit_vol_left_LA=Label(window, text="mL", bg="black", fg="white",font=("montserrat light",9,"normal"))
            property_vol_LA.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
            unit_vol_left_LA.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
            scale_alarm_vol_LA.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
            alarm_scale_vol_value_LA=Label(window, text=vol_LA, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
            vol_scale_unit_label_LA=Label(window, text="mL", bg="black", fg="white",font=("montserrat light",9,"normal"))
            scale_value_vol_entered_location_x_LA=line_1_x+x_increment+x_display_increment
            scale_value_vol_entered_location_y_LA=line_1_y+line*y_increment+y_display_increment
            alarm_scale_vol_value_LA.place(x=scale_value_vol_entered_location_x_LA,y=scale_value_vol_entered_location_y_LA, anchor = CENTER)
            vol_scale_unit_label_LA.place(x=line_1_x+x_increment_UL+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)
    def hide_alarm_scales():
        global property_p_insp_UA
        global unit_p_insp_left_UA
        global property_p_insp_LA
        global unit_p_insp_left_LA
        global scale_alarm_pressure_UA
        global scale_alarm_pressure_LA
        global alarm_scale_pressure_value_UA
        global alarm_scale_pressure_value_LA
        global p_scale_unit_label_UA
        global p_scale_unit_label_LA
        global property_flowrate_UA
        global unit_flowrate_left_UA
        global property_flowrate_LA
        global unit_flowrate_left_LA
        global scale_alarm_flowrate_UA
        global scale_alarm_flowrate_LA
        global alarm_scale_flowrate_value_UA
        global alarm_scale_flowrate_value_LA
        global flowrate_scale_unit_label_UA
        global flowrate_scale_unit_label_LA
        global property_peep_UA
        global unit_peep_UA
        global property_peep_LA
        global unit_peep_LA
        global scale_alarm_peep_UA
        global scale_alarm_peep_LA
        global alarm_scale_peep_value_UA
        global alarm_scale_peep_value_LA
        global peep_scale_unit_label_UA
        global peep_scale_unit_label_LA
        global property_bpm_UA
        global property_bpm_LA
        global scale_alarm_bpm_UA
        global scale_alarm_bpm_LA
        global alarm_scale_bpm_value_UA
        global alarm_scale_bpm_value_LA
        global property_vol_UA
        global unit_vol_left_UA
        global property_vol_LA
        global unit_vol_left_LA
        global scale_alarm_vol_UA
        global scale_alarm_vol_LA
        global alarm_scale_vol_value_UA
        global alarm_scale_vol_value_LA
        global vol_scale_unit_label_UA
        global vol_scale_unit_label_LA
        global property_oxygen_UA
        global unit_oxygen_left_UA
        global property_oxygen_LA
        global unit_oxygen_left_LA
        global scale_alarm_oxygen_UA
        global scale_alarm_oxygen_LA
        global alarm_scale_oxygen_value_UA
        global alarm_scale_oxygen_value_LA
        global oxygen_scale_unit_label_UA
        global oxygen_scale_unit_label_LA
        if mode==",pcv,":
            property_p_insp_UA.place_forget()
            unit_p_insp_left_UA.place_forget()
            property_p_insp_LA.place_forget()
            unit_p_insp_left_LA.place_forget()
            scale_alarm_pressure_UA.place_forget()
            scale_alarm_pressure_LA.place_forget()
            alarm_scale_pressure_value_UA.place_forget()
            alarm_scale_pressure_value_LA.place_forget()
            p_scale_unit_label_UA.place_forget()
            p_scale_unit_label_LA.place_forget()
        if mode==",vcv,":
            property_flowrate_UA.place_forget()
            unit_flowrate_left_UA.place_forget()
            property_flowrate_LA.place_forget()
            unit_flowrate_left_LA.place_forget()
            scale_alarm_flowrate_UA.place_forget()
            scale_alarm_flowrate_LA.place_forget()
            alarm_scale_flowrate_value_UA.place_forget()
            alarm_scale_flowrate_value_LA.place_forget()
            flowrate_scale_unit_label_UA.place_forget()
            flowrate_scale_unit_label_LA.place_forget()
        property_peep_UA.place_forget()
        unit_peep_UA.place_forget()
        property_peep_LA.place_forget()
        unit_peep_LA.place_forget()
        scale_alarm_peep_UA.place_forget()
        scale_alarm_peep_LA.place_forget()
        alarm_scale_peep_value_UA.place_forget()
        alarm_scale_peep_value_LA.place_forget()
        peep_scale_unit_label_UA.place_forget()
        peep_scale_unit_label_LA.place_forget()
        property_bpm_UA.place_forget()
        property_bpm_LA.place_forget()
        scale_alarm_bpm_UA.place_forget()
        scale_alarm_bpm_LA.place_forget()
        alarm_scale_bpm_value_UA.place_forget()
        alarm_scale_bpm_value_LA.place_forget()
        if mode==",vcv,":
            property_vol_UA.place_forget()
            unit_vol_left_UA.place_forget()
            property_vol_LA.place_forget()
            unit_vol_left_LA.place_forget()
            scale_alarm_vol_UA.place_forget()
            scale_alarm_vol_LA.place_forget()
            alarm_scale_vol_value_UA.place_forget()
            alarm_scale_vol_value_LA.place_forget()
            vol_scale_unit_label_UA.place_forget()
            vol_scale_unit_label_LA.place_forget()
        property_oxygen_UA.place_forget()
        unit_oxygen_left_UA.place_forget()
        property_oxygen_LA.place_forget()
        unit_oxygen_left_LA.place_forget()
        scale_alarm_oxygen_UA.place_forget()
        scale_alarm_oxygen_LA.place_forget()
        alarm_scale_oxygen_value_UA.place_forget()
        alarm_scale_oxygen_value_LA.place_forget()
        oxygen_scale_unit_label_UA.place_forget()
        oxygen_scale_unit_label_LA.place_forget()

    def stop_updating_alarms_mid_ventilation():

        global alarm_updates_button_mid_ventilation
        alarm_updates_button_mid_ventilation.place(x=1420,y=750)
        global alarm_stop_updating_button_mid_ventilation
        alarm_stop_updating_button_mid_ventilation.place_forget()
        ventilation_inputs.place_my_inputs()
        ventilation_inputs.place_user_entered_buttons()
        monitoring.start_monitoring()
        alarm_scales.hide_alarm_scales()
    global alarm_stop_updating_button_mid_ventilation
    alarm_stop_updating=PhotoImage(file="alarms_green.gif")
    alarm_stop_updating_button_mid_ventilation=Button(window, image=alarm_stop_updating, highlightthickness=0,bd=0,bg="white",command=stop_updating_alarms_mid_ventilation)

    def update_alarms_mid_ventilation():
        global cmv_blank_image_button
        global cmv_green_image_button
        global acv_blank_image_button
        global acv_green_image_button
        global simv_blank_image_button
        global simv_green_image_button
        global cpap_blank_image_button
        global cpap_green_image_button
        global pcv_blank_image_button
        global pcv_green_image_button
        global vcv_blank_image_button
        global vcv_green_image_button
        global Pressure_triggered_blank_image_button
        global Pressure_triggered_green_image_button
        global Flow_triggered_blank_image_button
        global Flow_triggered_green_image_button
        global user_entered_values_image_label
        cmv_blank_image_button.place_forget()
        cmv_green_image_button.place_forget()
        acv_blank_image_button.place_forget()
        acv_green_image_button.place_forget()
        simv_blank_image_button.place_forget()
        simv_green_image_button.place_forget()
        cpap_blank_image_button.place_forget()
        cpap_green_image_button.place_forget()
        pcv_blank_image_button.place_forget()
        pcv_green_image_button.place_forget()
        vcv_blank_image_button.place_forget()
        vcv_green_image_button.place_forget()
        Pressure_triggered_blank_image_button.place_forget()
        Pressure_triggered_green_image_button.place_forget()
        Flow_triggered_blank_image_button.place_forget()
        Flow_triggered_green_image_button.place_forget()
        user_entered_values_image_label.place_forget()
        global alarm_stop_updating_button_mid_ventilation
        alarm_stop_updating_button_mid_ventilation.place(x=1420,y=750)
        global alarm_updates_button_mid_ventilation
        alarm_updates_button_mid_ventilation.place_forget()
        monitoring.graphs.hide_graphs()
        ventilation_inputs.hide_user_entered_buttons()
        monitoring.stop_monitoring()
        ventilation_inputs.hide_my_inputs()
        ventilation_inputs.hide_scale_and_buttons()
        alarm_scales.place_alarm_scales()

    def stop_updating_alarms_mid_startup():
        global alarm_updates_button_mid_startup
        alarm_updates_button_mid_startup.place(x=1420,y=750)
        global alarm_stop_updating_button_mid_startup
        alarm_stop_updating_button_mid_startup.place_forget()
        startup_inputs.startup_protocol()
        # ventilation_inputs.place_my_inputs()
        # ventilation_inputs.place_user_entered_buttons()
        # monitoring.start_monitoring()
        alarm_scales.hide_alarm_scales()
    global alarm_stop_updating_button_mid_startup
    alarm_stop_updating_mid_startup=PhotoImage(file="alarms_green.gif")
    alarm_stop_updating_button_mid_startup=Button(window, image=alarm_stop_updating_mid_startup, highlightthickness=0,bd=0,bg="white",command=stop_updating_alarms_mid_startup)

    def update_alarms_mid_startup():
        global blank_image_button
        global cmv_green_image_button
        global acv_blank_image_button
        global acv_green_image_button
        global simv_blank_image_button
        global simv_green_image_button
        global cpap_blank_image_button
        global cpap_green_image_button
        global pcv_blank_image_button
        global pcv_green_image_button
        global vcv_blank_image_button
        global vcv_green_image_button
        global Pressure_triggered_blank_image_button
        global Pressure_triggered_green_image_button
        global Flow_triggered_blank_image_button
        global Flow_triggered_green_image_button
        global user_entered_values_image_label
        cmv_blank_image_button.place_forget()
        cmv_green_image_button.place_forget()
        acv_blank_image_button.place_forget()
        acv_green_image_button.place_forget()
        simv_blank_image_button.place_forget()
        simv_green_image_button.place_forget()
        cpap_blank_image_button.place_forget()
        cpap_green_image_button.place_forget()
        pcv_blank_image_button.place_forget()
        pcv_green_image_button.place_forget()
        vcv_blank_image_button.place_forget()
        vcv_green_image_button.place_forget()
        Pressure_triggered_blank_image_button.place_forget()
        Pressure_triggered_green_image_button.place_forget()
        Flow_triggered_blank_image_button.place_forget()
        Flow_triggered_green_image_button.place_forget()
        user_entered_values_image_label.place_forget()
        global alarm_stop_updating_button_mid_startup
        alarm_stop_updating_button_mid_startup.place(x=1420,y=750)
        global alarm_updates_button_mid_startup
        alarm_updates_button_mid_startup.place_forget()
        startup_inputs.hide_everything_in_startup()
        # monitoring.graphs.hide_graphs()
        # ventilation_inputs.hide_user_entered_buttons()
        # monitoring.stop_monitoring()
        # ventilation_inputs.hide_my_inputs()
        # ventilation_inputs.hide_scale_and_buttons()
        alarm_scales.place_alarm_scales()

"""CLASS: ALARM/END"""
class ventilation_inputs():
    global scale_value
    global scale_label
    global scale_unit_label
    scale_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
    scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
    scale_unit_label=Label(window, text=unit_of_property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
    global CustomScale
    class CustomScale(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = '{}.custom.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global scale_value
            global scale_label
            global property_being_updated
            global value_pressure_entered
            global value_flowrate_entered
            global value_vol_entered
            global value_bpm_entered
            global value_peep_entered
            global value_oxygen_entered
            global value_insp_time_entered
            global value_ie_entered
            global value_triggering_flow_entered
            global value_triggering_pressure_entered
            global packed_pressure
            global packed_flowrate
            global packed_peep
            global packed_bpm
            global packed_vol
            global packed_oxygen
            global packed_insp_time
            global packed_ie
            global packed_triggering_flow
            global packed_triggering_pressure
            scale_value.place_forget()
            scale_label.place_forget()
            if property_being_updated=="Pressure":
                value_pressure_entered=format(int(self.variable.get()))
                packed_pressure="p"+","+str(value_pressure_entered)+","
            if property_being_updated=="Flowrate":
                value_flowrate_entered=format(int(self.variable.get()))
                packed_flowrate="q"+","+str(value_flowrate_entered)+","
            if property_being_updated=="Tidal Volume":
                value_vol_entered=format(int(self.variable.get()))
                packed_vol="v"+","+str(value_vol_entered)+","
            if property_being_updated=="BPM":
                value_bpm_entered=format(int(self.variable.get()))
                packed_bpm="b"+","+str(value_bpm_entered)+","
            if property_being_updated=="PEEP":
                value_peep_entered=format(int(self.variable.get()))
                packed_peep="pp"+","+str(value_peep_entered)+","
            if property_being_updated=="Oxygen":
                value_oxygen_entered=format(int(self.variable.get()))
                packed_oxygen="O"+","+str(value_oxygen_entered)+","
            if property_being_updated=="insp_time":
                value_insp_time_entered="{:.1f}".format(self.variable.get())
                packed_insp_time="it"+","+str(value_insp_time_entered)+","
            if property_being_updated=="ie":
                value_ie_entered=format(int(self.variable.get()))
                packed_ie="ie"+","+"1:"+str(value_ie_entered)+","
            if property_being_updated=="Triggering flow":
                value_triggering_flow_entered=format(int(self.variable.get()))
                packed_triggering_flow="tf"+","+str(value_triggering_flow_entered)+","
            if property_being_updated=="Triggering pressure":
                value_triggering_pressure_entered=format(int(self.variable.get()))
                packed_triggering_pressure="tp"+","+str(value_triggering_pressure_entered)+","
            if property_being_updated=="ie":
                scale_value=Label(window, text="1:"+str(int(self.variable.get())), bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
                scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
            if property_being_updated=="insp_time":
                scale_value=Label(window, text="{:.1f}".format(self.variable.get()), bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
                scale_label=Label(window, text=property_being_updated, bg="black ", fg="white",font=("montserrat light",12,"normal"))
            if property_being_updated != "ie" and property_being_updated != "insp_time":
                scale_value=Label(window, text=str(int(self.variable.get())), bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
                scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
            if scaling=="yes":
                scale_value.place(x=scale_value_location_x,y=scale_value_location_y, anchor = CENTER)
                scale_label.place(x=scale_label_location_x,y=scale_label_location_y, anchor = CENTER)
            #style.configure(self._style_name, font=("montserrat semi bold",8), text="{:.1f}".format(int(self.variable.get())))

    def create_ventilation_bar_and_slider():
        global img_trough_ventilation
        global img_slider_ventilation
        img_trough_ventilation = PhotoImage(file="bar.gif")
        img_slider = PhotoImage(file="slider.gif")
    create_ventilation_bar_and_slider()

    def create_style_for_ventilation():
        global img_trough_ventilation
        global img_slider_ventilation
        img_trough_ventilation = PhotoImage(file="bar.gif")
        img_slider_ventilation = PhotoImage(file="slider.gif")
        # create scale elements
        string_ventilation_trough='.custom.Horizontal.Scale.trough'
        string_ventilation_slider='.custom.Horizontal.Scale.slider'
        style.element_create(string_ventilation_trough, 'image', img_trough_ventilation)
        style.element_create(string_ventilation_slider, 'image', img_slider_ventilation)
        # create custom layout
        style.layout('custom.Horizontal.TScale',[(string_ventilation_trough, {'sticky': 'ns'}),
                    (string_ventilation_slider, {'side': 'left', 'sticky': '','children': [('custom.Horizontal.Scale.label', {'sticky': ''})]})])
    create_style_for_ventilation()

    def create_ventilation_scales():
        global CustomScale
        global scale_vol
        global scale_pressure
        global scale_flowrate
        global scale_bpm
        global scale_peep
        global scale_oxygen
        global scale_insp_time
        global scale_ie
        global scale_flow_trigger
        global scale_pressure_trigger
        scale_vol= CustomScale(window, from_=LL_vol, to=UL_vol)
        scale_pressure = CustomScale(window, from_=LL_pressure, to=UL_pressure)
        scale_flowrate = CustomScale(window, from_=LL_flowrate, to=UL_flowrate)
        scale_bpm = CustomScale(window, from_=LL_bpm, to=UL_bpm)
        scale_peep = CustomScale(window, from_=LL_peep, to=UL_peep)
        scale_oxygen = CustomScale(window, from_=LL_oxygen, to=UL_oxygen)
        scale_insp_time = CustomScale(window, from_=LL_insp_time, to=UL_insp_time)
        scale_ie = CustomScale(window, from_=LL_ie, to=UL_ie)
        scale_flow_trigger = CustomScale(window, from_=LL_triggering_flow, to=UL_triggering_flow)
        scale_pressure_trigger = CustomScale(window, from_=LL_triggering_pressure, to=UL_triggering_pressure)
    create_ventilation_scales()
    global y_increment_update_buttons_block
    global scale_location_x
    global scale_location_y
    global unit_increment_y
    global value_increment_y
    global scale_label_location_x
    global scale_label_location_y
    global scale_value_location_x
    global scale_value_location_y
    global scale_value_unit_location_x
    global scale_value_unit_location_y
    global cross_location_x
    global cross_location_y
    global tick_location_x
    global tick_location_y
    y_increment_bottom_scale_block=600
    scale_location_x=365
    scale_location_y=28+y_increment_bottom_scale_block
    unit_increment_y=33
    value_increment_y=30
    scale_label_location_x=750
    scale_label_location_y=99+y_increment_bottom_scale_block
    scale_value_location_x=752
    scale_value_location_y=scale_label_location_y+value_increment_y
    scale_value_unit_location_x=750
    scale_value_unit_location_y=scale_value_location_y+unit_increment_y
    cross_location_x=300
    cross_location_y=30+y_increment_bottom_scale_block
    tick_location_x=cross_location_x+870 #950+220
    tick_location_y=cross_location_y

    def update_pressure():
        ventilation_inputs.hide_user_entered_buttons()
        global cross_button
        global tick_button
        global scaling
        global property_being_updated
        global value_pressure_entered
        global scale_value
        global scale_label
        global scale_unit_label
        cross_button.place(x=cross_location_x,y=cross_location_y)
        tick_button.place(x=tick_location_x,y=tick_location_y)
        property_being_updated="Pressure"
        unit_of_property_being_updated="cmH20"
        scaling="yes"
        scale_value=Label(window, text=value_pressure_entered, bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
        scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
        scale_unit_label=Label(window, text=unit_of_property_being_updated, bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_pressure.place(x=scale_location_x,y=scale_location_y)
        scale_pressure.set(value_pressure_entered)
        scale_value.place(x=scale_value_location_x,y=scale_value_location_y, anchor = CENTER)
        scale_label.place(x=scale_label_location_x,y=scale_label_location_y, anchor = CENTER)
        scale_unit_label.place(x=scale_value_unit_location_x,y=scale_value_unit_location_y, anchor = CENTER)

    def update_flowrate():
        ventilation_inputs.hide_user_entered_buttons()
        global cross_button
        global tick_button
        global scaling
        global property_being_updated
        global value_flowrate_entered
        global scale_value
        global scale_label
        global scale_unit_label
        cross_button.place(x=cross_location_x,y=cross_location_y)
        tick_button.place(x=tick_location_x,y=tick_location_y)
        property_being_updated="Flowrate"
        unit_of_property_being_updated="Lpm"
        scaling="yes"
        scale_value=Label(window, text=value_flowrate_entered, bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
        scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
        scale_unit_label=Label(window, text=unit_of_property_being_updated, bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_flowrate.place(x=scale_location_x,y=scale_location_y)
        scale_flowrate.set(value_flowrate_entered)
        scale_value.place(x=scale_value_location_x,y=scale_value_location_y, anchor = CENTER)
        scale_label.place(x=scale_label_location_x,y=scale_label_location_y, anchor = CENTER)
        scale_unit_label.place(x=scale_value_unit_location_x,y=scale_value_unit_location_y, anchor = CENTER)

    def update_peep():
        ventilation_inputs.hide_user_entered_buttons()
        global scaling
        global property_being_updated
        global value_peep_entered
        global scale_value
        global scale_label
        global scale_unit_label
        cross_button.place(x=cross_location_x,y=cross_location_y)
        tick_button.place(x=tick_location_x,y=tick_location_y)
        property_being_updated="PEEP"
        unit_of_property_being_updated="cmH20"
        scaling="yes"
        scale_value=Label(window, text=value_peep_entered, bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
        scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
        scale_unit_label=Label(window, text=unit_of_property_being_updated, bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_peep.place(x=scale_location_x,y=scale_location_y)
        scale_peep.set(value_peep_entered)
        scale_value.place(x=scale_value_location_x,y=scale_value_location_y, anchor = CENTER)
        scale_label.place(x=scale_label_location_x,y=scale_label_location_y, anchor = CENTER)
        scale_unit_label.place(x=scale_value_unit_location_x,y=scale_value_unit_location_y, anchor = CENTER)

    def update_bpm():
        ventilation_inputs.hide_user_entered_buttons()
        global scaling
        global property_being_updated
        global value_bpm_entered
        global scale_value
        global scale_label
        global scale_unit_label
        cross_button.place(x=cross_location_x,y=cross_location_y)
        tick_button.place(x=tick_location_x,y=tick_location_y)
        property_being_updated="BPM"
        unit_of_property_being_updated=""
        scaling="yes"
        scale_value=Label(window, text=value_bpm_entered, bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
        scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
        scale_unit_label=Label(window, text=unit_of_property_being_updated, bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_bpm.place(x=scale_location_x,y=scale_location_y)
        scale_bpm.set(value_bpm_entered)
        scale_value.place(x=scale_value_location_x,y=scale_value_location_y, anchor = CENTER)
        scale_label.place(x=scale_label_location_x,y=scale_label_location_y, anchor = CENTER)
        scale_unit_label.place(x=scale_value_unit_location_x,y=scale_value_unit_location_y, anchor = CENTER)

    def update_volume():
        ventilation_inputs.hide_user_entered_buttons()
        global cross_button
        global tick_button
        global scaling
        global property_being_updated
        global value_vol_entered
        global scale_value
        global scale_label
        global scale_unit_label
        cross_button.place(x=cross_location_x,y=cross_location_y)
        tick_button.place(x=tick_location_x,y=tick_location_y)
        property_being_updated="Tidal Volume"
        unit_of_property_being_updated="mL"
        scaling="yes"
        scale_value=Label(window, text=value_vol_entered, bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
        scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
        scale_unit_label=Label(window, text=unit_of_property_being_updated, bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_vol.place(x=scale_location_x,y=scale_location_y)
        scale_vol.set(value_vol_entered)
        scale_value.place(x=scale_value_location_x,y=scale_value_location_y, anchor = CENTER)
        scale_label.place(x=scale_label_location_x,y=scale_label_location_y, anchor = CENTER)
        scale_unit_label.place(x=scale_value_unit_location_x,y=scale_value_unit_location_y, anchor = CENTER)

    def update_oxygen():
        ventilation_inputs.hide_user_entered_buttons()
        global cross_button
        global tick_button
        global scaling
        global property_being_updated
        global value_oxygen_entered
        global scale_value
        global scale_label
        global scale_unit_label
        cross_button.place(x=cross_location_x,y=cross_location_y)
        tick_button.place(x=tick_location_x,y=tick_location_y)
        property_being_updated="Oxygen"
        unit_of_property_being_updated="%"
        scaling="yes"
        scale_value=Label(window, text=value_oxygen_entered, bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
        scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
        scale_unit_label=Label(window, text=unit_of_property_being_updated, bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_oxygen.place(x=scale_location_x,y=scale_location_y)
        scale_oxygen.set(value_oxygen_entered)
        scale_value.place(x=scale_value_location_x,y=scale_value_location_y, anchor = CENTER)
        scale_label.place(x=scale_label_location_x,y=scale_label_location_y, anchor = CENTER)
        scale_unit_label.place(x=scale_value_unit_location_x,y=scale_value_unit_location_y, anchor = CENTER)

    def update_insp_time():
        ventilation_inputs.hide_user_entered_buttons()
        global cross_button
        global tick_button
        global scaling
        global property_being_updated
        global value_insp_time_entered
        global scale_value
        global scale_label
        global scale_unit_label
        cross_button.place(x=cross_location_x,y=cross_location_y)
        tick_button.place(x=tick_location_x,y=tick_location_y)
        property_being_updated="insp_time"
        unit_of_property_being_updated="%"
        scaling="yes"
        scale_value=Label(window, text=value_insp_time_entered, bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
        scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
        scale_unit_label=Label(window, text=unit_of_property_being_updated, bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_insp_time.place(x=scale_location_x,y=scale_location_y)
        scale_insp_time.set(value_insp_time_entered)
        scale_value.place(x=scale_value_location_x,y=scale_value_location_y, anchor = CENTER)
        scale_label.place(x=scale_label_location_x,y=scale_label_location_y, anchor = CENTER)
        scale_unit_label.place(x=scale_value_unit_location_x,y=scale_value_unit_location_y, anchor = CENTER)

    def update_ie():
        ventilation_inputs.hide_user_entered_buttons()
        global cross_button
        global tick_button
        global scaling
        global property_being_updated
        global value_insp_time_entered
        global scale_value
        global scale_label
        cross_button.place(x=cross_location_x,y=cross_location_y)
        tick_button.place(x=tick_location_x,y=tick_location_y)
        property_being_updated="ie"
        scaling="yes"
        scale_value=Label(window, text="1:"+str(value_ie_entered), bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
        scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
        scale_ie.place(x=scale_location_x,y=scale_location_y)
        scale_ie.set(value_ie_entered)
        scale_value.place(x=scale_value_location_x,y=scale_value_location_y, anchor = CENTER)
        scale_label.place(x=scale_label_location_x,y=scale_label_location_y, anchor = CENTER)

    def update_triggering_flow():
        ventilation_inputs.hide_user_entered_buttons()
        global scaling
        global property_being_updated
        global value_vol_entered
        global scale_value
        global scale_label
        global scale_unit_label
        cross_button.place(x=cross_location_x,y=cross_location_y)
        tick_button.place(x=tick_location_x,y=tick_location_y)
        property_being_updated="Triggering flow"
        unit_of_property_being_updated="Lpm"
        scaling="yes"
        scale_value=Label(window, text=value_triggering_flow_entered, bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
        scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
        scale_unit_label=Label(window, text=unit_of_property_being_updated, bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_flow_trigger.place(x=scale_location_x,y=scale_location_y)
        scale_flow_trigger.set(value_triggering_flow_entered)
        scale_value.place(x=scale_value_location_x,y=scale_value_location_y, anchor = CENTER)
        scale_label.place(x=scale_label_location_x,y=scale_label_location_y, anchor = CENTER)
        scale_unit_label.place(x=scale_value_unit_location_x,y=scale_value_unit_location_y, anchor = CENTER)

    def update_triggering_pressure():
        ventilation_inputs.hide_user_entered_buttons()
        global scaling
        global property_being_updated
        global value_vol_entered
        global scale_value
        global scale_label
        global scale_unit_label
        cross_button.place(x=cross_location_x,y=cross_location_y)
        tick_button.place(x=tick_location_x,y=tick_location_y)
        property_being_updated="Triggering pressure"
        unit_of_property_being_updated="cmH20"
        scaling="yes"
        scale_value=Label(window, text=value_triggering_pressure_entered, bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
        scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
        scale_unit_label=Label(window, text=unit_of_property_being_updated, bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_pressure_trigger.place(x=scale_location_x,y=scale_location_y)
        scale_pressure_trigger.set(value_triggering_pressure_entered)
        scale_value.place(x=scale_value_location_x,y=scale_value_location_y, anchor = CENTER)
        scale_label.place(x=scale_label_location_x,y=scale_label_location_y, anchor = CENTER)
        scale_unit_label.place(x=scale_value_unit_location_x,y=scale_value_unit_location_y, anchor = CENTER)

    def update_pplat():
        global packed_manoeuvre
        packed_manoeuvre="m,1,"
        send_data_to_arduino()
    global update_pressure_button
    global update_flowrate_button
    global update_peep_button
    global update_bpm_button
    global update_vol_button
    global update_oxygen_button
    global update_insp_time_button
    global update_ie_button
    global update_triggering_flow_button
    global update_triggering_pressure_button
    global inspiratory_pause_manoeuvre_button
    update_pressure_button_image=PhotoImage(file="update_p.gif")
    update_pressure_button=Button(window, image=update_pressure_button_image, highlightthickness=0,bd=0,bg="white",command=update_pressure)
    update_flowrate_button_image=PhotoImage(file="update_insp_flow.gif")
    update_flowrate_button=Button(window, image=update_flowrate_button_image, highlightthickness=0,bd=0,bg="white",command=update_flowrate)
    update_peep_button_image=PhotoImage(file="update_peep.gif")
    update_peep_button=Button(window, image=update_peep_button_image, highlightthickness=0,bd=0,bg="white",command=update_peep)
    update_bpm_button_image=PhotoImage(file="update_bpm.gif")
    update_bpm_button=Button(window, image=update_bpm_button_image, highlightthickness=0,bd=0,bg="white",command=update_bpm)
    update_vol_button_image=PhotoImage(file="update_vol.gif")
    update_vol_button=Button(window, image=update_vol_button_image, highlightthickness=0,bd=0,bg="white",command=update_volume)
    update_oxygen_button_image=PhotoImage(file="update_O2.gif")
    update_oxygen_button=Button(window, image=update_oxygen_button_image, highlightthickness=0,bd=0,bg="white",command=update_oxygen)
    update_insp_time_button_image=PhotoImage(file="update insp time.gif")
    update_insp_time_button=Button(window, image=update_insp_time_button_image, highlightthickness=0,bd=0,bg="white",command=update_insp_time)
    update_ie_image=PhotoImage(file="update_IE.gif")
    update_ie_button=Button(window, image=update_ie_image, highlightthickness=0,bd=0,bg="white",command=update_ie)
    update_triggering_flow_button_image=PhotoImage(file="update trig flow.gif")
    update_triggering_flow_button=Button(window, image=update_triggering_flow_button_image, highlightthickness=0,bd=0,bg="white",command=update_triggering_flow)
    update_triggering_pressure_button_image=PhotoImage(file="update trig p.gif")
    update_triggering_pressure_button=Button(window, image=update_triggering_pressure_button_image, highlightthickness=0,bd=0,bg="white",command=update_triggering_pressure)
    inspiratory_pause_manoeuvre_button_image=PhotoImage(file="insp_pause_manoeuvre.gif")
    inspiratory_pause_manoeuvre_button=Button(window, image=inspiratory_pause_manoeuvre_button_image, highlightthickness=0,bd=0,bg="white",command=update_pplat)
    global user_entered_values_image_label
    user_entered_values_image=PhotoImage(file="user entered values label.gif")
    user_entered_values_image_label=Label (window, image=user_entered_values_image, bg="black")

    global cmv_blank_image_button
    global cmv_green_image_button
    global acv_blank_image_button
    global acv_green_image_button
    global simv_blank_image_button
    global simv_green_image_button
    global cpap_blank_image_button
    global cpap_green_image_button
    global pcv_blank_image_button
    global pcv_green_image_button
    global vcv_blank_image_button
    global vcv_green_image_button
    global Pressure_triggered_blank_image_button
    global Pressure_triggered_green_image_button
    global Flow_triggered_blank_image_button
    global Flow_triggered_green_image_button

    # BUTTONS AT THE TOP - start
    def dont_change_modes():
        print("nothing")

    def update_cmv():
        global control_mode
        control_mode = ",CMV,"
        global packed_control_mode
        packed_control_mode="cm"+control_mode
        global acv_green_image_button
        global cmv_blank_image_button
        global simv_green_image_button
        global cpap_green_image_button
        cmv_blank_image_button.place_forget()
        acv_green_image_button.place_forget()
        simv_green_image_button.place_forget()
        cpap_green_image_button.place_forget()
        x_ventilation_modes_first_line = 1180
        x_ventilation_modes_second_line = 1270
        x_ventilation_modes_third_line = 1250
        x_gap_between_buttons = 90
        y_first_line_ventilation_modes = 75
        y_distance_between_lines_ventilation_modes = 50
        cmv_green_image_button.place(x=x_ventilation_modes_first_line , y=y_first_line_ventilation_modes)
        acv_blank_image_button.place(x=x_ventilation_modes_first_line+1*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        simv_blank_image_button.place(x=x_ventilation_modes_first_line+2*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        cpap_blank_image_button.place(x=x_ventilation_modes_first_line+3*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        send_data_to_arduino()
    cmv_blank_image=PhotoImage(file="cmv_blank.gif")
    cmv_blank_image_button=Button(window, image=cmv_blank_image, highlightthickness=0,bd=0,bg="white",command=update_cmv)
    cmv_green_image=PhotoImage(file="cmv_green.gif")
    cmv_green_image_button=Button(window, image=cmv_green_image, highlightthickness=0,bd=0,bg="white",command=dont_change_modes)

    def update_acv():
        global control_mode
        control_mode = ",ACV,"
        global packed_control_mode
        packed_control_mode="cm"+control_mode
        global cmv_green_image_button
        global acv_blank_image_button
        global simv_green_image_button
        global cpap_green_image_button
        cmv_green_image_button.place_forget()
        acv_blank_image_button.place_forget()
        simv_green_image_button.place_forget()
        cpap_green_image_button.place_forget()
        x_ventilation_modes_first_line = 1180
        x_ventilation_modes_second_line = 1270
        x_ventilation_modes_third_line = 1250
        x_gap_between_buttons = 90
        y_first_line_ventilation_modes = 75
        y_distance_between_lines_ventilation_modes = 50
        cmv_blank_image_button.place(x=x_ventilation_modes_first_line , y=y_first_line_ventilation_modes)
        acv_green_image_button.place(x=x_ventilation_modes_first_line+1*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        simv_blank_image_button.place(x=x_ventilation_modes_first_line+2*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        cpap_blank_image_button.place(x=x_ventilation_modes_first_line+3*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        send_data_to_arduino()
    acv_blank_image=PhotoImage(file="acv_blank.gif")
    acv_blank_image_button=Button(window, image=acv_blank_image, highlightthickness=0,bd=0,bg="white",command=update_acv)
    acv_green_image=PhotoImage(file="acv_green.gif")
    acv_green_image_button=Button(window, image=acv_green_image, highlightthickness=0,bd=0,bg="white",command=dont_change_modes)

    def update_simv():
        global control_mode
        control_mode = ",SIMV,"
        global packed_control_mode
        packed_control_mode="cm"+control_mode
        global cmv_green_image_button
        global acv_green_image_button
        global simv_blank_image_button
        global cpap_green_image_button
        cmv_green_image_button.place_forget()
        acv_green_image_button.place_forget()
        simv_blank_image_button.place_forget()
        cpap_green_image_button.place_forget()
        x_ventilation_modes_first_line = 1180
        x_ventilation_modes_second_line = 1270
        x_ventilation_modes_third_line = 1250
        x_gap_between_buttons = 90
        y_first_line_ventilation_modes = 75
        y_distance_between_lines_ventilation_modes = 50
        cmv_blank_image_button.place(x=x_ventilation_modes_first_line , y=y_first_line_ventilation_modes)
        acv_blank_image_button.place(x=x_ventilation_modes_first_line+1*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        simv_green_image_button.place(x=x_ventilation_modes_first_line+2*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        cpap_blank_image_button.place(x=x_ventilation_modes_first_line+3*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        send_data_to_arduino()
    simv_blank_image=PhotoImage(file="simv_blank.gif")
    simv_blank_image_button=Button(window, image=simv_blank_image, highlightthickness=0,bd=0,bg="white",command=update_simv)
    simv_green_image=PhotoImage(file="simv_green.gif")
    simv_green_image_button=Button(window, image=simv_green_image, highlightthickness=0,bd=0,bg="white",command=dont_change_modes)

    def update_cpap():
        global control_mode
        control_mode = ",CPap,"
        global packed_control_mode
        packed_control_mode="cm"+control_mode
        global cmv_green_image_button
        global acv_green_image_button
        global simv_green_image_button
        global cpap_blank_image_button
        cmv_green_image_button.place_forget()
        acv_green_image_button.place_forget()
        simv_green_image_button.place_forget()
        cpap_blank_image_button.place_forget()
        x_ventilation_modes_first_line = 1180
        x_ventilation_modes_second_line = 1270
        x_ventilation_modes_third_line = 1250
        x_gap_between_buttons = 90
        y_first_line_ventilation_modes = 75
        y_distance_between_lines_ventilation_modes = 50
        cmv_blank_image_button.place(x=x_ventilation_modes_first_line , y=y_first_line_ventilation_modes)
        acv_blank_image_button.place(x=x_ventilation_modes_first_line+1*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        simv_blank_image_button.place(x=x_ventilation_modes_first_line+2*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        cpap_green_image_button.place(x=x_ventilation_modes_first_line+3*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        send_data_to_arduino()
    cpap_blank_image=PhotoImage(file="cpap_blank.gif")
    cpap_blank_image_button=Button(window, image=cpap_blank_image, highlightthickness=0,bd=0,bg="white",command=update_cpap)
    cpap_green_image=PhotoImage(file="cpap_green.gif")
    cpap_green_image_button=Button(window, image=cpap_green_image, highlightthickness=0,bd=0,bg="white",command=dont_change_modes)

    def update_pcv():
        global mode
        mode = ",pcv,"
        global pcv_blank_image_button
        global vcv_green_image_button
        pcv_blank_image_button.place_forget()
        vcv_green_image_button.place_forget()
        x_ventilation_modes_first_line = 1180
        x_ventilation_modes_second_line = 1270
        x_ventilation_modes_third_line = 1250
        x_gap_between_buttons = 90
        y_first_line_ventilation_modes = 75
        y_distance_between_lines_ventilation_modes = 50
        pcv_green_image_button.place(x=x_ventilation_modes_second_line , y=y_first_line_ventilation_modes+1*y_distance_between_lines_ventilation_modes)
        vcv_blank_image_button.place(x=x_ventilation_modes_second_line+1*x_gap_between_buttons , y=y_first_line_ventilation_modes+1*y_distance_between_lines_ventilation_modes)
        stop_ventilating()
        start_ventilating_in_full_mode()
        monitoring.display_values_being_monitored.hide_monitored_values()
        monitoring.display_values_being_monitored.display_monitored_values()
        ventilation_inputs.hide_my_inputs()
        ventilation_inputs.place_my_inputs()
        ventilation_inputs.configure_my_inputs()
        send_data_to_arduino()
    pcv_blank_image=PhotoImage(file="pcv_blank.gif")
    pcv_blank_image_button=Button(window, image=pcv_blank_image, highlightthickness=0,bd=0,bg="white",command=update_pcv)
    pcv_green_image=PhotoImage(file="pcv_green.gif")
    pcv_green_image_button=Button(window, image=pcv_green_image, highlightthickness=0,bd=0,bg="white",command=dont_change_modes)

    def update_vcv():
        global mode
        mode = ",vcv,"
        global pcv_green_image_button
        global vcv_blank_image_button
        pcv_green_image_button.place_forget()
        vcv_blank_image_button.place_forget()
        x_ventilation_modes_first_line = 1180
        x_ventilation_modes_second_line = 1270
        x_ventilation_modes_third_line = 1250
        x_gap_between_buttons = 90
        y_first_line_ventilation_modes = 75
        y_distance_between_lines_ventilation_modes = 50
        pcv_blank_image_button.place(x=x_ventilation_modes_second_line , y=y_first_line_ventilation_modes+1*y_distance_between_lines_ventilation_modes)
        vcv_green_image_button.place(x=x_ventilation_modes_second_line+1*x_gap_between_buttons , y=y_first_line_ventilation_modes+1*y_distance_between_lines_ventilation_modes)
        stop_ventilating()
        start_ventilating_in_full_mode()
        monitoring.display_values_being_monitored.hide_monitored_values()
        monitoring.display_values_being_monitored.display_monitored_values()
        ventilation_inputs.hide_my_inputs()
        ventilation_inputs.place_my_inputs()
        ventilation_inputs.configure_my_inputs()
        send_data_to_arduino()
    vcv_blank_image=PhotoImage(file="vcv_blank.gif")
    vcv_blank_image_button=Button(window, image=vcv_blank_image, highlightthickness=0,bd=0,bg="white",command=update_vcv)
    vcv_green_image=PhotoImage(file="vcv_green.gif")
    vcv_green_image_button=Button(window, image=vcv_green_image, highlightthickness=0,bd=0,bg="white",command=dont_change_modes)

    def update_pressure_trigger_mode():
        global trigger_mode
        trigger_mode = "P"
        global Pressure_triggered_blank_image_button
        global Flow_triggered_green_image_button
        Pressure_triggered_blank_image_button.place_forget()
        Flow_triggered_green_image_button.place_forget()
        x_ventilation_modes_first_line = 1180
        x_ventilation_modes_second_line = 1270
        x_ventilation_modes_third_line = 1250
        x_gap_between_buttons = 90
        y_first_line_ventilation_modes = 75
        y_distance_between_lines_ventilation_modes = 50
        Pressure_triggered_green_image_button.place(x=x_ventilation_modes_third_line , y=y_first_line_ventilation_modes+2*y_distance_between_lines_ventilation_modes)
        Flow_triggered_blank_image_button.place(x=x_ventilation_modes_third_line+1.5*x_gap_between_buttons , y=y_first_line_ventilation_modes+2*y_distance_between_lines_ventilation_modes)
        stop_ventilating()
        start_ventilating_in_full_mode()
        monitoring.display_values_being_monitored.hide_monitored_values()
        monitoring.display_values_being_monitored.display_monitored_values()
        ventilation_inputs.hide_my_inputs()
        ventilation_inputs.place_my_inputs()
        ventilation_inputs.configure_my_inputs()
        send_data_to_arduino()
    Pressure_triggered_blank_image=PhotoImage(file="Pressure_triggered_blank.gif")
    Pressure_triggered_blank_image_button=Button(window, image=Pressure_triggered_blank_image, highlightthickness=0,bd=0,bg="white",command=update_pressure_trigger_mode)
    Pressure_triggered_green_image=PhotoImage(file="Pressure_triggered_green.gif")
    Pressure_triggered_green_image_button=Button(window, image=Pressure_triggered_green_image, highlightthickness=0,bd=0,bg="white",command=dont_change_modes)

    def update_flow_trigger_mode():
        global trigger_mode
        trigger_mode = "F"
        global Pressure_triggered_green_image_button
        global Flow_triggered_blank_image_button
        Pressure_triggered_green_image_button.place_forget()
        Flow_triggered_blank_image_button.place_forget()
        x_ventilation_modes_first_line = 1180
        x_ventilation_modes_second_line = 1270
        x_ventilation_modes_third_line = 1250
        x_gap_between_buttons = 90
        y_first_line_ventilation_modes = 75
        y_distance_between_lines_ventilation_modes = 50
        Pressure_triggered_blank_image_button.place(x=x_ventilation_modes_third_line , y=y_first_line_ventilation_modes+2*y_distance_between_lines_ventilation_modes)
        Flow_triggered_green_image_button.place(x=x_ventilation_modes_third_line+1.5*x_gap_between_buttons , y=y_first_line_ventilation_modes+2*y_distance_between_lines_ventilation_modes)
        stop_ventilating()
        start_ventilating_in_full_mode()
        monitoring.display_values_being_monitored.hide_monitored_values()
        monitoring.display_values_being_monitored.display_monitored_values()
        ventilation_inputs.hide_my_inputs()
        ventilation_inputs.place_my_inputs()
        ventilation_inputs.configure_my_inputs()
        send_data_to_arduino()
    Flow_triggered_blank_image=PhotoImage(file="Flow_triggered_blank.gif")
    Flow_triggered_blank_image_button=Button(window, image=Flow_triggered_blank_image, highlightthickness=0,bd=0,bg="white",command=update_flow_trigger_mode)
    Flow_triggered_green_image=PhotoImage(file="Flow_triggered_green.gif")
    Flow_triggered_green_image_button=Button(window, image=Flow_triggered_green_image, highlightthickness=0,bd=0,bg="white",command=dont_change_modes)
    # BUTTONS AT THE TOP - end

    global alarm_updates_button_mid_ventilation
    alarm_updates=PhotoImage(file="alarms.gif")
    alarm_updates_button_mid_ventilation=Button(window, image=alarm_updates, highlightthickness=0,bd=0,bg="white",command=alarm_scales.update_alarms_mid_ventilation)

    global my_inputs_being_placed
    my_inputs_being_placed="no"
    def place_user_entered_buttons():
        global my_inputs_being_placed
        if my_inputs_being_placed=="no":
            ventilation_inputs.create_labels_that_show_me_my_inputs()
            ventilation_inputs.place_my_inputs()
            my_inputs_being_placed="yes"
        if my_inputs_being_placed=="yes":
            ventilation_inputs.configure_my_inputs()
        user_entered_values_image_label.place(x=1200,y=30)
        global update_pressure_button
        global update_flowrate_button
        global update_peep_button
        global update_bpm_button
        global update_vol_button
        global update_oxygen_button
        global update_insp_time_button
        global update_ie_button
        global update_triggering_flow_button
        global update_triggering_pressure_button
        global inspiratory_pause_manoeuvre_button
        global display_monitored_values_image_label
        y_increment_monitored_values_block=100
        x_increment=0
        y_increment=65
        line_1_x=1400
        line_1_y=130+y_increment_monitored_values_block
        line_number=1
        line=line_number-1
        if mode==",pcv,":
            update_pressure_button.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        if mode==",vcv,":
            update_flowrate_button.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        line_number=2
        line=line_number-1
        update_peep_button.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        line_number=3
        line=line_number-1
        update_bpm_button.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        line_number=4
        line=line_number-1
        update_oxygen_button.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        line_number=5
        line=line_number-1
        if mode==",pcv,":
            update_insp_time_button.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        if mode==",vcv,":
            update_vol_button.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        line_number=6
        line=line_number-1
        update_ie_button.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        line_number=7
        line=line_number-1
        if trigger_mode=="F":
            update_triggering_flow_button.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        if trigger_mode=="P":
            update_triggering_pressure_button.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        line_number=8
        line=line_number-1
        inspiratory_pause_manoeuvre_button.place(x=line_1_x+x_increment-100,y=line_1_y+line*y_increment)
        global cmv_blank_image_button
        global cmv_green_image_button
        global acv_blank_image_button
        global acv_green_image_button
        global simv_blank_image_button
        global simv_green_image_button
        global cpap_blank_image_button
        global cpap_green_image_button
        global pcv_blank_image_button
        global pcv_green_image_button
        global vcv_blank_image_button
        global vcv_green_image_button
        global Pressure_triggered_blank_image_button
        global Pressure_triggered_green_image_button
        global Flow_triggered_blank_image_button
        global Flow_triggered_green_image_button
        x_ventilation_modes_first_line = 1180
        x_ventilation_modes_second_line = 1270
        x_ventilation_modes_third_line = 1250
        x_gap_between_buttons = 90
        y_first_line_ventilation_modes = 75
        y_distance_between_lines_ventilation_modes = 50
        if control_mode == ",CMV,":
            cmv_green_image_button.place(x=x_ventilation_modes_first_line , y=y_first_line_ventilation_modes)
            acv_blank_image_button.place(x=x_ventilation_modes_first_line+1*x_gap_between_buttons , y=y_first_line_ventilation_modes)
            simv_blank_image_button.place(x=x_ventilation_modes_first_line+2*x_gap_between_buttons , y=y_first_line_ventilation_modes)
            cpap_blank_image_button.place(x=x_ventilation_modes_first_line+3*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        if control_mode == ",ACV,":
            cmv_blank_image_button.place(x=x_ventilation_modes_first_line , y=y_first_line_ventilation_modes)
            acv_green_image_button.place(x=x_ventilation_modes_first_line+1*x_gap_between_buttons , y=y_first_line_ventilation_modes)
            simv_blank_image_button.place(x=x_ventilation_modes_first_line+2*x_gap_between_buttons , y=y_first_line_ventilation_modes)
            cpap_blank_image_button.place(x=x_ventilation_modes_first_line+3*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        if control_mode == ",SIMV,":
            cmv_blank_image_button.place(x=x_ventilation_modes_first_line , y=y_first_line_ventilation_modes)
            acv_blank_image_button.place(x=x_ventilation_modes_first_line+1*x_gap_between_buttons , y=y_first_line_ventilation_modes)
            simv_green_image_button.place(x=x_ventilation_modes_first_line+2*x_gap_between_buttons , y=y_first_line_ventilation_modes)
            cpap_blank_image_button.place(x=x_ventilation_modes_first_line+3*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        if control_mode == ",CPap,":
            cmv_blank_image_button.place(x=x_ventilation_modes_first_line , y=y_first_line_ventilation_modes)
            acv_blank_image_button.place(x=x_ventilation_modes_first_line+1*x_gap_between_buttons , y=y_first_line_ventilation_modes)
            simv_blank_image_button.place(x=x_ventilation_modes_first_line+2*x_gap_between_buttons , y=y_first_line_ventilation_modes)
            cpap_green_image_button.place(x=x_ventilation_modes_first_line+3*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        if mode == ",pcv,":
            pcv_green_image_button.place(x=x_ventilation_modes_second_line , y=y_first_line_ventilation_modes+1*y_distance_between_lines_ventilation_modes)
            vcv_blank_image_button.place(x=x_ventilation_modes_second_line+1*x_gap_between_buttons , y=y_first_line_ventilation_modes+1*y_distance_between_lines_ventilation_modes)
        if mode == ",vcv,":
            pcv_blank_image_button.place(x=x_ventilation_modes_second_line , y=y_first_line_ventilation_modes+1*y_distance_between_lines_ventilation_modes)
            vcv_green_image_button.place(x=x_ventilation_modes_second_line+1*x_gap_between_buttons , y=y_first_line_ventilation_modes+1*y_distance_between_lines_ventilation_modes)
        if trigger_mode == "P":
            Pressure_triggered_green_image_button.place(x=x_ventilation_modes_third_line , y=y_first_line_ventilation_modes+2*y_distance_between_lines_ventilation_modes)
            Flow_triggered_blank_image_button.place(x=x_ventilation_modes_third_line+1.5*x_gap_between_buttons , y=y_first_line_ventilation_modes+2*y_distance_between_lines_ventilation_modes)
        if trigger_mode == "F":
            Pressure_triggered_blank_image_button.place(x=x_ventilation_modes_third_line , y=y_first_line_ventilation_modes+2*y_distance_between_lines_ventilation_modes)
            Flow_triggered_green_image_button.place(x=x_ventilation_modes_third_line+1.5*x_gap_between_buttons , y=y_first_line_ventilation_modes+2*y_distance_between_lines_ventilation_modes)

    def cross_pressed():
        global update_pressure_button
        global update_flowrate_button
        global update_peep_button
        global update_bpm_button
        global update_vol_button
        global update_oxygen_button
        global update_insp_time_button
        global update_ie_button
        global update_triggering_flow_button
        global update_triggering_pressure_button
        global scale_value
        global scale_label
        global scale_unit_label
        ventilation_inputs.hide_user_entered_buttons()
        ventilation_inputs.hide_scale_bars()
        ventilation_inputs.hide_numeric_display_for_scale()
        ventilation_inputs.hide_tick_and_cross_buttons()
        ventilation_inputs.place_user_entered_buttons()
    global cross_button
    cross_button_image=PhotoImage(file="cross.gif")
    cross_button=Button(window, image=cross_button_image, highlightthickness=0,bd=0,bg="white",command=cross_pressed)

    def create_labels_that_show_me_my_inputs():
        global displayed_value_pressure_entered
        global displayed_value_flowrate_entered
        global displayed_value_peep_entered
        global displayed_value_bpm_entered
        global displayed_value_vol_entered
        global displayed_value_oxygen_entered
        global displayed_value_insp_time_entered
        global displayed_value_ie_entered
        global unit_displayed_value_pressure_entered
        global unit_displayed_value_flowrate_entered
        global unit_displayed_value_peep_entered
        global unit_displayed_value_vol_entered
        global unit_displayed_value_oxygen_entered
        global unit_displayed_value_insp_time_entered
        global unit_displayed_triggering_pressure_entered
        global unit_displayed_triggering_flow_entered
        global displayed_value_triggering_pressure_entered
        global displayed_value_triggering_flow_entered
        displayed_value_pressure_entered=           Label(window, text=value_pressure_entered,   bg="black", fg="white",font=("montserrat light",30,"normal"))
        unit_displayed_value_pressure_entered=      Label(window, text="cmH20",   bg="black", fg="white",font=("montserrat light",9,"normal"))
        displayed_value_flowrate_entered=           Label(window, text=value_flowrate_entered,   bg="black", fg="white",font=("montserrat light",30,"normal"))
        unit_displayed_value_flowrate_entered=      Label(window, text="Lpm",   bg="black", fg="white",font=("montserrat light",9,"normal"))
        displayed_value_peep_entered=               Label(window, text=value_peep_entered,   bg="black", fg="white",font=("montserrat light",30,"normal"))
        unit_displayed_value_peep_entered=          Label(window, text="cmH20",   bg="black", fg="white",font=("montserrat light",9,"normal"))
        displayed_value_bpm_entered=                Label(window, text=value_bpm_entered,   bg="black", fg="white",font=("montserrat light",30,"normal"))
        displayed_value_vol_entered=                Label(window, text=value_vol_entered,   bg="black", fg="white",font=("montserrat light",30,"normal"))
        unit_displayed_value_vol_entered=           Label(window, text="mL",   bg="black", fg="white",font=("montserrat light",9,"normal"))
        displayed_value_oxygen_entered=             Label(window, text=value_oxygen_entered,   bg="black", fg="white",font=("montserrat light",30,"normal"))
        unit_displayed_value_oxygen_entered=        Label(window, text="%",   bg="black", fg="white",font=("montserrat light",9,"normal"))
        displayed_value_insp_time_entered=          Label(window, text=value_insp_time_entered,   bg="black", fg="white",font=("montserrat light",30,"normal"))
        unit_displayed_value_insp_time_entered=     Label(window, text="sec",   bg="black", fg="white",font=("montserrat light",9,"normal"))
        displayed_value_ie_entered=                 Label(window, text="1:"+str(value_ie_entered),   bg="black", fg="white",font=("montserrat light",30,"normal"))
        displayed_value_triggering_pressure_entered=Label(window, text=value_triggering_pressure_entered, bg="black", fg="white",font=("montserrat light",30,"normal"))
        unit_displayed_triggering_pressure_entered= Label(window, text="cmH20",   bg="black", fg="white",font=("montserrat light",9,"normal"))
        displayed_value_triggering_flow_entered=    Label(window, text=value_triggering_flow_entered, bg="black", fg="white",font=("montserrat light",30,"normal"))
        unit_displayed_triggering_flow_entered=     Label(window, text="Lpm",   bg="black", fg="white",font=("montserrat light",9,"normal"))

    def place_my_inputs():
        global displayed_value_pressure_entered
        global displayed_value_flowrate_entered
        global displayed_value_peep_entered
        global displayed_value_bpm_entered
        global displayed_value_vol_entered
        global displayed_value_oxygen_entered
        global displayed_value_insp_time_entered
        global displayed_value_ie_entered
        global displayed_value_triggering_pressure_entered
        global displayed_value_triggering_flow_entered
        global unit_displayed_value_pressure_entered
        global unit_displayed_value_flowrate_entered
        global unit_displayed_value_peep_entered
        global unit_displayed_value_vol_entered
        global unit_displayed_value_oxygen_entered
        global unit_displayed_value_insp_time_entered
        global unit_displayed_triggering_pressure_entered
        global unit_displayed_triggering_flow_entered
        y_increment_monitored_values_block=95
        gap_for_unit=25
        x_increment=0
        y_increment=65
        line_1_x=1350
        line_1_y=150+y_increment_monitored_values_block
        line_number=1
        line=line_number-1
        if mode==",pcv,":
            displayed_value_pressure_entered.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment, anchor='center')
            unit_displayed_value_pressure_entered.place(x=line_1_x+x_increment,y=gap_for_unit+line_1_y+line*y_increment, anchor='center')
        if mode==",vcv,":
            displayed_value_flowrate_entered.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment, anchor='center')
            unit_displayed_value_flowrate_entered.place(x=line_1_x+x_increment,y=gap_for_unit+line_1_y+line*y_increment, anchor='center')
        line_number=2
        line=line_number-1
        displayed_value_peep_entered.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment, anchor='center')
        unit_displayed_value_peep_entered.place(x=line_1_x+x_increment,y=gap_for_unit+line_1_y+line*y_increment, anchor='center')
        line_number=3
        line=line_number-1
        displayed_value_bpm_entered.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment, anchor='center')
        line_number=4
        line=line_number-1
        displayed_value_oxygen_entered.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment, anchor='center')
        unit_displayed_value_oxygen_entered.place(x=line_1_x+x_increment,y=gap_for_unit+line_1_y+line*y_increment, anchor='center')
        line_number=5
        line=line_number-1
        if mode==",pcv,":
            displayed_value_insp_time_entered.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment, anchor='center')
            unit_displayed_value_insp_time_entered.place(x=line_1_x+x_increment,y=gap_for_unit+line_1_y+line*y_increment, anchor='center')
        if mode==",vcv,":
            displayed_value_vol_entered.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment, anchor='center')
            unit_displayed_value_vol_entered.place(x=line_1_x+x_increment,y=gap_for_unit+line_1_y+line*y_increment, anchor='center')
        line_number=6
        line=line_number-1
        displayed_value_ie_entered.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment, anchor='center')
        line_number=7
        line=line_number-1
        if trigger_mode=="P":
            displayed_value_triggering_pressure_entered.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment, anchor='center')
            unit_displayed_triggering_pressure_entered.place(x=line_1_x+x_increment,y=gap_for_unit+line_1_y+line*y_increment, anchor='center')
        if trigger_mode=="F":
            displayed_value_triggering_flow_entered.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment, anchor='center')
            unit_displayed_triggering_flow_entered.place(x=line_1_x+x_increment,y=gap_for_unit+line_1_y+line*y_increment, anchor='center')
        global alarm_updates_button_mid_ventilation                     # place the button that updates alarm limits during ventilation
        alarm_updates_button_mid_ventilation.place(x=1420,y=750)

    def configure_my_inputs():
        global displayed_value_pressure_entered
        global displayed_value_flowrate_entered
        global displayed_value_peep_entered
        global displayed_value_bpm_entered
        global displayed_value_vol_entered
        global displayed_value_oxygen_entered
        global displayed_value_insp_time_entered
        global displayed_value_ie_entered
        global displayed_value_triggering_pressure_entered
        global displayed_value_triggering_flow_entered
        if mode==",pcv,":
            displayed_value_pressure_entered.configure(text= value_pressure_entered)
        if mode==",vcv,":
            displayed_value_flowrate_entered.configure(text= value_flowrate_entered)
        displayed_value_peep_entered.configure(text= value_peep_entered)
        displayed_value_bpm_entered.configure(text= value_bpm_entered)
        displayed_value_oxygen_entered.configure(text= value_oxygen_entered)
        if mode==",pcv,":
            displayed_value_insp_time_entered.configure(text= value_insp_time_entered)
        if mode==",vcv,":
            displayed_value_vol_entered.configure(text= value_vol_entered)
        displayed_value_ie_entered.configure(text= "1:"+str(value_ie_entered))
        if trigger_mode=="P":
            displayed_value_triggering_pressure_entered.configure(text= value_triggering_pressure_entered)
        if trigger_mode=="F":
            displayed_value_triggering_flow_entered.configure(text= value_triggering_flow_entered)

    def hide_my_inputs():
        global displayed_value_pressure_entered
        global displayed_value_flowrate_entered
        global displayed_value_peep_entered
        global displayed_value_bpm_entered
        global displayed_value_vol_entered
        global displayed_value_oxygen_entered
        global displayed_value_insp_time_entered
        global displayed_value_ie_entered
        global displayed_value_triggering_pressure_entered
        global displayed_value_triggering_flow_entered
        global unit_displayed_value_pressure_entered
        global unit_displayed_value_flowrate_entered
        global unit_displayed_value_peep_entered
        global unit_displayed_value_vol_entered
        global unit_displayed_value_oxygen_entered
        global unit_displayed_value_insp_time_entered
        global unit_displayed_triggering_pressure_entered
        global unit_displayed_triggering_flow_entered
        # global acv_blank_image_button
        # global acv_green_image_button
        # global simv_blank_image_button
        # global simv_green_image_button
        # global cpap_blank_image_button
        # global cpap_green_image_button
        # global pcv_blank_image_button
        # global pcv_green_image_button
        # global vcv_blank_image_button
        # global vcv_green_image_button
        # global Pressure_triggered_blank_image_button
        # global Pressure_triggered_green_image_button
        # global Flow_triggered_blank_image_button
        # global Flow_triggered_green_image_button
        # global user_entered_values_image_label
        displayed_value_pressure_entered.place_forget()
        displayed_value_flowrate_entered.place_forget()
        displayed_value_peep_entered.place_forget()
        displayed_value_bpm_entered.place_forget()
        displayed_value_vol_entered.place_forget()
        displayed_value_oxygen_entered.place_forget()
        displayed_value_insp_time_entered.place_forget()
        displayed_value_triggering_pressure_entered.place_forget()
        displayed_value_triggering_flow_entered.place_forget()
        unit_displayed_value_pressure_entered.place_forget()
        unit_displayed_value_flowrate_entered.place_forget()
        unit_displayed_value_peep_entered.place_forget()
        unit_displayed_value_vol_entered.place_forget()
        unit_displayed_value_oxygen_entered.place_forget()
        unit_displayed_value_insp_time_entered.place_forget()
        displayed_value_ie_entered.place_forget()
        unit_displayed_triggering_flow_entered.place_forget()
        unit_displayed_triggering_pressure_entered.place_forget()
        # acv_blank_image_button.place_forget()
        # acv_green_image_button.place_forget()
        # simv_blank_image_button.place_forget()
        # simv_green_image_button.place_forget()
        # cpap_blank_image_button.place_forget()
        # cpap_green_image_button.place_forget()
        # pcv_blank_image_button.place_forget()
        # pcv_green_image_button.place_forget()
        # vcv_blank_image_button.place_forget()
        # vcv_green_image_button.place_forget()
        # Pressure_triggered_blank_image_button.place_forget()
        # Pressure_triggered_green_image_button.place_forget()
        # Flow_triggered_blank_image_button.place_forget()
        # Flow_triggered_green_image_button.place_forget()
        #user_entered_values_image_label.place_forget()
        global alarm_updates_button_mid_ventilation
        alarm_updates_button_mid_ventilation.place_forget()
    def hide_tick_and_cross_buttons():
        tick_button.place_forget()
        cross_button.place_forget()
    def hide_scale_bars():
        scale_pressure.place_forget()
        scale_flowrate.place_forget()
        scale_vol.place_forget()
        scale_bpm.place_forget()
        scale_peep.place_forget()
        scale_oxygen.place_forget()
        scale_insp_time.place_forget()
        scale_ie.place_forget()
        scale_flow_trigger.place_forget()
        scale_pressure_trigger.place_forget()

    def hide_numeric_display_for_scale():
        scale_value.place_forget()
        scale_label.place_forget()
        scale_unit_label.place_forget()

    def hide_user_entered_buttons():
        global update_pressure_button
        global update_flowrate_button
        global update_peep_button
        global update_bpm_button
        global update_vol_button
        global update_oxygen_button
        global update_insp_time_button
        global update_ie_button
        global update_triggering_flow_button
        global update_triggering_pressure_button
        global inspiratory_pause_manoeuvre_button
        global user_entered_values_image_label
        update_pressure_button.place_forget()
        update_flowrate_button.place_forget()
        update_vol_button.place_forget()
        update_bpm_button.place_forget()
        update_peep_button.place_forget()
        update_oxygen_button.place_forget()
        update_insp_time_button.place_forget()
        update_ie_button.place_forget()
        update_triggering_flow_button.place_forget()
        update_triggering_pressure_button.place_forget()
        inspiratory_pause_manoeuvre_button.place_forget()
    def tick_pressed():
        ventilation_inputs.place_user_entered_buttons()
        ventilation_inputs.hide_numeric_display_for_scale()
        ventilation_inputs.hide_scale_bars()
        ventilation_inputs.hide_tick_and_cross_buttons()
        send_data_to_arduino()
    global tick_button
    tick_button_image=PhotoImage(file="tick.gif")
    tick_button=Button(window, image=tick_button_image, highlightthickness=0,bd=0,bg="white",command=tick_pressed)

    def hide_scale_and_buttons():
        ventilation_inputs.hide_user_entered_buttons()
        ventilation_inputs.hide_numeric_display_for_scale()
        ventilation_inputs.hide_scale_bars()
        ventilation_inputs.hide_tick_and_cross_buttons()
"""CLASS: USER ENTERED SYSTEM/END"""

"CLASS: STARTUP PROTOCOLS"
class startup_inputs():
    global CustomScale_pressure
    global CustomScale_flowrate
    global CustomScale_vol
    global CustomScale_bpm
    global CustomScale_peep
    global CustomScale_oxygen
    global CustomScale_insp_time
    global CustomScale_ie
    global CustomScale_pressure_trigger
    global CustomScale_flow_trigger
    class CustomScale_pressure(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'pressure_custom.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global value_pressure_entered
            global packed_pressure
            if scaling=="yes":
                if scale_location_status=="centered":
                    global startup_scale_pressure_value
                    startup_scale_pressure_value.place_forget()
                    value_pressure_entered=format(int(self.variable.get()))
                    startup_scale_pressure_value=Label(window, text=str(value_pressure_entered), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    startup_scale_pressure_value.place(x=scale_value_pressure_entered_location_x,y=scale_value_pressure_entered_location_y, anchor = CENTER)
                    packed_pressure="p"+","+str(value_pressure_entered)+","
                    #style.configure(self._style_name, font=("montserrat semi bold",8), text="{:.1f}".format(int(self.variable.get())))
    class CustomScale_flowrate(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'flowrate_custom.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global value_flowrate_entered
            global packed_flowrate
            if scaling=="yes":
                if scale_location_status=="centered":
                    global startup_scale_flowrate_value
                    startup_scale_flowrate_value.place_forget()
                    value_flowrate_entered=format(int(self.variable.get()))
                    startup_scale_flowrate_value=Label(window, text=str(value_flowrate_entered), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    startup_scale_flowrate_value.place(x=scale_value_flowrate_entered_location_x,y=scale_value_flowrate_entered_location_y, anchor = CENTER)
                    packed_flowrate="q"+","+str(value_flowrate_entered)+","
                    #style.configure(self._style_name, font=("montserrat semi bold",8), text="{:.1f}".format(int(self.variable.get())))
    class CustomScale_peep(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'peep_custom.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global value_peep_entered
            global packed_peep
            if scaling=="yes":
                if scale_location_status=="centered":
                    global startup_scale_peep_value
                    startup_scale_peep_value.place_forget()
                    value_peep_entered=format(int(self.variable.get()))
                    startup_scale_peep_value=Label(window, text=str(value_peep_entered), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    startup_scale_peep_value.place(x=scale_value_peep_entered_location_x,y=scale_value_peep_entered_location_y, anchor = CENTER)
                    packed_peep="pp"+","+str(value_peep_entered)+","
                    #style.configure(self._style_name, font=("montserrat semi bold",8), text="{:.1f}".format(int(self.variable.get())))
    class CustomScale_bpm(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'bpm_custom.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global value_bpm_entered
            global packed_bpm
            if scaling=="yes":
                if scale_location_status=="centered":
                    global startup_scale_bpm_value
                    startup_scale_bpm_value.place_forget()
                    value_bpm_entered=format(int(self.variable.get()))
                    startup_scale_bpm_value=Label(window, text=str(value_bpm_entered), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    startup_scale_bpm_value.place(x=scale_value_bpm_entered_location_x,y=scale_value_bpm_entered_location_y, anchor = CENTER)
                    packed_bpm="b"+","+str(value_bpm_entered)+","
                    #style.configure(self._style_name, font=("montserrat semi bold",8), text="{:.1f}".format(int(self.variable.get())))
    class CustomScale_oxygen(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'oxygen_custom.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global value_oxygen_entered
            global packed_oxygen
            if scaling=="yes":
                if scale_location_status=="centered":
                    global startup_scale_oxygen_value
                    startup_scale_oxygen_value.place_forget()
                    value_oxygen_entered=format(int(self.variable.get()))
                    startup_scale_oxygen_value=Label(window, text=str(value_oxygen_entered), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    startup_scale_oxygen_value.place(x=scale_value_oxygen_entered_location_x,y=scale_value_oxygen_entered_location_y, anchor = CENTER)
                    packed_oxygen="O"+","+str(value_oxygen_entered)+","
                    #style.configure(self._style_name, font=("montserrat semi bold",8), text="{:.1f}".format(int(self.variable.get())))
    class CustomScale_vol(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'vol_custom.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global value_vol_entered
            global packed_vol
            if scaling=="yes":
                if scale_location_status=="centered":
                    global startup_scale_vol_value
                    startup_scale_vol_value.place_forget()
                    value_vol_entered=format(int(self.variable.get()))
                    startup_scale_vol_value=Label(window, text=str(value_vol_entered), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    startup_scale_vol_value.place(x=scale_value_vol_entered_location_x,y=scale_value_vol_entered_location_y, anchor = CENTER)
                    packed_vol="v"+","+str(value_vol_entered)+","
                    #style.configure(self._style_name, font=("montserrat semi bold",8), text="{:.1f}".format(int(self.variable.get())))
    class CustomScale_insp_time(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'insp_time_custom.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global value_insp_time_entered
            global packed_insp_time
            if scaling=="yes":
                if scale_location_status=="centered":
                    global startup_scale_insp_time_value
                    startup_scale_insp_time_value.place_forget()
                    value_insp_time_entered="{:.1f}".format(self.variable.get())
                    startup_scale_insp_time_value=Label(window, text=str(value_insp_time_entered), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    startup_scale_insp_time_value.place(x=scale_value_insp_time_entered_location_x,y=scale_value_insp_time_entered_location_y, anchor = CENTER)
                    packed_insp_time="it"+","+str(value_insp_time_entered)+","
                    #style.configure(self._style_name, font=("montserrat semi bold",8), text="{:.1f}".format(int(self.variable.get())))
    class CustomScale_ie(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'ie_custom.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global value_ie_entered
            global packed_ie
            if scaling=="yes":
                if scale_location_status=="centered":
                    global startup_scale_ie_value
                    startup_scale_ie_value.place_forget()
                    value_ie_entered=format(int(self.variable.get()))
                    startup_scale_ie_value=Label(window, text=str("1:")+str(value_ie_entered), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    startup_scale_ie_value.place(x=scale_value_ie_entered_location_x,y=scale_value_ie_entered_location_y, anchor = CENTER)
                    packed_ie="ie"+","+"1:"+str(value_ie_entered)+","
                    # print(packed_ie)
                    #style.configure(self._style_name, font=("montserrat semi bold",8), text="{:.1f}".format(int(self.variable.get())))
    class CustomScale_pressure_trigger(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'pressure_trigger_custom.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global value_triggering_pressure_entered
            global packed_triggering_pressure
            if scaling=="yes":
                if scale_location_status=="centered":
                    global startup_scale_pressure_trigger_value
                    startup_scale_pressure_trigger_value.place_forget()
                    value_triggering_pressure_entered=format(int(self.variable.get()))
                    startup_scale_pressure_trigger_value=Label(window, text=str(value_triggering_pressure_entered), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    startup_scale_pressure_trigger_value.place(x=scale_value_triggering_pressure_entered_location_x,y=scale_value_triggering_pressure_entered_location_y, anchor = CENTER)
                    packed_triggering_pressure="tp"+","+str(value_triggering_pressure_entered)+","
                    #style.configure(self._style_name, font=("montserrat semi bold",8), text="{:.1f}".format(int(self.variable.get())))
    class CustomScale_flow_trigger(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', DoubleVar(master))
            ttk.Scale.__init__(self, master, orient='horizontal', variable=self.variable, **kw)
            self._style_name = 'flow_trigger_custom.Horizontal.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update_text)
            self._update_text()
        def _update_text(self, *args):
            global scaling
            global value_triggering_flow_entered
            global packed_triggering_flow
            if scaling=="yes":
                if scale_location_status=="centered":
                    global startup_scale_flow_trigger_value
                    startup_scale_flow_trigger_value.place_forget()
                    value_triggering_flow_entered=format(int(self.variable.get()))
                    startup_scale_flow_trigger_value=Label(window, text=str(value_triggering_flow_entered), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    startup_scale_flow_trigger_value.place(x=scale_value_triggering_flow_entered_location_x,y=scale_value_triggering_flow_entered_location_y, anchor = CENTER)
                    packed_triggering_flow="tf"+","+str(value_triggering_flow_entered)+","
                    #style.configure(self._style_name, font=("montserrat semi bold",8), text="{:.1f}".format(int(self.variable.get())))

    def create_startup_bar_and_slider():
        global startup_img_trough
        global startup_img_slider
        startup_img_trough = PhotoImage(file="startup_bar.gif")
        startup_img_slider = PhotoImage(file="startup_slider.gif")
    create_startup_bar_and_slider()
    def create_scale_styles_for_startup():
        # create scale elements
        string_startup_trough='pressure_custom.Horizontal.Scale.trough'
        string_startup_slider='pressure_custom.Horizontal.Scale.slider'
        style.element_create(string_startup_trough, 'image', startup_img_trough)
        style.element_create(string_startup_slider, 'image', startup_img_slider)
        # create custom layout
        style.layout('pressure_custom.Horizontal.TScale',[(string_startup_trough, {'sticky': 'ns'}),
                    (string_startup_slider, {'side': 'left', 'sticky': '','children': [('pressure_custom.Horizontal.Scale.label', {'sticky': ''})]})])
        # create scale elements
        string_startup_trough='flowrate_custom.Horizontal.Scale.trough'
        string_startup_slider='flowrate_custom.Horizontal.Scale.slider'
        style.element_create(string_startup_trough, 'image', startup_img_trough)
        style.element_create(string_startup_slider, 'image', startup_img_slider)
        # create custom layout
        style.layout('flowrate_custom.Horizontal.TScale',[(string_startup_trough, {'sticky': 'ns'}),
                    (string_startup_slider, {'side': 'left', 'sticky': '','children': [('flowrate_custom.Horizontal.Scale.label', {'sticky': ''})]})])
        string_startup_trough='peep_custom.Horizontal.Scale.trough'
        string_startup_slider='peep_custom.Horizontal.Scale.slider'
        style.element_create(string_startup_trough, 'image', startup_img_trough)
        style.element_create(string_startup_slider, 'image', startup_img_slider)
        # create custom layout
        style.layout('peep_custom.Horizontal.TScale',[(string_startup_trough, {'sticky': 'ns'}),
                    (string_startup_slider, {'side': 'left', 'sticky': '','children': [('peep_custom.Horizontal.Scale.label', {'sticky': ''})]})])
        string_startup_trough='vol_custom.Horizontal.Scale.trough'
        string_startup_slider='vol_custom.Horizontal.Scale.slider'
        style.element_create(string_startup_trough, 'image', startup_img_trough)
        style.element_create(string_startup_slider, 'image', startup_img_slider)
        # create custom layout
        style.layout('vol_custom.Horizontal.TScale',[(string_startup_trough, {'sticky': 'ns'}),
                    (string_startup_slider, {'side': 'left', 'sticky': '','children': [('vol_custom.Horizontal.Scale.label', {'sticky': ''})]})])
        string_startup_trough='oxygen_custom.Horizontal.Scale.trough'
        string_startup_slider='oxygen_custom.Horizontal.Scale.slider'
        style.element_create(string_startup_trough, 'image', startup_img_trough)
        style.element_create(string_startup_slider, 'image', startup_img_slider)
        # create custom layout
        style.layout('oxygen_custom.Horizontal.TScale',[(string_startup_trough, {'sticky': 'ns'}),
                    (string_startup_slider, {'side': 'left', 'sticky': '','children': [('oxygen_custom.Horizontal.Scale.label', {'sticky': ''})]})])
        string_startup_trough='bpm_custom.Horizontal.Scale.trough'
        string_startup_slider='bpm_custom.Horizontal.Scale.slider'
        style.element_create(string_startup_trough, 'image', startup_img_trough)
        style.element_create(string_startup_slider, 'image', startup_img_slider)
        # create custom layout
        style.layout('bpm_custom.Horizontal.TScale',[(string_startup_trough, {'sticky': 'ns'}),
                    (string_startup_slider, {'side': 'left', 'sticky': '','children': [('bpm_custom.Horizontal.Scale.label', {'sticky': ''})]})])
        string_startup_trough='insp_time_custom.Horizontal.Scale.trough'
        string_startup_slider='insp_time_custom.Horizontal.Scale.slider'
        style.element_create(string_startup_trough, 'image', startup_img_trough)
        style.element_create(string_startup_slider, 'image', startup_img_slider)
        # create custom layout
        style.layout('insp_time_custom.Horizontal.TScale',[(string_startup_trough, {'sticky': 'ns'}),
                    (string_startup_slider, {'side': 'left', 'sticky': '','children': [('insp_time_custom.Horizontal.Scale.label', {'sticky': ''})]})])
        string_startup_trough='pressure_trigger_custom.Horizontal.Scale.trough'
        string_startup_slider='pressure_trigger_custom.Horizontal.Scale.slider'
        style.element_create(string_startup_trough, 'image', startup_img_trough)
        style.element_create(string_startup_slider, 'image', startup_img_slider)
        # create custom layout
        style.layout('pressure_trigger_custom.Horizontal.TScale',[(string_startup_trough, {'sticky': 'ns'}),
                    (string_startup_slider, {'side': 'left', 'sticky': '','children': [('pressure_trigger_custom.Horizontal.Scale.label', {'sticky': ''})]})])
        string_startup_trough='flow_trigger_custom.Horizontal.Scale.trough'
        string_startup_slider='flow_trigger_custom.Horizontal.Scale.slider'
        style.element_create(string_startup_trough, 'image', startup_img_trough)
        style.element_create(string_startup_slider, 'image', startup_img_slider)
        # create custom layout
        style.layout('flow_trigger_custom.Horizontal.TScale',[(string_startup_trough, {'sticky': 'ns'}),
                    (string_startup_slider, {'side': 'left', 'sticky': '','children': [('flow_trigger_custom.Horizontal.Scale.label', {'sticky': ''})]})])
        string_startup_trough='ie_custom.Horizontal.Scale.trough'
        string_startup_slider='ie_custom.Horizontal.Scale.slider'
        style.element_create(string_startup_trough, 'image', startup_img_trough)
        style.element_create(string_startup_slider, 'image', startup_img_slider)
        # create custom layout
        style.layout('ie_custom.Horizontal.TScale',[(string_startup_trough, {'sticky': 'ns'}),
                    (string_startup_slider, {'side': 'left', 'sticky': '','children': [('ie_custom.Horizontal.Scale.label', {'sticky': ''})]})])
    create_scale_styles_for_startup()

    def create_startup_scales():
        global scale_startup_vol
        global scale_startup_pressure
        global scale_startup_flowrate
        global scale_startup_bpm
        global scale_startup_peep
        global scale_startup_oxygen
        global scale_startup_insp_time
        global scale_startup_ie
        global scale_startup_pressure_trigger
        global scale_startup_flow_trigger
        scale_startup_pressure = CustomScale_pressure(window, from_=LL_pressure, to=UL_pressure)
        scale_startup_flowrate = CustomScale_flowrate(window, from_=LL_flowrate, to=UL_flowrate)
        scale_startup_bpm = CustomScale_bpm(window, from_=LL_bpm, to=UL_bpm)
        scale_startup_peep = CustomScale_peep(window, from_=LL_peep, to=UL_peep)
        scale_startup_oxygen = CustomScale_oxygen(window, from_=LL_oxygen, to=UL_oxygen)
        scale_startup_insp_time = CustomScale_insp_time(window, from_=LL_insp_time, to=UL_insp_time)
        scale_startup_vol= CustomScale_vol(window, from_=LL_vol, to=UL_vol)
        scale_startup_pressure_trigger = CustomScale_pressure_trigger(window, from_=LL_triggering_pressure, to=UL_triggering_pressure)
        scale_startup_flow_trigger = CustomScale_flow_trigger(window, from_=LL_triggering_flow, to=UL_triggering_flow)
        scale_startup_ie = CustomScale_ie(window, from_=LL_ie, to=UL_ie)
    create_startup_scales()

    global scale_value_pressure_entered_location_x
    global scale_value_pressure_entered_location_y
    global scale_value_flowrate_entered_location_x
    global scale_value_flowrate_entered_location_y
    global scale_value_peep_entered_location_x
    global scale_value_peep_entered_location_y
    global scale_value_bpm_entered_location_x
    global scale_value_bpm_entered_location_y
    global scale_value_vol_entered_location_x
    global scale_value_vol_entered_location_y
    global scale_value_oxygen_entered_location_x
    global scale_value_oxygen_entered_location_y
    global scale_value_insp_time_entered_location_x
    global scale_value_insp_time_entered_location_y
    global scale_value_ie_entered_location_x
    global scale_value_ie_entered_location_y
    global scale_value_triggering_pressure_entered_location_x
    global scale_value_triggering_pressure_entered_location_y
    global scale_value_triggering_flow_entered_location_x
    global scale_value_triggering_flow_entered_location_y
    global startup_scale_pressure_value
    global startup_scale_flowrate_value
    global startup_scale_peep_value
    global startup_scale_bpm_value
    global startup_scale_vol_value
    global startup_scale_oxygen_value
    global startup_scale_insp_time_value
    global startup_scale_pressure_trigger_value
    global startup_scale_flow_trigger_value
    scale_value_pressure_entered_location_x=0
    scale_value_pressure_entered_location_y=0
    scale_value_flowrate_entered_location_x=0
    scale_value_flowrate_entered_location_y=0
    scale_value_peep_entered_location_x=0
    scale_value_peep_entered_location_y=0
    scale_value_bpm_entered_location_x=0
    scale_value_bpm_entered_location_y=0
    scale_value_vol_entered_location_x=0
    scale_value_vol_entered_location_y=0
    scale_value_oxygen_entered_location_x=0
    scale_value_oxygen_entered_location_y=0
    scale_value_insp_time_entered_location_x=0
    scale_value_insp_time_entered_location_y=0
    scale_value_ie_entered_location_x=0
    scale_value_ie_entered_location_y=0
    scale_value_triggering_pressure_entered_location_x=0
    scale_value_triggering_pressure_entered_location_y=0
    scale_value_triggering_flow_entered_location_x=0
    scale_value_triggering_flow_entered_location_y=0
    startup_scale_pressure_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
    startup_scale_flowrate_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
    startup_scale_peep_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
    startup_scale_bpm_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
    startup_scale_vol_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
    startup_scale_oxygen_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
    startup_scale_insp_time_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
    startup_scale_ie_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
    startup_scale_pressure_trigger_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
    startup_scale_flow_trigger_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))

    # BUTTONS AT THE TOP - start
    global cmv_blank_image_startup_button
    global cmv_green_image_startup_button
    global acv_blank_image_startup_button
    global acv_green_image_startup_button
    global simv_blank_image_startup_button
    global simv_green_image_startup_button
    global cpap_blank_image_startup_button
    global cpap_green_image_startup_button
    global pcv_blank_image_startup_button
    global pcv_green_image_startup_button
    global vcv_blank_image_startup_button
    global vcv_green_image_startup_button
    global Pressure_triggered_blank_image_startup_button
    global Pressure_triggered_green_image_startup_button
    global Flow_triggered_blank_image_startup_button
    global Flow_triggered_green_image_startup_button
            #creating these labels just so that they can be hidden when startup_inputs.hide_everything_in_startup() is called - reason being that when a mode is changed with a button, its labels can only be hidden by place_forget() if they already exist. By default, they're not even created so they can't be hidden when hide_everything_in_startup() is called. So we create them here.
    global property_p_insp
    global unit_p_insp_left
    global p_scale_unit_label
    global property_flowrate
    global unit_flowrate_left
    global flowrate_scale_unit_label
    global property_insp_time
    global unit_insp_time_left
    global property_vol
    global unit_vol_left
    global vol_scale_unit_label
    property_p_insp=Label(window, text="Pressure", bg="black", fg="white",font=("montserrat",18,"normal"))
    unit_p_insp_left=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
    p_scale_unit_label=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
    property_flowrate=Label(window, text="Flowrate", bg="black", fg="white",font=("montserrat",18,"normal"))
    unit_flowrate_left=Label(window, text="Lpm", bg="black", fg="white",font=("montserrat light",9,"normal"))
    flowrate_scale_unit_label=Label(window, text="Lpm", bg="black", fg="white",font=("montserrat light",9,"normal"))
    property_insp_time=Label(window, text="Insptime", bg="black", fg="white",font=("montserrat",18,"normal"))
    unit_insp_time_left=Label(window, text="seconds", bg="black", fg="white",font=("montserrat light",9,"normal"))
    insp_time_scale_unit_label=Label(window, text="seconds", bg="black", fg="white",font=("montserrat light",9,"normal"))
    property_vol=Label(window, text="Tidal Volume", bg="black", fg="white",font=("montserrat",18,"normal"))
    unit_vol_left=Label(window, text="mL", bg="black", fg="white",font=("montserrat light",9,"normal"))
    vol_scale_unit_label=Label(window, text="mL", bg="black", fg="white",font=("montserrat light",9,"normal"))
    global property_pressure_trigger
    global unit_pressure_trigger_left
    global pressure_trigger_scale_unit_label
    property_pressure_trigger=Label(window, text="Trig. Pressure ", bg="black", fg="white",font=("montserrat",18,"normal"))
    unit_pressure_trigger_left=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
    pressure_trigger_scale_unit_label=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
    global property_flow_trigger
    global unit_flow_trigger_left
    global flow_trigger_scale_unit_label
    property_flow_trigger=Label(window, text="Trig. Flow", bg="black", fg="white",font=("montserrat",18,"normal"))
    unit_flow_trigger_left=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
    flow_trigger_scale_unit_label=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))

    def dont_change_modes():
        print("nothing")

    def update_cmv():
        global control_mode
        control_mode = ",CMV,"
        global packed_control_mode
        packed_control_mode="cm"+control_mode
        global acv_green_image_startup_button
        global cmv_blank_image_startup_button
        global simv_green_image_startup_button
        global cpap_green_image_startup_button
        cmv_blank_image_startup_button.place_forget()
        acv_green_image_startup_button.place_forget()
        simv_green_image_startup_button.place_forget()
        cpap_green_image_startup_button.place_forget()
        x_ventilation_modes_first_line = 101
        x_ventilation_modes_second_line = 101
        x_ventilation_modes_third_line = 101
        x_gap_between_buttons = 90
        y_first_line_ventilation_modes = 635
        y_distance_between_lines_ventilation_modes = 50
        cmv_green_image_startup_button.place(x=x_ventilation_modes_first_line , y=y_first_line_ventilation_modes)
        acv_blank_image_startup_button.place(x=x_ventilation_modes_first_line+1*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        simv_blank_image_startup_button.place(x=x_ventilation_modes_first_line+2*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        cpap_blank_image_startup_button.place(x=x_ventilation_modes_first_line+3*x_gap_between_buttons , y=y_first_line_ventilation_modes)
    cmv_blank_image=PhotoImage(file="cmv_blank.gif")
    cmv_blank_image_startup_button=Button(window, image=cmv_blank_image, highlightthickness=0,bd=0,bg="white",command=update_cmv)
    cmv_green_image=PhotoImage(file="cmv_green.gif")
    cmv_green_image_startup_button=Button(window, image=cmv_green_image, highlightthickness=0,bd=0,bg="white",command=dont_change_modes)

    def update_acv():
        global control_mode
        control_mode = ",ACV,"
        global packed_control_mode
        packed_control_mode="cm"+control_mode
        global cmv_green_image_startup_button
        global acv_blank_image_startup_button
        global simv_green_image_startup_button
        global cpap_green_image_startup_button
        cmv_green_image_startup_button.place_forget()
        acv_blank_image_startup_button.place_forget()
        simv_green_image_startup_button.place_forget()
        cpap_green_image_startup_button.place_forget()
        x_ventilation_modes_first_line = 101
        x_ventilation_modes_second_line = 101
        x_ventilation_modes_third_line = 101
        x_gap_between_buttons = 90
        y_first_line_ventilation_modes = 635
        y_distance_between_lines_ventilation_modes = 50
        cmv_blank_image_startup_button.place(x=x_ventilation_modes_first_line , y=y_first_line_ventilation_modes)
        acv_green_image_startup_button.place(x=x_ventilation_modes_first_line+1*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        simv_blank_image_startup_button.place(x=x_ventilation_modes_first_line+2*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        cpap_blank_image_startup_button.place(x=x_ventilation_modes_first_line+3*x_gap_between_buttons , y=y_first_line_ventilation_modes)
    acv_blank_image=PhotoImage(file="acv_blank.gif")
    acv_blank_image_startup_button=Button(window, image=acv_blank_image, highlightthickness=0,bd=0,bg="white",command=update_acv)
    acv_green_image=PhotoImage(file="acv_green.gif")
    acv_green_image_startup_button=Button(window, image=acv_green_image, highlightthickness=0,bd=0,bg="white",command=dont_change_modes)

    def update_simv():
        global control_mode
        control_mode = ",SIMV,"
        global packed_control_mode
        packed_control_mode="cm"+control_mode
        global cmv_green_image_startup_button
        global acv_green_image_startup_button
        global simv_blank_image_startup_button
        global cpap_green_image_startup_button
        cmv_green_image_startup_button.place_forget()
        acv_green_image_startup_button.place_forget()
        simv_blank_image_startup_button.place_forget()
        cpap_green_image_startup_button.place_forget()
        x_ventilation_modes_first_line = 101
        x_ventilation_modes_second_line = 101
        x_ventilation_modes_third_line = 101
        x_gap_between_buttons = 90
        y_first_line_ventilation_modes = 635
        y_distance_between_lines_ventilation_modes = 50
        cmv_blank_image_startup_button.place(x=x_ventilation_modes_first_line , y=y_first_line_ventilation_modes)
        acv_blank_image_startup_button.place(x=x_ventilation_modes_first_line+1*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        simv_green_image_startup_button.place(x=x_ventilation_modes_first_line+2*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        cpap_blank_image_startup_button.place(x=x_ventilation_modes_first_line+3*x_gap_between_buttons , y=y_first_line_ventilation_modes)
    simv_blank_image=PhotoImage(file="simv_blank.gif")
    simv_blank_image_startup_button=Button(window, image=simv_blank_image, highlightthickness=0,bd=0,bg="white",command=update_simv)
    simv_green_image=PhotoImage(file="simv_green.gif")
    simv_green_image_startup_button=Button(window, image=simv_green_image, highlightthickness=0,bd=0,bg="white",command=dont_change_modes)

    def update_cpap():
        global control_mode
        control_mode = ",CPap,"
        global packed_control_mode
        packed_control_mode="cm"+control_mode
        global cmv_green_image_startup_button
        global acv_green_image_startup_button
        global simv_green_image_startup_button
        global cpap_blank_image_startup_button
        cmv_green_image_startup_button.place_forget()
        acv_green_image_startup_button.place_forget()
        simv_green_image_startup_button.place_forget()
        cpap_blank_image_startup_button.place_forget()
        x_ventilation_modes_first_line = 101
        x_ventilation_modes_second_line = 101
        x_ventilation_modes_third_line = 101
        x_gap_between_buttons = 90
        y_first_line_ventilation_modes = 635
        y_distance_between_lines_ventilation_modes = 50
        cmv_blank_image_startup_button.place(x=x_ventilation_modes_first_line , y=y_first_line_ventilation_modes)
        acv_blank_image_startup_button.place(x=x_ventilation_modes_first_line+1*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        simv_blank_image_startup_button.place(x=x_ventilation_modes_first_line+2*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        cpap_green_image_startup_button.place(x=x_ventilation_modes_first_line+3*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        # send_data_to_arduino()
    cpap_blank_image=PhotoImage(file="cpap_blank.gif")
    cpap_blank_image_startup_button=Button(window, image=cpap_blank_image, highlightthickness=0,bd=0,bg="white",command=update_cpap)
    cpap_green_image=PhotoImage(file="cpap_green.gif")
    cpap_green_image_startup_button=Button(window, image=cpap_green_image, highlightthickness=0,bd=0,bg="white",command=dont_change_modes)

    def update_pcv():
        global property_flowrate
        global unit_flowrate_left
        global scale_startup_flowrate
        global startup_scale_flowrate_value
        global flowrate_scale_unit_label
        global property_vol
        global unit_vol_left
        global scale_startup_vol
        global startup_scale_vol_value
        global vol_scale_unit_label
        property_flowrate.place_forget()
        unit_flowrate_left.place_forget()
        scale_startup_flowrate.place_forget()
        startup_scale_flowrate_value.place_forget()
        flowrate_scale_unit_label.place_forget()
        property_vol.place_forget()
        unit_vol_left.place_forget()
        scale_startup_vol.place_forget()
        startup_scale_vol_value.place_forget()
        vol_scale_unit_label.place_forget()
        global mode
        mode = ",pcv,"
        global pcv_blank_image_startup_button
        global vcv_green_image_startup_button
        pcv_blank_image_startup_button.place_forget()
        x_ventilation_modes_first_line = 101
        x_ventilation_modes_second_line = 101
        x_ventilation_modes_third_line = 101
        x_gap_between_buttons = 90
        y_first_line_ventilation_modes = 635
        y_distance_between_lines_ventilation_modes = 50
        pcv_green_image_startup_button.place(x=x_ventilation_modes_second_line , y=y_first_line_ventilation_modes+1*y_distance_between_lines_ventilation_modes)
        vcv_blank_image_startup_button.place(x=x_ventilation_modes_second_line+1*x_gap_between_buttons , y=y_first_line_ventilation_modes+1*y_distance_between_lines_ventilation_modes)
        startup_inputs.hide_everything_in_startup()

        startup_inputs.startup_protocol()
    pcv_blank_image=PhotoImage(file="pcv_blank.gif")
    pcv_blank_image_startup_button=Button(window, image=pcv_blank_image, highlightthickness=0,bd=0,bg="white",command=update_pcv)
    pcv_green_image=PhotoImage(file="pcv_green.gif")
    pcv_green_image_startup_button=Button(window, image=pcv_green_image, highlightthickness=0,bd=0,bg="white",command=dont_change_modes)

    def update_vcv():
        global property_p_insp
        global scale_startup_pressure
        global startup_scale_pressure_value
        global p_scale_unit_label
        global property_insp_time
        global unit_insp_time_left
        global scale_startup_insp_time
        global startup_scale_insp_time_value
        global insp_time_scale_unit_label
        property_p_insp.place_forget()                                                      #hide the labels of the other mode coz we're about to change the mode. Once we do, hide_everything_in_startup() won't hide the labels of the other mode as they're placed in an "if"
        unit_p_insp_left.place_forget()
        scale_startup_pressure.place_forget()
        startup_scale_pressure_value.place_forget()
        p_scale_unit_label.place_forget()
        property_insp_time.place_forget()
        unit_insp_time_left.place_forget()
        scale_startup_insp_time.place_forget()
        startup_scale_insp_time_value.place_forget()
        insp_time_scale_unit_label.place_forget()
        global mode
        mode = ",vcv,"
        global pcv_green_image_startup_button
        global vcv_blank_image_startup_button
        pcv_green_image_startup_button.place_forget()
        vcv_blank_image_startup_button.place_forget()
        x_ventilation_modes_first_line = 101
        x_ventilation_modes_second_line = 101
        x_ventilation_modes_third_line = 101
        x_gap_between_buttons = 90
        y_first_line_ventilation_modes = 635
        y_distance_between_lines_ventilation_modes = 50
        pcv_blank_image_startup_button.place(x=x_ventilation_modes_second_line , y=y_first_line_ventilation_modes+1*y_distance_between_lines_ventilation_modes)
        vcv_green_image_startup_button.place(x=x_ventilation_modes_second_line+1*x_gap_between_buttons , y=y_first_line_ventilation_modes+1*y_distance_between_lines_ventilation_modes)
        startup_inputs.hide_everything_in_startup()
        startup_inputs.startup_protocol()
    vcv_blank_image=PhotoImage(file="vcv_blank.gif")
    vcv_blank_image_startup_button=Button(window, image=vcv_blank_image, highlightthickness=0,bd=0,bg="white",command=update_vcv)
    vcv_green_image=PhotoImage(file="vcv_green.gif")
    vcv_green_image_startup_button=Button(window, image=vcv_green_image, highlightthickness=0,bd=0,bg="white",command=dont_change_modes)

    def update_pressure_trigger_mode():
        global trigger_mode
        trigger_mode = "P"
        global Pressure_triggered_blank_image_startup_button
        global Flow_triggered_green_image_startup_button
        Pressure_triggered_blank_image_startup_button.place_forget()
        Flow_triggered_green_image_startup_button.place_forget()
        x_ventilation_modes_first_line = 101
        x_ventilation_modes_second_line = 101
        x_ventilation_modes_third_line = 101
        x_gap_between_buttons = 90
        y_first_line_ventilation_modes = 635
        y_distance_between_lines_ventilation_modes = 50
        Pressure_triggered_green_image_startup_button.place(x=x_ventilation_modes_third_line , y=y_first_line_ventilation_modes+2*y_distance_between_lines_ventilation_modes)
        Flow_triggered_blank_image_startup_button.place(x=x_ventilation_modes_third_line+1.5*x_gap_between_buttons , y=y_first_line_ventilation_modes+2*y_distance_between_lines_ventilation_modes)
        startup_inputs.pressure_trigger_mode()
    Pressure_triggered_blank_image=PhotoImage(file="Pressure_triggered_blank.gif")
    Pressure_triggered_blank_image_startup_button=Button(window, image=Pressure_triggered_blank_image, highlightthickness=0,bd=0,bg="white",command=update_pressure_trigger_mode)
    Pressure_triggered_green_image=PhotoImage(file="Pressure_triggered_green.gif")
    Pressure_triggered_green_image_startup_button=Button(window, image=Pressure_triggered_green_image, highlightthickness=0,bd=0,bg="white",command=dont_change_modes)

    def update_flow_trigger_mode():
        global trigger_mode
        trigger_mode = "F"
        global Pressure_triggered_green_image_startup_button
        global Flow_triggered_blank_image_startup_button
        Pressure_triggered_green_image_startup_button.place_forget()
        Flow_triggered_blank_image_startup_button.place_forget()
        x_ventilation_modes_first_line = 101
        x_ventilation_modes_second_line = 101
        x_ventilation_modes_third_line = 101
        x_gap_between_buttons = 90
        y_first_line_ventilation_modes = 635
        y_distance_between_lines_ventilation_modes = 50
        Pressure_triggered_blank_image_startup_button.place(x=x_ventilation_modes_third_line , y=y_first_line_ventilation_modes+2*y_distance_between_lines_ventilation_modes)
        Flow_triggered_green_image_startup_button.place(x=x_ventilation_modes_third_line+1.5*x_gap_between_buttons , y=y_first_line_ventilation_modes+2*y_distance_between_lines_ventilation_modes)
        startup_inputs.flow_trigger_mode()
    Flow_triggered_blank_image=PhotoImage(file="Flow_triggered_blank.gif")
    Flow_triggered_blank_image_startup_button=Button(window, image=Flow_triggered_blank_image, highlightthickness=0,bd=0,bg="white",command=update_flow_trigger_mode)
    Flow_triggered_green_image=PhotoImage(file="Flow_triggered_green.gif")
    Flow_triggered_green_image_startup_button=Button(window, image=Flow_triggered_green_image, highlightthickness=0,bd=0,bg="white",command=dont_change_modes)
    # BUTTONS AT THE TOP - end

    global alarm_updates_button_mid_startup
    alarm_updates=PhotoImage(file="alarms.gif")
    alarm_updates_button_mid_startup=Button(window, image=alarm_updates, highlightthickness=0,bd=0,bg="white",command=alarm_scales.update_alarms_mid_startup)
    def place_startup_scales():
        global alarm_updates_button_mid_startup
        alarm_updates_button_mid_startup.place(x=1420,y=750)
        global property_p_insp
        global unit_p_insp_left
        global scale_startup_pressure
        global startup_scale_pressure_value
        global p_scale_unit_label
        global property_flowrate
        global unit_flowrate_left
        global scale_startup_flowrate
        global startup_scale_flowrate_value
        global flowrate_scale_unit_label
        global property_peep
        global unit_peep
        global scale_startup_peep
        global startup_scale_peep_value
        global peep_scale_unit_label
        global property_bpm
        global scale_startup_bpm
        global startup_scale_bpm_value
        global property_vol
        global unit_vol_left
        global scale_startup_vol
        global startup_scale_vol_value
        global vol_scale_unit_label
        global property_oxygen
        global unit_oxygen_left
        global scale_startup_oxygen
        global startup_scale_oxygen_value
        global oxygen_scale_unit_label
        global property_insp_time
        global unit_insp_time_left
        global scale_startup_insp_time
        global startup_scale_insp_time_value
        global insp_time_scale_unit_label
        global property_ie
        global scale_startup_ie
        global startup_scale_ie_value
        global scaling
        scaling="yes"
        global property_being_updated
        global scale_location_status
        scale_location_status="centered"
        y_increment_entire_block=65      # change this to move everything up or down
        line_1_y=50+y_increment_entire_block
        y_increment=75                   #gap b/w lines
        y_unit_increment=35              #gap b/w property and unit
        y_scale_increment=-1             #gap b/w everything else and the scale. Use this to move just the scales up and down
        y_display_increment=10
        line_1_x=100                     # x location of line no.1. Since all labels are inclined verticaly. All have the same x_location. Change this to move everything horizontally
        x_increment=0                    # use this to change things horizontally rather than editing the value of line_1_x
        x_scale_increment=175            #gap b/w label and scale
        x_display_increment=1250         # gap b/w scale and the display to the right side of the scale
        global value_pressure_entered
        global scale_value_pressure_entered_location_x
        global scale_value_pressure_entered_location_y
        global value_flowrate_entered
        global scale_value_flowrate_entered_location_x
        global scale_value_flowrate_entered_location_y
        line_no=1
        line=line_no-1
        if mode==",pcv,":
            property_p_insp=Label(window, text="Pressure", bg="black", fg="white",font=("montserrat",18,"normal"))
            unit_p_insp_left=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
            property_p_insp.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
            unit_p_insp_left.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
            #scale in the middle
            scale_startup_pressure.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
            #values on the right
            startup_scale_pressure_value=Label(window, text=value_pressure_entered, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
            p_scale_unit_label=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
            scale_value_pressure_entered_location_x=line_1_x+x_increment+x_display_increment
            scale_value_pressure_entered_location_y=line_1_y+line*y_increment+y_display_increment
            startup_scale_pressure_value.place(x=scale_value_pressure_entered_location_x,y=scale_value_pressure_entered_location_y, anchor = CENTER)
            p_scale_unit_label.place(x=line_1_x+x_increment+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)

        if mode==",vcv,":
            property_flowrate=Label(window, text="Flowrate", bg="black", fg="white",font=("montserrat",18,"normal"))
            unit_flowrate_left=Label(window, text="Lpm", bg="black", fg="white",font=("montserrat light",9,"normal"))
            property_flowrate.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
            unit_flowrate_left.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
            scale_startup_flowrate.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
            startup_scale_flowrate_value=Label(window, text=value_flowrate_entered, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
            flowrate_scale_unit_label=Label(window, text="Lpm", bg="black", fg="white",font=("montserrat light",9,"normal"))
            scale_value_flowrate_entered_location_x=line_1_x+x_increment+x_display_increment
            scale_value_flowrate_entered_location_y=line_1_y+line*y_increment+y_display_increment
            startup_scale_flowrate_value.place(x=scale_value_flowrate_entered_location_x,y=scale_value_flowrate_entered_location_y, anchor = CENTER)
            flowrate_scale_unit_label.place(x=line_1_x+x_increment+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)
        global value_peep_entered
        global scale_value_peep_entered_location_x
        global scale_value_peep_entered_location_y
        line_no=2
        line=line_no-1
        property_peep=Label(window, text="PEEP", bg="black", fg="white",font=("montserrat",18,"normal"))
        unit_peep=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
        property_peep.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        unit_peep.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
        scale_startup_peep.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
        startup_scale_peep_value=Label(window, text=value_peep_entered, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        peep_scale_unit_label=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_value_peep_entered_location_x=line_1_x+x_increment+x_display_increment
        scale_value_peep_entered_location_y=line_1_y+line*y_increment+y_display_increment
        startup_scale_peep_value.place(x=scale_value_peep_entered_location_x,y=scale_value_peep_entered_location_y, anchor = CENTER)
        peep_scale_unit_label.place(x=line_1_x+x_increment+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)
        global value_bpm_entered
        global scale_value_bpm_entered_location_x
        global scale_value_bpm_entered_location_y
        line_no=3
        line=line_no-1
        property_bpm=Label(window, text="BPM", bg="black", fg="white",font=("montserrat",18,"normal"))
        property_bpm.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        scale_startup_bpm.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
        startup_scale_bpm_value=Label(window, text=value_bpm_entered, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        scale_value_bpm_entered_location_x=line_1_x+x_increment+x_display_increment
        scale_value_bpm_entered_location_y=line_1_y+line*y_increment+y_display_increment
        startup_scale_bpm_value.place(x=scale_value_bpm_entered_location_x,y=scale_value_bpm_entered_location_y, anchor = CENTER)
        global value_oxygen_entered
        global scale_value_oxygen_entered_location_x
        global scale_value_oxygen_entered_location_y
        line_no=4
        line=line_no-1
        property_oxygen=Label(window, text="Oxygen", bg="black", fg="white",font=("montserrat",18,"normal"))
        unit_oxygen_left=Label(window, text="%", bg="black", fg="white",font=("montserrat light",9,"normal"))
        property_oxygen.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        unit_oxygen_left.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
        scale_startup_oxygen.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
        startup_scale_oxygen_value=Label(window, text=value_oxygen_entered, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        oxygen_scale_unit_label=Label(window, text="%", bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_value_oxygen_entered_location_x=line_1_x+x_increment+x_display_increment
        scale_value_oxygen_entered_location_y=line_1_y+line*y_increment+y_display_increment
        startup_scale_oxygen_value.place(x=scale_value_oxygen_entered_location_x,y=scale_value_oxygen_entered_location_y, anchor = CENTER)
        oxygen_scale_unit_label.place(x=line_1_x+x_increment+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)
        global value_insp_time_entered
        global scale_value_insp_time_entered_location_x
        global scale_value_insp_time_entered_location_y
        global value_vol_entered
        global scale_value_vol_entered_location_x
        global scale_value_vol_entered_location_y
        line_no=5
        line=line_no-1
        if mode==",pcv,":
            property_insp_time=Label(window, text="Insptime", bg="black", fg="white",font=("montserrat",18,"normal"))
            unit_insp_time_left=Label(window, text="seconds", bg="black", fg="white",font=("montserrat light",9,"normal"))
            property_insp_time.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
            unit_insp_time_left.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
            scale_startup_insp_time.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
            startup_scale_insp_time_value=Label(window, text=value_insp_time_entered, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
            insp_time_scale_unit_label=Label(window, text="seconds", bg="black", fg="white",font=("montserrat light",9,"normal"))
            scale_value_insp_time_entered_location_x=line_1_x+x_increment+x_display_increment
            scale_value_insp_time_entered_location_y=line_1_y+line*y_increment+y_display_increment
            startup_scale_insp_time_value.place(x=scale_value_insp_time_entered_location_x,y=scale_value_insp_time_entered_location_y, anchor = CENTER)
            insp_time_scale_unit_label.place(x=line_1_x+x_increment+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)
        if mode==",vcv,":
            property_vol=Label(window, text="Tidal Volume", bg="black", fg="white",font=("montserrat",18,"normal"))
            unit_vol_left=Label(window, text="mL", bg="black", fg="white",font=("montserrat light",9,"normal"))
            property_vol.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
            unit_vol_left.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
            scale_startup_vol.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
            startup_scale_vol_value=Label(window, text=value_vol_entered, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
            vol_scale_unit_label=Label(window, text="mL", bg="black", fg="white",font=("montserrat light",9,"normal"))
            scale_value_vol_entered_location_x=line_1_x+x_increment+x_display_increment
            scale_value_vol_entered_location_y=line_1_y+line*y_increment+y_display_increment
            startup_scale_vol_value.place(x=scale_value_vol_entered_location_x,y=scale_value_vol_entered_location_y, anchor = CENTER)
            vol_scale_unit_label.place(x=line_1_x+x_increment+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)
        global value_ie_entered
        global scale_value_ie_entered_location_x
        global scale_value_ie_entered_location_y
        line_no=6
        line=line_no-1
        property_ie=Label(window, text="IE", bg="black", fg="white",font=("montserrat",18,"normal"))
        property_ie.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        scale_startup_ie.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
        startup_scale_ie_value=Label(window, text="1:"+str(value_ie_entered), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        scale_value_ie_entered_location_x=line_1_x+x_increment+x_display_increment
        scale_value_ie_entered_location_y=line_1_y+line*y_increment+y_display_increment
        startup_scale_ie_value.place(x=scale_value_ie_entered_location_x,y=scale_value_ie_entered_location_y, anchor = CENTER)
        line_no=7
        line=line_no-1
        if trigger_mode=="P":
            startup_inputs.pressure_trigger_mode()
        if trigger_mode=="F":
            startup_inputs.flow_trigger_mode()
        global cmv_blank_image_startup_button
        global cmv_green_image_startup_button
        global acv_blank_image_startup_button
        global acv_green_image_startup_button
        global simv_blank_image_startup_button
        global simv_green_image_startup_button
        global cpap_blank_image_startup_button
        global cpap_green_image_startup_button
        global pcv_blank_image_startup_button
        global pcv_green_image_startup_button
        global vcv_blank_image_startup_button
        global vcv_green_image_startup_button
        global Pressure_triggered_blank_image_startup_button
        global Pressure_triggered_green_image_startup_button
        global Flow_triggered_blank_image_startup_button
        global Flow_triggered_green_image_startup_button
        x_ventilation_modes_first_line = 101
        x_ventilation_modes_second_line = 101
        x_ventilation_modes_third_line = 101
        x_gap_between_buttons = 90
        y_first_line_ventilation_modes = 635
        y_distance_between_lines_ventilation_modes = 50
        if control_mode == ",CMV,":
            cmv_green_image_startup_button.place(x=x_ventilation_modes_first_line , y=y_first_line_ventilation_modes)
            acv_blank_image_startup_button.place(x=x_ventilation_modes_first_line+1*x_gap_between_buttons , y=y_first_line_ventilation_modes)
            simv_blank_image_startup_button.place(x=x_ventilation_modes_first_line+2*x_gap_between_buttons , y=y_first_line_ventilation_modes)
            cpap_blank_image_startup_button.place(x=x_ventilation_modes_first_line+3*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        if control_mode == ",ACV,":
            cmv_blank_image_startup_button.place(x=x_ventilation_modes_first_line , y=y_first_line_ventilation_modes)
            acv_green_image_startup_button.place(x=x_ventilation_modes_first_line+1*x_gap_between_buttons , y=y_first_line_ventilation_modes)
            simv_blank_image_startup_button.place(x=x_ventilation_modes_first_line+2*x_gap_between_buttons , y=y_first_line_ventilation_modes)
            cpap_blank_image_startup_button.place(x=x_ventilation_modes_first_line+3*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        if control_mode == ",SIMV,":
            cmv_blank_image_startup_button.place(x=x_ventilation_modes_first_line , y=y_first_line_ventilation_modes)
            acv_blank_image_startup_button.place(x=x_ventilation_modes_first_line+1*x_gap_between_buttons , y=y_first_line_ventilation_modes)
            simv_green_image_startup_button.place(x=x_ventilation_modes_first_line+2*x_gap_between_buttons , y=y_first_line_ventilation_modes)
            cpap_blank_image_startup_button.place(x=x_ventilation_modes_first_line+3*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        if control_mode == ",CPap,":
            cmv_blank_image_startup_button.place(x=x_ventilation_modes_first_line , y=y_first_line_ventilation_modes)
            acv_blank_image_startup_button.place(x=x_ventilation_modes_first_line+1*x_gap_between_buttons , y=y_first_line_ventilation_modes)
            simv_blank_image_startup_button.place(x=x_ventilation_modes_first_line+2*x_gap_between_buttons , y=y_first_line_ventilation_modes)
            cpap_green_image_startup_button.place(x=x_ventilation_modes_first_line+3*x_gap_between_buttons , y=y_first_line_ventilation_modes)
        if mode == ",pcv,":
            pcv_green_image_startup_button.place(x=x_ventilation_modes_second_line , y=y_first_line_ventilation_modes+1*y_distance_between_lines_ventilation_modes)
            vcv_blank_image_startup_button.place(x=x_ventilation_modes_second_line+1*x_gap_between_buttons , y=y_first_line_ventilation_modes+1*y_distance_between_lines_ventilation_modes)
        if mode == ",vcv,":
            pcv_blank_image_startup_button.place(x=x_ventilation_modes_second_line , y=y_first_line_ventilation_modes+1*y_distance_between_lines_ventilation_modes)
            vcv_green_image_startup_button.place(x=x_ventilation_modes_second_line+1*x_gap_between_buttons , y=y_first_line_ventilation_modes+1*y_distance_between_lines_ventilation_modes)
        if trigger_mode == "P":
            Pressure_triggered_green_image_startup_button.place(x=x_ventilation_modes_third_line , y=y_first_line_ventilation_modes+2*y_distance_between_lines_ventilation_modes)
            Flow_triggered_blank_image_startup_button.place(x=x_ventilation_modes_third_line+1.5*x_gap_between_buttons , y=y_first_line_ventilation_modes+2*y_distance_between_lines_ventilation_modes)
        if trigger_mode == "F":
            Pressure_triggered_blank_image_startup_button.place(x=x_ventilation_modes_third_line , y=y_first_line_ventilation_modes+2*y_distance_between_lines_ventilation_modes)
            Flow_triggered_green_image_startup_button.place(x=x_ventilation_modes_third_line+1.5*x_gap_between_buttons , y=y_first_line_ventilation_modes+2*y_distance_between_lines_ventilation_modes)

    def place_pressure_trigger_scale():
        global property_pressure_trigger
        global unit_pressure_trigger_left
        global scale_startup_pressure_trigger
        global startup_scale_pressure_trigger_value
        global pressure_trigger_scale_unit_label
        y_increment_entire_block=65                 # change this to move everything up or down
        line_1_y=50+y_increment_entire_block
        y_increment=75                               #gap b/w lines
        y_unit_increment=35                          #gap b/w property and unit
        y_scale_increment=-1                         #gap b/w everything else and the scale. Use this to move just the scales up and down
        y_display_increment=10
        line_1_x=100                                 # x location of line no.1. Since all labels are inclined verticaly. All have the same x_location. Change this to move everything horizontally
        x_increment=0                                # use this to change things horizontally rather than editing the value of line_1_x
        x_scale_increment=175                        #gap b/w label and scale
        x_display_increment=1250                     # gap b/w scale and the display to the right side of the scale
        global value_triggering_pressure_entered
        global scale_value_triggering_pressure_entered_location_x
        global scale_value_triggering_pressure_entered_location_y
        line_no=7
        line=line_no-1
        property_pressure_trigger=Label(window, text="Trig. Pressure ", bg="black", fg="white",font=("montserrat",18,"normal"))
        unit_pressure_trigger_left=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
        property_pressure_trigger.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        unit_pressure_trigger_left.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
        scale_startup_pressure_trigger.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
        startup_scale_pressure_trigger_value=Label(window, text=value_triggering_pressure_entered, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        pressure_trigger_scale_unit_label=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_value_triggering_pressure_entered_location_x=line_1_x+x_increment+x_display_increment
        scale_value_triggering_pressure_entered_location_y=line_1_y+line*y_increment+y_display_increment
        startup_scale_pressure_trigger_value.place(x=scale_value_triggering_pressure_entered_location_x,y=scale_value_triggering_pressure_entered_location_y, anchor = CENTER)
        pressure_trigger_scale_unit_label.place(x=line_1_x+x_increment+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)

    def place_flow_trigger_scale():
        global property_flow_trigger
        global unit_flow_trigger_left
        global scale_startup_flow_trigger
        global startup_scale_flow_trigger_value
        global flow_trigger_scale_unit_label
        y_increment_entire_block=65    # change this to move everything up or down
        line_1_y=50+y_increment_entire_block
        y_increment=75 #gap b/w lines
        y_unit_increment=35 #gap b/w property and unit
        y_scale_increment=-1 #gap b/w everything else and the scale. Use this to move just the scales up and down
        y_display_increment=10
        line_1_x=100    # x location of line no.1. Since all labels are inclined verticaly. All have the same x_location. Change this to move everything horizontally
        x_increment=0   # use this to change things horizontally rather than editing the value of line_1_x
        x_scale_increment=175 #gap b/w label and scale
        x_display_increment=1250 # gap b/w scale and the display to the right side of the scale
        global value_triggering_flow_entered
        global scale_value_triggering_flow_entered_location_x
        global scale_value_triggering_flow_entered_location_y
        line_no=7
        line=line_no-1
        property_flow_trigger=Label(window, text="Trig. Flow", bg="black", fg="white",font=("montserrat",18,"normal"))
        unit_flow_trigger_left=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
        property_flow_trigger.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        unit_flow_trigger_left.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
        scale_startup_flow_trigger.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
        startup_scale_flow_trigger_value=Label(window, text=value_triggering_flow_entered, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        flow_trigger_scale_unit_label=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_value_triggering_flow_entered_location_x=line_1_x+x_increment+x_display_increment
        scale_value_triggering_flow_entered_location_y=line_1_y+line*y_increment+y_display_increment
        startup_scale_flow_trigger_value.place(x=scale_value_triggering_flow_entered_location_x,y=scale_value_triggering_flow_entered_location_y, anchor = CENTER)
        flow_trigger_scale_unit_label.place(x=line_1_x+x_increment+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)

    def pressure_trigger_mode():
        global property_pressure_trigger
        global unit_pressure_trigger_left
        global scale_startup_pressure_trigger
        global startup_scale_pressure_trigger_value
        global pressure_trigger_scale_unit_label
        property_pressure_trigger.place_forget()
        unit_pressure_trigger_left.place_forget()
        scale_startup_pressure_trigger.place_forget()
        startup_scale_pressure_trigger_value.place_forget()
        pressure_trigger_scale_unit_label.place_forget()
        global property_flow_trigger
        global unit_flow_trigger_left
        global scale_startup_flow_trigger
        global startup_scale_flow_trigger_value
        global flow_trigger_scale_unit_label
        property_flow_trigger.place_forget()
        unit_flow_trigger_left.place_forget()
        scale_startup_flow_trigger.place_forget()
        startup_scale_flow_trigger_value.place_forget()
        flow_trigger_scale_unit_label.place_forget()
        # global pressure_triggered_button
        # global flow_triggered_button
        # flow_triggered_button.place_forget()
        # pressure_triggered_button.place_forget()
        global trigger_mode
        trigger_mode="P"
        startup_inputs.place_pressure_trigger_scale()
    # global pressure_triggered_button
    # pressure_triggered_image=PhotoImage(file="Pressure_triggered.gif")
    # pressure_triggered_button=Button(window, image=pressure_triggered_image, highlightthickness=0,bd=0,bg="white",command=pressure_trigger_mode)
    # pressure_triggered_button.place(x=350,y=570)

    def flow_trigger_mode():
        # global property_pressure_trigger
        # global unit_pressure_trigger_left
        # global pressure_trigger_scale_unit_label
        # property_pressure_trigger.place_forget()
        # unit_pressure_trigger_left.place_forget()
        # pressure_trigger_scale_unit_label.place_forget()
        # global property_flow_trigger
        # global unit_flow_trigger_left
        # global flow_trigger_scale_unit_label
        # property_flow_trigger.place_forget()
        # unit_flow_trigger_left.place_forget()
        # flow_trigger_scale_unit_label.place_forget()
        global property_pressure_trigger
        global unit_pressure_trigger_left
        global scale_startup_pressure_trigger
        global startup_scale_pressure_trigger_value
        global pressure_trigger_scale_unit_label
        property_pressure_trigger.place_forget()
        unit_pressure_trigger_left.place_forget()
        scale_startup_pressure_trigger.place_forget()
        startup_scale_pressure_trigger_value.place_forget()
        pressure_trigger_scale_unit_label.place_forget()
        global property_flow_trigger
        global unit_flow_trigger_left
        global scale_startup_flow_trigger
        global startup_scale_flow_trigger_value
        global flow_trigger_scale_unit_label
        property_flow_trigger.place_forget()
        unit_flow_trigger_left.place_forget()
        scale_startup_flow_trigger.place_forget()
        startup_scale_flow_trigger_value.place_forget()
        flow_trigger_scale_unit_label.place_forget()

        # global pressure_triggered_button
        # global flow_triggered_button
        # flow_triggered_button.place_forget()
        # pressure_triggered_button.place_forget()
        global trigger_mode
        trigger_mode="F"
        startup_inputs.place_flow_trigger_scale()
    # global flow_triggered_button
    # flow_triggered_image=PhotoImage(file="Flow_triggered.gif")
    # flow_triggered_button=Button(window, image=flow_triggered_image, highlightthickness=0,bd=0,bg="white",command=flow_trigger_mode)
    # flow_triggered_button.place(x=850,y=570)

    def hide_the_scales_in_startup():   #this function hides the scales placed in startup
        global alarm_updates_button_mid_startup
        alarm_updates_button_mid_startup.place_forget()
        global property_p_insp
        global unit_p_insp_left
        global scale_startup_pressure
        global startup_scale_pressure_value
        global p_scale_unit_label
        global property_flowrate
        global unit_flowrate_left
        global scale_startup_flowrate
        global startup_scale_flowrate_value
        global flowrate_scale_unit_label
        global property_peep
        global unit_peep
        global scale_startup_peep
        global startup_scale_peep_value
        global peep_scale_unit_label
        global property_bpm
        global scale_startup_bpm
        global startup_scale_bpm_value
        global property_vol
        global unit_vol_left
        global scale_startup_vol
        global startup_scale_vol_value
        global vol_scale_unit_label
        global property_oxygen
        global unit_oxygen_left
        global scale_startup_oxygen
        global startup_scale_oxygen_value
        global oxygen_scale_unit_label
        global property_insp_time
        global unit_insp_time_left
        global scale_startup_insp_time
        global startup_scale_insp_time_value
        global insp_time_scale_unit_label
        global property_ie
        global unit_ie_left
        global scale_startup_ie
        global startup_scale_ie_value
        global ie_scale_unit_label
        global property_pressure_trigger
        global unit_pressure_trigger_left
        global scale_startup_pressure_trigger
        global startup_scale_pressure_trigger_value
        global pressure_trigger_scale_unit_label
        global property_flow_trigger
        global unit_flow_trigger_left
        global scale_startup_flow_trigger
        global startup_scale_flow_trigger_value
        global flow_trigger_scale_unit_label
        if mode==",pcv,":
            property_p_insp.place_forget()
            unit_p_insp_left.place_forget()
            scale_startup_pressure.place_forget()
            startup_scale_pressure_value.place_forget()
            p_scale_unit_label.place_forget()
        if mode==",vcv,":
            property_flowrate.place_forget()
            unit_flowrate_left.place_forget()
            scale_startup_flowrate.place_forget()
            startup_scale_flowrate_value.place_forget()
            flowrate_scale_unit_label.place_forget()
        property_peep.place_forget()
        unit_peep.place_forget()
        scale_startup_peep.place_forget()
        startup_scale_peep_value.place_forget()
        peep_scale_unit_label.place_forget()
        property_bpm.place_forget()
        scale_startup_bpm.place_forget()
        startup_scale_bpm_value.place_forget()
        if mode==",pcv,":
            property_insp_time.place_forget()
            unit_insp_time_left.place_forget()
            scale_startup_insp_time.place_forget()
            startup_scale_insp_time_value.place_forget()
            insp_time_scale_unit_label.place_forget()
        if mode==",vcv,":
            property_vol.place_forget()
            unit_vol_left.place_forget()
            scale_startup_vol.place_forget()
            startup_scale_vol_value.place_forget()
            vol_scale_unit_label.place_forget()
        property_oxygen.place_forget()
        unit_oxygen_left.place_forget()
        scale_startup_oxygen.place_forget()
        startup_scale_oxygen_value.place_forget()
        oxygen_scale_unit_label.place_forget()
        property_ie.place_forget()
        scale_startup_ie.place_forget()
        startup_scale_ie_value.place_forget()
        if trigger_mode=="P":                               #hide the pressure triggering labels if pressure triggered mode was selected
            property_pressure_trigger.place_forget()
            unit_pressure_trigger_left.place_forget()
            scale_startup_pressure_trigger.place_forget()
            startup_scale_pressure_trigger_value.place_forget()
            pressure_trigger_scale_unit_label.place_forget()
        if trigger_mode=="F":                               #hide the flow triggering labels if flow triggered mode was selected
            property_flow_trigger.place_forget()
            unit_flow_trigger_left.place_forget()
            scale_startup_flow_trigger.place_forget()
            startup_scale_flow_trigger_value.place_forget()
            flow_trigger_scale_unit_label.place_forget()
        global cmv_blank_image_startup_button
        global cmv_green_image_startup_button
        global acv_blank_image_startup_button
        global acv_green_image_startup_button
        global simv_blank_image_startup_button
        global simv_green_image_startup_button
        global cpap_blank_image_startup_button
        global cpap_green_image_startup_button
        global pcv_blank_image_startup_button
        global pcv_green_image_startup_button
        global vcv_blank_image_startup_button
        global vcv_green_image_startup_button
        global Pressure_triggered_blank_image_startup_button
        global Pressure_triggered_green_image_startup_button
        global Flow_triggered_blank_image_startup_button
        global Flow_triggered_green_image_startup_button
        global user_entered_values_image_label
        cmv_blank_image_startup_button.place_forget()
        cmv_green_image_startup_button.place_forget()
        acv_blank_image_startup_button.place_forget()
        acv_green_image_startup_button.place_forget()
        simv_blank_image_startup_button.place_forget()
        simv_green_image_startup_button.place_forget()
        cpap_blank_image_startup_button.place_forget()
        cpap_green_image_startup_button.place_forget()
        pcv_blank_image_startup_button.place_forget()
        pcv_green_image_startup_button.place_forget()
        vcv_blank_image_startup_button.place_forget()
        vcv_green_image_startup_button.place_forget()
        Pressure_triggered_blank_image_startup_button.place_forget()
        Pressure_triggered_green_image_startup_button.place_forget()
        Flow_triggered_blank_image_startup_button.place_forget()
        Flow_triggered_green_image_startup_button.place_forget()
        user_entered_values_image_label.place_forget()

    def hide_testing_and_next_buttons():    #this function just hides the two buttons that are placed at startup
        global next_startup_button
        global test_startup_button
        next_startup_button.place_forget()
        test_startup_button.place_forget()
    # def hide_triggering_buttons():
    #     global flow_triggered_button
    #     global pressure_triggered_button
    #     flow_triggered_button.place_forget()
    #     pressure_triggered_button.place_forget()

    def hide_everything_in_startup():       #this function hides everything in startup. buttons and scales, both.
        startup_inputs.hide_the_scales_in_startup()
        startup_inputs.hide_testing_and_next_buttons()
        # startup_inputs.hide_triggering_buttons()

    def start_ventilating():                #this button quits the startup and starts full mode ventilation
        # time.sleep(2)
        startup_inputs.hide_everything_in_startup()
        start_ventilating_in_full_mode()

    def test_ventilation():                 #this button quits the startup and starts test mode ventilation for a small amount of time and then startup resumes
        startup_inputs.hide_everything_in_startup()
        test_protocol()

    global next_startup_button
    global test_startup_button
    next_startup_button_image=PhotoImage(file="next.gif")
    next_startup_button=Button(window, image=next_startup_button_image, highlightthickness=0,bd=0,bg="white",command=start_ventilating)
    test_startup_button_image=PhotoImage(file="test.gif")
    test_startup_button=Button(window, image=test_startup_button_image, highlightthickness=0,bd=0,bg="white",command=test_ventilation)


    def place_all_startup_buttons():
        global next_startup_button
        global test_startup_button
        next_startup_button.place(x=test_startup_x_location,y=test_startup_y_location)
        test_startup_button.place(x=next_startup_x_location,y=next_startup_y_location)


    def button_configuration_startup_testing_finished_phase():
        global next_startup_button
        global test_startup_button
        next_startup_button.place(x=test_startup_x_location,y=test_startup_y_location)
        test_startup_button.place(x=next_startup_x_location,y=next_startup_y_location)
        # global flow_triggered_button
        # global pressure_triggered_button
        # flow_triggered_button.place(x=850,y=570)
        # pressure_triggered_button.place(x=350,y=570)

    def button_configuration_startup_initial_phase():
        global test_startup_x_location
        global test_startup_y_location
        global next_startup_x_location
        global next_startup_y_location
        test_startup_x_location=750
        test_startup_y_location=675
        gap_between_buttons=-150
        next_startup_x_location=test_startup_x_location+gap_between_buttons
        next_startup_y_location=test_startup_y_location
        global test_startup_button
        test_startup_button.place(x=test_startup_x_location,y=test_startup_y_location)
        # global flow_triggered_button
        # global pressure_triggered_button
        # flow_triggered_button.place(x=850,y=570)
        # pressure_triggered_button.place(x=350,y=570)

    def startup_protocol():
        startup_inputs.place_startup_scales()                                       #place all scales for startup
        if testing_time_start<testing_time_end:
            startup_inputs.button_configuration_startup_initial_phase()             #place testing button with the flow and pressure buttons in standard display - next button is not originally placed
        if testing_time_start>=testing_time_end:
            startup_inputs.button_configuration_startup_testing_finished_phase()    #place both testing and next once testing is done

testing_time_start=0
testing_time_end=0
testing_time_end=testing_time_end+2
testing_time_display=Label(window, text="dummy for initialization", bg="black", fg="white",font=("montserrat",18,"normal"))
def time_testing_display():
    global testing_time_start
    global testing_time_display
    time_display=str(testing_time_start)+" seconds"
    testing_time_display.place_forget()
    testing_time_display=Label(window, text=time_display, bg="black", fg="white",font=("montserrat",18,"normal"))
    testing_time_start=testing_time_start+1
    if testing_time_start<testing_time_end:
        window.after(30,time_testing_display)
        testing_time_display.place(x=100,y=100)
    if testing_time_start>=testing_time_end:
        # print("time's up")
        testing_time_display.place_forget()
        stop_ventilating()
        startup_inputs.startup_protocol()

def test_protocol():
    global testing_time_start
    global testing_time_end
    testing_time_start=0
    time_testing_display()
    send_data_to_arduino()
    monitoring.start_monitoring()

def send_data_to_arduino():
    global packed_manoeuvre
    if mode==",pcv,":
        if trigger_mode=="P":
            str_pack=str(len(mode))+"s"+str(len(packed_pressure))+"s"+str(len(packed_peep))+"s"+str(len(packed_oxygen))+"s"+str(len(packed_bpm))+"s"+str(len(packed_vol))+"s"+str(len(packed_insp_time))+"s"+str(len(packed_triggering_pressure))+"s"+str(len(packed_ie))+"s"+str(len(packed_manoeuvre))+"s"+str(len(packed_control_mode))+"s"
            string_to_send=struct.pack(str_pack, mode.encode('UTF-8'), packed_pressure.encode('UTF-8'),packed_peep.encode('UTF-8'),packed_oxygen.encode('UTF-8'),packed_bpm.encode('UTF-8'),packed_vol.encode('UTF-8'),packed_insp_time.encode('UTF-8'),packed_triggering_pressure.encode('UTF-8'),packed_ie.encode('UTF-8'),packed_manoeuvre.encode('UTF-8'),packed_control_mode.encode('UTF-8'))
            arduino_data.write(string_to_send)
        if trigger_mode=="F":
            str_pack=str(len(mode))+"s"+str(len(packed_pressure))+"s"+str(len(packed_peep))+"s"+str(len(packed_oxygen))+"s"+str(len(packed_bpm))+"s"+str(len(packed_vol))+"s"+str(len(packed_insp_time))+"s"+str(len(packed_triggering_flow))+"s"+str(len(packed_ie))+"s"+str(len(packed_manoeuvre))+"s"+str(len(packed_control_mode))+"s"
            string_to_send=struct.pack(str_pack, mode.encode('UTF-8'), packed_pressure.encode('UTF-8'),packed_peep.encode('UTF-8'),packed_oxygen.encode('UTF-8'),packed_bpm.encode('UTF-8'),packed_vol.encode('UTF-8'),packed_insp_time.encode('UTF-8'),packed_triggering_flow.encode('UTF-8'),packed_ie.encode('UTF-8'),packed_manoeuvre.encode('UTF-8'),packed_control_mode.encode('UTF-8'))
            arduino_data.write(string_to_send)
    if mode==",vcv,":
        if trigger_mode=="P":
            str_pack=str(len(mode))+"s"+str(len(packed_flowrate))+"s"+str(len(packed_peep))+"s"+str(len(packed_oxygen))+"s"+str(len(packed_bpm))+"s"+str(len(packed_vol))+"s"+str(len(packed_triggering_pressure))+"s"+str(len(packed_ie))+"s"+str(len(packed_manoeuvre))+"s"+str(len(packed_control_mode))+"s"
            string_to_send=struct.pack(str_pack, mode.encode('UTF-8'), packed_flowrate.encode('UTF-8'),packed_peep.encode('UTF-8'),packed_oxygen.encode('UTF-8'),packed_bpm.encode('UTF-8'),packed_vol.encode('UTF-8'),packed_triggering_pressure.encode('UTF-8'),packed_ie.encode('UTF-8'),packed_manoeuvre.encode('UTF-8'),packed_control_mode.encode('UTF-8'))
            arduino_data.write(string_to_send)
        if trigger_mode=="F":
            str_pack=str(len(mode))+"s"+str(len(packed_flowrate))+"s"+str(len(packed_peep))+"s"+str(len(packed_oxygen))+"s"+str(len(packed_bpm))+"s"+str(len(packed_vol))+"s"+str(len(packed_triggering_flow))+"s"+str(len(packed_ie))+"s"+str(len(packed_manoeuvre))+"s"+str(len(packed_control_mode))+"s"
            string_to_send=struct.pack(str_pack, mode.encode('UTF-8'), packed_flowrate.encode('UTF-8'),packed_peep.encode('UTF-8'),packed_oxygen.encode('UTF-8'),packed_bpm.encode('UTF-8'),packed_vol.encode('UTF-8'),packed_triggering_flow.encode('UTF-8'),packed_ie.encode('UTF-8'),packed_manoeuvre.encode('UTF-8'),packed_control_mode.encode('UTF-8'))
            arduino_data.write(string_to_send)
    packed_manoeuvre="m,6,"
    print(string_to_send)

def stop_ventilating():
    ventilation_inputs.hide_scale_and_buttons()
    monitoring.stop_monitoring()

def start_ventilating_in_full_mode():
    ventilation_inputs.place_user_entered_buttons()
    monitoring.start_monitoring()

startup_inputs.startup_protocol()


# alarm_scales.place_alarm_scales()



window.mainloop()
