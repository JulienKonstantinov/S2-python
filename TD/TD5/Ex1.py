
table_hachage=[1,2,3,4,5,6,7,8,9,9,9]

#Question1
def rechercher(table,entier):
    if entier in table:
        print("True")
    elif type(entier)!=int:
        print("Ce n'est pas un entier !")
    else:
        print("False")

rechercher(table_hachage,9)

#Question2
def ajouter(table,entier):
    if entier not in table and type(entier)==int:
        table.append(entier)
    elif type(entier)!=int:
        print("Ce n'est pas un entier !")
    else:
        pass

ajouter(table_hachage,10)
print(table_hachage)

#Question3
def supprimer(table,entier):
    if entier in table and type(entier)==int:
        while entier in table:
            table.remove(entier)
    elif type(entier)!=int:
        print("Ce n'est pas un entier !")
    else:
        pass

supprimer(table_hachage,9)
print(table_hachage)
    

