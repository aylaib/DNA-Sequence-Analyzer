def calculer_frequences_codons(sequence):
    """
    Calcule les fréquences relatives des codons dans une séquence d'ADN.

    Parameters:
    - sequence (str): La séquence d'ADN.

    Returns:
    - dict: Un dictionnaire contenant les fréquences relatives des codons.
    """
    # Initialiser un dictionnaire pour stocker les fréquences des codons
    frequences_codons = {}

    # Parcourir la séquence par pas de 3 (car les codons ont une longueur de 3)
    for i in range(0, len(sequence), 3):
        # Extraire le codon de la séquence
        codon = sequence[i:i+3]

        # Mettre à jour le compteur de fréquence du codon dans le dictionnaire
        if codon in frequences_codons:
            frequences_codons[codon] += 1
        else:
            frequences_codons[codon] = 1

    # Calculer les fréquences relatives en divisant par la longueur totale de la séquence
    total_codons = len(sequence) // 3
    frequences_relative = {codon: count / total_codons for codon, count in frequences_codons.items()}

    return frequences_relative
