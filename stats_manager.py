from input_ import detect_key
import time
import threading

running = True
ms_true = 0
ms_fals = 0
ms_true_s = 0
ms_fals_s = 0
best_run = 0
last_run = 0

def stats():
    global ms_true, ms_fals, ms_true_s, ms_fals_s, running
    while running:
        if detect_key():
            ms_true += 1
            ms_true_s += 1
        else:
            ms_fals += 1
            ms_fals_s += 1
        time.sleep(0.001)

def reset_stats_s():
    global ms_true_s, ms_fals_s, last_run, best_run
    while running:
        time.sleep(0.5)
        if ms_true_s > 0:
            last_run = ms_fals_s / ms_true_s
        else:
            last_run = 0
        ms_true_s = 0
        ms_fals_s = 0

        if abs(last_run - 1) < abs(best_run - 1):
            best_run = last_run

def get_stats():
    return best_run, last_run

def start_stats_threads():
    thread_stats = threading.Thread(target=stats, daemon=True)
    thread_reset = threading.Thread(target=reset_stats_s, daemon=True)
    thread_stats.start()
    thread_reset.start()
    return thread_stats, thread_reset