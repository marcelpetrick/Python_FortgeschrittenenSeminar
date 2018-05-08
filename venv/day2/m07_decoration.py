# goal: print the name of the function

# decorator
def hello(f):
    def g(n): # Definition der neuen Funktion
        print("Hello! :)") # Zusatzaufruf
        return f(n) # Aufruf der ursprünglichen, zu dekorierenden Funktion
    return g # wird vom Dekorateur zurückgegeben

@hello
def fakultaet_rekursiv(n): # maybe add a check for positivity of n
    if n < 0:
        return -1 # error!

    if n == 0:
        return 1
    else:
        return n * fakultaet_rekursiv(n - 1)

print(fakultaet_rekursiv(5)) # aufgrund des rekursiven Charakters bekommt man aber für jeden Aufruf eine Ausgabe -> sechs Ausgaben
