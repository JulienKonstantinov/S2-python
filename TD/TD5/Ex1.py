
table_hachage=[[10,20,30],[11,21,111],[12,22,32],[13,23,33],[14,24,34],[15,25,35],[16,26,36],[17,27,37],[18,28,38],[19,29,39]]

print(table_hachage)

#Question1
def rechercher(table,entier):
    unite=str(entier)[-1]
    if entier in table[int(unite)]:
        return True
    else:
        return False

rechercher(table_hachage,20)

#Question2
def ajouter(table,entier):
    if not rechercher(table,entier):
        table[abs(entier%10)].append(entier)

ajouter(table_hachage,20)
print(table_hachage)

#Question3
def supprimer(table,entier):
    for i in range(len(table)):
        for j in range(len(table[i])):
            if entier==table[i][j]:
                table[i][j]=table[i][-1]
                table[i].pop()
                return table

supprimer(table_hachage,20)
print(table_hachage)
    

