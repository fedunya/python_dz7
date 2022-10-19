def import_txt(file_name):    
    with open(file_name, 'r') as f:
        data = f.read()    
    list_data = []
    for line in data.splitlines():
        line = line.replace(',',' ')                
        data_list = list(filter(lambda x: ':' not in x, line.split()))
        list_data.append(data_list)
    return list_data
def data_to_csv(file_name, list_data):
    with open(file_name, 'a') as csvfile:
        wr_csv = csv.writer(csvfile, lineterminator = '\r')    
        for i in list_data:
            wr_csv.writerow(i)
    return
def import_json(file_name):
    with open(file_name, 'r') as jsonfile:
        data = json.load(jsonfile)        
    list_data = []
    for d in data:
        data_list = list(map(str, d.values()))
        list_data.append(data_list)    
    return list_data

import csv, json
