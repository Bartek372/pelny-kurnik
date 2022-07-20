import random

# TODO check if int
# TODO gracze >= 1 and gracze <= 6
# TODO while not, keep asking
gracze = int(input("Ile ma być graczy?"))
if gracze >= 6:
    print("Nie moze byc wiecej graczy niz 6.")


# we know that gracze >=1 and gracze <= 6 and it's an int

# TODO loop over all gracze
for gracz in range(gracze):
    print("Gracz #", gracz)

# if gracze == 2:
#     dice1 = input("Podaj rzut kostki pierwszego gracza: ")
# dice2 = input("Podaj rzut kostki drugiego gracza: ")
# dice3 = input("Podaj rzut kostki trzeciego gracza: ")

    