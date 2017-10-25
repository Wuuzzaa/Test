import csv


def csvZeilenAuslesen(filename='noten.csv'):
    with open(filename, newline="") as f:
        reader = csv.reader(f, delimiter='\t', quotechar='|')
        zeilen = []
        for row in reader:
            #print(row[0])
            zeilen.append(row)
        return zeilen

#print(csvZeilenAuslesen())
