# Beispiel: https://www.python-kurs.eu/threads.php
# Achtung: scheint noch Python 2 zu sein

import threading
from time import sleep
import random

# --------------------------------------------------------

# Wir brauchen jetzt ein Objekt, welches auch irgendetwas macht
def kunde(vorname, sleepDuration = 0.5):
    while (True):
        print("%s betritt die Bank." % vorname)
        #sleepDuration = 0.5
        sleep(sleepDuration)
        r = random.randint(0, 2)
        if r == 0:
            print("%s üerfällt die Bank." % vorname)
        elif r == 1:
            print("%s zieht die Kontoauszüge." % vorname)
        elif r == 2:
            print("%s hebt Geld ab." % vorname)
        sleep(sleepDuration)
        print("%s verlässt die Bank." % vorname)
        sleep(sleepDuration)

# --------------------------------------------------------

#k0 = kunde("Bernd", 1)
#k0 = kunde("Peter", 0.5)

threading._start_new_thread(kunde, ('Anna', )) # last komma for the param-list is needed, else the Tuple (which is required) is missing -> error
threading._start_new_thread(kunde, ('Peter', 1, ))
threading._start_new_thread(kunde, ('Bernd', 1, ))

input("Ende?\n")
