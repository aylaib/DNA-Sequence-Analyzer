"""
    Compte le nombre d'occurrences de chaque base nucléique dans une séquence d'ADN.

    Parameters:
    - sequence (str): La séquence d'ADN à analyser.

    Returns:
    - dict: Un dictionnaire contenant le nombre d'occurrences de chaque base (A, C, G, T).
"""
    
def CountNuc(sequence):
        # Initialiser un dictionnaire pour stocker les fréquences des bases nucléiques
    Freq = {"A": 0,"C": 0,"G": 0,"T": 0,}
        # Parcourir la séquence et mettre à jour les fréquences
    for nuc in sequence:
        Freq[nuc] += 1
    return Freq