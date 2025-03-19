#Required to record keyboard
import keyboard
# #I believe I need to implement a Listener to be able to break out of the playback
# from threading import Thread
#
# #Listener implementation
# #Can be found on : https://stackoverflow.com/questions/13180941/how-to-kill-a-while-loop-with-a-keystroke
# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(
#             key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(
#             key))
#
# if __name__ == '__main__':
#     abortKey = 'ctrl'
#     listener = keyboard.Listener(on_press=on_press, abortKey=abortKey)
#     listener.start()  # start to listen on a separate thread
#
#     # start thread with loop
#     Thread(target=input_playback, args=(), name='input_playback', daemon=True).start()
#
#     listener.join() # wait for abortKey

#the main function of the program, recording and playing back key sequence
def input_playback():
    events = keyboard.record('shift')
    try:
        while True:
            # play these events
            keyboard.play(events)
    except KeyboardInterrupt:
        pass
input_playback()