def suppression_tableau(L,i):
    '''Une fonction qui permet d'enlever un élément d'une liste à un indice donné'''
    K=[]
    for j in range(len(L)):
        if j==i:
            K=L[:i+1]
            K.pop()
            K=K+L[i+1:]
    return(K)

#Autre méthode :
#Voir photo

liste_test=[1,2,3,4]

print(suppression_tableau(liste_test,1))