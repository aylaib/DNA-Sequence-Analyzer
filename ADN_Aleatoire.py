import random
"""
    Génère une séquence d'ADN aléatoire de la longueur spécifiée.

    Parameters:
    - longueur (int): La longueur de la séquence d'ADN à générer.

    Returns:
    - str: La séquence d'ADN générée.
"""
def generer_sequence_adn(longueur):
        # Liste des bases de l'ADN
    bases_adn = ['A', 'C', 'G', 'T'] 
        # Génération de la séquence d'ADN
    sequence = ''.join(random.choice(bases_adn) for _ in range(longueur))
    return sequence