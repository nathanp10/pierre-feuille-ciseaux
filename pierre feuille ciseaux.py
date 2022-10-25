import random
def jeu():
    if joueur==1 or ordi==1:
        print('ciseaux')
    elif joueur==2 or ordi==2:
        print('pierre')
    elif joueur==3 or ordi==3:
        print('papier')
scoreordi=0
scorejoueur=0
joueur=1
nom=input('Quel est votre nom ? ')
nomordi='Michel'

joueur=int(input(' 0 = sortir\n 1 = pierre\n 2 = feuille \n 3 = ciseaux\n Alors tu choisit quoi chakal ?\n  '))

while joueur!=0 or ( scorejoueur <=3 or scoreordi<=3 ) :
    ordi= random.randint(1,3)
    if (joueur < ordi and joueur+1==ordi) or (joueur> ordi and joueur-2==ordi):
        scoreordi=scoreordi+1
        print('\n',nomordi,' ',ordi,'-',joueur,' ',nom)
        print(' Vous avez perdu!!! \n','Score de',nomordi,scoreordi,'-','Score de ',nom,scorejoueur,'\n')
        
    elif joueur==ordi:
        print('\n',ordi,'-',joueur)
        print('Egalité\n','Score de',nomordi,scoreordi,'-','Score de',nom,scorejoueur,'\n')
    else:
        scorejoueur=scorejoueur+1
        print('\n',ordi,'-',joueur)
        print('Vous avez gagner \n','Score de',nomordi,scoreordi,'-','Score de',nom,scorejoueur,'\n')
    joueur=int(input(' 0 = sortir\n 1 = pierre\n 2 = feuille \n 3 = ciseaux\n Alors tu choisit quoi chakal ?\n  '))
print("Merci d'avoir joué")
