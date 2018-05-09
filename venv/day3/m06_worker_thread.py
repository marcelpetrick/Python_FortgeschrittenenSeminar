# https://docs.python.org/3/library/threading.html
# What exists on a high-level to communicate with a worker-thread?
# Executor objects: https://pymotw.com/2/threading/
# Tkinter - für graphische Oberflächen

# taken from en.wikipedia.org
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super(Application, self).__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.goButton = tk.Button(self, text='Go', command=self.go) # hat schon eine Ereignisbehandlungsmethode
        self.goButton.grid()

    def go(self):
        print("Foo")

app = Application()
app.master.title('m06_worker_thread')
app.mainloop()
