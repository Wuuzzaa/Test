class Fach(object):
    def __init__(self, name, note, gewichtung, semester, credits, istBestanden):
        self.name = name
        self.note = note
        self.gewichtung = gewichtung
        self.semester = semester
        self.credits = credits
        self.istBestanden = istBestanden

    # Less Than Methode dient dazu, Objekte einer Klasse zu vergleichen via sort()
    def __lt__(self, other):
        return self.note < other.note

    @property
    def name(self):
        return self.__name

    @property
    def note(self):
        return self.__note

    @property
    def gewichtung(self):
        return self.__gewichtung

    @property
    def semester(self):
        return self.__semester

    @property
    def credits(self):
        return self.__credits

    @property
    def istBestanden(self):
        return self.__istBestanden

    @name.setter
    def name(self, name):
        self.__name = name

    @note.setter
    def note(self, note):
        self.__note = note

    @gewichtung.setter
    def gewichtung(self, gewichtung):
        self.__gewichtung = gewichtung

    @semester.setter
    def semester(self, semester):
        self.__semester = semester

    @credits.setter
    def credits(self, credits):
        self.__credits = credits

    @istBestanden.setter
    def istBestanden(self, istBestanden):
        self.__istBestanden = istBestanden