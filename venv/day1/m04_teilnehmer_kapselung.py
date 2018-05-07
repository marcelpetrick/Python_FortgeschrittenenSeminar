import datetime
class Teilnehmer(object):
    def __init__(self, vorname, geburtsdatum, ort, sprachen): #magische Methode notwendig; Initialisieren des neuen Objektes; Konstruktormehtode
        '''
        Konstruktormethode - ganz spezielle Methode
        self: bedeutet die instanz, die mitgegeben wird
        Dokumentationskommentar
        '''
# Doxygen ... zum Beispiel um Zeugs zu kommentieren
        self.vorname = vorname
        self.geburtsdatum = geburtsdatum
        self.ort = ort
        self.sprachen = sprachen

    # new magic method: representation
    def __repr__(self): # string angeben was ausgegeben werden soll, was derzeit das objekt ist; meist nie selber aufgerufen
        return "%s %s %s %s" % (self.vorname, self.geburtsdatum, self.ort, self.sprachen)

    # age of the current object
    def alter(self): #signatur of the method
        heute = datetime.date.today()
        datum = self.geburtsdatum
        jahre = heute.year - datum.year  # syntax highlighting
        if (datum.month, datum.day) < (heute.month, heute.day):  # lexikographischer vergleich
            jahre -= 1  # remove one if no party in the current year :'(

        return jahre
    ## ende der funktion

# variablen name = Instanziierung eines Objektes; ANlegen einer neuen Instanz
thomas = Teilnehmer("Thomas", datetime.date(1970,2,2), "Bielefeld", ["C", "Bash"])
marcel = Teilnehmer("Marcel", datetime.date(1983,1,1), "Kiel", ["C++", "Bash"])
henning = Teilnehmer("Henning", datetime.date(1960,1,16), "Hildesheim", ["Assembler", "RexX"])
martin = Teilnehmer(" Martin", datetime.date(1987,3,3), "Sindelfingen", ["Matlab"])
matthias = Teilnehmer("Matthias", datetime.date(1989,8,18), "Lichtenau", ["Matlab"])
daniel = Teilnehmer("Daniel", datetime.date(1980,1,1), "Bielefeld", ["Python", "Java"])

gruppe = [thomas, marcel, henning, martin, matthias, daniel]
print(gruppe) # einzeilige Ausgabe