from ADN_Aleatoire import generer_sequence_adn
from ADN_consensus import generer_sequences_adn2, calculer_profil, calculer_consensus
from ADN_TO_ARN import Transcription
from Codon_frequencies import calculer_frequences_codons
from Complement_reverse import DNA_COMPREVERSE, CompReverse
from Count_bases import CountNuc
from GC_content import gc_content
from Motif import cherche_motif
from Mutation import effectuer_mutations
from Read_ADN import lire_sequence_de_fichier
from Translation import RNA_TO_PROTIEN
from Validate_ADN import Check_ADN_Seq

while True:
    print("\nMenu principal:")
    print("1. Générer une chaîne ADN aléatoire")
    print("2. Choisir une chaîne ADN à partir d'un fichier")
    print("0. Quitter")

    choix_menu_principal = input("Veuillez choisir une option (0-2): ")

    if choix_menu_principal == '0':
        print("Au revoir!")
        break

    elif choix_menu_principal == '1':
        longueur = int(input("Entrez la longueur de la séquence ADN aléatoire: "))
        sequence = generer_sequence_adn(longueur)
        print("Séquence ADN générée:", sequence)

    elif choix_menu_principal == '2':
        fichier = input("Entrez le nom du fichier contenant la séquence ADN: ")
        sequence = lire_sequence_de_fichier(fichier)  
        print("Séquence ADN générée:", sequence)

    if sequence:
        while True:
            print("\nSous-menu - Options pour la séquence ADN à partir d'un fichier:")
            print("3. Vérifier la validité de la chaîne ADN")
            print("4. Calculer les fréquences des bases nucléiques dans la chaîne ADN")
            print("5. Transcrire la chaîne ADN en une chaîne ARN")
            print("6. Transcrire la chaîne ARN en protéines (acides aminés)")
            print("7. Calculer le complément inverse de la chaîne ADN")
            print("8. Calculer le taux de GC de la séquence ADN")
            print("9. Calculer les fréquences de codons dans la chaîne ADN")
            print("10. Réaliser des mutations aléatoires sur la chaîne ADN")
            print("11. Chercher un motif dans la chaîne ADN")
            print("12. Générer la chaîne ADN consensus et la matrice profil")
            print("0. Retour au menu principal")

            choix_sous_menu = input("Veuillez choisir une option (0-12): ")

            if choix_sous_menu == '0':
                break  # Retour au menu principal

            elif choix_sous_menu == '3':
                # Vérifier la validité de la séquence ADN
                if sequence and Check_ADN_Seq(sequence):
                    print("La séquence ADN est valide.")
                else:
                    print("La séquence ADN n'est pas valide, Veuillez lire un autre fichier")
                    break
            elif choix_sous_menu == '4':
                # Calculer les fréquences des bases nucléiques
                frequencies = CountNuc(sequence)
                print("Fréquences des bases nucléiques:", frequencies)

            elif choix_sous_menu == '5':
                # Transcrire la chaîne ADN en ARN
                arn_sequence = Transcription(sequence)
                print("Séquence ARN correspondante:", arn_sequence)

            elif choix_sous_menu == '6':
                # Transcrire la chaîne ARN en protéines
                arn_sequence = Transcription(sequence)
                RNA_TO_PROTIEN(arn_sequence)

            elif choix_sous_menu == '7':
                # Calculer le complément inverse
                comp_reverse_sequence = CompReverse(sequence)
                print("Complément inverse de la séquence ADN:", comp_reverse_sequence)

            elif choix_sous_menu == '8':
                # Calculer le taux de GC
                gc_percentage = gc_content(sequence)
                print("Taux de GC de la séquence ADN:", gc_percentage, "%")

            elif choix_sous_menu == '9':
                # Calculer les fréquences de codons
                codon_frequencies = calculer_frequences_codons(sequence)
                print("Fréquences des codons:", codon_frequencies)

            elif choix_sous_menu == '10':
                # Réaliser des mutations aléatoires
                mutations = int(input("Entrez le nombre de mutations à réaliser: "))
                mutated_sequence = effectuer_mutations(sequence, mutations)
                print("Séquence ADN mutante:", mutated_sequence)

            elif choix_sous_menu == '11':
                # Chercher un motif dans la chaîne ADN
                motif = input("Entrez le motif à rechercher: ")
                positions = cherche_motif(sequence, motif)
                if positions:
                    print(f"Le motif '{motif}' a été trouvé aux positions : {positions}")
                else:
                    print(f"Le motif '{motif}' n'a pas été trouvé dans la séquence.")


            elif choix_sous_menu == '12':
                # Générer la chaîne ADN consensus et la matrice profil
                n = int(input("Entrez la longueur des séquences ADN: "))
                m = int(input("Entrez le nombre de séquences ADN: "))
                sequences = generer_sequences_adn2(n, m)
                print("Les sequences sont", sequences)
                
                matrice = calculer_profil(sequences, n)
                print("Matrice Profil:")
                
                for nucleotide, occurrences in matrice.items():
                    print(f"{nucleotide} : {', '.join(map(str, occurrences))}")
                
                consensus_sequence = calculer_consensus(matrice, n)
                print("Chaîne ADN consensus:", consensus_sequence)

            else:
                print("Option non valide. Veuillez choisir un nombre entre 0 et 12.")

