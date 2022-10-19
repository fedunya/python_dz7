def view_horizontal(data, fields, count):
    for row in data:        
        print(f'{fields[0]}: {row[0]}, {fields[1]}: {row[1]}, '
            f'{fields[2]}: {row[2]}, {fields[3]}: {row[3]}')
    return
def view_vertical(data, fields, count):
    for row in data:        
        print(f'{fields[0]}: {row[0]}\n{fields[1]}: {row[1]}\n'
            f'{fields[2]}: {row[2]}\n{fields[3]}: {row[3]}\n\n')
    return
