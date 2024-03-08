def insertion_tableau(L,v,i):
    '''Une fonction qui permet d'insérer une valeur à un indice donnée d'une liste'''
    #test de la validité de la position
    if i < 0 or i > len(L):
        return
    
    L.append(0) #on ajoute une case
    j=len(L)-1
    while i<j:
        L[j]=L[j-1] #on décale les éléments
        j-=1
    L[i]=v
    return(L)


liste_test=[1,2,3,4]

print(insertion_tableau(liste_test,1,2))

