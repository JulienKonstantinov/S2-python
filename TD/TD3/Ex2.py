
#Question1
def ajout_reference():
    article={}
    prix=float(input("Entrez le prix"))
    article['prix']=prix

    quantite=int(input("Entrez le nombre de produits restants"))
    article['quantite']=quantite

    couleur=input("Quelle est la couleur du produit ?")
    article['couleur']=couleur

    return article

reference = ajout_reference()
print(reference)

#Question2
stock=[]
menu=1
while menu!=2:
    stock.append(ajout_reference())
    print("Que voulez-vous faire ?")
    print("Ajouter référence, tapez 1")
    print("Quittez, tappez 2")
    menu=int(input())


montant_total=0
for i in len(stock):
    montant_total+=stock[i]["Prix"]*stock[i]["Quantité"]
    i+=1
print

