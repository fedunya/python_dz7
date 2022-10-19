def csv_to_data(file_name):
    fields = []
    data = []
    with open(file_name, 'r') as f:
        csv_f = csv.reader(f)
        fields = next(csv_f)            
        for row in csv_f:            
            data.append(row)
        count = csv_f.line_num
    return data, fields, count
def export_txt(file_name, data, fields, count):
    with open(file_name, 'w') as txt:
        txt.write('')
    for row in data:
        with open(file_name, 'a') as txt:
            txt.write(f'{fields[0]}: {row[0]},{fields[1]}: {row[1]},'
                f'{fields[2]}: {row[2]},{fields[3]}: {row[3]}\n')
    return
def export_json(file_name, data, fields, count):
    d_json = []
    for row in data:
        d_json.append(dict(zip(fields, row)))    
    with open(file_name, 'w') as json_file:
        json.dump(d_json, json_file, indent = 5)

import csv, json
