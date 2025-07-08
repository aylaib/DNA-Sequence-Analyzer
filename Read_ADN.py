def lire_sequence_de_fichier(nom_fichier):
    """
    Lit une séquence d'ADN à partir d'un fichier.

    Parameters:
    - nom_fichier (str): Le nom du fichier à lire.

    Returns:
    - str: La séquence d'ADN lue depuis le fichier.
    - None: Si le fichier n'est pas trouvé.
    """
    try:
        with open(nom_fichier, 'r') as fichier:
            sequence = fichier.read().strip()
        return sequence
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
        return None
        
