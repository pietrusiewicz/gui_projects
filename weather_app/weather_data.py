import requests as r
import json
import math


class Weather:
    def __init__(self):
        self.cities = json.load(open("miasta_pl.json"))
        self.jsonfile_weather = json.loads(self.get_current_weather())


    def get_nearest_weather(self, city_name, key=''):
        lengths = []
        city = [_ for _ in self.cities if city_name == _['city']][0]
        for station in self.jsonfile_weather:
            try:
                x1,y1 = self.get_coords_weather_city(station)
            except TypeError:
                continue
            x2,y2 = float(city['lon']), float(city['lat'])
            distance = self.length_of_track_two_points(x1,x2, y1,y2)
            lengths.append((station, distance))

        the_nearest_station = min(lengths, key=lambda x: x[1])
        return the_nearest_station[key] if key else the_nearest_station


    def get_current_weather(self):
        return r.get("https://danepubliczne.imgw.pl/api/data/synop").content

    def get_coords_weather_city(self, station):
        for line in self.cities:
            if station['stacja']==line['city']:
                return float(line['lon']), float(line['lat'])


    def length_of_track_two_points(self, xa, xb, ya, yb):
        return math.sqrt( (xb-xa)**2 + (yb-ya)**2 )

if __name__ == "__main__":
    w = Weather()
    miejscowosc = input("Podaj miejscowość, a podam ci:\n\ttemperature,\n\tprędkość wiatru,\n\tkierunek wiatru,\n\twilgotność względną,\n\tsumę opadu,\n\tciśnienie\n")
    print(w.get_nearest_weather(miejscowosc))
