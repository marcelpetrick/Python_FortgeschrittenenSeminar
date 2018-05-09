from collections import Iterator

# just for testing to import the package-loading
from day2.m04_fibonacci import fib as oldFib

#-------------------------------------------
# alwasys forward - never "back"
class Fib(Iterator):
    def __init__(self):
        self.a = 1
        self.b = 1

    # Plan: das Objekt ist selber der Iterator!
    def __iter__(self):
        return self

    # override!
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.b

#-------------------------------------------
fib = Fib()
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())

# just for testing with the import
print(oldFib(10))


# infinite return ...
#for x in Fib():
#    print(x)
