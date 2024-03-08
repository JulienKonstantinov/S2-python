def deplacer(T,k):
    i,j=0,len(T)-1
    while i!=j:
        if T[i]<k:
            i+=1
        elif T[j]<k:
            T[i],T[j]=T[j],T[i] #Permutation
            i+=1
        else:
            j+=1
    return T

def test_deplacer():
    liste_test=list(range(100))[::-1]
    liste_50=deplacer(liste_test,50)
    if all([x<50 for x in liste_50[:50]]):
        print("OK")
    else:
        print("X")