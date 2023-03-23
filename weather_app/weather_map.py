import tkinter as tk
import json
import math
import weather_data


class Weather_map(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)


    """
    def display_voivodeships(self, city, wthr):
        names = ["Łobez", "Kościerzyna", "Biskupiec", "Białystok", "Świebodzin", "Września", "Warszawa", "Lublin", "Toruń", "Legnica", "Opole", "Katowice", "Wieliczka", "Kielce", "Rzeszów"]
        for name in names:
            if name == city['city']:
                tempra = float(wthr["temperatura"])
                x,y = float(city['lon']), 60-float(city['lat'])
                btn = tk.Button(self, height=8, width=10)
                btn["bg"] = self.give_color(tempra)
                btn["text"] = wthr["temperatura"]
                btn["command"] = lambda x=city["city"]: print(x)
                btn.place(x=x*100-1250, y=y*120-675)
    """
        

    def display_button(self, city, wthr):
        tempra = float(wthr["temperatura"])
        x,y  = float(city['lon']), 60-float(city['lat'])
        btn = tk.Button(self)
        btn["bg"] = self.give_color(tempra)
        btn["text"] = wthr["temperatura"]
        btn["command"] = lambda x=city["city"]: print(x)
        btn.place(x=x*100-1250, y=y*120-620)


    def display_cities_nearby_station(self, station):
        w = weather_data.Weather()
        for city in w.stations_and_cities[station]:
            lon,lat = ([(_['lon'], _['lat']) for _ in w.cities if _['city']==city][0])
            city_obj = {"city": city, 'lon':lon, 'lat':lat}
            self.display_button(city_obj, weather)
        

    def display_map(self):
        w = weather_data.Weather()
        for i, station in enumerate(list(w.stations_and_cities)):
            weather = w.get_nearest_weather(station)
            for city in w.stations_and_cities[station]:
                lon,lat = ([(_['lon'], _['lat']) for _ in w.cities if _['city']==city][0])
                city_obj = {"city": city, 'lon':lon, 'lat':lat}
                self.display_button(city_obj, weather)
            print(f"Loading {int((i/len(w.stations_and_cities))*100)}%", end="\r")
        print("Loaded 100%", end="\r")

        """
        w = weather_data.Weather()
        for i,city in enumerate(w.cities):
            weather = w.get_nearest_weather(city['city'])
            print(f"Loading {int((i/len(w.cities))*100)}%", end="\r")
            #print(weather)
            self.display_button(city, weather)
            #self.display_voivodeships(city, weather)
        
        print("Loaded 100%", end="\r")
        """
    

    def display_map_stations(self):
        w = weather_data.Weather()
        for i, station in enumerate(w.stations):
            xy = w.get_coords_city(station['stacja'])
            if xy==None:
                continue
            x,y = xy
            city = {"city":station['stacja'] , "lon":x, "lat":y}
            print(f"Loading {int((i/len(w.cities))*100)}%", end="\r")
            #print(weather)
            self.display_button(city, station)
            #self.display_voivodeships(city, weather)
        
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
    w = Weather_map()
    w.display_map_stations()
    #w.display_map()
    w.mainloop()
