import random
gracze = int(input("Ile ma być graczy?"))
if gracze >= 6:
    print("Nie moze byc wiecej graczy niz 6.")
else:
    for i in range(gracze):
        dice = random.randint(1, 6)