# nice way to get porperties with get and set without doing it always "yourself"
def autoproperty(name, has_getter=True, has_setter=True, default_value=0):
    def get(self):
        return getattr(self, name, default_value) # last param is some kind of default return-value in case the param does not exist

    def set(self, value):
        setattr(self, name, value)

    return property(get if has_getter else None, set if has_setter else None) # the part inside the else branch is just syntactical sugar
# those lines above could be used for all similar classes with "get a bigger parameter-list and then convert them to a fixed amount of slots (so there are just a fixed number of data-members)

#------------------------------------------------------------

class Sportwagen(object):
    __slots__ = ('_marke', '_modell', '_ps')
    marke = autoproperty('_marke')
    modell = autoproperty('_modell', default_value='')
    ps = autoproperty('_ps')

    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])



s = Sportwagen(marke="Lambo", modell="Gallardo", ps=500)
print(s.ps)
# s.foo = 42