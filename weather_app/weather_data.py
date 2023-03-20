import requests as r
import json
import math
import statistics


class Weather:
    def __init__(self):
        self.cities = json.load(open("miasta_pl.json"))
        self.stations = json.loads(self.get_current_weather())
        self.stations_and_cities = json.load(open("cities_and_stations.json"))


    def get_nearest_weather(self, city_name, key=''):
        the_nearest_station = ("start",10000000)
        try:
            city = [_ for _ in self.cities if city_name == _['city']][0]
        except:
            print(city_name)
        for station in self.stations:
            try:
                x1,y1 = self.get_coords_city(station["stacja"])
            except TypeError:
                continue
            x2,y2 = float(city['lon']), float(city['lat'])
            distance = self.length_of_track_two_points(x1,x2, y1,y2)
            if distance < the_nearest_station[1]:
                the_nearest_station = (station, distance)

        the_nearest_station = the_nearest_station[0]

        return the_nearest_station[key] if key else the_nearest_station


    def get_current_weather(self):
        return r.get("https://danepubliczne.imgw.pl/api/data/synop").content


    def get_coords_city(self, station_city):
        for line in self.cities:
            if station_city==line['city']:
                return float(line['lon']), float(line['lat'])


    def length_of_track_two_points(self, xa,xb, ya,yb):
        return math.sqrt( (xb-xa)**2 + (yb-ya)**2 )

    # saves the nearest station for city
    def prepare_json_cities_and_stations(self):
        new_dict = {}
        for city in self.cities:
            city_name = city['city']
            station = self.get_nearest_weather(city_name, 'stacja')
            if station in list(new_dict):
                new_dict[station].append(city_name)
            else:
                new_dict[station]=[city_name]

        return new_dict

if __name__ == "__main__":
    w = Weather()
    #dict_cities = w.prepare_json_cities_and_stations()
    #json.dump(dict_cities, open('cities_and_stations.json','w'))
    #miejscowosc = input("Podaj miejscowość, a podam ci:\n\ttemperature,\n\tprędkość wiatru,\n\tkierunek wiatru,\n\twilgotność względną,\n\tsumę opadu,\n\tciśnienie\n")
    #print(w.get_nearest_weather(miejscowosc))
