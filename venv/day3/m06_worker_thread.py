# https://docs.python.org/3/library/threading.html
# What exists on a high-level to communicate with a worker-thread?
# Executor objects: https://pymotw.com/2/threading/
# Tkinter - für graphische Oberflächen

# taken from en.wikipedia.org

# adding some shared data structure: synchronized queue: https://docs.python.org/3/library/queue.html
import tkinter as tk
from threading import Thread, Lock
from queue import Queue
import copy

# Fibonacci-implementation
def fib(n):
    if n in (0,1):
        return 1
    return fib(n-2) + fib(n-1) #else vermieden: Einrückungstiefe gespart

#--------------------------------------------------------------------

# worker thread
class MeinThread(Thread):
    # was wäre mit Klasseneigenschaft für den Queue?
    liste = Queue()

    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        result = fib(self.n)
        MeinThread.liste.put(result)
        print(result)
        # alternativ dann die neue Liste in der GUI ausgeben
        MeinThread.updateResults() # dynamisch hinzugefügt bei Konstruktion

#--------------------------------------------------------------------

# the real application
class Application(tk.Frame):
    def __init__(self, master=None):
        super(Application, self).__init__(master)
        self.grid()
        self.createWidgets()
        MeinThread.updateResults = lambda: self.updateResults() # wie bekommt man aber hier die Objektreferenz rein?

    def createWidgets(self):
        # grapisches Werkzeug für die GUI-Erstellung: PAGE (sieht aber arg hässlich aus .. vergleichen mit Qt)
        self.goButton = tk.Button(self, text='Go', command=self.go) # hat schon eine Ereignisbehandlungsmethode
        self.goButton.grid()
        # neues Steuerelement für die Ausgabe
        self.resultsLabel = tk.Label(self, text="results will be displayed here")
        self.resultsLabel.grid()

    def go(self):
        print("Foo")
        t = MeinThread(30)
        t.start()

    # diese Methode kann man dann dem Workerthread übergeben
    def updateResults(self):
        resultString = ""
        # create a copy of the queue and the iterate over it by consuming all items
        copyListe = copy.copy(MeinThread.liste) # THIS is wrong, because no copy
        while not copyListe.empty():
            resultString += str(copyListe.get_nowait())
        #self.resultsLabel.config(text = MeinThread.liste)
        self.resultsLabel.config(text = resultString)

#--------------------------------------------------------------------

app = Application()
app.master.title('m06_worker_thread')
app.mainloop()
