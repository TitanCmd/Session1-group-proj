from tkinter import *
import time
from random import randint
from datetime import datetime
import sys

"""
this program will be a stopwatch with a gui
"""


class Stopwatch:
    # add stopwatch functions
    def __init__(self, master):
        self.master = master
        self.master.title("Stopwatch")
        self.master.geometry("400x200")
        self.master.resizable(False, False)
        self.master.configure(background="white")
        self.time = 0
        self.is_running = False
        self.create_widgets()

    def create_widgets(self):
        self.start_button = Button(self.master, text="Start", command=self.start)
        self.start_button.grid(row=0, column=0, padx=10, pady=10)
        self.stop_button = Button(self.master, text="Stop", command=self.stop)
        self.stop_button.grid(row=0, column=1, padx=10, pady=10)
        self.reset_button = Button(self.master, text="Reset", command=self.reset)
        self.reset_button.grid(row=0, column=2, padx=10, pady=10)
        self.time_label = Label(self.master, text="0:00:00", font=("Helvetica", 20))
        self.time_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        self.save_button = Button(self.master, text="Save", command=self.save)
        self.save_button.grid(row=2, column=1, padx=10, pady=10)
    
    def start(self):
        self.is_running = True
        self.start_button.config(state=DISABLED)
        self.stop_button.config(state=NORMAL)
        self.reset_button.config(state=DISABLED)
        self.update_time()
    
    def stop(self):
        self.is_running = False
        self.start_button.config(state=NORMAL)
        self.stop_button.config(state=DISABLED)
        self.reset_button.config(state=NORMAL)

    def reset(self):
        self.time = 0
        self.update_time()

    def save(self):
        """
        Writes time to a file (rand num) TODO DATETIME
        """
        file_title = f"{randint(1, 1000)}.txt"
        with open(file_title, 'w') as time_log:
            time_log.write(f"{self.time}")
            print(file_title)
    
    def update_time(self):
        if self.is_running:
            self.time += 1
            self.time_label.config(text=self.time_to_string(self.time))
            self.master.after(1000, self.update_time)
        else:
            self.time_label.config(text=self.time_to_string(self.time))
    
    def time_to_string(self, time):
        minutes = time // 60
        seconds = time % 60
        return "{:02d}:{:02d}:{:02d}".format(minutes, seconds // 10, seconds % 10)
    
    def main(self):
        self.master.mainloop()
    
if __name__ == "__main__":
    st = Stopwatch(Tk())
    st.main()
    sys.exit()
