# fichier vers tableau
def fichierVersTableau(nomFichier):
    f = open(nomFichier, "rb")
    T = array([{} for i in range(999999)])
    n = 0
    try:
        while True:
            livre = load(f)
            T[n] = livre
            n += 1
    except EOFError:
        f.close()
    return T[:n], n

# tableau vers fichier
def tableauVersFichier(T, nomFichier):
    f = open(nomFichier, "wb")
    for i in range(len(T)):
        dump(T[i], f)
    f.close()

# afficher livres.dat
def afficher():
    f = open("livres.dat", "rb")
    try:
        while True:
            livre = load(f)
            print(livre)
    except EOFError:
        f.close()

# mise a jour du disponibilite d'un livre
def maj():
    afficher()
    ref = int(input("Reference: "))
    estAjout = input("Ajouter ou retirer (a/r): ")
    T,n = fichierVersTableau("livres.dat")
    i = 0
    while i < n and T[i]["ref"] != ref:
        i += 1
    if i < n:
        if estAjout == "a":
            T[i]["disp"] += 1
        else:
            T[i]["disp"] -= 1
        tableauVersFichier(T, "livres.dat")
    else:
        print("Reference invalide")
