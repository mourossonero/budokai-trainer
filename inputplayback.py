# Required to record keyboard
import keyboard
# Required to monitor 'stop key' press during playback
import threading
# Required to pause between loops
import time

# Variables to control the loop
stop_playback = False
# Function to enable multiple recordings
def replay_requested():
    global stop_playback
    print("Press 'r' to restart or 'ctrl' to exit\n")
    while True:
        if keyboard.is_pressed('r'):
            stop_playback = False
            input_playback()
        elif keyboard.is_pressed('ctrl'):
            break
        time.sleep(0.1)

# Function to make CTRL 'stop key' when the next replay ends
def check_for_stop_key():
    global stop_playback
    while not stop_playback:
        if keyboard.is_pressed('ctrl'):
            print("\n'ctrl' has been pressed, ending replay")
            stop_playback = True
            break

# Main function of the program, recording and playing back sequence
def input_playback():
    try:
        print("Press 'shift' to start/stop recording")
        keyboard.wait('shift')
        print("\nRecording now...")
        # Records the inputs pressed, held, released until Shift is pressed
        events = keyboard.record(until='shift')
        # Above input is held when we exit out the replay
        print("Sequence has been recorded\n")
        print("Press 'ctrl' to stop the program\n")
        # Start a thread to watch the 'stop key'
        stop_thread = threading.Thread(target=check_for_stop_key, daemon=True)
        stop_thread.start()

        while not stop_playback:
            print("Now replaying the input sequence...")
            # Playback the recording at normal speed
            keyboard.play(events, speed_factor=1.0)
            time.sleep(0.1)
        # Explicitly release 'a' before restarting
        keyboard.release('shift')
        # Small pause to ensure proper handling
        time.sleep(0.1)
        # Ask user if new replay or exit
        replay_requested()

    except KeyboardInterrupt:
        pass

#Run the function
print("Welcome to the Budokai Trainer tool!\n")
input_playback()
print("Ending Program...\n")