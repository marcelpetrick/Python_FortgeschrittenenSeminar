# Fakultät:
# (erste Implementierung wird nicht sehr effizient sein)
# (Ziel: Funktion schreiben, die eine neue Funktion schreibt)
# 3! = 3 * 2 * 1 ..
# (todo bring the map-files)
# (todo: write a program which counts all files recursively in folders/subfolders)

# Rekursive Definition:
# n! = n * (n-1)! für n >= 1
# 0! = 1

# 5! = 5 * (5-1)! = 5 * (4 * (4-1)!) = ..

def fakultaet_rekursiv(n): #maybe add a check for positivity of n
    if n < 0:
        return -1 #error!

    if n == 0:
        return 1
    else:
        return n * fakultaet_rekursiv(n - 1)

fak = fakultaet_rekursiv(997) # 998 too big
print("fak of 997 is:", fak)

fak = fakultaet_rekursiv(-5)
print("fak of -5 is:", fak)