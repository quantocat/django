"""
Partial => Partieller Aufruf einer Funktion
"""

from functools import partial


def fn(a, b):
    print(a, b)


# Partieller Aufruf von fn mit dem Wert 3
f = partial(fn, 3)  # Rückgabe ist partielle Funktion
f(4)

def g(name: str):
    return name.upper()

assert 1 == 1, "Eins ist Eins"
assert g("A") == "a"