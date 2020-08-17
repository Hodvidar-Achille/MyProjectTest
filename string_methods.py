prenom = "Paul"
nom = "Dupont"
age = 21
print(
    "Je m'appelle {0} {1} ({3} {0} pour l'administration) et j'ai {2} "
    "ans.".format(prenom, nom, age, nom.upper()))

date = "Dimanche 24 juillet 2011"
heure = "17:00"
print("Cela s'est produit le {}, à {}.".format(date, heure))

# formatage d'une adresse
adresse = """
{no_rue}, {nom_rue}
 {code_postal} {nom_ville} ({pays})
""".format(no_rue=5, nom_rue="rue des Postes", code_postal=75003, nom_ville="Paris", pays="France")
print(adresse)

chaine = "Salut les ZER0S !"
print(chaine)
print("1ere lettre : "+chaine[0])
print("2e lettre : "+chaine[2])
print("dernière lettre : "+chaine[-1])
print("Quelques lettres : "+chaine[5:12])
print("Toutes sauf début : "+chaine[3:])
