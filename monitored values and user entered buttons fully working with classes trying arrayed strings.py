from tkinter import *
from tkinter import ttk
import time
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


scaling="not"
property_being_updated="none"
unit_of_property_being_updated="none"
value_pressure_entered=0
value_vol_entered=0
value_peep_entered=0
value_bpm_entered=0
value_oxygen_entered=0

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
    global UL_pressure
    global LL_pressure
    global UL_peep
    global LL_peep
    global UL_pplat
    global LL_pplat
    global UL_bpm
    global LL_bpm
    global UL_oxygen
    global LL_oxygen
    global UL_vol
    global LL_vol
    global UL_insp_time
    global LL_insp_time
    global UL_triggering_pressure
    global LL_triggering_pressure
    global UL_triggering_flow
    global LL_triggering_flow
    UL_pressure=35
    LL_pressure=5
    UL_peep=35
    LL_peep=5
    UL_pplat=35
    LL_pplat=5
    UL_bpm=30
    LL_bpm=15
    UL_oxygen=70
    LL_oxygen=40
    UL_vol=3000
    LL_vol=2600
    UL_insp_time=3
    LL_insp_time=1
    UL_triggering_pressure=40
    LL_triggering_pressure=25
    UL_triggering_flow=120
    LL_triggering_flow=90
    class testing_inputs_and_playing_alarms():
        global notification_label_pressure
        global notification_label_peep
        global notification_label_pplat
        global notification_label_bpm
        global notification_label_oxygen
        global notification_label_pressure
        notification_label_pressure=Label(window, text="fuck this", bg="black", fg="white",font=("montserrat light",12,"normal"))
        notification_label_peep=Label(window, text="fuck this", bg="black", fg="white",font=("montserrat light",12,"normal"))
        notification_label_pplat=Label(window, text="fuck this", bg="black", fg="white",font=("montserrat light",12,"normal"))
        notification_label_bpm=Label(window, text="fuck this", bg="black", fg="white",font=("montserrat light",12,"normal"))
        notification_label_oxygen=Label(window, text="fuck this", bg="black", fg="white",font=("montserrat light",12,"normal"))

        def notifications(property, displayed_string):
            global notification_label_pressure
            global notification_label_peep
            global notification_label_pplat
            global notification_label_bpm
            global notification_label_oxygen
            global notification_label_pressure
            if displayed_string=="P clear":
                notification_label_pressure.place_forget()
            if displayed_string=="peep clear":
                notification_label_peep.place_forget()
            if displayed_string=="pplat clear":
                notification_label_pplat.place_forget()
            if displayed_string=="bpm clear":
                notification_label_bpm.place_forget()
            if displayed_string=="oxygen clear":
                notification_label_oxygen.place_forget()

            x_notifications=10
            y_notifications=600
            gap_notifications_y=30
            if property=="P" and displayed_string!="P clear":
                line_number=1
                line=line_number-1
                notification_label_pressure=Label(window, text=displayed_string, bg="red", fg="white",font=("montserrat light",12,"normal"))
                notification_label_pressure.place(x=x_notifications,y=y_notifications+line*gap_notifications_y)
            if property=="peep" and displayed_string!="peep clear":
                line_number=2
                line=line_number-1
                notification_label_peep=Label(window, text=displayed_string, bg="red", fg="white",font=("montserrat light",12,"normal"))
                notification_label_peep.place(x=x_notifications,y=y_notifications+line*gap_notifications_y)
            if property=="pplat" and displayed_string!="pplat clear":
                line_number=3
                line=line_number-1
                notification_label_pplat=Label(window, text=displayed_string, bg="red", fg="white",font=("montserrat light",12,"normal"))
                notification_label_pplat.place(x=x_notifications,y=y_notifications+line*gap_notifications_y0)
            if property=="bpm" and displayed_string!="bpm clear":
                line_number=4
                line=line_number-1
                notification_label_bpm=Label(window, text=displayed_string, bg="red", fg="white",font=("montserrat light",12,"normal"))
                notification_label_bpm.place(x=x_notifications,y=y_notifications+line*gap_notifications_y)
            if property=="oxygen" and displayed_string!="oxygen clear":
                line_number=5
                line=line_number-1
                notification_label_oxygen=Label(window, text=displayed_string, bg="red", fg="white",font=("montserrat light",12,"normal"))
                notification_label_oxygen.place(x=x_notifications,y=y_notifications+line*gap_notifications_y)

        def testing_received_values():
            if value_pressure_received_5<=LL_pressure:
                monitoring.testing_inputs_and_playing_alarms.notifications("P", "Pressure kam ee")
            if value_pressure_received_5>=UL_pressure:
                monitoring.testing_inputs_and_playing_alarms.notifications("P", "Pressure baun zada ee")
            if value_pressure_received_5>LL_pressure and value_pressure_received_5<UL_pressure:
                monitoring.testing_inputs_and_playing_alarms.notifications("P", "P clear")

            if value_peep_received_5<=LL_peep:
                monitoring.testing_inputs_and_playing_alarms.notifications("peep", "peep kam ee")
            if value_peep_received_5>=UL_peep:
                monitoring.testing_inputs_and_playing_alarms.notifications("peep","peep baun zada ee")
            if value_peep_received_5>LL_peep and value_peep_received_5<UL_peep:
                monitoring.testing_inputs_and_playing_alarms.notifications("peep","peep clear")

            if value_pplat_received_5<=LL_pplat:
                monitoring.testing_inputs_and_playing_alarms.notifications("pplat","pplat kam ee")
            if value_pplat_received_5>=UL_pplat:
                monitoring.testing_inputs_and_playing_alarms.notifications("pplat","pplat baun zada ee")
            if value_pplat_received_5>LL_pplat and value_pplat_received_5<UL_pplat:
                monitoring.testing_inputs_and_playing_alarms.notifications("pplat","pplat clear")

            if value_bpm_received_5<=LL_bpm:
                monitoring.testing_inputs_and_playing_alarms.notifications("bpm","bpm kam ee")
            if value_bpm_received_5>=UL_bpm:
                monitoring.testing_inputs_and_playing_alarms.notifications("bpm","bpm baun zada ee")
            if value_bpm_received_5>LL_bpm and value_bpm_received_5<UL_bpm:
                monitoring.testing_inputs_and_playing_alarms.notifications("bpm","bpm clear")

            if value_oxygen_received_5<=LL_oxygen:
                monitoring.testing_inputs_and_playing_alarms.notifications("oxygen","oxygen kam ee")
            if value_oxygen_received_5>=UL_oxygen:
                monitoring.testing_inputs_and_playing_alarms.notifications("oxygen","oxygen baun zada ee")
            if value_oxygen_received_5>LL_oxygen and value_oxygen_received_5<UL_oxygen:
                monitoring.testing_inputs_and_playing_alarms.notifications("oxygen","oxygen clear")

        def hide_notifications():
            global notification_label_pressure
            global notification_label_peep
            global notification_label_pplat
            global notification_label_bpm
            global notification_label_oxygen
            notification_label_pressure.place_forget()
            notification_label_peep.place_forget()
            notification_label_pplat.place_forget()
            notification_label_bpm.place_forget()
            notification_label_oxygen.place_forget()

    class receiving_data_from_arduino():
        global i
        i=0
        def grab_raw_input_from_arduino():
            global data_received

            global i
            if i==0:
                data_received="PP,1,2,3,4,132,PEEP,31,31,31,31,111,PPl,32,32,32,32,32,bpm,16,16,16,16,16,IE,12,12,12,12,12,FiO2,50,50,50,50,1,"
            if i==1:
                data_received="PP,1,2,3,4,222,PEEP,31,31,31,31,111,PPl,32,32,32,32,32,bpm,16,16,16,16,16,IE,12,12,12,12,12,FiO2,50,50,50,50,1,"
            if i==2:
                data_received="PP,1,2,3,4,1,PEEP,31,31,31,31,111,PPl,32,32,32,32,32,bpm,16,16,16,16,16,IE,12,12,12,12,12,FiO2,50,50,50,50,1,"
            if i==3:
                data_received="PP,1,2,3,4,444,PEEP,31,31,31,31,111,PPl,32,32,32,32,32,bpm,16,16,16,16,16,IE,12,12,12,12,12,FiO2,50,50,50,50,1,"
            if i==4:
                data_received="PP,1,2,3,4,111,PEEP,31,31,31,31,111,PPl,32,32,32,32,32,bpm,16,16,16,16,16,IE,12,12,12,12,12,FiO2,50,50,50,50,1,"
            if i==5:
                data_received="PP,1,2,3,4,12,PEEP,31,31,31,31,111,PPl,32,32,32,32,32,bpm,16,16,16,16,16,IE,12,12,12,12,12,FiO2,50,50,50,50,1,"
            if i==6:
                data_received="PP,1,2,3,4,3,PEEP,31,31,31,31,111,PPl,32,32,32,32,32,bpm,16,16,16,16,16,IE,12,12,12,12,12,FiO2,50,50,50,50,1,"
            if i==7:
                data_received="PP,1,2,3,4,311,PEEP,31,31,31,31,111,PPl,32,32,32,32,32,bpm,16,16,16,16,16,IE,12,12,12,12,12,FiO2,50,50,50,50,1,"
            if i==8:
                data_received="PP,1,2,3,4,1231,PEEP,31,31,31,31,111,PPl,32,32,32,32,32,bpm,16,16,16,16,16,IE,12,12,12,12,12,FiO2,50,50,50,50,1,"
            if i==9:
                data_received="PP,1,2,3,4,123,PEEP,31,31,31,31,111,PPl,32,32,32,32,32,bpm,16,16,16,16,16,IE,12,12,12,12,12,FiO2,50,50,50,50,1,"
            if i==10:
                data_received="PP,1,2,3,4,1123,PEEP,31,31,31,31,111,PPl,32,32,32,32,32,bpm,16,16,16,16,16,IE,12,12,12,12,12,FiO2,50,50,50,50,1,"
            if i==11:
                data_received="PP,1,2,3,4,331,PEEP,31,31,31,31,111,PPl,32,32,32,32,32,bpm,16,16,16,16,16,IE,12,12,12,12,12,FiO2,50,50,50,50,1,"
            if i==12:
                data_received="PP,1,2,3,4,112,PEEP,31,31,31,31,111,PPl,32,32,32,32,32,bpm,16,16,16,16,16,IE,12,12,12,12,12,FiO2,50,50,50,50,1,"
            if i==13:
                data_received="PP,1,2,3,4,666,PEEP,31,31,31,31,111,PPl,32,32,32,32,32,bpm,16,16,16,16,16,IE,12,12,12,12,12,FiO2,50,50,50,50,1,"
            if i==14:
                data_received="PP,1,2,3,4,888,PEEP,31,31,31,31,111,PPl,32,32,32,32,32,bpm,16,16,16,16,16,IE,12,12,12,12,12,FiO2,50,50,50,50,1,"
            i=i+1
        def convert_raw_input_into_values():
            global data_received
            global value_pressure_received_1
            global value_pressure_received_2
            global value_pressure_received_3
            global value_pressure_received_4
            global value_pressure_received_5
            global value_peep_received_1
            global value_peep_received_2
            global value_peep_received_3
            global value_peep_received_4
            global value_peep_received_5
            global value_pplat_received_1
            global value_pplat_received_2
            global value_pplat_received_3
            global value_pplat_received_4
            global value_pplat_received_5
            global value_bpm_received_1
            global value_bpm_received_2
            global value_bpm_received_3
            global value_bpm_received_4
            global value_bpm_received_5
            global value_IE_received_1
            global value_IE_received_2
            global value_IE_received_3
            global value_IE_received_4
            global value_IE_received_5
            global value_oxygen_received_1
            global value_oxygen_received_2
            global value_oxygen_received_3
            global value_oxygen_received_4
            global value_oxygen_received_5
            opened_string=data_received.split(',')
            value_pressure_received_1=int(opened_string[1])
            value_pressure_received_2=int(opened_string[2])
            value_pressure_received_3=int(opened_string[3])
            value_pressure_received_4=int(opened_string[4])
            value_pressure_received_5=int(opened_string[5])
            print(value_pressure_received_5)
            value_peep_received_1=int(opened_string[7])
            value_peep_received_2=int(opened_string[8])
            value_peep_received_3=int(opened_string[9])
            value_peep_received_4=int(opened_string[10])
            value_peep_received_5=int(opened_string[11])
            value_pplat_received_1=int(opened_string[13])
            value_pplat_received_2=int(opened_string[14])
            value_pplat_received_3=int(opened_string[15])
            value_pplat_received_4=int(opened_string[16])
            value_pplat_received_5=int(opened_string[17])
            value_bpm_received_1=int(opened_string[19])
            value_bpm_received_2=int(opened_string[20])
            value_bpm_received_3=int(opened_string[21])
            value_bpm_received_4=int(opened_string[22])
            value_bpm_received_5=int(opened_string[23])
            value_IE_received_1=int(opened_string[25])
            value_IE_received_2=int(opened_string[26])
            value_IE_received_3=int(opened_string[27])
            value_IE_received_4=int(opened_string[28])
            value_IE_received_5=int(opened_string[29])
            value_oxygen_received_1=int(opened_string[31])
            value_oxygen_received_2=int(opened_string[32])
            value_oxygen_received_3=int(opened_string[33])
            value_oxygen_received_4=int(opened_string[34])
            value_oxygen_received_5=int(opened_string[35])

        def get_shit_from_arduino_and_update_it_live():
            global value_pressure_received
            monitoring.receiving_data_from_arduino.grab_raw_input_from_arduino()
            monitoring.receiving_data_from_arduino.convert_raw_input_into_values()



    class display_values_being_monitored():
        global y_increment_monitored_values_block
        y_increment_monitored_values_block=100
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
            x_increment_text_right=20        #use this to change gap b/w number and text to its right
            Peak_P_number=Label(window, text=Peak_Pressure, bg="black", fg="white",font=("montserrat",34,"normal"))
            Peak_P_label=Label(window, text="Peak Pressure", bg="black", fg="white",font=("montserrat light",12,"normal"))
            Peak_P_unit=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",12,"normal"))
            Peak_P_maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
            Peak_P_minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
            Peak_P_number.place(x=120+x_increment,y=y_increment_monitored_values_block+40+line*y_increment)
            Peak_P_label.place(x=185+x_increment+x_increment_text_right,y=y_increment_monitored_values_block+47+line*y_increment)
            Peak_P_unit.place(x=185+x_increment+x_increment_text_right,y=y_increment_monitored_values_block+68+line*y_increment)
            Peak_P_maximum.place(x=45+x_increment,y=y_increment_monitored_values_block+50+line*y_increment)
            Peak_P_minimum.place(x=45+x_increment,y=y_increment_monitored_values_block+70+line*y_increment)

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
            x_increment_text_right=20        #use this to change gap b/w number and text to its right
            PEEP_number=Label(window, text=PEEP, bg="black", fg="white",font=("montserrat",34,"normal"))
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
            x_increment_text_right=20        #use this to change gap b/w number and text to its right
            P_plat_number=Label(window, text=P_plat, bg="black", fg="white",font=("montserrat",34,"normal"))
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
            x_increment_text_right=20        #use this to change gap b/w number and text to its right
            BPM_number=Label(window, text=BPM, bg="black", fg="white",font=("montserrat",34,"normal"))
            BPM_label=Label(window, text="BPM", bg="black", fg="white",font=("montserrat light",12,"normal"))
            BPM_maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
            BPM_minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
            BPM_number.place(x=120+x_increment,y=y_increment_monitored_values_block+40+line*y_increment)
            BPM_label.place(x=185+x_increment+x_increment_text_right,y=y_increment_monitored_values_block+47+line*y_increment)
            BPM_maximum.place(x=45+x_increment,y=y_increment_monitored_values_block+50+line*y_increment)
            BPM_minimum.place(x=45+x_increment,y=y_increment_monitored_values_block+70+line*y_increment)

        # def display_Flow(Flow,max,min):
        #     global flow_number
        #     global flow_label
        #     global flow_unit
        #     global flow_maximum
        #     global flow_minimum
        #     line_number=4
        #     line=line_number-1
        #     x_increment=0; y_increment=65
        #     flow_number=Label(window, text=Flow, bg="black", fg="white",font=("montserrat",34,"normal"))
        #     flow_label=Label(window, text="Flow", bg="black", fg="white",font=("montserrat light",12,"normal"))
        #     flow_unit=Label(window, text="L/min", bg="black", fg="white",font=("montserrat light",12,"normal"))
        #     flow_maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
        #     flow_minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
        #     flow_number.place(x=120+x_increment,y=y_increment_monitored_values_block+40+line*y_increment)
        #     flow_label.place(x=185+x_increment,y=y_increment_monitored_values_block+47+line*y_increment)
        #     flow_unit.place(x=185+x_increment,y=y_increment_monitored_values_block+68+line*y_increment)
        #     flow_maximum.place(x=45+x_increment,y=y_increment_monitored_values_block+50+line*y_increment)
        #     flow_minimum.place(x=45+x_increment,y=y_increment_monitored_values_block+70+line*y_increment)

        # def display_VTE(VTE,max,min):
        #     global VTE_number
        #     global VTE_label
        #     global VTE_unit
        #     global VTE_maximum
        #     global VTE_minimum
        #     line_number=5
        #     line=line_number-1
        #     x_increment=0; y_increment=65
        #     VTE_number=Label(window, text=VTE, bg="black", fg="white",font=("montserrat",34,"normal"))
        #     VTE_label=Label(window, text="VTE", bg="black", fg="white",font=("montserrat light",12,"normal"))
        #     VTE_unit=Label(window, text="mL", bg="black", fg="white",font=("montserrat light",12,"normal"))
        #     VTE_maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
        #     VTE_minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
        #     VTE_number.place(x=90+x_increment,y=y_increment_monitored_values_block+40+line*y_increment)
        #     VTE_label.place(x=185+x_increment,y=y_increment_monitored_values_block+47+line*y_increment)
        #     VTE_unit.place(x=185+x_increment,y=y_increment_monitored_values_block+68+line*y_increment)
        #     VTE_maximum.place(x=45+x_increment,y=y_increment_monitored_values_block+50+line*y_increment)
        #     VTE_minimum.place(x=45+x_increment,y=y_increment_monitored_values_block+70+line*y_increment)

        def display_IE(IE,max,min):
            global IE_number
            global IE_label
            global IE_unit
            global IE_maximum
            global IE_minimum
            line_number=5
            line=line_number-1
            x_increment=0
            y_increment=65
            x_increment_text_right=20        #use this to change gap b/w number and text to its right
            IE_number=Label(window, text="1:"+str(IE), bg="black", fg="white",font=("montserrat",34,"normal"))
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
            line_number=6
            line=line_number-1
            x_increment=0
            y_increment=65
            x_increment_text_right=20
            FiO2_number=Label(window, text=FiO2, bg="black", fg="white",font=("montserrat",34,"normal"))
            FiO2_label=Label(window, text="FiO2", bg="black", fg="white",font=("montserrat light",12,"normal"))
            FiO2_unit=Label(window, text="%", bg="black", fg="white",font=("montserrat light",12,"normal"))
            FiO2_maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
            FiO2_minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
            FiO2_number.place(x=120+x_increment,y=y_increment_monitored_values_block+40+line*y_increment)
            FiO2_label.place(x=185+x_increment+x_increment_text_right,y=y_increment_monitored_values_block+47+line*y_increment)
            FiO2_unit.place(x=185+x_increment+x_increment_text_right,y=y_increment_monitored_values_block+68+line*y_increment)
            FiO2_maximum.place(x=45+x_increment,y=y_increment_monitored_values_block+50+line*y_increment)
            FiO2_minimum.place(x=45+x_increment,y=y_increment_monitored_values_block+70+line*y_increment)

        def display_insp_time(insp_time,max,min):
            global insp_time_number
            global insp_time_label
            global insp_time_unit
            global insp_time_maximum
            global insp_time_minimum
            line_number=6
            line=line_number-1
            x_increment=0; y_increment=65
            insp_time_number=Label(window, text=insp_time, bg="black", fg="white",font=("montserrat",34,"normal"))
            insp_time_label=Label(window, text="Insp time", bg="black", fg="white",font=("montserrat light",12,"normal"))
            insp_time_unit=Label(window, text="sec", bg="black", fg="white",font=("montserrat light",12,"normal"))
            insp_time_maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
            insp_time_minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
            insp_time_number.place(x=120+x_increment,y=y_increment_monitored_values_block+40+line*y_increment)
            insp_time_label.place(x=185,y=y_increment_monitored_values_block+47+line*y_increment)
            insp_time_unit.place(x=185+x_increment,y=y_increment_monitored_values_block+68+line*y_increment)
            insp_time_maximum.place(x=45+x_increment,y=y_increment_monitored_values_block+50+line*y_increment)
            insp_time_minimum.place(x=45+x_increment,y=y_increment_monitored_values_block+70+line*y_increment)

        def display_insp_time(insp_time,max,min):
            global insp_time_number
            global insp_time_label
            global insp_time_unit
            global insp_time_maximum
            global insp_time_minimum
            line_number=7
            line=line_number-1
            x_increment=0; y_increment=65
            insp_time_number=Label(window, text=insp_time, bg="black", fg="white",font=("montserrat",34,"normal"))
            insp_time_label=Label(window, text="Insp time", bg="black", fg="white",font=("montserrat light",12,"normal"))
            insp_time_unit=Label(window, text="sec", bg="black", fg="white",font=("montserrat light",12,"normal"))
            insp_time_maximum=Label(window, text=max, bg="black", fg="white",font=("montserrat light",9,"normal"))
            insp_time_minimum=Label(window, text=min, bg="black", fg="white",font=("montserrat light",9,"normal"))
            insp_time_number.place(x=120+x_increment,y=y_increment_monitored_values_block+40+line*y_increment)
            insp_time_label.place(x=185,y=y_increment_monitored_values_block+47+line*y_increment)
            insp_time_unit.place(x=185+x_increment,y=y_increment_monitored_values_block+68+line*y_increment)
            insp_time_maximum.place(x=45+x_increment,y=y_increment_monitored_values_block+50+line*y_increment)
            insp_time_minimum.place(x=45+x_increment,y=y_increment_monitored_values_block+70+line*y_increment)

        def display_monitored_values_label():
            global display_monitored_values_image_label
            global display_monitored_values_image
            display_monitored_values_image=PhotoImage(file="monitored values image.gif")
            display_monitored_values_image_label=Label (window, image=display_monitored_values_image, bg="black")
            display_monitored_values_image_label.place(x=25,y=70)

        def display_monitored_values():
            monitoring.receiving_data_from_arduino.grab_raw_input_from_arduino()
            monitoring.receiving_data_from_arduino.convert_raw_input_into_values()
            monitoring.display_values_being_monitored.display_monitored_values_label()
            print(value_pressure_received_5)
            monitoring.display_values_being_monitored.display_Peak_Pressure(value_pressure_received_5,32,2)
            monitoring.display_values_being_monitored.display_PEEP(value_peep_received_5,1.5,1.25)
            monitoring.display_values_being_monitored.display_P_plat(value_pplat_received_5,1.5,1.25)
            monitoring.display_values_being_monitored.display_BPM(value_bpm_received_5,32,2)
            # monitoring.display_values_being_monitored.display_Flow(8.1,32,2)
            # monitoring.display_values_being_monitored.display_VTE(value_vol_received,1400,500)
            monitoring.display_values_being_monitored.display_IE(value_IE_received_5,1.5,1.25)
            monitoring.display_values_being_monitored.display_FiO2(value_oxygen_received_5,1.5,1.25)
            # monitoring.display_values_being_monitored.display_insp_time(121,1.5,1.25)


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
            global BPM_number
            global BPM_label
            global BPM_unit
            global BPM_maximum
            global BPM_minimum
            BPM_number.place_forget()
            BPM_label.place_forget()
            BPM_maximum.place_forget()
            BPM_minimum.place_forget()
            # global flow_number
            # global flow_label
            # global flow_unit
            # global flow_maximum
            # global flow_minimum
            # flow_number.place_forget()
            # flow_label.place_forget()
            # flow_unit.place_forget()
            # flow_maximum.place_forget()
            # flow_minimum.place_forget()
            # global VTE_number
            # global VTE_label
            # global VTE_unit
            # global VTE_maximum
            # global VTE_minimum
            # VTE_number.place_forget()
            # VTE_label.place_forget()
            # VTE_unit.place_forget()
            # VTE_maximum.place_forget()
            # VTE_minimum.place_forget()
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
            # global insp_time_number
            # global insp_time_label
            # global insp_time_unit
            # global insp_time_maximum
            # global insp_time_minimum
            # insp_time_number.place_forget()
            # insp_time_label.place_forget()
            # insp_time_unit.place_forget()
            # insp_time_maximum.place_forget()
            # insp_time_minimum.place_forget()
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
        global array_character_number_being_printed
        global data_points_in_one_array
        x_data_pressure = np.array([0])
        y_data_pressure = np.array([0])
        starting_time_pressure=0
        array_character_number_being_printed=1
        data_points_in_one_array=5
        time_interval_pressure=0.1/data_points_in_one_array
        total_time_pressure=5
        data_points_pressure=total_time_pressure/time_interval_pressure
        animation_loop_counter_pressure=0
        def animation_frame_pressure(i):
            global time_interval_pressure
            global starting_time_pressure
            global y_val_pressure
            global x_data_pressure
            global y_data_pressure
            global animation_loop_counter_pressure
            global array_character_number_being_printed
            starting_time_pressure=starting_time_pressure+time_interval_pressure
            if animation_loop_counter_pressure<data_points_pressure:
                if array_character_number_being_printed==1:
                    x_data_pressure=np.append(x_data_pressure,[starting_time_pressure])
                    y_data_pressure=np.append(y_data_pressure,[value_pressure_received_1])
                if array_character_number_being_printed==2:
                    x_data_pressure=np.append(x_data_pressure,[starting_time_pressure])
                    y_data_pressure=np.append(y_data_pressure,[value_pressure_received_2])
                if array_character_number_being_printed==3:
                    x_data_pressure=np.append(x_data_pressure,[starting_time_pressure])
                    y_data_pressure=np.append(y_data_pressure,[value_pressure_received_3])
                if array_character_number_being_printed==4:
                    x_data_pressure=np.append(x_data_pressure,[starting_time_pressure])
                    y_data_pressure=np.append(y_data_pressure,[value_pressure_received_4])
                if array_character_number_being_printed==5:
                    x_data_pressure=np.append(x_data_pressure,[starting_time_pressure])
                    y_data_pressure=np.append(y_data_pressure,[value_pressure_received_5])
            if animation_loop_counter_pressure>=data_points_pressure:
                if array_character_number_being_printed==1:
                    y_data_pressure=np.append(y_data_pressure,[value_pressure_received_1])
                    y_data_pressure=np.delete(y_data_pressure,0)
                if array_character_number_being_printed==2:
                    y_data_pressure=np.append(y_data_pressure,[value_pressure_received_2])
                    y_data_pressure=np.delete(y_data_pressure,0)
                if array_character_number_being_printed==3:
                    y_data_pressure=np.append(y_data_pressure,[value_pressure_received_3])
                    y_data_pressure=np.delete(y_data_pressure,0)
                if array_character_number_being_printed==4:
                    y_data_pressure=np.append(y_data_pressure,[value_pressure_received_4])
                    y_data_pressure=np.delete(y_data_pressure,0)
                if array_character_number_being_printed==5:
                    y_data_pressure=np.append(y_data_pressure,[value_pressure_received_5])
                    y_data_pressure=np.delete(y_data_pressure,0)
            line_pressure.set_xdata(x_data_pressure)
            line_pressure.set_ydata(y_data_pressure)
            animation_loop_counter_pressure=animation_loop_counter_pressure+1
            array_character_number_being_printed=array_character_number_being_printed+1
            if array_character_number_being_printed==6:     #this number will be 6 when array_character_number_being_printed has hit 5 and thus, all data points have been plotted
                array_character_number_being_printed=1
            return line_pressure,
        global line_pressure
        total_time_pressure=5
        fig_pressure=Figure(figsize=(9,2.3), dpi=100)
        ax_pressure = fig_pressure.add_subplot(111)
        ax_pressure.set_facecolor('xkcd:black')   #background color
        fig_pressure.patch.set_facecolor('xkcd:black')
        ax_pressure.set_xlim(0, total_time_pressure)
        ax_pressure.set_ylim(-12, 12)
        line_pressure, = ax_pressure.plot(0, 0, color='white')
        graph_pressure = FigureCanvasTkAgg(fig_pressure, master=window)
        canvas_pressure=graph_pressure.get_tk_widget()
        animation_pressure = FuncAnimation(fig_pressure, func=animation_frame_pressure, frames=1000, interval=1)

        global x_data_flow
        global y_data_flow
        global starting_time_flow
        global time_interval_flow
        global total_time_flow
        global data_points_flow
        global animation_loop_counter_flow
        x_data_flow = np.array([0])
        y_data_flow = np.array([0])
        starting_time_flow=0
        time_interval_flow=0.1
        total_time_flow=5
        data_points_flow=total_time_flow/time_interval_flow
        animation_loop_counter_flow=0
        def animation_frame_flow(i):
            global starting_time_flow
            global y_val_flow
            global x_data_flow
            global y_data_flow
            global animation_loop_counter_flow
            starting_time_flow=starting_time_flow+time_interval_flow
            if animation_loop_counter_flow<data_points_flow:
                x_data_flow=np.append(x_data_flow,[starting_time_flow])
                y_data_flow=np.append(y_data_flow,[value_flow_received])
            if animation_loop_counter_flow>=data_points_flow:
                y_data_flow=np.append(y_data_flow,[value_flow_received])
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
        ax_flow.set_ylim(-12, 12)
        line_flow, = ax_flow.plot(0, 0, color='white')
        graph_flow = FigureCanvasTkAgg(fig_flow, master=window)
        canvas_flow=graph_flow.get_tk_widget()
        animation2 = FuncAnimation(fig_flow, func=animation_frame_flow, frames=1000, interval=10)

        def display_graphs():
            global value_flow_received
            value_flow_received=10
            monitoring.graphs.canvas_pressure.place(x=300,y=130)
            monitoring.graphs.canvas_flow.place(x=300,y=380)

        def hide_graphs():
            monitoring.graphs.canvas_pressure.place_forget()
            monitoring.graphs.canvas_flow.place_forget()
    global ii
    ii=0
    def start_monitoring():
        global ii
        if ii==0:
            monitoring.graphs.display_graphs()
            monitoring.receiving_data_from_arduino.get_shit_from_arduino_and_update_it_live()
            monitoring.testing_inputs_and_playing_alarms.testing_received_values()
            monitoring.display_values_being_monitored.display_monitored_values()
        ii=1
        if testing_time_start>=testing_time_end:
            # monitoring.graphs.hide_graphs()
            monitoring.display_values_being_monitored.hide_monitored_values()
            monitoring.testing_inputs_and_playing_alarms.hide_notifications()
            window.after(2000,monitoring.start_monitoring)


        # monitoring.receiving_data_from_arduino.get_shit_from_arduino_and_update_it_live()
        # monitoring.testing_inputs_and_playing_alarms.testing_received_values()
        # monitoring.display_values_being_monitored.display_monitored_values()
        # monitoring.graphs.display_graphs()

    def stop_monitoring():
        monitoring.graphs.hide_graphs()
        monitoring.display_values_being_monitored.hide_monitored_values()
        monitoring.testing_inputs_and_playing_alarms.hide_notifications()

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
            global value_vol_entered
            global value_bpm_entered
            global value_peep_entered
            global value_oxygen_entered
            global value_triggering_flow_entered
            global value_triggering_pressure_entered
            global packed_bpm
            global packed_vol
            global packed_peep
            global packed_oxygen
            global packed_pressure
            global packed_triggering_flow
            global packed_triggering_pressure
            scale_value.place_forget()
            scale_label.place_forget()
            if property_being_updated=="Pressure":
                value_pressure_entered=format(int(self.variable.get()))
                packed_pressure="pressure"+","+str(value_pressure_entered)+","
            if property_being_updated=="Tidal Volume":
                value_vol_entered=format(int(self.variable.get()))
                packed_vol="vol"+","+str(value_vol_entered)+","
            if property_being_updated=="BPM":
                value_bpm_entered=format(int(self.variable.get()))
                packed_bpm="bpm"+","+str(value_bpm_entered)+","
            if property_being_updated=="PEEP":
                value_peep_entered=format(int(self.variable.get()))
                packed_peep="peep"+","+str(value_peep_entered)+","
            if property_being_updated=="Oxygen":
                value_oxygen_entered=format(int(self.variable.get()))
                packed_oxygen="Oxygen"+","+str(value_oxygen_entered)+","
            if property_being_updated=="Triggering flow":
                value_triggering_flow_entered=format(int(self.variable.get()))
                packed_triggering_flow="Triggering flow"+","+str(value_triggering_flow_entered)+","
            if property_being_updated=="Triggering pressure":
                value_triggering_pressure_entered=format(int(self.variable.get()))
                packed_triggering_pressure="Triggering pressure"+","+str(value_triggering_pressure_entered)+","
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
        global scale_bpm
        global scale_peep
        global scale_oxygen
        global scale_flow_trigger
        global scale_pressure_trigger
        scale_vol= CustomScale(window, from_=LL_vol, to=UL_vol)
        scale_pressure = CustomScale(window, from_=LL_pressure, to=UL_pressure)
        scale_bpm = CustomScale(window, from_=LL_bpm, to=UL_bpm)
        scale_peep = CustomScale(window, from_=LL_peep, to=UL_peep)
        scale_oxygen = CustomScale(window, from_=LL_oxygen, to=UL_oxygen)
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
    scale_location_x=300
    scale_location_y=10+y_increment_bottom_scale_block
    unit_increment_y=33
    value_increment_y=30
    scale_label_location_x=750
    scale_label_location_y=99+y_increment_bottom_scale_block
    scale_value_location_x=752
    scale_value_location_y=scale_label_location_y+value_increment_y
    scale_value_unit_location_x=750
    scale_value_unit_location_y=scale_value_location_y+unit_increment_y
    cross_location_x=220
    cross_location_y=30+y_increment_bottom_scale_block
    tick_location_x=cross_location_x+1070
    tick_location_y=cross_location_y
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
        unit_of_property_being_updated="mmH20"
        scaling="yes"
        scale_value=Label(window, text=LL_peep, bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
        scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
        scale_unit_label=Label(window, text=unit_of_property_being_updated, bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_peep.place(x=scale_location_x,y=scale_location_y)
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
        scale_value=Label(window, text=LL_bpm, bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
        scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
        scale_unit_label=Label(window, text=unit_of_property_being_updated, bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_bpm.place(x=scale_location_x,y=scale_location_y)
        scale_value.place(x=scale_value_location_x,y=scale_value_location_y, anchor = CENTER)
        scale_label.place(x=scale_label_location_x,y=scale_label_location_y, anchor = CENTER)
        scale_unit_label.place(x=scale_value_unit_location_x,y=scale_value_unit_location_y, anchor = CENTER)

    def update_volume():
        ventilation_inputs.hide_user_entered_buttons()
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
        scale_value=Label(window, text=LL_vol, bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
        scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
        scale_unit_label=Label(window, text=unit_of_property_being_updated, bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_vol.place(x=scale_location_x,y=scale_location_y)
        scale_value.place(x=scale_value_location_x,y=scale_value_location_y, anchor = CENTER)
        scale_label.place(x=scale_label_location_x,y=scale_label_location_y, anchor = CENTER)
        scale_unit_label.place(x=scale_value_unit_location_x,y=scale_value_unit_location_y, anchor = CENTER)

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
        unit_of_property_being_updated="mmH20"
        scaling="yes"
        scale_value=Label(window, text=LL_pressure, bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
        scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
        scale_unit_label=Label(window, text=unit_of_property_being_updated, bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_pressure.place(x=scale_location_x,y=scale_location_y)
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
        scale_value=Label(window, text=LL_oxygen, bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
        scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
        scale_unit_label=Label(window, text=unit_of_property_being_updated, bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_oxygen.place(x=scale_location_x,y=scale_location_y)
        scale_value.place(x=scale_value_location_x,y=scale_value_location_y, anchor = CENTER)
        scale_label.place(x=scale_label_location_x,y=scale_label_location_y, anchor = CENTER)
        scale_unit_label.place(x=scale_value_unit_location_x,y=scale_value_unit_location_y, anchor = CENTER)

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
        property_being_updated="triggering flow"
        scaling="yes"
        scale_value=Label(window, text=LL_triggering_flow, bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
        scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
        scale_unit_label=Label(window, text=unit_of_property_being_updated, bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_flow_trigger.place(x=scale_location_x,y=scale_location_y)
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
        property_being_updated="triggering pressure"
        scaling="yes"
        scale_value=Label(window, text=LL_triggering_pressure, bg="black", fg="white",font=("montserrat semi bold",30,"normal"))
        scale_label=Label(window, text=property_being_updated, bg="black", fg="white",font=("montserrat light",12,"normal"))
        scale_unit_label=Label(window, text=unit_of_property_being_updated, bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_pressure_trigger.place(x=scale_location_x,y=scale_location_y)
        scale_value.place(x=scale_value_location_x,y=scale_value_location_y, anchor = CENTER)
        scale_label.place(x=scale_label_location_x,y=scale_label_location_y, anchor = CENTER)
        scale_unit_label.place(x=scale_value_unit_location_x,y=scale_value_unit_location_y, anchor = CENTER)

    global update_peep_button
    global update_bpm_button
    global update_vol_button
    global update_pressure_button
    global update_oxygen_button
    global update_triggering_flow_button
    global update_triggering_pressure_button

    update_peep_button_image=PhotoImage(file="update_peep.gif")
    update_peep_button=Button(window, image=update_peep_button_image, highlightthickness=0,bd=0,bg="white",command=update_peep)
    update_bpm_button_image=PhotoImage(file="update_bpm.gif")
    update_bpm_button=Button(window, image=update_bpm_button_image, highlightthickness=0,bd=0,bg="white",command=update_bpm)
    update_vol_button_image=PhotoImage(file="update_vol.gif")
    update_vol_button=Button(window, image=update_vol_button_image, highlightthickness=0,bd=0,bg="white",command=update_volume)
    update_pressure_button_image=PhotoImage(file="update_p.gif")
    update_pressure_button=Button(window, image=update_pressure_button_image, highlightthickness=0,bd=0,bg="white",command=update_pressure)
    update_oxygen_button_image=PhotoImage(file="update_O2.gif")
    update_oxygen_button=Button(window, image=update_oxygen_button_image, highlightthickness=0,bd=0,bg="white",command=update_oxygen)
    update_triggering_flow_button_image=PhotoImage(file="update_IE.gif")
    update_triggering_flow_button=Button(window, image=update_triggering_flow_button_image, highlightthickness=0,bd=0,bg="white",command=update_triggering_flow)
    update_triggering_pressure_button_image=PhotoImage(file="update_IE.gif")
    update_triggering_pressure_button=Button(window, image=update_triggering_pressure_button_image, highlightthickness=0,bd=0,bg="white",command=update_triggering_pressure)
    global user_entered_values_image_label
    user_entered_values_image=PhotoImage(file="user entered values label.gif")
    user_entered_values_image_label=Label (window, image=user_entered_values_image, bg="black")

    def place_user_entered_buttons():
        user_entered_values_image_label.place(x=1200,y=70)
        global update_peep_button
        global update_bpm_button
        global update_vol_button
        global update_pressure_button
        global update_oxygen_button
        global update_triggering_flow_button
        global update_triggering_pressure_button
        global display_monitored_values_image_label
        y_increment_monitored_values_block=100
        x_increment=0
        y_increment=75
        line_1_x=1400
        line_1_y=50+y_increment_monitored_values_block
        line_number=1
        line=line_number-1
        update_pressure_button.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        line_number=2
        line=line_number-1
        update_peep_button.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        line_number=3
        line=line_number-1
        update_bpm_button.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        line_number=4
        line=line_number-1
        update_vol_button.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        line_number=5
        line=line_number-1
        update_oxygen_button.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        line_number=6
        line=line_number-1
        if trigger_mode=="F":
            update_triggering_flow_button.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        if trigger_mode=="P":
            update_triggering_pressure_button.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
    def cross_pressed():
        global update_peep_button
        global update_bpm_button
        global update_vol_button
        global update_pressure_button
        global update_oxygen_button
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

    def hide_tick_and_cross_buttons():
        tick_button.place_forget()
        cross_button.place_forget()

    def hide_scale_bars():
        scale_pressure.place_forget()
        scale_vol.place_forget()
        scale_bpm.place_forget()
        scale_peep.place_forget()
        scale_oxygen.place_forget()
        scale_flow_trigger.place_forget()
        scale_pressure_trigger.place_forget()

    def hide_numeric_display_for_scale():
        scale_value.place_forget()
        scale_label.place_forget()
        scale_unit_label.place_forget()

    def hide_user_entered_buttons():
        global update_peep_button
        global update_bpm_button
        global update_vol_button
        global update_pressure_button
        global update_oxygen_button
        global update_triggering_flow_button
        global update_triggering_pressure_button
        global user_entered_values_image_label

        update_pressure_button.place_forget()
        update_vol_button.place_forget()
        update_bpm_button.place_forget()
        update_peep_button.place_forget()
        update_oxygen_button.place_forget()
        update_triggering_flow_button.place_forget()
        update_triggering_pressure_button.place_forget()
        user_entered_values_image_label.place_forget()

    def tick_pressed():
        global value_vol_entered
        global value_pressure_entered
        global value_bpm_entered
        global value_peep_entered
        global property_being_updated
        global packed_bpm
        global packed_vol
        global packed_peep
        global packed_oxygen
        global packed_pressure
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
    global packed_bpm
    global packed_vol
    global packed_peep
    global packed_oxygen
    global packed_pressure
    global packed_insp_time
    global packed_triggering_pressure
    global packed_triggering_flow
    packed_bpm="packed bpm"
    packed_vol="packed vol"
    packed_peep="packed peep"
    packed_oxygen="packed oxygen"
    packed_pressure="packed pressure"
    packed_insp_time="packed insp_time"
    packed_triggering_pressure="packed triggering pressure"
    packed_triggering_flow="packed triggering flow"
    global CustomScale_vol
    global CustomScale_bpm
    global CustomScale_peep
    global CustomScale_peep
    global CustomScale_oxygen
    global CustomScale_pressure
    global CustomScale_insp_time
    global CustomScale_pressure_trigger
    global CustomScale_flow_trigger
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
                    packed_vol="vol"+","+str(value_vol_entered)+","
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
                    packed_bpm="bpm"+","+str(value_bpm_entered)+","
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
                    packed_peep="peep"+","+str(value_peep_entered)+","
                    #style.configure(self._style_name, font=("montserrat semi bold",8), text="{:.1f}".format(int(self.variable.get())))
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
                    packed_pressure="pressure"+","+str(value_pressure_entered)+","
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
                    value_insp_time_entered=format(int(self.variable.get()))
                    startup_scale_insp_time_value=Label(window, text=str(value_insp_time_entered), bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
                    startup_scale_insp_time_value.place(x=scale_value_insp_time_entered_location_x,y=scale_value_insp_time_entered_location_y, anchor = CENTER)
                    packed_insp_time="insp_time"+","+str(value_insp_time_entered)+","
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
                    packed_triggering_pressure="insp_time"+","+str(value_triggering_pressure_entered)+","
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
                    packed_triggering_flow="triggering flow"+","+str(value_triggering_flow_entered)+","
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
    create_scale_styles_for_startup()

    def create_startup_scales():
        global scale_startup_vol
        global scale_startup_pressure
        global scale_startup_bpm
        global scale_startup_peep
        global scale_startup_oxygen
        global scale_startup_insp_time
        global scale_startup_pressure_trigger
        global scale_startup_flow_trigger
        scale_startup_vol= CustomScale_vol(window, from_=LL_vol, to=UL_vol)
        scale_startup_pressure = CustomScale_pressure(window, from_=LL_pressure, to=UL_pressure)
        scale_startup_bpm = CustomScale_bpm(window, from_=LL_bpm, to=UL_bpm)
        scale_startup_peep = CustomScale_peep(window, from_=LL_peep, to=UL_peep)
        scale_startup_oxygen = CustomScale_oxygen(window, from_=LL_oxygen, to=UL_oxygen)
        scale_startup_insp_time = CustomScale_insp_time(window, from_=LL_insp_time, to=UL_insp_time)
        scale_startup_pressure_trigger = CustomScale_pressure_trigger(window, from_=LL_triggering_pressure, to=UL_triggering_pressure)
        scale_startup_flow_trigger = CustomScale_flow_trigger(window, from_=LL_triggering_flow, to=UL_triggering_flow)
    create_startup_scales()

    global scale_value_pressure_entered_location_x
    global scale_value_pressure_entered_location_y
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
    global scale_value_triggering_pressure_entered_location_x
    global scale_value_triggering_pressure_entered_location_y
    global scale_value_triggering_flow_entered_location_x
    global scale_value_triggering_flow_entered_location_y
    global startup_scale_pressure_value
    global startup_scale_peep_value
    global startup_scale_bpm_value
    global startup_scale_vol_value
    global startup_scale_oxygen_value
    global startup_scale_insp_time_value
    global startup_scale_pressure_trigger_value
    global startup_scale_flow_trigger_value
    scale_value_pressure_entered_location_x=0
    scale_value_pressure_entered_location_y=0
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
    scale_value_triggering_pressure_entered_location_x=0
    scale_value_triggering_pressure_entered_location_y=0
    scale_value_triggering_flow_entered_location_x=0
    scale_value_triggering_flow_entered_location_y=0
    startup_scale_pressure_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
    startup_scale_peep_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
    startup_scale_bpm_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
    startup_scale_vol_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
    startup_scale_oxygen_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
    startup_scale_insp_time_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
    startup_scale_pressure_trigger_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))
    startup_scale_flow_trigger_value=Label(window, text=0, bg="black", fg="white",font=("montserrat light",12,"normal"))

    def place_startup_scales():
        global property_p_insp
        global unit_p_insp_left
        global scale_startup_pressure
        global startup_scale_pressure_value
        global p_scale_unit_label
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
        global scaling
        scaling="yes"
        global property_being_updated
        global scale_location_status
        scale_location_status="centered"
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
        global value_pressure_entered
        global scale_value_pressure_entered_location_x
        global scale_value_pressure_entered_location_y
        line_no=1
        line=line_no-1
        #label on the left
        #property_being_updated1="Pressure"
        property_p_insp=Label(window, text="Pressure", bg="black", fg="white",font=("montserrat",18,"normal"))
        unit_p_insp_left=Label(window, text="cmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
        property_p_insp.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        unit_p_insp_left.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
        #scale in the middle
        scale_startup_pressure.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
        #values on the right
        startup_scale_pressure_value=Label(window, text=LL_pressure, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        p_scale_unit_label=Label(window, text="mmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_value_pressure_entered_location_x=line_1_x+x_increment+x_display_increment
        scale_value_pressure_entered_location_y=line_1_y+line*y_increment+y_display_increment
        startup_scale_pressure_value.place(x=scale_value_pressure_entered_location_x,y=scale_value_pressure_entered_location_y, anchor = CENTER)
        p_scale_unit_label.place(x=line_1_x+x_increment+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)
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
        startup_scale_peep_value=Label(window, text=LL_peep, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        peep_scale_unit_label=Label(window, text="mmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
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
        startup_scale_bpm_value=Label(window, text=LL_bpm, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        scale_value_bpm_entered_location_x=line_1_x+x_increment+x_display_increment
        scale_value_bpm_entered_location_y=line_1_y+line*y_increment+y_display_increment
        startup_scale_bpm_value.place(x=scale_value_bpm_entered_location_x,y=scale_value_bpm_entered_location_y, anchor = CENTER)
        global value_vol_entered
        global scale_value_vol_entered_location_x
        global scale_value_vol_entered_location_y
        line_no=4
        line=line_no-1
        property_vol=Label(window, text="Tidal Volume", bg="black", fg="white",font=("montserrat",18,"normal"))
        unit_vol_left=Label(window, text="mL", bg="black", fg="white",font=("montserrat light",9,"normal"))
        property_vol.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        unit_vol_left.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
        scale_startup_vol.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
        startup_scale_vol_value=Label(window, text=LL_vol, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        vol_scale_unit_label=Label(window, text="mL", bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_value_vol_entered_location_x=line_1_x+x_increment+x_display_increment
        scale_value_vol_entered_location_y=line_1_y+line*y_increment+y_display_increment
        startup_scale_vol_value.place(x=scale_value_vol_entered_location_x,y=scale_value_vol_entered_location_y, anchor = CENTER)
        vol_scale_unit_label.place(x=line_1_x+x_increment+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)
        global value_oxygen_entered
        global scale_value_oxygen_entered_location_x
        global scale_value_oxygen_entered_location_y
        line_no=5
        line=line_no-1
        property_oxygen=Label(window, text="Oxygen", bg="black", fg="white",font=("montserrat",18,"normal"))
        unit_oxygen_left=Label(window, text="%", bg="black", fg="white",font=("montserrat light",9,"normal"))
        property_oxygen.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        unit_oxygen_left.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
        scale_startup_oxygen.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
        startup_scale_oxygen_value=Label(window, text=LL_oxygen, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        oxygen_scale_unit_label=Label(window, text="%", bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_value_oxygen_entered_location_x=line_1_x+x_increment+x_display_increment
        scale_value_oxygen_entered_location_y=line_1_y+line*y_increment+y_display_increment
        startup_scale_oxygen_value.place(x=scale_value_oxygen_entered_location_x,y=scale_value_oxygen_entered_location_y, anchor = CENTER)
        oxygen_scale_unit_label.place(x=line_1_x+x_increment+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)
        global value_insp_time_entered
        global scale_value_insp_time_entered_location_x
        global scale_value_insp_time_entered_location_y
        line_no=6
        line=line_no-1
        property_insp_time=Label(window, text="Insptime", bg="black", fg="white",font=("montserrat",18,"normal"))
        unit_insp_time_left=Label(window, text="seconds", bg="black", fg="white",font=("montserrat light",9,"normal"))
        property_insp_time.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        unit_insp_time_left.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
        scale_startup_insp_time.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
        startup_scale_insp_time_value=Label(window, text=LL_insp_time, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        insp_time_scale_unit_label=Label(window, text="seconds", bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_value_insp_time_entered_location_x=line_1_x+x_increment+x_display_increment
        scale_value_insp_time_entered_location_y=line_1_y+line*y_increment+y_display_increment
        startup_scale_insp_time_value.place(x=scale_value_insp_time_entered_location_x,y=scale_value_insp_time_entered_location_y, anchor = CENTER)
        insp_time_scale_unit_label.place(x=line_1_x+x_increment+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)

    def place_pressure_trigger_scale():
        global property_pressure_trigger
        global unit_pressure_trigger_left
        global scale_startup_pressure_trigger
        global startup_scale_pressure_trigger_value
        global pressure_trigger_scale_unit_label
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
        global value_triggering_pressure_entered
        global scale_value_triggering_pressure_entered_location_x
        global scale_value_triggering_pressure_entered_location_y
        line_no=7
        line=line_no-1
        property_pressure_trigger=Label(window, text="Trig. Pressure ", bg="black", fg="white",font=("montserrat",18,"normal"))
        unit_pressure_trigger_left=Label(window, text="mmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
        property_pressure_trigger.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        unit_pressure_trigger_left.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
        scale_startup_pressure_trigger.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
        startup_scale_pressure_trigger_value=Label(window, text=LL_triggering_pressure, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        pressure_trigger_scale_unit_label=Label(window, text="mmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
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
        unit_flow_trigger_left=Label(window, text="mmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
        property_flow_trigger.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment)
        unit_flow_trigger_left.place(x=line_1_x+x_increment,y=line_1_y+line*y_increment+y_unit_increment)
        scale_startup_flow_trigger.place(x=line_1_x+x_increment+x_scale_increment,y=y_scale_increment+line_1_y+line*y_increment)
        startup_scale_flow_trigger_value=Label(window, text=LL_triggering_flow, bg="black", fg="white",font=("montserrat semi bold",36,"normal"))
        flow_trigger_scale_unit_label=Label(window, text="mmH20", bg="black", fg="white",font=("montserrat light",9,"normal"))
        scale_value_triggering_flow_entered_location_x=line_1_x+x_increment+x_display_increment
        scale_value_triggering_flow_entered_location_y=line_1_y+line*y_increment+y_display_increment
        startup_scale_flow_trigger_value.place(x=scale_value_triggering_flow_entered_location_x,y=scale_value_triggering_flow_entered_location_y, anchor = CENTER)
        flow_trigger_scale_unit_label.place(x=line_1_x+x_increment+x_display_increment,y=3+line_1_y+line*y_increment+y_unit_increment+y_display_increment, anchor = CENTER)

    def pressure_trigger_mode():
        global pressure_triggered_button
        global flow_triggered_button
        flow_triggered_button.place_forget()
        pressure_triggered_button.place_forget()
        global trigger_mode
        trigger_mode="P"
        startup_inputs.place_pressure_trigger_scale()
    global pressure_triggered_button
    pressure_triggered_image=PhotoImage(file="Pressure_triggered.gif")
    pressure_triggered_button=Button(window, image=pressure_triggered_image, highlightthickness=0,bd=0,bg="white",command=pressure_trigger_mode)
    # pressure_triggered_button.place(x=350,y=570)

    def flow_trigger_mode():
        global pressure_triggered_button

        global flow_triggered_button
        flow_triggered_button.place_forget()
        pressure_triggered_button.place_forget()
        global trigger_mode
        trigger_mode="F"
        print(trigger_mode)
        startup_inputs.place_flow_trigger_scale()
    global flow_triggered_button
    flow_triggered_image=PhotoImage(file="Flow_triggered.gif")
    flow_triggered_button=Button(window, image=flow_triggered_image, highlightthickness=0,bd=0,bg="white",command=flow_trigger_mode)
    # flow_triggered_button.place(x=850,y=570)

    def hide_the_scales_in_startup():   #this function hides the scales placed in startup
        global property_p_insp
        global unit_p_insp_left
        global scale_startup_pressure
        global startup_scale_pressure_value
        global p_scale_unit_label
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
        property_p_insp.place_forget()
        unit_p_insp_left.place_forget()
        scale_startup_pressure.place_forget()
        startup_scale_pressure_value.place_forget()
        p_scale_unit_label.place_forget()
        property_peep.place_forget()
        unit_peep.place_forget()
        scale_startup_peep.place_forget()
        startup_scale_peep_value.place_forget()
        peep_scale_unit_label.place_forget()
        property_bpm.place_forget()
        scale_startup_bpm.place_forget()
        startup_scale_bpm_value.place_forget()
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
        property_insp_time.place_forget()
        unit_insp_time_left.place_forget()
        scale_startup_insp_time.place_forget()
        startup_scale_insp_time_value.place_forget()
        insp_time_scale_unit_label.place_forget()
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

    def hide_testing_and_next_buttons():    #this function just hides the two buttons that are placed at startup
        global next_startup_button
        global test_startup_button
        next_startup_button.place_forget()
        test_startup_button.place_forget()
    def hide_triggering_buttons():
        global flow_triggered_button
        global pressure_triggered_button
        flow_triggered_button.place_forget()
        pressure_triggered_button.place_forget()

    def hide_everything_in_startup():       #this function hides everything in startup. buttons and scales, both.
        startup_inputs.hide_the_scales_in_startup()
        startup_inputs.hide_testing_and_next_buttons()
        startup_inputs.hide_triggering_buttons()

    def start_ventilating():                #this button quits the startup and starts full mode ventilation
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
        global flow_triggered_button
        global pressure_triggered_button
        flow_triggered_button.place(x=850,y=570)
        pressure_triggered_button.place(x=350,y=570)

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
        global flow_triggered_button
        global pressure_triggered_button
        flow_triggered_button.place(x=850,y=570)
        pressure_triggered_button.place(x=350,y=570)

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
        window.after(1000,time_testing_display)
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
    if trigger_mode=="P":
        print(packed_pressure+packed_peep+packed_oxygen+packed_bpm+packed_vol+packed_insp_time+packed_triggering_pressure)
    if trigger_mode=="F":
        print(packed_pressure+packed_peep+packed_oxygen+packed_bpm+packed_vol+packed_insp_time+packed_triggering_flow)

def stop_ventilating():
    ventilation_inputs.hide_scale_and_buttons()
    monitoring.stop_monitoring()

def start_ventilating_in_full_mode():
    ventilation_inputs.place_user_entered_buttons()
    monitoring.start_monitoring()

startup_inputs.startup_protocol()

window.mainloop()
