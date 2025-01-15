def calculatrice():
    print("Calculatrice")
    print("Opérations disponibles : +, -, *, /")
    
    num1 = float(input("Entrez le premier nombre : "))
    operateur = input("Entrez un opérateur : ")
    num2 = float(input("Entrez le deuxième nombre : "))
    
    # Ajout de l'historique pour complexifier le code
    
    if operateur == '+':
        print(f"Résultat : {num1 + num2}")
    elif operateur == '-':
        print(f"Résultat : {num1 - num2}")
    elif operateur == '*':
        print(f"Résultat : {num1 * num2}")
    elif operateur == '/':
        if num2 != 0:
            print(f"Résultat : {num1 / num2}")
        else:
            print("Erreur : Division par zéro !")
    else:
        print("Opérateur invalide.")

calculatrice()
