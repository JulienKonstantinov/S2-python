import json

lettres={}
entree = open("/Users/julienkonstantinov/Documents/UVSQ/Cours_L1/INFORMATIQUE/Semestre 2/LSIN200N/S2-python/TD/TD4/zadig.txt").read().replace(" ","").replace("\n","")
increment=1/len(entree)
for char in entree:
    if char in lettres.keys():
        lettres[char]+=increment
    else:
        lettres[char]=increment
out=open("/Users/julienkonstantinov/Documents/UVSQ/Cours_L1/INFORMATIQUE/Semestre 2/LSIN200N/S2-python/TD/TD4/statistiques.json",'w')
json.dump(lettres,out,indent=4)
out.close()