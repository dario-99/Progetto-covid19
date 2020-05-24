import csv
import datetime

today = str(datetime.datetime.now())
current_month = int(today[5:7])
current_day = int(today[8:10])
start_month = 2
start_day = 24

cond = True
with open('Z:\Developing\Sql\PROGETTO\DATI\proiezioni_letti_regioni_italiane_giornalieri.csv','r') as inp, open('Z:\Developing\Python\CSV\output.csv', 'w', newline='') as out:
    writer = csv.writer(out)
    parser = csv.reader(inp, delimiter= ',')
    for row in parser:
        if row[2] != 'date':
            date = row[2]
            month = int(date[5:7])
            day = int(date[8:10])
            if month > current_month or month == current_month and day > current_day or month == 2 and day < 24:
                cond = False
        if cond:
            writer.writerow(row)
        cond = True