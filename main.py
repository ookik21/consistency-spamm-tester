from input_ import start_thread_key_press_listener
from cps import threads_cps
from stats_manager import start_stats_threads
from gui import start_gui

start_thread_key_press_listener()
thread_input_cps, thread_cps_calc = threads_cps()
thread_stats, thread_reset = start_stats_threads()

start_gui()