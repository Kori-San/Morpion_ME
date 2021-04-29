from tkinter import *
from tkinter.messagebox import *

def demarrer():
    #On définit la matrice à 0 partout
    Morpion = [[0,0,0], [0,0,0], [0,0,0]]
    #On définit une fênetre de 150x150
    fen1.geometry("150x150")
    #On vide le canvas pour enlever d'éventuelles pion
    canv.delete("all")
    #On cache le bouton
    bouton.pack_forget()
    #On affiche notre grille
    grille()
    #On lie au 2 bouton droit et gauche de la souris les fonctions utile aux 2 joueurs
    canv.bind("<Button-1>",lambda event: clic(event, Morpion))
    canv.bind("<Button-3>",lambda event: clic_2(event, Morpion))
    #On utilise lambda pour pouvoir faire un fonction unique qui servira à donner 'Morpion' et 'event' comme argument à clic et clic_2
    
def grille() :
    for k in range (3) :
        canv.create_line(50*k,0,50*k,1000, fill = 'dark gray')
        canv.create_line(0,50*k,1000,50*k, fill = 'dark gray')

def clic(event, Morpion):
    pion(event, Morpion)
    ConditionsDeVictoire1(Morpion)

def clic_2(event, Morpion):
    pion_2(event, Morpion)
    ConditionsDeVictoire2(Morpion)
        
def pion(event, Morpion) :
    #Matrice Rang 0
    #Si 0 < x < 49,9 et que 0 < y < 49,9 et que la matrice ne contient pas déjà un pion d'une autre couleur on place le pion rouge
    if 0 <= event.x <= 49.9 and 0 <= event.y <= 49.9 and Morpion[0][0] != 2 :
        Morpion[0][0] = 1
        canv.create_oval(10,10,40,40, outline = 'black', fill = 'red')

    #Matrice Rang 0
    #On réitére pour les 8 autres cases
    elif 0 <= event.x <= 49.9 and 50 <= event.y <= 99.9 and Morpion[0][1] != 2 :
        Morpion[0][1] = 1
        canv.create_oval(10,60,40,90, outline = 'black', fill = 'red')

    #Matrice Rang 0
    elif 0 <= event.x <= 49.9 and 100 <= event.y <= 150 and Morpion[0][2] != 2 :
        Morpion[0][2] = 1
        canv.create_oval(10,110,40,140, outline = 'black', fill = 'red')

    
    #Matrice Rang 1
    elif 50 <= event.x <= 99.9 and 0 <= event.y <= 49.9 and Morpion[1][0] != 2 :
        Morpion[1][0] = 1
        canv.create_oval(60,10,90,40, outline = 'black', fill = 'red')
        
    #Matrice Rang 1
    elif 50 <= event.x <= 99.9 and 50 <= event.y <= 99.9 and Morpion[1][1] != 2 :
         Morpion[1][1] = 1
         canv.create_oval(60,60,90,90, outline = 'black', fill = 'red')

    #Matrice Rang 1
    elif 50 <= event.x <= 99.9 and 100 <= event.y <= 150 and Morpion[1][2] != 2 :
        Morpion[1][2] = 1
        canv.create_oval(60,110,90,140, outline = 'black', fill = 'red')

    
    #Matrice Rang 2
    elif 100 <= event.x <= 150 and 0 <= event.y <= 49.9 and Morpion[2][0] != 2 :
        Morpion[2][0] = 1
        canv.create_oval(110,10,140,40, outline = 'black', fill = 'red')

    #Matrice Rang 2
    elif 100 <= event.x <= 150 and 50 <= event.y <= 99.9 and Morpion[2][1] != 2 :
        Morpion[2][1] = 1
        canv.create_oval(110,60,140,90, outline = 'black', fill = 'red')

    #Matrice Rang 2
    elif 100 <= event.x <= 150 and 100 <= event.y <= 150 and Morpion[2][2] != 2 :
        Morpion[2][2] = 1
        canv.create_oval(110,110,140,140, outline = 'black', fill = 'red')

        
def ConditionsDeVictoire1(Morpion) :
    #On met la victoire à False pour forcer la vérifiction de l'égalité
    victoire = False
#On vérifie les 8 possibilités de gagner et le match nul
    #Horizontal 1
    if Morpion[0][0] == 1 and Morpion[0][1] == 1 and Morpion[0][2] == 1 :
        victoire = True
    #Horizontal 2
    elif Morpion[1][0] == 1 and Morpion[1][1] == 1 and Morpion[1][2] == 1 :
        victoire = True
    #Horizontal 3   
    elif Morpion[2][0] == 1 and Morpion[2][1] == 1 and Morpion[2][2] == 1 :
        victoire = True
    #Verticale 1
    elif Morpion[0][0] == 1 and Morpion[1][0] == 1 and Morpion[2][0] == 1 :
        victoire = True
    #Verticale 2
    elif Morpion[0][1] == 1 and Morpion[1][1] == 1 and Morpion[2][1] == 1 :
        victoire = True
    #Verticale 3    
    elif Morpion[0][2] == 1 and Morpion[1][2] == 1 and Morpion[2][2] == 1 :
        victoire = True
    #Diagonale 1
    elif Morpion[0][0] == 1 and Morpion[1][1] == 1 and Morpion [2][2] == 1 :
        victoire = True
    #Diagonale 2
    elif Morpion[2][0] == 1 and Morpion[1][1] == 1 and Morpion [0][2] == 1 :
        victoire = True
    #Match Nul
    elif Morpion[0][0] != 0 and Morpion[0][1] != 0 and Morpion[0][2] != 0 and Morpion[1][0] != 0 and Morpion[1][1] != 0 and Morpion[1][2] != 0 and Morpion[2][0] != 0 and Morpion[2][1] != 0 and Morpion[2][2] != 0 :
        canv.unbind("<Button-1>")
        canv.unbind("<Button-3>")
        canv.create_text(75,75,text="Match Nul !",fill="White")
        fen1.geometry("150x170")
        bouton.pack()
     #Si la victoire est validée on délie les 2 boutons pour éviter de placer des points aprés la victoire
     #On affiche le message de victoire et le bouton   
    if victoire == True :
        canv.unbind("<Button-1>")
        canv.unbind("<Button-3>")
        canv.create_text(75,75,text="Le joueur 1 à gagné !",fill="white")
        #On définit une fênetre de 150x170 (Intialement 150x150 mais on rajoute 20 pour le bouton)
        fen1.geometry("150x170")
        bouton.pack()

#Version de pion pour le 2éme joueur
def pion_2(event, Morpion) :
    #Matrice Rang 0
    if 0 <= event.x <= 49.9 and 0 <= event.y <= 49.9 and Morpion[0][0] != 1 :
        Morpion[0][0] = 2
        canv.create_oval(10,10,40,40, outline = 'black', fill = 'blue')

    #Matrice Rang 0
    elif 0 <= event.x <= 49.9 and 50 <= event.y <= 99.9 and Morpion[0][1] != 1 :
        Morpion[0][1] = 2
        canv.create_oval(10,60,40,90, outline = 'black', fill = 'blue')

    #Matrice Rang 0
    elif 0 <= event.x <= 49.9 and 100 <= event.y <= 150 and Morpion[0][2] != 1 :
        Morpion[0][2] = 2
        canv.create_oval(10,110,40,140, outline = 'black', fill = 'blue')

    
    #Matrice Rang 1
    elif 50 <= event.x <= 99.9 and 0 <= event.y <= 49.9 and Morpion[1][0] != 1 :
        Morpion[1][0] = 2
        canv.create_oval(60,10,90,40, outline = 'black', fill = 'blue')
        
    #Matrice Rang 1
    elif 50 <= event.x <= 99.9 and 50 <= event.y <= 99.9 and Morpion[1][1] != 1 :
         Morpion[1][1] = 2
         canv.create_oval(60,60,90,90, outline = 'black', fill = 'blue')

    #Matrice Rang 1
    elif 50 <= event.x <= 99.9 and 100 <= event.y <= 150 and Morpion[1][2] != 1 :
        Morpion[1][2] = 2
        canv.create_oval(60,110,90,140, outline = 'black', fill = 'blue')

    
    #Matrice Rang 2
    elif 100 <= event.x <= 150 and 0 <= event.y <= 49.9 and Morpion[2][0] != 1 :
        Morpion[2][0] = 2
        canv.create_oval(110,10,140,40, outline = 'black', fill = 'blue')

    #Matrice Rang 2
    elif 100 <= event.x <= 150 and 50 <= event.y <= 99.9 and Morpion[2][1] != 1 :
        Morpion[2][1] = 2
        canv.create_oval(110,60,140,90, outline = 'black', fill = 'blue')

    #Matrice Rang 2
    elif 100 <= event.x <= 150 and 100 <= event.y <= 150 and Morpion[2][2] != 1 :
        Morpion[2][2] = 2
        canv.create_oval(110,110,140,140, outline = 'black', fill = 'blue')

#Version de ConditionsDeVictoire1 pour le 2éme joueur
def ConditionsDeVictoire2(Morpion) :
    victoire_2 = False
    
    if Morpion[0][0] == 2 and Morpion[0][1] == 2 and Morpion[0][2] == 2 :
        victoire_2 = True
    elif Morpion[1][0] == 2 and Morpion[1][1] == 2 and Morpion[1][2] == 2 :
        victoire_2 = True 
    elif Morpion[2][0] == 2 and Morpion[2][1] == 2 and Morpion[2][2] == 2 :
        victoire_2 = True
    elif Morpion[0][0] == 2 and Morpion[1][0] == 2 and Morpion[2][0] == 2 :
        victoire_2 = True
    elif Morpion[0][1] == 2 and Morpion[1][1] == 2 and Morpion[2][1] == 2 :
        victoire_2 = True   
    elif Morpion[0][2] == 2 and Morpion[1][2] == 2 and Morpion[2][2] == 2 :
        victoire_2 = True
    elif Morpion[0][0] == 2 and Morpion[1][1] == 2 and Morpion [2][2] == 2 :
        victoire_2 = True
    elif Morpion[2][0] == 2 and Morpion[1][1] == 2 and Morpion [0][2] == 2 :
        victoire_2 = True
    elif Morpion[0][0] != 0 and Morpion[0][1] != 0 and Morpion[0][2] != 0 and Morpion[1][0] != 0 and Morpion[1][1] != 0 and Morpion[1][2] != 0 and Morpion[2][0] != 0 and Morpion[2][1] != 0 and Morpion[2][2] != 0 :
        canv.unbind("<Button-1>")
        canv.unbind("<Button-3>")
        canv.create_text(75,75,text="Match Nul !",fill="White")
        fen1.geometry("150x170")
        bouton.pack()

    if victoire_2 == True :
        canv.unbind("<Button-3>")
        canv.unbind("<Button-1>")
        canv.create_text(75,75,text="Le joueur 2 à gagné !",fill="White")
        fen1.geometry("150x170")
        bouton.pack()

fen1 =Tk()
#On définit un canvas de 150x150 avec une couleur grise
canv = Canvas(fen1, width=150, height =150, bg='grey')
#On affiche un message expliquant les régles du jeu
showinfo('Les régles du jeu !', 'Utilisez le clic gauche pour placer un pion en tant que joueur 1 et le clic droit pour placer un pion en tant que joueur 2. Le premier joueur qui arrive à alligner 3 pion gagne ! Bonne Chance !')
canv.pack()
#On définit le bouton qui servira à rejouer
bouton = Button(fen1, text='Rejouer', command=demarrer)
demarrer()
fen1.mainloop()
