import csv
regioni = ['Lombardia','location_name' ,'Abruzzo', 'Campania', 'Basilicata', 'Calabria', 'Emilia-Romagna', 'Friuli-Venezia Giulia', 'Italy', 'Lazio', 'Liguria', 'Marche', 'Molise', 'Provincia autonoma di Bolzano',
           'Provincia autonoma di Trento', 'Puglia', 'Sardegna', 'Sicilia', 'Toscana', 'Umbria', "Valle d'Aosta", 'Veneto', 'Calabria']
with open('Z:\Developing\Sql\PROGETTO\DATI\world_bed_ventilators_projection\summary_stats_all_locs.csv','r') as inp, open('Z:\Developing\Sql\PROGETTO\output.csv', 'w', newline='') as out:
    writer = csv.writer(out)
    parser = csv.reader(inp, delimiter= ',')
    for row in parser:
        for reg in regioni:
            if row[0] == reg:
                writer.writerow(row)
