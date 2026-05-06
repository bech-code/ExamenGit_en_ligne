def addition(a, b):
    """Retourne la somme de a et b"""
    return a + b

def soustraction(a, b):
    """Retourne la difference entre a et b"""
    return a - b

def multiplication(a, b):
    """Retourne le produit de a et b"""
    return a * b

def division(a, b):
    """Retourne la division de a par b"""
    if b == 0:
        raise ValueError("Division par zero impossible")
    return a / b

def est_pair(n):
    """Retourne True si n est pair"""
    return n % 2 == 0

def factorielle(n):
    """Retourne la factorielle de n"""
    if n < 0:
        raise ValueError("Entier negatif")
    if n == 0:
        return 1
    return n * factorielle(n - 1)

def fibonacci(n):
    """Retourne le n-ieme terme de Fibonacci"""
    if n <= 0: return 0
    if n == 1: return 1
    return fibonacci(n-1) + fibonacci(n-2)

def est_premier(n):
    """Retourne True si n est premier"""
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def inverser_chaine(s):
    """Retourne la chaine s inversee"""
    return s[::-1]

def max_liste(lst):
    """Retourne le maximum d'une liste"""
    if not lst:
        raise ValueError("Liste vide")
    return max(lst)
