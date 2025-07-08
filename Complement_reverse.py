DNA_COMPREVERSE = {'A': 'T','T': 'A','G': 'C','C': 'G'}
"""
    Effectue la complémentarité inverse d'une séquence d'ADN.

    Parameters:
    - sequence (str): La séquence d'ADN à inverser.

    Returns:
    - str: La séquence complémentaire inverse.
"""
    # Utilise la correspondance des bases pour inverser la séquence et obtenir la complémentarité inverse
    
def CompReverse(sequence):
    return ''.join([DNA_COMPREVERSE[nuc] for nuc in sequence])[::-1]
