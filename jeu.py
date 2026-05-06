import random

def jeu_devinette():
    """Jeu de devinette : deviner un nombre entre 1 et 100"""
    nombre_secret = random.randint(1, 100)
    tentatives = 0
    max_tentatives = 10
    print("=== JEU DE DEVINETTE ===")
    print(f"Devinez un nombre entre 1 et 100. Vous avez {max_tentatives} essais.")
    while tentatives < max_tentatives:
        try:
            guess = int(input(f"Tentative {tentatives+1}/{max_tentatives} : "))
        except ValueError:
            print("Entrez un nombre valide.")
            continue
        tentatives += 1
        if guess < nombre_secret:
            print("Trop petit !")
        elif guess > nombre_secret:
            print("Trop grand !")
        else:
            print(f"Bravo ! Vous avez trouve en {tentatives} tentative(s) !")
            return True
    print(f"Perdu ! Le nombre etait {nombre_secret}.")
    return False

if __name__ == '__main__':
    jeu_devinette()
