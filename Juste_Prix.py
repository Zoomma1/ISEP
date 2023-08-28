import random
pmini=1
pmaxi=20
f=0

#Tirer au sort un prix

prix=random.randint(pmini,pmaxi)
prix_user=None

#Choix du joueur
#Si prix trouver -> message
#Sinon affiché pas assez ou trop
#5 essayes
#Si prix non trouvé au bout des 5 essayes afficher message Perdu


for i in range(5):
    try:
        prix_user = int(input("Veuillez choisir un chiffre entre " + str(pmini) + " et " + str(pmaxi) + " : "))
    except ValueError:
        print("Valeur invalide")
        continue
    if prix_user == prix:
        f=1
        break
    else:
        print("Dommage vous n'avez pas trouve il vous reste " + str(5-i) + " essayes")
        if prix_user>prix:
            print("Votre Prix est trop haut ")
        elif prix_user<prix:
            print("Votre prix est trop bas ")
print("Vous avez perdu") if f==0 else print("Felicitaion vous avez gagne !")

#Fin

