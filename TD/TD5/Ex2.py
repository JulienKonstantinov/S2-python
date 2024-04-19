
#Question1
# Fonction de hachage définie en cours

def hachage(str):
    nombre = 0
    i = 0
    while i < len(str):
        nombre += ord(str[i])
        i += 1
    return nombre

def rechercher2(table,valeur):
    h=hachage(valeur if isinstance(valeur,str) else str(valeur))
    for j in table[h%len(table)]:
        if j==valeur:
            return True
    return False
   

#Question2
def ajouter2(table,valeur):
    h=hachage(valeur if isinstance(valeur,str) else str(valeur))
    if not rechercher2(table,valeur):
        table[h%len(table)].append(valeur)


#Question3
def supprimer2(table,valeur):
    h=hachage(valeur if isinstance(valeur,str) else str(valeur))
    i=h%len(table)
    for i in range(len(table)):
        for j in range(len(table[i])):
            if valeur==table[i][j]:
                table[i][j]=table[i][-1]
                table[i].pop()
                return table