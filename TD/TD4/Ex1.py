
#Question1
file = open("/Users/julienkonstantinov/Documents/UVSQ/Cours_L1/INFORMATIQUE/Semestre 2/LSIN200N/S2-python/TD/TD4/question1.txt", 'w') #on ouvre le fichier en écriture
i=0
while i<10000:
    file.write(str(i)+"\n") #on écrit tous les entiers avec un retour à la ligne tant que i est inférieur à 10000
    i+=1

file.close() #on ferme le fichier en écriture

file = open("/Users/julienkonstantinov/Documents/UVSQ/Cours_L1/INFORMATIQUE/Semestre 2/LSIN200N/S2-python/TD/TD4/question1.txt", 'r') #on ouvre le fichier en lecture

tab = [] #on créé un tableau vide
read = file.readline() #on définit read qui lit la première ligne
while(read!='') : #tant que read lit un caractère, on ajoute ce caractère au tableau, puis on passe à la ligne suivante
    tab.append(int(read))
    read = file.readline()
print(tab) #affichage du tableau

file.close() #on ferme le fichier en lecture



#Question2
file2 = open("/Users/julienkonstantinov/Documents/UVSQ/Cours_L1/INFORMATIQUE/Semestre 2/LSIN200N/S2-python/TD/TD4/question2.txt", 'w')
i=0
while i<10000:
    file2.write(str(i)+";")
    i+=1

file2.close()

file2 = open("/Users/julienkonstantinov/Documents/UVSQ/Cours_L1/INFORMATIQUE/Semestre 2/LSIN200N/S2-python/TD/TD4/question2.txt", 'r')

tab2 = []
read2 = file2.readline()

while(read2!='') :
    tab2.append(int(read2.split(";")))
    read2 = file2.readline()
print(tab2)

file2.close()