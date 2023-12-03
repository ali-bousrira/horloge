#import de la fonction pour regler le delai dexecution
import time

def pause ():
    test_pausz = input ("le temp est en pause si vous vouler relancée taper 'relancée' \n")
    while (test_pausz != "relancée"):
        test_pausz = input ("le temp est en pause si vous vouler relancée taper 'relancée' \n")

#fonction d'affichege du temp
def horloge (temp):
    #divisition du tuple temp pour faciliter le travaille
    sec = temp [2]
    min = temp [1]
    heur = temp [0]
    #demande de mode d'affichage
    type = input("donner le mode d'affichage de l'heure soit 12 ou 24: \n")
    while not(type == "12" or type == "24"):
        type = input("donner le mode d'affichage de l'heure soit 12 ou 24: \n")
        #boucle infinie
    while True:
        #determination du temp de pause
        if temp == (12,0,0):
            pause()


        #delai dexecution
        time.sleep (1)
        
        sec += 1

        if (sec == 60) :
            sec = 00
            min += 1
        if (min == 60) :
            min = 00
            heur += 1
        if (heur == 24):
            heur = 00
        #affichage avec le mode 24
        if (type == "24"):
            temp = heur, min, sec
            print (str(temp [0]).zfill(2), str(temp [1]).zfill(2), str(temp [2]).zfill(2), sep = ":")
        #affichage avec le mode 12 PM
        elif (heur > 12):
            temp = heur , min, sec
            print (str(temp [0] % 12).zfill(2).rjust(2,'0') , str(temp [1]).zfill(2), str(temp [2]).zfill(2), sep = ":", end = "")
            print (" PM")
        #affichage avec le mode 12 AM
        else :
            temp = heur, min, sec
            print (str(temp [0]).zfill(2), str(temp [1]).zfill(2), str(temp [2]).zfill(2), sep = ":", end = "")
            print (" AM")


temp = 11, 59, 55

horloge(temp)