import random
import time

print("-------------------------")
print("Witamy w grze Pełny Kurnik.")
print("-------------------------")

eggs = 0
chickens = 0
hens = 0
rooster = False

USE_RANDOM = True

def rollDice():
    if USE_RANDOM:
        return random.randint(1, 6)
    else:
        return int(input("Podaj wartość kostki: "))

def rollDices():
    dice1 = rollDice()
    dice2 = rollDice()
    return (dice1, dice2)

def gameLogic(dice1, dice2):
    global eggs
    global chickens
    global hens
    global rooster
    if dice1 == 1 and dice2 == 1:
        print("Oddaj 1 jajko innemu graczowi.")
        # TODO
    elif dice1 == 2 and dice2 == 2:
        print("Oddaj 1 kurczaka innemu graczowi.")
        # TODO
    elif dice1 == 3 and dice2 == 3:
        print("Oddaj 1 kurę innemu graczowi.")
        # TODO
    elif dice1 == 4 and dice2 == 4:
        print("Oddaj wszystkie jajka do wspólnej puli.")
        eggs = 0
    elif dice1 == 5 and dice2 == 5:
        additionalDice = rollDice()
        print("Gracz ponownie rzuca kostką i wypada: ", additionalDice)
        if additionalDice <= 3:
            print("Jeśli wypadnie 1, 2 lub 3, to gracz traci następną kolejkę") # TODO
        if additionalDice == 4 or additionalDice == 5:
            print("Jeśli wypadnie 4 lub 5, to gracz musi oddać wszystkie kurczaki do wspólnej puli.")
            chickens = 0
        if additionalDice == 6:
            print("Jeśli wypadnie 6, to gracz musi oddać wszystkie kury do wspólnej puli.")
            hens = 0
            haHa = random.randint(1,5)
            if haHa == 1:
                print("Ha, ha")
            elif haHa == 2:
                print("He, he")
            elif haHa == 3:
                print("Ha, he")
            elif haHa == 4:
                print("He, ha")
            elif haHa == 5:
                print("Ha, ha, he")
    elif dice1 == 6 and dice2 == 6:
        print("Przychodzi lis")
        if rooster:
            print("Kogut ostrzega farmera, lis ucieka i nic się nie dzieje")
        else:
            print("Gracz nie ma koguta")
            additionalDice = rollDice()
            print("Gracz ponownie rzuca kostką i wypada: ", additionalDice)
            print("Gracz traci kury")
            hens -= additionalDice
            if hens < 0:
                print("Gracz traci kurczaki")
                chickens -= -hens
                hens = 0
                if chickens < 0:
                    print("Gracz traci jajka")
                    eggs -= -chickens
                    chickens = 0
                    if eggs < 0:
                        eggs = 0
           
    else:
        for dice in [dice1, dice2]:
            if dice <= 3:
                print("Gracz dostaje jajko")
                eggs += 1
            if dice >= 4 and dice <=5:
                print("Gracz dostaje kurczaka")
                chickens += 1
            if dice == 6:
                print("Gracz dostaje kurę")
                hens += 1

    if eggs >= 3:
        print("Gracz wymienia 3 jajka na kurczaka")
        chickens += 1
        eggs -= 3

    if chickens >= 3:
        print("Gracz wymienia 3 kurczaki na kurę")
        hens += 1
        chickens -= 3

    if hens >= 3 and rooster == False:
        if USE_RANDOM:
            kogut = "nie"
        else: 
            kogut = input("Czy chcesz wymienić trzy kury na jednego koguta? (Odpowiedz Tak lub Nie): ")
        if kogut.lower() == "tak":
            rooster = True
            hens -= 3
        elif kogut.lower() == "nie":
            print("No cóż. To był twój wybór!")

def gameRound(dice1, dice2):
    print("Wypadło: " + str(dice1) + " oraz " + str(dice2))
    gameLogic(dice1, dice2)

def isGameOver():
    if hens >= 9:
        print("Koniec gry!!!!!!!!!!!!!!!!!!!!!!!")
        return True
    return False

def printRoundSummary():
    print("Na koniec rundy:")
    print("Jajka: ", eggs)
    print("Kurczaki: ", chickens)
    print("Kury: ", hens)
    print("Kogut: ", rooster)
    print("-------------------------")

# main game loop
while not isGameOver():
    dice1, dice2 = rollDices()
    gameRound(dice1, dice2)
    printRoundSummary()
    time.sleep(1)

print("-------------------------")
print("Koniec gry. Masz Pełny Kurnik!!!")
print("-------------------------")
