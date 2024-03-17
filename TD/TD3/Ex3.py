
#Question1
trad = {"Stop" : "Stop", "Violet" : "Purple", "Chat" : 'Cat', "Chien" : "Dog", "Lapin" : "Rabbit"}
trad["Rose"] = "Pink"
print(trad)


#Question2
def ajout(mot1, mot2, dico):
    if mot1 in dico:
        print("Deja")
        pass
    else:
        dico[mot1] = mot2

    return dico

print(ajout("Bonjour", "Hello",trad))


#Question3
def affichage(dico):
    return dico.values()

print(affichage(trad))


#Question4
def supprime(car, dico):
    cles_a_supprimer = []
    
    for clé in dico.keys():
        if clé[0]==car:
            cles_a_supprimer.append(clé)

    for clé in cles_a_supprimer:
        del dico[clé]
# Car on ne peut pas modifier un dico en cours de boucle
    return dico

trad_2 = {"Stop" : "Stop_1", "Violet" : "Purple", "Chat" : 'Cat', "Chien" : "Dog", "Lapin" : "Rabbit"}
print(supprime("S", trad_2))