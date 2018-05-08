# goal: add some check for the type (is number?) and if positive
def fakultaet_rekursiv(n):
    #if type(n) == int # chould have been done. But if G. v. Rossum wanted to have a type-check, he would have implemented it
    if n == 0:
        return 1
    else:
        return n * fakultaet_rekursiv(n - 1)
