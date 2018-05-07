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

# variablen name = Instanziierung eines Objektes; ANlegen einer neuen Instanz
thomas = Teilnehmer("Thomas", datetime.date(1970,2,2), "Bielefeld",
                    ["C", "Bash"])
marcel = Teilnehmer("Marcel", datetime.date(1983,1,1), "Kiel", ["C++", "Bash"])
henning = Teilnehmer("Henning", datetime.date(1960,1,16), "Hildesheim", ["Assembler", "RexX"])
martin = Teilnehmer(" Martin", datetime.date(1987,3,3), "Sindelfingen", ["Matlab"])
matthias = Teilnehmer("Matthias", datetime.date(1989,8,18), "Lichtenau", ["Matlab"])
daniel = Teilnehmer("Daniel", datetime.date(1980,1,1), "Bielefeld", ["Python", "Java"])

## pythontutor.com <---- wichtig! dort kan man durch den Code steppen
# visualisiert den quellcode; dort ist stack un dheap sichtbar!
# Etiketten und Objekte
# Achtung: vier Parameter, aber ein fünfter kommt dazu: das "self"!
# es wäre möglich einen zweiten konstruktur mit (zB) weniger Feldern anzulegen; programm stürtz deann halt ab, aber das ist so. keine defaultwerte
# in dem codevisualizer werden strings direkt dargestellt, sinder aber auch objekte



