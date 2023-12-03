#import des bibliotheque
import pygame
import sys



#demande de mode d'affichage
type = input("donner le mode d'affichage de l'heure soit 12 ou 24: \n")
while not(type == "12" or type == "24"):
    type = input("donner le mode d'affichage de l'heure soit 12 ou 24: \n")

#temp initial
temp = 23,59,57

#initialisation de pygame
pygame.init()

#creation de la font
font=pygame.font.Font('freesansbold.ttf',25)


# creation de la fenetre
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Horloge")


#converstioon de l'affichage du temp selont le type choisie
def conv (x, type):
    ret = ""
    if type == "24" :
        for i in range (len(x)):
            if i == len(x)-1:
                if len (str(x [i])) == 2:
                    ret += str(x[i])
                else:
                    ret += "0" + str(x[i])
            else:
                if len (str(x [i])) == 2:
                    ret += str(x[i]) + ":"
                else:
                    ret += "0" + str(x[i]) +":"


    elif (x[0] > 12):
        if len (str(x[0] -12 )) == 2:
            ret += str(x[0] - 12) + ":"
        else:
            ret += "0" + str(x[0] - 12) + ":"
        
        if len (str(x [1])) == 2:
            ret += str(x [1]) + ":"
        else:
            ret += "0" + str(x [1]) + ":"

        if len (str(x [2])) == 2:
            ret += str(x [2]) + "PM"
        else:
            ret += "0" + str(x [2]) + "PM"
    
    else:
        if len (str(x[0])) == 2:
            ret += str(x[0]) + ":"
        else:
            ret += "0" + str(x[0]) + ":"
        
        if len (str(x [1])) == 2:
            ret += str(x [1]) + ":"
        else:
            ret += "0" + str(x [1]) + ":"

        if len (str(x [2])) == 2:
            ret += str(x [2]) + "AM"
        else:
            ret += "0" + str(x [2]) + "AM"

    return ret


#incremantation du temp
def horloge (temp):
    #divisition du tuple temp pour faciliter le travaille
    sec = temp [2]
    min = temp [1]
    heur = temp [0]
 
    sec += 1

    if (sec == 60) :
        sec = 00
        min += 1
    if (min == 60) :
        min = 00
        heur += 1
    if (heur == 24):
        heur = 00

    temp = heur, min, sec

    return temp

#creation d'un timer
timer = pygame.USEREVENT + 1

pygame.time.set_timer(timer, 1000)



#creation de valeure test pour le pause
test = False



# Main game loop
while True:

    #remplir lecran en noire
    screen.fill((0, 0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # affichage de la touche taper
            print("Key pressed:", pygame.key.name(event.key))
            #changement du statu pause
            test = not test
        #timer de 1 seconde
        elif event.type ==  timer:
            if not test :
                temp = horloge(temp)

        
    #test du statu pause
    if test:
        #affichage de "paused"
        display_pause = font.render("paused", True, (200, 200 ,200))

        screen.blit(display_pause, (width / 2, height / 2 ))

    else:
        display_temp = font.render(conv (temp, type), True, (200, 200 ,200))

    #affichage du temp

    screen.blit(display_temp, (width / 2, height / 2 + 30))


    pygame.display.flip()