import tkinter as tk

app = tk.Tk()

app.geometry("505x270+200+200")

from time import strftime

def update_clock():
    time_string = strftime("%I:%M:%S %p\n %A \n %x")
    digital_clock_lbl.config(text = time_string)
    digital_clock_lbl.after(1000, update_clock)
font = ('times', 52, 'bold')
digital_clock_lbl = tk.Label(app, font=font)
digital_clock_lbl.grid(row = 1, column = 1, padx = 5, pady = 25)


update_clock()

app.mainloop()