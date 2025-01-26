import tkinter as tk
from cProfile import label
from alarm_clock import set_alarm

def create_UI():
    root = tk.Tk()
    root.title("Alarm Clock")

    #the UI componets
    label = tk.Label(root, text="Enter alarm time (hh:mm:ss AM/PM)", font=("Arial Bold", 14))
    label.pack(pady=10)

    entry = tk.Entry(root, font=("Arial Bold",14), width=15)
    entry.pack(pady=5)

    set_button = tk.Button(root, text="set Alarm", font=("Arial Bold",14), command=lambda: set_alarm(entry.get()))
    set_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_UI()