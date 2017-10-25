from CsvReader import csvZeilenAuslesen
from Fach import Fach


def faecherEinlesen():
    faecher = []
    for fach in csvZeilenAuslesen()[1:]:
        fach = str(fach).replace('\'', '')
        fach = str(fach).replace('[', '')
        fach = str(fach).replace(']', '')
        fach = str(fach).replace(',', '.')

        x = str(fach).split(";")

        #Prüfen/Parsen ob Modul bestanden ist
        if(x[5] == 'j'):
            x[5] = True
        else:
            x[5] = False

        faecher.append(Fach(str(x[0]), float(x[1]), float(x[2]), int(x[3]), int(x[4]), bool(x[5])))
    return faecher


def faecherAusgeben(faecher):
    print("Fachbezeichnung : Note : Gewichtung : Semester : Credits : Bestanden")
    for fach in faecher:
        print(fach.name, ":", fach.note, ":", fach.gewichtung, ":", fach.semester, ":", fach.credits, ":", fach.istBestanden)


def gewichteterNotendurchschnitt(faecher):
    sum = 0
    gewichteterTeiler = 0
    for fach in faecher:
        if fach.istBestanden:
            sum += fach.note * fach.gewichtung
            gewichteterTeiler += fach.gewichtung
    return float(sum/gewichteterTeiler)


def gewichteterNotendurchschnittWorstCase(faecher):
    sum = 0
    gewichteterTeiler = 0
    for fach in faecher:
            sum += fach.note * fach.gewichtung
            gewichteterTeiler += fach.gewichtung
    return float(sum/gewichteterTeiler)


def notendurchschnittSemester(faecher, semester):
    sum = 0
    gewichteterTeiler = 0
    for fach in faecher:
        if fach.semester == semester and fach.istBestanden:
            sum += fach.note * fach.gewichtung
            gewichteterTeiler += fach.gewichtung
    return float(sum/gewichteterTeiler)


def berechneCredits(faecher):
    sum = 0
    for fach in faecher:
        if fach.istBestanden:
            sum += fach.credits
    return sum


def faecherAusgebenNachNoten(faecher):
    print("Fachbezeichnung : Note : Gewichtung : Semester : Credits : Bestanden")
    faecher.sort()
    for fach in faecher:
        print(fach.name, ":", fach.note, ":", fach.gewichtung, ":", fach.semester, ":", fach.credits, ":", fach.istBestanden)


faecher = faecherEinlesen()
#faecherAusgeben(faecher)
faecherAusgebenNachNoten(faecher)
print("Aktuelle Credits: ", berechneCredits(faecher), " von 180" )
print("Aktueller Notendurchschnitt: ", gewichteterNotendurchschnitt(faecher))
print("Notendurchschnitt falls nicht bestandene Module mit 4.0 abgeschlossen werden: ", gewichteterNotendurchschnittWorstCase(faecher))
print("Notendurchschnitt 1 Semester: ", notendurchschnittSemester(faecher, 1))
print("Notendurchschnitt 2 Semester: ", notendurchschnittSemester(faecher, 2))
print("Notendurchschnitt 3 Semester: ", notendurchschnittSemester(faecher, 3))
print("Notendurchschnitt 4 Semester: ", notendurchschnittSemester(faecher, 4))