import random
"""
    Effectue un nombre spécifié de mutations aléatoires dans une séquence d'ADN.

    Parameters:
    - sequence (str): La séquence d'ADN initiale.
    - nombre_mutations (int): Le nombre de mutations à effectuer.

    Returns:
    - str: La séquence d'ADN mutante après les mutations.
"""
def effectuer_mutations(sequence, nombre_mutations):
        # Bases d'ADN possibles
    bases_adn = ['A', 'C', 'G', 'T']

    # Convertir la séquence en une liste modifiable
    sequence_mutante = list(sequence)

    # Effectuer le nombre spécifié de mutations
    for _ in range(nombre_mutations):
        # Choisir une position aléatoire dans la séquence
        position = random.randint(0, len(sequence) - 1)

        # Choisir un nucléotide différent au hasard
        nouveau_nucleotide = random.choice([base for base in bases_adn if base != sequence_mutante[position]])

        # Effectuer la substitution
        sequence_mutante[position] = nouveau_nucleotide

    # Convertir la liste modifiée en une chaîne
    sequence_mutante = ''.join(sequence_mutante)
    
    return sequence_mutante
