import tkinter as tk
from input_ import detect_key
from cps import get_cps
from stats_manager import get_stats

def start_gui():
    root = tk.Tk()
    root.title("Spam Consistency Tester")

    cps_label = tk.Label(root, text="CPS : 0", font=("Helvetica", 20))
    cps_label.pack(pady=10)

    max_cps_label = tk.Label(root, text="max CPS : 0", font=("Helvetica", 20))
    max_cps_label.pack(pady=10)

    click_total_label = tk.Label(root, text="Clicks : 0", font=("Helvetica", 20))
    click_total_label.pack(pady=10)

    detect_key_label = tk.Label(root, text="Key pressed : False", font=("Helvetica", 20))
    detect_key_label.pack(pady=10)

    concistancy_label = tk.Label(root, text="Best consistency : 0", font=("Helvetica", 20))
    concistancy_label.pack(pady=10)

    last_concistancy_label = tk.Label(root, text="Last consistency : 0", font=("Helvetica", 20))
    last_concistancy_label.pack(pady=10)

    def update_gui():
        cps_label.config(text=f"CPS : {get_cps()[0]}")
        max_cps_label.config(text=f"max CPS : {get_cps()[2]}")
        detect_key_label.config(text=f"Key pressed : {detect_key()}")
        concistancy_label.config(text=f"Best consistency : {get_stats()[0]:.3f}")
        click_total_label.config(text=f"Clicks : {get_cps()[1]}")
        last_concistancy_label.config(text=f"Last consistency : {get_stats()[1]:.3f}")
        root.after(50, update_gui)

    update_gui()
    root.mainloop()
