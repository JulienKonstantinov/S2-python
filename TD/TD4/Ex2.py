
#Question1
liste_prenoms=['Jean','Ali','Bertrand']
file = open("/Users/julienkonstantinov/Documents/UVSQ/Cours_L1/INFORMATIQUE/Semestre 2/LSIN200N/S2-python/TD/TD4/prenoms.txt", 'w')
for i in liste_prenoms:
    file.write(i+"\n")
file.close()

#Question2
file = open("/Users/julienkonstantinov/Documents/UVSQ/Cours_L1/INFORMATIQUE/Semestre 2/LSIN200N/S2-python/TD/TD4/prenoms.txt", 'r')
read = file.readline()
print(read[:-1],",",len(read)-1)
while(read!=''):
    read = file.readline()
    print(read[:-1],",",len(read)-1)
    
file.close()

#Question3
file2 = open("/Users/julienkonstantinov/Documents/UVSQ/Cours_L1/INFORMATIQUE/Semestre 2/LSIN200N/S2-python/TD/TD4/prenoms.csv", 'w')
file = open("/Users/julienkonstantinov/Documents/UVSQ/Cours_L1/INFORMATIQUE/Semestre 2/LSIN200N/S2-python/TD/TD4/prenoms.txt", 'r')
read = file.readline()
file2.write(str(read[:-1])+","+str(len(read)-1)+"\n")
while(read!='') :
    read = file.readline()
    file2.write(str(read[:-1])+","+str(len(read)-1)+"\n")

file.close()
file2.close()
