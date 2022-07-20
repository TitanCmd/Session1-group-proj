from tkinter import *
import time
from random import randint
import csv
import sys

"""
this program will be a stopwatch with a gui
"""


class Stopwatch:
    # add stopwatch functions
    def __init__(self, master):
        self.master = master
        self.master.title("Stopwatch")
        self.master.geometry("600x300")
        self.master.resizable(True, True)
        self.master.configure(background="white")
        self.time = 0
        self.times = []
        self.is_running = False
        self.create_widgets()

    def create_widgets(self):
        self.start_button = Button(self.master, text="Start", command=self.start)
        self.start_button.grid(row=0, column=0, padx=10, pady=10)
        self.stop_button = Button(self.master, text="Stop", command=self.stop)
        self.stop_button.grid(row=0, column=1, padx=10, pady=10)
        self.reset_button = Button(self.master, text="Reset", command=self.reset)
        self.reset_button.grid(row=0, column=2, padx=10, pady=10)
        self.lap_button = Button(self.master, text="Lap", command=self.lap)
        self.lap_button.grid(row=0, column=3, padx=10, pady=10)
        self.time_label = Label(self.master, text="0:00:00:0", font=("Helvetica", 20))
        self.time_label.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
        self.lap_times_label = Label(self.master, text="", font=("Helvetica", 14))
        self.lap_times_label.grid(row=2, column=0, columnspan=4, padx=10, pady=10)
        self.save_button = Button(self.master, text="Save", command=self.save)
        self.save_button.grid(row=0, column=4, padx=10, pady=10)
        self.load()
    
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

    def lap(self):
        self.times.append([len(self.times) + 1, self.time])

        if len(self.times) > 1:
            self.lap_times_label['text'] += "\n"

        self.lap_times_label['text'] += "Lap " + str(self.times[-1][0]) + ": " + self.time_to_string(self.times[-1][1])

    def reset(self):
        self.time = 0
        self.times = []
        self.lap_times_label['text'] = ""
        self.update_time()

    def save(self):
        """
        Writes time to a file (laps if laps are recorded or single time if not)
        """
        file_title = f"times.csv"
        with open(file_title, 'w') as time_log:
            csv_interpreter = csv.writer(time_log)

            for row in self.times:
                csv_interpreter.writerow(row)
                
    def load(self):
        """
        Loads time from a file ()
        :return: 
        """

        print("load")

        file_title = f"times.csv"
        with open(file_title, 'r') as time_log:
            csv_interpreter = csv.reader(time_log)
            self.times = []

            for row in csv_interpreter:
                self.times.append([])
                for column in row:
                    self.times[-1].append(column)

            for time in self.times:
                print(time)
                if len(time) > 1:
                    self.lap_times_label['text'] += f"Lap {str(time[0])} : {self.time_to_string(int(time[1]))}\n"

    def update_time(self):
        if self.is_running:
            self.time += 1
            self.time_label.config(text=self.time_to_string(self.time))
            self.master.after(100, self.update_time)
        else:
            self.time_label.config(text=self.time_to_string(self.time))
    
    def time_to_string(self, time):
        hours = time // 36000
        minutes = (time // 600) - (hours * 60)
        seconds = (time // 10) - (minutes * 60)
        miliseconds = time % 10
        return "{:02d}:{:02d}:{:02d}:{:01d}".format(hours, minutes, seconds, miliseconds)
    
    def main(self):
        self.master.mainloop()
    
if __name__ == "__main__":
    st = Stopwatch(Tk())
    st.main()
    sys.exit()
