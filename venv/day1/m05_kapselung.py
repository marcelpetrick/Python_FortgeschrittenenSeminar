

class Teilnehmer(object):
    def __init__(self, vorname, handicap):

        if not(Teilnehmer.validHandicap(handicap)):
            raise Exception("Invalid Initialization of Teilnehmer instance") #or return ...
        self.vorname = vorname
        self.handicap = handicap

    # klassen oder grundsätzliche frage?
    # hängt nicht von eigenschaften des teilnehmers ab - sondern eher grundsätzlich
    # Objekt- und Klassenmethoden
    @staticmethod
    def validHandicap(handicap): #ist Klassen (statische) Methode - self fällt weg
        return handicap > 0 # wenn also positiv, dann zulässig

    def __getHandicap(self):
        return self.__getHandicap

    def __setHandicap(self, handicap):
        self.__getHandicap = handicap

    handicap = property(__getHandicap, __setHandicap)

# hier noch falsch, weil ohne prüfungen implementiert - aber wenn man später den direkten Zugriff auf Proper
try:
    anna =  Teilnehmer("Anna", 7) # if you write here -7, then an exception is raised and handled: in error-case then no object exists
except Exception:
    print("Bockmist")

anna.handicap = -42
anna.vorname = "Gabi"
anna.vornamen = "peter" # geht, aber sollte liebernicht so ausgeführt werden können
# dies kann man über slots machen - und darüber prüfen, ob gültige Methode

print(Teilnehmer.validHandicap(anna.handicap))

# https://github.com/python/cpython/blob/master/Lib/datetime.py
# Die Frage, was ist der heutige Tag ist nichts, was man an ein Datumsobjekt stellen möchte. Sondern eher statisch, aber in größeren Rahmen einetten. Kontext damit gegeben.

# Morgen: Slots - dann zusammen mit der Wiederholung