import time
import os
import sys

def nouvelle_partie(joueur1, joueur2):
    os.system('cls')
    print("Chargement d'une nouvelle partie...")
    time.sleep(2)
    joueur_contre_joueur(joueur1, joueur2)

def init_grille():
    # Coder par Lenzo
    """
    Initialise la liste {grille} qui prend toute les valeurs à ' '
    Retourne la liste
    met la variable grille en global
    """
    # [[(' ', ' '), (' ', ' '), (' ', ' ')], [(' ', ' '), (' ', ' '), (' ', ' ')], [(' ', ' '), (' ', ' '), (' ', ' ')]]
    grille = [[(' ', ' '), (' ', ' '), (' ', ' ')], [(' ', ' '), (' ', ' '), (' ', ' ')], [(' ', ' '), (' ', ' '), (' ', ' ')]]
    afficher_grille(grille)
    return grille

def afficher_grille(G):
    # Coder par Mael
    """
    Paramètre = une grillle
    Affiche la grille dans la console
    i = nombre initialiser à 0 puis + 1 à chaque exécution de la boucle
    tableau = initialiser à une chaîne de caractère vide
    return le nouveau tableau
    """
    i = 0
    tableau = ''
    while i < len(G):
        ligne = f'{i+1} {G[i][0][1]}|{G[i][1][1]}|{G[i][2][1]}\n'
        if tableau == '':
            tableau = '  1 2 3\n' + ligne
        else :
            tableau += ligne
        i+=1
    return print(tableau)

def jouer_un_coup(G, Joueur, Pos):
    # Coder par François
    """
    paramètre = grille + joueur (nom d'utilisateur, pion) + position (ligne, colone)
    return True ou None si erreur
    """
    
    Bool = True
    y = Pos[0]
    x = Pos[1]
    
    if G[Pos[0]][Pos[1]] != (' ', ' '):
        Bool = None
        
    G[y][x] = Joueur
    return Bool

def grille_pleine(G):
    # Coder par François
    """
    paramètre = grille
    return True si grille pleine return False si grille non pleine
    """

    Bool = False
    msg = ''

    for i in range(len(G)):
        for i2 in range(len(G[i])):
            if G[i][i2] == (' ', ' '):
                msg+='f'
            else:
                msg+='t'

    if msg == 'ttttttttt':
        Bool = True

    return Bool

def grille_gagnante(G, J1, J2):
    # Coder par Mael

    """
    paramètre = grille + joueur1 + joueur2
    return True si un joueur a gagner et le joueur en question. si aucun joueur ne gagne return False + None
    """

    Bool = False
    Joueur = None

    def Chek(m):
        """
        paramètre = list des éléments (exemple : '000', 'xxx', 'OxO', 'xOO', etc)
        return True si un joueur a gagner et le joueur en question. si aucun joueur ne gagne return False + None
        """

        Bool = False
        Joueur = False

        if m == 'OOO':
            Bool = True
            Joueur = J1
        elif m == 'XXX':
            Bool = True
            Joueur = J2
        else:
            Bool = False
            Joueur = None
        return (Bool, Joueur)

    # Vérification verticale
    if Bool == False:
        for i in range(len(G)):
            msg=''
            for i2 in range(len(G[i])):
                if G[i][i2][1] == 'O' or G[i][i2][1] == 'X':
                    msg+=f'{G[i][i2][1]}'
                Cheking = Chek(msg)
                if Cheking[0] == True:
                    Bool = Cheking[0]
                    Joueur = Cheking[1]

    # Vérification horizontale
    if Bool == False:
        for i in range(len(G)):
            msg=''
            for i2 in range(len(G[i])):
                if G[i2][i][1] == 'O' or G[i2][i][1] == 'X':
                    msg+=f'{G[i2][i][1]}'
                Cheking = Chek(msg)
                if Cheking[0] == True:
                    Bool = Cheking[0]
                    Joueur = Cheking[1]

    # Vérification diagonale (haut gauche vers bas droite)
    if Bool == False:
        msg=''
        for i in range(len(G)):
            if G[i][i][1] == 'O' or G[i][i][1] == 'X':
                msg+=f'{G[i][i][1]}'
            Cheking = Chek(msg)
            if Cheking[0] == True:
                Bool = Cheking[0]
                Joueur = Cheking[1]

    # Vérification diagonale (bas gauche vers haut droite)
    if Bool == False:
        y = 2
        msg=''
        for i in range(len(G)):
            if G[i][y][1] == 'O' or G[i][y][1] == 'X':
                msg+=f'{G[i][y][1]}'
            Cheking = Chek(msg)
            if Cheking[0] == True:
                Bool = Cheking[0]
                Joueur = Cheking[1]
            y-=1
            
    return (Bool, Joueur)

def joueur_contre_joueur(J1, J2):
    # Coder par Mael, Lenzo, François
    """
    paramètre = deux joueurs J1 = joueur1 et J2 = joueur2
    initialise la grille
    faire jouer les joueurs à tour de rôle
    vérifier s'il y a un gagnant à chaque coup joué
    afficher la nouvelle grille à chaque
    afficher le nom du vainqueur
    """
    y = None
    x = None
    Player = None
    Tour = 'J1'
    J1 = (J1,'O')
    J2 = (J2,'X')
    Tableau = init_grille()
    while True:

        Player_win = grille_gagnante(Tableau, J1[0], J2[0])

        if Player_win[0]:
            play_again = input(f"{Player_win[1]} a gagné ! voulez-vous rejouer ? (y/n) -> ")
            if play_again == 'y':
                nouvelle_partie(J1[0], J2[0])
            else:
                os.system('cls')
                sys.exit()

        if grille_pleine(Tableau):
            play_again = input("Personne n'a gagné... voulez-vous rejouer ? (y/n) -> ")
            if play_again == 'y':
                nouvelle_partie(J1[0], J2[0])
            else:
                os.system('cls')
                sys.exit()

        if Tour == 'J1':
            Player=J1
        else:
            Player=J2
        
        def y_number():
            number = '123'
            y = input(f"{Player[0]} à toi de jouer, choisi le numéro d'une ligne -> ")
            if y == '':
                print("Le caractère choisi n'est pas valide !")
                y = None
                time.sleep(1)
                return y_number()
            if y in number:
                y = int(y)-1
            else:
                print("Le caractère choisi n'est pas valide !")
                y = None
                time.sleep(1)
                return y_number()
            return y
        def x_number():
            number = '123'
            x = input(f"{Player[0]} à toi de jouer, choisi le numéro d'une colone -> ")
            if x == '':
                print("Le caractère choisi n'est pas valide !")
                x = None
                time.sleep(1)
                return x_number()
            if x in number:
                x = int(x)-1
            else:
                print("Le caractère choisi n'est pas valide !")
                x = None
                time.sleep(1)
                return x_number()
            return x

        Pos = (y_number(), x_number())
        
        Jouer = jouer_un_coup(Tableau, Player, (Pos[0], Pos[1]))
        
        if Jouer == True:
            afficher_grille(Tableau)
            if Tour == 'J1':
                Tour = 'J2'
            else:
                Tour = 'J1'
        elif Jouer == None:
            print("Cette case est déjà utilisée... veuillez rejouer")
            time.sleep(1)
            afficher_grille(Tableau)

def set_name1():
    name = input("Entrer le nom du Joueur 1 -> ")
    return name
def set_name2():
    name = input("Entrer le nom du Joueur 2 -> ")
    return name
name1 = set_name1()
if name1 == '':
    print("Veuillez mettre un premier nom !")
    time.sleep(1)
    name1 = set_name1()
name2 = set_name2()
if name2 == '':
    print("Veuillez mettre un deuxième nom !")
    time.sleep(1)
    name2 = set_name2()
        
joueur_contre_joueur(name1, name2)