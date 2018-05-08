# goal: add some check for the type (is number?) and if positive
# duck typing: alles was wie eine Ente watschelt, quakt und fliegt ist eine Ente (für mich)
# eigentlich will man es gar nicht, dass man auf Typen prüft (pythonisch unüblich)
def fakultaet_rekursiv(n):
    # print(type(n)) # chould have been done. But if G. v. Rossum wanted to have a type-check, he would have implemented it
    if type(n) == int: # this is not pythonic
        if n == 0:
            return 1
        else:
            return n * fakultaet_rekursiv(n - 1)
    else:
        raise TypeError()

# ~~~~~~~~~~~ calls ~~~~~~~~~~~~~~~~~
result = fakultaet_rekursiv(4)
print(result)
result = fakultaet_rekursiv("xx")
print(result) # results: "None" - not a bug