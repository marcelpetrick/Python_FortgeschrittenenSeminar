def intarg(f):
    def g(n):
        if type(n) == int:
            return f(n)
        else:
            raise TypeError()
    return g

# goal: add some check for the type (is number?) and if positive
# duck typing: alles was wie eine Ente watschelt, quakt und fliegt ist eine Ente (für mich)
# eigentlich will man es gar nicht, dass man auf Typen prüft (pythonisch unüblich)
@intarg
def fakultaet_rekursiv(n):
    if n == 0:
        return 1
    else:
        return n * fakultaet_rekursiv(n - 1)

# ~~~~~~~~~~~ calls ~~~~~~~~~~~~~~~~~
result = fakultaet_rekursiv(4)
print(result)
result = fakultaet_rekursiv("xx")
print(result) # results: "None" - not a bug

# my idea: chould be really helpful to add in quick time some output for debugging (print output of the results for function-calls)
# define decorater as printing of call-param plus result - just add via @ to the different functions

# map, filter, lambda expressions: very important
# tomorrow: Generatoren
# also: unit tests
