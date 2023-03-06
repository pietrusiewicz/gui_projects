import tkinter as tk
import json
import math
import weather_data


class Weather_map(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.cities = json.load(open("miasta_pl.json"))


    def display_button(self, city, wthr):
        #print(wthr)
        tempra = float(wthr[0]["temperatura"])
        x,y = float(city['lon']), 60-float(city['lat'])
        btn = tk.Button(self)
        btn["bg"] = self.give_color(tempra)
        btn["command"] = lambda x=city["city"]: print(x)
        btn.place(x=x*100-1250, y=y*120-620)


    def display_map(self):
        w = weather_data.Weather()
        for i,city in enumerate(self.cities):
            weather = w.get_nearest_weather(city['city'])
            print(f"Loading {int((i/len(self.cities))*100)}%", end="\r")
            #print(weather)
            self.display_button(city, weather)
        
        print("Loaded 100%", end="\r")


    def give_color(self, degrees):
        if degrees <= -7:
            return "#1184e8"
        elif degrees <= -2:
            return "#3c89d0"
        elif degrees <= 3:
            return "#7ecfd4"
        elif degrees <= 9:
            return "#99fadc"
        elif degrees <= 14:
            return "#88c7dc"
        elif degrees <= 19:
            return "#ffd700"
        elif degrees <= 24:
            return "#ffa500"
        elif degrees <= 29:
            return "#ff4500"
        elif degrees <= 34:
            return "#ff0000"
        else:
            return "#dc143c"


if __name__ == '__main__':
    w = Weather_map()
    w.display_map()
    w.mainloop()
