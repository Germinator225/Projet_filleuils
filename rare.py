#programme permettant de créer un fichier, de l'ouvrir et de le lire
import pickle
#pour commencer je vais definir des fonctions qui m'interessent
def ajouter():
    'ajouter des elements au fichier'
    fichier = open(nom_fichier, 'w')
    while 1:
        texte=input("entrez le nom du texte")
        fichier.write(texte+'\n')
        if texte=="":
            break
    fichier.close()

def troncature(mot):
    'couper la dernière lettre du mot'
    vari=""
    a,b=0,len(mot)-1
    while a<b:
        vari=vari+mot[a]
        a=a+1
    return vari

def afficher():
    'afficher les elements du fichier'
    ff=0
    nombre=[]
    liste=[]
    gg=0
    fichier = open(nom_fichier, 'r')
    while 1:
        lecture=fichier.readline()
        if lecture=="":
            break
        x1=troncature(lecture)
        liste.append(x1)
    fichier.close()
    return liste
    while ff<len(liste):
        nombre.append(len(liste[ff]))
        a=a+1
    return nombre
    while gg<len(nombre):
        if max(nombre)==nombre[gg]:
            return liste[gg]
        gg=gg+1
    print(liste[gg])



#-------------------------------------programme principale--------------------------------------

nom_fichier=input('entrer le nom du fichier')
bb=input("voulez vous afficher du contenu (O) ou ajouter du contenu (A)?")
if bb=="O" or bb=="o":
    afficher()
elif bb=="A" or bb=="a":
    ajouter()
    cc=input("voulez vous afficher le contenu ? O ou N")
    if cc=="o" or cc=="O" :
        afficher()


