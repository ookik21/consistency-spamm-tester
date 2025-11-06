from pynput import keyboard

key_pressed = False
running = True

def _on_press(key):
    global key_pressed
    key_pressed = True

def _on_release(key):
    global key_pressed
    key_pressed = False

def start_thread_key_press_listener():
    listener = keyboard.Listener(on_press=_on_press, on_release=_on_release)
    listener.daemon = True
    listener.start()
    return listener

def detect_key():
    return key_pressed
