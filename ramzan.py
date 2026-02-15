import tkinter  as tk 
from datetime import datetime,timedelta

root = tk.Tk()
root.title("Ramzan Countdown Timer")
root.geometry("500x250")
root.configure(bg="#1e1e2f")


title = tk.Label(root, text="Ramzan Countdown Timer 🌙",font=("Arial", 18 , "bold"),bg="#1e1e2f", fg="white")
title.pack(pady=10)

date_entry = tk.Entry(root, font=("Arial", 12))
date_entry.pack()

timer_label = tk.Label(root, font=("Arial", 14),bg="#1e1e2f", fg="white")
timer_label.pack(pady=10)

# ---------------countdown logic-------------
def update_timer():
    try:
        user_date =datetime.strptime(date_entry.get(),"%Y-%m-%d")
        ramzan_date = datetime(2026,2,18)
        now = datetime.now()
        remaining = ramzan_date - user_date
        
        if remaining.total_seconds() < 0:
            timer_label.config(text="Date Passed")
        elif remaining.total_seconds() == 0:
            timer_label.config(text="🌙 Ramzan Mubarak 🌙")
        else:
            timer_label.config(text=f"{remaining.days} Days Left")

    except ValueError:
        timer_label.config(text="Invalid Date Format")
start_btn = tk.Button(root, text="Start Countdown",command=update_timer)
start_btn.pack()

root.mainloop()
