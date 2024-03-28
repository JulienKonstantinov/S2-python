
#Question1
file = open("/Users/julienkonstantinov/Documents/UVSQ/Cours_L1/INFORMATIQUE/Semestre 2/LSIN200N/S2-python/TD/TD4/question1.txt", 'w')
i=0
while i<10000:
    file.write(str(i)+"\n")
    i+=1

file = open("/Users/julienkonstantinov/Documents/UVSQ/Cours_L1/INFORMATIQUE/Semestre 2/LSIN200N/S2-python/TD/TD4/question1.txt", 'r')

tab = []
read = file.readline()
print(read)
while(read!='') :
    tab.append(int(read))
    read = file.readline()
print(tab)

file.close()



#Question2
file2 = open("/Users/julienkonstantinov/Documents/UVSQ/Cours_L1/INFORMATIQUE/Semestre 2/LSIN200N/S2-python/TD/TD4/question2.txt", 'w')
i=0
while i<10000:
    file2.write(str(i)+";")
    i+=1

file2 = open("/Users/julienkonstantinov/Documents/UVSQ/Cours_L1/INFORMATIQUE/Semestre 2/LSIN200N/S2-python/TD/TD4/question2.txt", 'r')

tab2 = []
read2 = file2.readline()
print(read2)
while(read2!='') :
    tab2.append(int(read2))
    read2 = file2.readline()
print(tab2)

file2.close()