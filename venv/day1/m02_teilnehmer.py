import datetime

# was ist eine klasse? mit eigenen worten?
# typ mit individuellen methoden und daten(feldern)

# Alan Kay der Vater der objektorientierten Programmierung; Erfinder von Smalltalk
# Squeak(?)

# was wäre für die VHS interessant? die personen, das konto, ..
# Objekte haben ihren eigenen Speicher - alles ist gekapselt; Objekte haben "Eigenschaften"
# Objekte kommunizieren miteinander via Nachrichten - "Fragestellung -> Antwort"
# anders als vorher, wo man Daten und Methoden getrennt hatte - haben wir jetzt ein Objekt, welches direkt sagen kann wie alt es ist. wird befragt. funktionalität zur beantwortung ist teil des objektes
# caching basiertes verfahren: frage nach altern; nicht immer neu errechnen; sondern einfach den berechneten wert herausgeben
# in Python ist sogar die Klasse ein Objekt
# Klasenobjekt mit speziellem Charakter!
# Von Objekt Klasse bilden und Speicher belegen


# Thomas, 2.2.70, Bielefeld, C, Java
# Marcel, 1.1.83, Kiel, C++, Bash
# Henning, 16.1.60, Hildesheim, Assembler, RexX
# Martin, 3.3.87, Sindelfingen, Matlab
# Matthias, 18.8.89, Lichtenau, Matlab
# Daniel, 1.1.80, Bielefeld, Python, Java

# man erbt immer von einer anderen klasse, auch wenn man es nicht angibt
# explicit is better than implicit!
# stattdessen könnt man auch: "class Teilnehmer:" schreiben
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
        #return self.vorname + " " + str(blubb) # very ugly
        # therefore: formatted output: %s or %2f
        return "%s %s %s %s %s" % (self.__class__, self.vorname, self.geburtsdatum, self.ort, self.sprachen)
    # wie representation-name ausgeben? - siehe erstes attribut, self.__class__ - aber instanz selber hat keinen namen

##this annotation is important: just for testing
#    @staticmethod
#    def foo():
#        pass

    # birth date of the current object
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

## pythontutor.com <---- wichtig! dort kan man durch den Code steppen
# visualisiert den quellcode; dort ist stack un dheap sichtbar!
# Etiketten und Objekte
# Achtung: vier Parameter, aber ein fünfter kommt dazu: das "self"!
# es wäre möglich einen zweiten konstruktur mit (zB) weniger Feldern anzulegen; programm stürtz deann halt ab, aber das ist so. keine defaultwerte
# in dem codevisualizer werden strings direkt dargestellt, sinder aber auch objekte

# console für python öffnen
# oder: python.org: launch interactive shell

# jetzt muss die altersberechnung noch implementiert werden: direkt als methode des objektes

# call of the functions
print(gruppe) #print the whole memory layout - but very ugly: see the type and which location in memory
# both work!
print(marcel.alter())
print("alter:", Teilnehmer.alter(marcel)) # here the object is also given


# zeilenweise ausgabe - erst am ende der elemente, aber wie für jedes element
print(gruppe, sep="\n")
# liste konsumieren: interpretiere die einzelnen bestandteil der liste
print(*gruppe, sep="\n") # linewise printing


# 1) Jüngste Teilnehmer
# liste der jüngsten Teilnehmer erstellen
smolAge = 999
for teilnehmer in gruppe:
    if(teilnehmer.alter() < smolAge):
        smolAge = teilnehmer.alter()
print(smolAge)
# iterate over all members
# pick the ones with the youngest members
#print
juenglinge = []
for teilnehmer in gruppe:
    if(teilnehmer.alter() == smolAge):
        juenglinge.append(teilnehmer)

print(juenglinge)

# 2) Orte der jüngsten Teilnehmer
#print(*juenglinge ort)
for leute in juenglinge:
    print(leute.ort)

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

############### solution from the guy ##########
# 1) jüngste teilnehmer
altersliste = [teilnehmer.alter() for teilnehmer in gruppe]
kleinstes = min(altersliste)
juengsteTeilnehmer = [teilnehmer for teilnehmer in gruppe #komplett aufnhemne, jeden Teilnehmer aus der Gruppe
                   if  teilnehmer.alter() == kleinstes] # wenn gleich das min. Alter ist

print(juengsteTeilnehmer)

# 2) Orte der Teilnehmer
orte = [teilnehmer.ort for teilnehmer in juengsteTeilnehmer]
# Aufgabe remove dupcliates!!
print(orte)