# Fibonacci-Zahlewn:;
# Rekursive Definition:
# fib(n) = fib(n-2) + fib(n-1) für n => 2
# fib(0) = 1
# fib(1) = 1
# Iterative Definition anhand von Beispielen:
# fib(5) = 1 1
#            1 2
#              2 3
#                3 5
#                  5 8

def fib(n):
    if n in (0,1):
        return 1
    return fib(n-2) + fib(n-1) #else vermieden: Einrückungstiefe gespart

if __name__ == "__main__": # new
    fib = fib(40) # aber hat exponentielle Laufzeit
    print(fib)
    # deshalb gleich neu: Memoisation - Caching! Merken von bereits bestimmten Ergebnissen
