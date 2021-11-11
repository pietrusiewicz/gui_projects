import json, time, os


class File():
    def __init__(self):
        self.file_name = f"{__import__('os').getcwd()}/app_names.json"
        self.keys = ['app_name', 'path_name', 'start_hour_access', 'cooldown_hours']

    def valid_data(self, vals=['','','','']):
        try:
            app_name = vals[0]
            #check_path = lambda: vals[1] if os.path.isfile(vals[1]) else Exception('sciezka nie istnieje')
            p_name = lambda: val[1] if os.path.isfile(vals[1]) else False
            path_name = p_name()
            s_h_access = lambda n: 23 if n > 23 else n
            start_hour_access = s_h_access(int(vals[2][:2]))
            c_hours = lambda n: 24-start_hour_access if n+start_hour_access>24 else n
            cooldown_hours = c_hours(int(vals[3][:2]))
            self.add_app([app_name, path_name, start_hour_access, cooldown_hours])
        except:
            pass


    def add_app(self, vals=['','','','']):
        try:
            d = json.load(open(self.file_name))
            lennames = str(len(d['app_names']))

            d2f = {}; d2f[lennames] = {} 
            for i, key in enumerate(self.keys):
                d2f[lennames][key] = vals[i]
            d['app_names'].append(d2f)
            self.save_file(d)

        except:
            self.add_beg(vals)


    def add_beg(self, vals):
        f = open(self.file_name, 'w')
        f.write('{"app_names":[]}')
        f.close()
        self.add_app(vals)


    def del_app(self, pk):
        d3f = {'app_names': []}
        d2f = json.load(open(self.file_name,'r'))
        ditems = d2f['app_names']
        del ditems[pk]
        for i, val in enumerate(ditems):
            vkey = [_ for _ in val.keys()][0]
            val = val[vkey]
            d3f['app_names'].append({str(i): val})
        self.save_file(d3f)


    def save_file(self, d):
        f = open(self.file_name, 'w') 
        json.dump(d, f, indent=2)
        f.close()


    def get_apps(self):
        try:
            apps = json.load(open(self.file_name))['app_names']
        except:
            apps = {}
        return apps

