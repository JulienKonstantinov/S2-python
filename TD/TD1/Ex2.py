
def suppression_tableau(L,i):
    '''Une fonction qui permet d'enlever un élément d'une liste à un indice donné'''
    K=[] #création d'une liste vide
    for j in range(len(L)): #on parcours la liste
        if j==i: #si on tombe sur le bon indice, on prend la liste jusqu'à cet indice, on l'ajoute à notre liste vide, on supprime le dernier élément, et on ajoute dans un deuxième temps le reste de la première liste
            K=L[:i+1]
            K.pop()
            K=K+L[i+1:]
    return(K)

#Autre méthode :
#Voir photo

liste_test=[1,2,3,4]

print(suppression_tableau(liste_test,1))