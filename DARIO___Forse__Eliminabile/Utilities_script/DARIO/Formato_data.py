# CAMBIARE IL FORMATO DELLE DATE DA TIMESTAMP IN GG-Mese-AAAA dove mese sono le tre iniziali del mese in italiano
import csv

# DATI DA INIZIALIZZARE
# salvo i dati in una struttura dati cosi facendo posso associare ad ogni mese il suo corrispettivo mese in lettere
mesi = [
    ('01', 'GEN'),
    ('02', 'FEB'),
    ('03', 'MAR'),
    ('04', 'APR'),
    ('05', 'MAG'),
    ('06', 'GIU'),
    ('07', 'LUG'),
    ('08', 'AGO'),
    ('09', 'SET'),
    ('10', 'OTT'),
    ('11', 'NOV'),
    ('12', 'DIC')
]
# path del file di input e di output
path_inp = 'dpc-covid19-ita-province.csv'
path_out = 'Output.csv'
# Posizione nel file csv del TIMESTAMP
pos = 0
# nome colonna di intestazione
intestazione = 'data'

#APERTURA FILE
with open(path_inp, 'r') as inp, open(path_out, 'w', newline='') as out:
    writer = csv.writer(out)                    # scrive le row in formato corretto nel file di output
    parser = csv.reader(inp, delimiter=',')     # lettore delle row nel file di input non modificato
    for row in parser:
        temp = row[pos]                         # salvo in una stringa il contenuto del timestamp
        if temp != intestazione:                      # controllo che non sia la riga di intestazione
            anno = temp[0:4]
            mese_old = temp[5:7]
            giorno = temp[8:10]
            # associo a mese_old il mese in lettere
            for mese in mesi:
                if mese_old == mese[0]:
                    mese_old = mese[1]          # Mese_old contiene adesso il mese corretto
            # modifico la data nel formato corretto
            row[pos] = giorno + '-' + mese_old + '-' + anno
        # scrivo nel file di output la row corretta e quella di intestazione
        writer.writerow(row)
