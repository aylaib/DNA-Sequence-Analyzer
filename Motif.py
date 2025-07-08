"""
    Recherche un motif dans une séquence d'ADN.

    Parameters:
    - sequence (str): La séquence d'ADN dans laquelle rechercher le motif.
    - motif (str): Le motif à rechercher.

    Returns:
    - int or None: La position du début du motif dans la séquence (1-indexed) s'il est trouvé,
      ou None si le motif n'est pas présent dans la séquence.
"""
def cherche_motif(sequence, motif):
    positions = []
    for i in range(len(sequence)):
                        # Vérifier si la séquence à partir de l'indice i commence par le motif
        if sequence[i:].startswith(motif):
                        # Retourner la position du début du motif (1-indexed)
            positions.append(i+1)
    return positions
