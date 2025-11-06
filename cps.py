from input_ import detect_key
import threading
import time

running=True
cps = 0
max_cps = 0
click_count = 0
click_count_second = 0
last_is_true = False

def detect_input():
    global click_count, click_count_second, last_is_true, running
    while running:
        actual_is_true = detect_key() 
        if actual_is_true and not last_is_true:
            click_count_second += 1
            click_count += 1
        last_is_true = actual_is_true
        time.sleep(0.001)

def calculate_cps():
    global cps, click_count_second, running, max_cps
    while running:
        time.sleep(1)
        cps = click_count_second
        if cps > max_cps:
            max_cps = cps
        click_count_second = 0

def threads_cps():
    thread_input = threading.Thread(target=detect_input, daemon=True)
    thread_cps = threading.Thread(target=calculate_cps, daemon=True)
    thread_input.start()
    thread_cps.start()
    return thread_input, thread_cps

def get_cps():
    return cps, click_count, max_cps
