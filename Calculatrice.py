def calculatrice():
    print("Calculatrice")
    print("Opérations disponibles : +, -, *, /")

    try:
        num1 = float(input("Entrez le premier nombre : "))
        operateur = input("Entrez un opérateur : ")
        num2 = float(input("Entrez le deuxième nombre : "))

        if operateur == '+':
            print(f"Résultat : {num1 + num2}")
        elif operateur == '-':
            print(f"Résultat : {num1 - num2}")
        elif operateur == '*':
            print(f"Résultat : {num1 * num2}")
        elif operateur == '/':
            try:
                print(f"Résultat : {num1 / num2}")
            except ZeroDivisionError:
                print("Erreur : Division par zéro !")
        else:
            print("Opérateur invalide.")
    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide.")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")

calculatrice()