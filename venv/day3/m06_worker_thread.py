# https://docs.python.org/3/library/threading.html
# What exists on a high-level to communicate with a worker-thread?
# Executor objects: https://pymotw.com/2/threading/
# Tkinter - für graphische Oberflächen

# !/usr/bin/env python3
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super(Application, self).__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()

app = Application()
app.master.title('Sample application')
app.mainloop()
