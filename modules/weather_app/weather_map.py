import tkinter as tk
import json
import math
try:
    import weather_data
except ModuleNotFoundError:
    from . import weather_data


#class Weather_map(tk.Tk):
class Weather_map:

    #def __init__(self):
    def __init__(self, master):
        # m like master for short
        self.m = master
        self.w = weather_data.Weather()
        #tk.Tk.__init__(self)


    def display_button(self, city: str, wthr):
        #w = weather_data.Weather()
        lon,lat = [(_['lon'], _['lat']) for _ in self.w.cities if _['city']==city][0]
        city_obj = {"city": city, 'lon':lon, 'lat':lat}

        tempra = float(wthr["temperatura"])
        x,y  = float(city_obj['lon']),60-float(city_obj['lat'])

        # display button
        btn = tk.Button(self.m)
        btn["bg"] = self.give_color(tempra)
        btn["text"] = wthr["temperatura"]
        btn["command"] = lambda x=city_obj["city"]: self.display_cities_nearby_station(x)
        btn.place(x=x*100-1250, y=y*120-620)


    def display_cities_nearby_station(self, station):
        try:
            weather = self.w.get_nearest_weather(station)
            for city in self.w.stations_and_cities[station]:
                self.display_button(city, weather)
        except:
            print(station)
        

    def display_map(self):
        for i, station in enumerate(list(self.w.stations_and_cities)):
            weather = self.w.get_nearest_weather(station)
            for city in self.w.stations_and_cities[station]:
                self.display_button(city, weather)
            print(f"Loading {int((i/len(w.stations_and_cities))*100)}%", end="\r")
        print("Loaded 100%", end="\r")
    

    def display_map_stations(self):
        for i, station in enumerate(self.w.stations):
            print(f"Loading {i//len(self.w.stations)*100}%", end="\r")
            if self.w.get_coords_city(station['stacja'])==None:
                continue
            self.display_button(station['stacja'], station)
        
        print("Loaded 100%")

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
    r = tk.Tk()
    r.geometry("1280x720")
    w = Weather_map(r)
    w.display_map_stations()
    #w.display_map()
    r.mainloop()
