from ADN_Aleatoire import generer_sequence_adn

"""
    Génère une liste de séquences d'ADN aléatoires.

    Parameters:
    - taille_sequence (int): La longueur de chaque séquence d'ADN.
    - nombre_sequences (int): Le nombre de séquences à générer.

    Returns:
    - list: Liste des séquences d'ADN générées.
"""

def generer_sequences_adn2(taille_sequence, nombre_sequences):
        # Générer une liste de séquences en utilisant la fonction existante
    sequences = [generer_sequence_adn(taille_sequence) for _ in range(nombre_sequences)]
    return sequences

"""
    Trouve la séquence consensus à partir d'une liste de séquences d'ADN.

    Parameters:
    - sequences (list): Liste des séquences d'ADN.
    - n (int): Longueur des séquences d'ADN.

    Returns:
    - str: Séquence consensus.
"""
def calculer_profil(sequences, n):
    Profil = {
        'A': [0] * n,
        'C': [0] * n,
        'G': [0] * n,
        'T': [0] * n
    }
    
    # Remplir le profil avec les occurrences de chaque nucléotide à chaque position
    for dna in sequences:
        for i, nuc in enumerate(dna):
            Profil[nuc][i] += 1
    
    return Profil

def calculer_consensus(profil, n):
    result = []
    for i in range(n):
        max_count = 0
        max_nuc = None
        for nuc in ['A', 'C', 'G', 'T']:
            count = profil[nuc][i]
            if count > max_count:
                max_count = count
                max_nuc = nuc
        result.append(max_nuc)
    
    # Concaténer les nucléotides pour obtenir la séquence consensus
    consensus = ''.join(result)
    return consensus

def consensus(sequences, n):
    profil = calculer_profil(sequences, n)
    consensus_sequence = calculer_consensus(profil, n)
    return consensus_sequence, profil
