#Required to record keyboard
import keyboard
#Required to monitor 'stop key' press during playback
import threading

# Variable to control the loop
stop_playback = False
# Function to make CTRL 'stop key' when the next replay ends
def check_for_stop_key():
    global stop_playback
    while not stop_playback:
        if keyboard.is_pressed('ctrl'):
            print("CTRL has been pressed, ending program")
            stop_playback = True
            break

# Main function of the program, recording and playing back sequence
def input_playback():
    try:
        print("Input the desired sequence now then press Shift to stop recording")
        # Records the inputs pressed, held, released until Shift is pressed
        events = keyboard.record('shift')
        print("Press CTRL to stop the program")
        # Start a thread to watch the 'stop key'
        stop_thread = threading.Thread(target=check_for_stop_key, daemon=True)
        stop_thread.start()

        while not stop_playback:
            print("Now replaying the input sequence...")
            # Playback the recording at normal speed
            keyboard.play(events, speed_factor=1.0)
    except KeyboardInterrupt:
        pass

#Run the function
input_playback()