def Check_ADN_Seq(sequence):
    sequence=sequence.upper()
    for i in sequence:
        if i not in ['A','C','G','T']:     # Vérifie que tous les caractères de la séquence sont des bases ADN valides
            return False
    return True