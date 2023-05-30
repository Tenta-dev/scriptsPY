# print("Salut") #Affiche une donnée de type chaine de caractère
# print(2023) #Affiche une donnée de type nombre
# print(" ============ ")
# print(" < Mon code > ") #test
# print(" ============ ")

# leNom = input("Veuillez saisir votre prénom : ") #Permet de saisir une donnée dans une variable
# print("Votre nom : " + leNom) #Affiche le nom concaténé avec une chaine de caractère

# anneeNaissance = int(input("Veuillez saisir votre date de naissance : "))
# age = 2023 - anneeNaissance
# print(leNom, "né en", anneeNaissance, "as donc", age, "ans.")

# userFirstName = "Benjamin"
# userLastName = "Cls"
# userAge = 24
# userHeight = 170
# userWork = True

# user = {
#     "nom": userFirstName,
#     "prenom": userLastName,
#     "age": userAge,
#     "taille": userHeight,
#     "travaille": userWork
# }
# user["nom"] = input("saisie : ")
# print(user["nom"])

from datetime import datetime

annee = datetime.now().year

print(annee)