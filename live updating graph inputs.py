



def live_updates():
    monitoring.receiving_data_from_arduino.get_shit_from_arduino_and_update_it_live()
    monitoring.testing_inputs_and_playing_alarms.testing_received_values()
    monitoring.display_values_being_monitored.configure_monitored_values()
    window.after(2000,monitoring.live_updates)
