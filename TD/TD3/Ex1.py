
#Question1
lunes = {'Mercure':0,'Vénus':0,'Terre':1,'Mars':2}
lunes['Jupyter']=63
lunes['Saturne']=61
lunes['Uranus']=27
lunes['Neptune']=11

#Question2a
lunes['Neptune']=13
print(lunes)

#Question2b
print("Le nombre de satellites de la Terre est", lunes['Terre'])

#Question2c
print("La liste des planètes est :",list(lunes))

#print("Le nombre de satellites de chaque planète est :")
#clef=list(lunes)
#for i in range(len(clef)):
    #cl=clef[i]
    #print(cl, ,lunes[cl])
    #i+=1"""

#Question2d
for i in lunes.values():
    print("Le nombre de satellites de", list(lunes)[i], "est :",i)

#Question2e
#print("Le nombre total de satellites est :",)
#valeur=list(lunes.values())
#v=0
#for i in range(len(valeur)):
    #v+=valeur[i]
    #i+=1
    #str(v)

print("somme :",  sum(lunes.values()))




