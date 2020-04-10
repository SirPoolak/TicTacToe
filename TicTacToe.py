# Jeux Morpion
import os

def clear_window(): #Effacer le fenetre windows
    os.system('cls')
    print('*****************')
    print('*  TIC TAC TOE  *')
    print('*****************')
    print('* P1: X * P2: O *')
    print('*****************')
    print('print "quit" to close the game\n')

def jouer(): #Choix de rejouer
    i = 0
    while i < 1:
        print('Do you vant to replay ? (Yes/No)')
        play = input()
        clear_window()
        afficher_plateau(plateau())
        if play.lower() == 'yes' or play.lower() == 'y':
            clear_window()
            i += 1
            return True
        elif play.lower() == 'no' or play.lower() == 'n':
            os.system('cls')
            break

def plateau(): #le plateau de jeux
    list_plateau = [
    ' ',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ',' \n',
    ' ',' ','1',' ','|',' ','2',' ','|',' ','3',' ',' \n',
    ' ',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ',' \n',
    '-','-','-','-','+','-','-','-','+','-','-','-','-\n',
    ' ',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ',' \n',
    ' ',' ','4',' ','|',' ','5',' ','|',' ','6',' ',' \n',
    ' ',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ',' \n',
    '-','-','-','-','+','-','-','-','+','-','-','-','-\n',
    ' ',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ',' \n',
    ' ',' ','7',' ','|',' ','8',' ','|',' ','9',' ',' \n',
    ' ',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ',' \n',]
    return list_plateau

# fonction qui remplace les chifres du plateau par les X pour le Player1 ou O pour le Player2
def remplace_nombre(choix, tours, listplateaujeux, list_victoire_j1, list_victoire_j2):
    int_choix = int(choix)
    idx = listplateaujeux.index(choix)
    if choix == listplateaujeux[idx]:
        if tours % 2 == 0:
            removelist(list_victoire_j2, int_choix)
            listplateaujeux[idx] = 'O'
        else:
            removelist(list_victoire_j1, int_choix)
            listplateaujeux[idx] = 'X'
    clear_window()
    afficher_plateau(listplateaujeux)
    return listplateaujeux, list_victoire_j1, list_victoire_j2

#fonction qui parmet d'afficher le plateau correctement
def afficher_plateau(name):
    x = ''.join(name)
    print(x)

# fonction qui enleve un numero dans toutes les listes d'une même liste
def removelist(list, num):
    for i in list:
        i.append(num)
    for s in list:
        p = set(s)
        s.clear()
        for k in p:
            s.append(k)
    for r in list:
        r.remove(num)
    return list

#fonction qui verifie la victoire
def victoire(list):
    verif = 0
    for i in list:
        if i == []:
            verif +=1
        else:
            verif +=0
    if verif == 1:
        return True

#fonction jeux
def game():
    tours = 0
    list_num_plateau = []
    plateau_jeux = plateau()
    list_victoire_j1 = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
    list_victoire_j2 = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
    clear_window()
    afficher_plateau(plateau_jeux)

    #debut du jeux
    while tours < 10:
        # une fois sur deux on demande quel jouer doit jouer
        if tours % 2 == 0:
            print('\nPayer 2, chose your case:')
        else:
            print('\nPayer 1, chose your case:')

# le choix du joueur
        choix = input()

        # le choix pour quitter la partie
        if choix.lower() == 'quit' or choix.lower() == 'q': #pour quitter le jeux a n'impore quel moment
            os.system('cls')
            break
        # le choix entre 1 et 9
        elif list_num_plateau.count(choix) == 0 and  0 < int(choix) < 10:
            list_num_plateau.append(choix)
            remplace_nombre(choix, tours, plateau_jeux, list_victoire_j1, list_victoire_j2)
            tours += 1
        # quand le choix n'est pas bon
        else:
            clear_window()
            afficher_plateau(plateau_jeux)
            print('\nChoose another number!')

# Verification de victoire
        # Victoire de Player 1
        if victoire(list_victoire_j1) == True:
            clear_window()
            afficher_plateau(plateau_jeux)
            print('\nPLAYER 1 WIN')
            if jouer() == True:
                return game()
            else:
                break
        # Victoire de Player 2
        if victoire(list_victoire_j2) == True:
            clear_window()
            afficher_plateau(plateau_jeux)
            print('\nPLAYER 2 WIN')
            if jouer() == True:
                return game()
            else:
                break
# en cas d'egalité
    else:
        clear_window()
        afficher_plateau(plateau_jeux)
        print('DRAW !')
        if jouer() == True:
            return game()
#lancement du jeux
game()
