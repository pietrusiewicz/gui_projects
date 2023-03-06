import tkinter as tk
import json
import math
import weather_data


class Weather_map(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.cities = json.load(open("miasta_pl.json"))


    def display_button(self, city):
        x,y = float(city['lon']), 60-float(city['lat'])
        print(x,y)
        #x,y = str(x), str(y)
        #btn = tk.Label(self, text=f'{city["city"]}')
        btn = tk.Button(self)
        btn["command"] = lambda x=city["city"]: print(x)
        btn.place(x=x*100-1250, y=y*120-620)
        #btn.grid(column=int(x), row=int(y))


    def display_map(self):
        w = weather_data.Weather()
        for i,city in enumerate(self.cities):
            print(city)
            #weather = w.get_nearest_weather(city)
            #print(weather)

            self.display_button(city)


if __name__ == '__main__':
    w = Weather_map()
    w.display_map()
    w.mainloop()
