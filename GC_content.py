def gc_content(sequence):
    return round((sequence.count('C') + sequence.count('G')) / len(sequence) * 100)
