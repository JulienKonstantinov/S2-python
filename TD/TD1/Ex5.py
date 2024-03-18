
def deplacer(T,k):
    i,j=0,len(T)-1
    while i!=j:
        if T[i]<k: #si i inférieur à k, on continue de parcourir la liste
            i+=1
        elif T[j]<k: #si j est inférieur à k, on permute T[i] et T[j]
            T[i],T[j]=T[j],T[i] #Permutation
            i+=1
        else:
            j+=1
    return T

def test_deplacer():
    liste_test=list(range(100))[::-1]
    liste_50=deplacer(liste_test,50)
    if all([x<50 for x in liste_50[:50]]): #si tous les éléments d'une liste de 100 à 1 inférieurs ou égaux à 50 sont dans les 50 premières positions de nouvelle liste, alors OK
        print("OK")
    else:
        print("X")