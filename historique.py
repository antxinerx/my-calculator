import datetime


fichier_historique = "historique_calculatrice.txt"

def ajouter_historique(operation, resultat):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ligne = f"[{timestamp}] {operation} = {resultat}\n"
    
    with open(fichier_historique, "a") as fichier:
        fichier.write(ligne)

def lire_historique():
    try:
        with open(fichier_historique, "r") as fichier:
            return fichier.readlines()
    except FileNotFoundError:
        return ["Aucun calcul effectué pour l'instant."]
    print(num1 / num2)