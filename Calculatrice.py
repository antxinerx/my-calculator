import datetime
import os
import keyboard

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

def calculatrice():
    print("Calculatrice")
    print("Opérations disponibles : +, -, *, /")

    try:
        num1 = float(input("Entrez le premier nombre : "))
        operateur = input("Entrez un opérateur : ")
        num2 = float(input("Entrez le deuxième nombre : "))

        if operateur == '+':
            resultat = num1 + num2
        elif operateur == '-':
            resultat = num1 - num2
        elif operateur == '*':
            resultat = num1 * num2
        elif operateur == '/':
            try:
                resultat = num1 / num2
            except ZeroDivisionError:
                print("Erreur : Division par zéro !")
                input("Appuyez sur Entrée pour continuer...")
                return
        else:
            print("Opérateur invalide.")
            input("Appuyez sur Entrée pour continuer...") 
            return
        
        print(f"Résultat : {resultat}")
        ajouter_historique(f"{num1} {operateur} {num2}", resultat)
        input("Appuyez sur Entrée pour continuer...") 
    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide.")
        input("Appuyez sur Entrée pour continuer...") 
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
        input("Appuyez sur Entrée pour continuer...") 

    os.system('cls' if os.name == 'nt' else 'clear') # Efface le terminal après le calcul 

def afficher_menu():
    os.system('cls' if os.name == 'nt' else 'clear') 
    print("\n--- Menu ---")
    print("1. Effectuer un calcul")
    print("2. Voir l'historique")
    print("3. Quitter")

if __name__ == "__main__":
    while True:
        afficher_menu()
        choix = input("Entrez votre choix (1-3) : ")
        os.system('cls' if os.name == 'nt' else 'clear') # Le code pour effacer le terminal est déplacé ici

        if choix == '1':
            calculatrice()
        elif choix == '2':
            print("\nHistorique des calculs :")
            historique = lire_historique()
            for ligne in historique:
                print(ligne, end="")
            input("Appuyez sur Entrée pour continuer...") 
        elif choix == '3':
            break
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 3.")

