import tkinter as tk
from datetime import datetime, timedelta

def reset_timer():
    global start_time
    start_time = datetime.now()
    update_timer()

def update_timer():
    elapsed_time = datetime.now() - start_time
    remaining_time = timedelta(seconds=timer_interval) - elapsed_time
    if remaining_time <= timedelta():
        text_box.delete(1.0, tk.END)
        reset_timer()
    else:
        timer_label.config(text=f"Time remaining: {remaining_time}")
        timer_label.after(100, update_timer)

def handle_keypress(event):
    reset_timer()

root = tk.Tk()
root.title("Disappearing Text Writing App")

# Create the text box
text_box = tk.Text(root, font=("Helvetica", 12))
text_box.pack(expand=True, fill="both")

# Create the timer label
timer_label = tk.Label(root, font=("Helvetica", 12))
timer_label.pack()

# Set the timer interval in seconds
timer_interval = 5

# Start the timer
reset_timer()

# Bind the text box to a keypress event handler
text_box.bind("<Key>", handle_keypress)

root.mainloop()
