import tkinter as tk
from weather_app import weather_map
import os


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

    def display_buttons(self):
        func = lambda: [w := weather_map.Weather_map(), w.display_map_stations(), w.mainloop()]
        btn = tk.Button(self, text="weather_app", command=func)
        #weather_map = importlib.import_module("weather_app.weather_map")
        #os.chdir("weather_app/weather_map")
        #btn.command = lambda: print("hell oworld")#
        btn.grid(row=0, column=0)

if __name__ == '__main__':
    a = App()
    a.display_buttons()
    a.mainloop()
