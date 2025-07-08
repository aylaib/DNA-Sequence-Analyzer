import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import random
from tkinter import Scrollbar

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


class DNAAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DNA Analyzer App")
        self.root.resizable(width=False, height=False)

        # Chargez l'image pour le fond d'écran
        image_path = "assets/Dna.jpg"
        self.image = Image.open(image_path)
        self.background_image = ImageTk.PhotoImage(self.image)

        # Ajustez les dimensions de la fenêtre
        window_width = 800
        window_height = 800
        self.root.geometry(f"{window_width}x{window_height}")

        # Créez un canevas avec le fond d'écran
        self.canvas = tk.Canvas(root, width=window_width, height=window_height)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)

        # Ajoutez le message au-dessus de l'image et au milieu
        label_text = "Hello, you are in\nDNA Analyzer App"
        label = tk.Label(root, text=label_text, font=("Poppins", 26, "bold"), bd=2, bg="#FBE1D8")
        label.place(relx=0.5, rely=0.13, anchor=tk.CENTER)

        # Ajoutez les trois boutons
        generate_button = tk.Button(
            root,
            text="Générer l'ADN aléatoire",
            font=("Poppins", 16, "bold"),
            bg="#FFCEB5",
            fg="#1C1C1C",
            bd=3,
            relief="solid",
            borderwidth=3,
            highlightthickness=0,
            command=lambda: self.show_specific_window("generate"),
        )
        generate_button.place(relx=0.288, rely=0.26, height=60, width=340)
        read_button = tk.Button(
            root,
            text="Lire un fichier",
            font=("Poppins", 16, "bold"),
            bg="#FFCEB5",
            fg="#1C1C1C",
            bd=3,
            relief="solid",
            borderwidth=3,
            highlightthickness=0,
            command=self.choose_file,
        )
        read_button.place(relx=0.288, rely=0.36, height=60, width=340)
        quit_button = tk.Button(
            root,
            text="Quitter",
            font=("Poppins", 16, "bold"),
            bg="#FFCEB5",
            fg="#1C1C1C",
            bd=3,
            relief="solid",
            borderwidth=3,
            highlightthickness=0,
            command=root.destroy,
        )
        quit_button.place(relx=0.288, rely=0.46, height=60, width=340)

        self.length_entry = None
        self.submit_button = None

    def choose_file(self):
        file_path = filedialog.askopenfilename(title="Choisir un fichier")
        if file_path:
            # Si un fichier est sélectionné, affichez la deuxième fenêtre
            self.show_specific_window("read", file_path)

    
    def show_specific_window(self, action, file_path=None):
        self.root.withdraw()
        specific_window = tk.Toplevel()
        specific_window.title("DNA Analyzer Options")
        specific_window.resizable(width=False, height=False)  # Ajoutez cette ligne

        # Chargez une autre image pour le fond d'écran en fonction de l'action
        new_image_path = "assets/rna.jpg"
        new_image = Image.open(new_image_path)

        # Redimensionnez l'image pour qu'elle couvre toute la fenêtre
        new_image = new_image.resize((800, 800), Image.LANCZOS)
        new_background_image = ImageTk.PhotoImage(new_image)

        # Ajustez les dimensions de la nouvelle fenêtre
        window_width = 800
        window_height = 800
        specific_window.geometry(f"{window_width}x{window_height}")

        # Créez un canevas avec le fond d'écran
        specific_canvas = tk.Canvas(specific_window, width=window_width, height=window_height)
        specific_canvas.pack()
        specific_canvas.create_image(0, 0, anchor=tk.NW, image=new_background_image)


        # Générer la séquence ADN aléatoire si l'action est "generate"
        sequence_adn = None
        if action == "read" and file_path:
            sequence_adn = lire_sequence_de_fichier(file_path)
        
        # Lire la séquence ADN à partir du fichier si l'action est "read"
        elif action == "generate":
            length_label = tk.Label(specific_window, text="Entrez la longueur de la\nséquence ADN aléatoire:", font=("Poppins", 22, "bold"), bd=2, bg="#FBE1D8")
            length_label.place(relx=0.5, rely=0.135, anchor=tk.CENTER)

            length_entry = tk.Entry(
                specific_window,
                font=("Poppins", 16, "bold"),
                bg="#FFEEE5",
                fg="#1C1C1C",
                bd=3,
                relief=tk.FLAT,
                borderwidth=20,
                highlightthickness=0,
            )
            length_entry.place(relx=0.39, rely=0.26, height=60, width=170)
            
            submit_button = tk.Button(
                specific_window,
                text="Générer",
                font=("Poppins", 16, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.generate_sequence_and_display(length_entry, submit_button, return_button, specific_window)
            )
            submit_button.place(relx=0.28, rely=0.36, height=60, width=340)
            return_button = tk.Button(
                specific_window,
                text="Retour au menu principal",
                font=("Poppins", 16, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.return_to_main_menu(specific_window),
            )
            return_button.place(relx=0.28, rely=0.46, height=60, width=340)

        if (sequence_adn):
            # Ajouter le Text widget pour afficher la séquence ADN
            text_frame = tk.Frame(specific_window,
                bg="#FFEEE5",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
            )
            text_frame.place(relx=0.53, rely=0.26, height=442, width=360)
            text_widget = tk.Text(text_frame,
                wrap="word",
                bg="#FFEEE5",
                font=("Poppins", 12, "bold"),
                bd=0,
                relief=tk.FLAT,
                highlightthickness=0,
            )
            text_widget.insert(tk.END, f"Séquence ADN :\n{sequence_adn}")
            scrollbar = tk.Scrollbar(text_frame, command=text_widget.yview)
            scrollbar.pack(side="right", fill="y")
            text_widget.config(yscrollcommand=scrollbar.set)
            text_widget.pack(padx=10, pady=10, fill="both", expand=True) 

            # text_widget.insert(tk.END, f"Séquence ADN :\n\n{sequence_adn}")

            check_validity_button = tk.Button(
                specific_window,
                text="Vérifier la validité de ADN",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.perform_option(3, sequence_adn, text_widget),
            )
            check_validity_button.place(relx=0.02, rely=0.26, height=50, width=400)

            calculate_frequencies_button = tk.Button(
                specific_window,
                text="Calculer les fréquences des bases nucléiques",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.perform_option(4, sequence_adn, text_widget),
            )
            calculate_frequencies_button.place(relx=0.02, rely=0.33, height=50, width=400)

            transcribe_to_arn_button = tk.Button(
                specific_window,
                text="Transcrire ADN en une chaîne ARN",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.perform_option(5, sequence_adn, text_widget),
            )
            transcribe_to_arn_button.place(relx=0.02, rely=0.40, height=50, width=400)

            translate_to_protein_button = tk.Button(
                specific_window,
                text="Transcrire ARN en protéines",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.perform_option(6, sequence_adn, text_widget),
            )
            translate_to_protein_button.place(relx=0.02, rely=0.47, height=50, width=400)

            reverse_complement_button = tk.Button(
                specific_window,
                text="Calculer le complément inverse de ADN",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.perform_option(7, sequence_adn, text_widget),
            )
            reverse_complement_button.place(relx=0.02, rely=0.54, height=50, width=400)

            calculate_gc_content_button = tk.Button(
                specific_window,
                text="Calculer le taux de GC de la séquence ADN",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.perform_option(8, sequence_adn, text_widget),
            )
            calculate_gc_content_button.place(relx=0.02, rely=0.61, height=50, width=400)

            calculate_codon_frequencies_button = tk.Button(
                specific_window,
                text="Calculer les fréquences de codons",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.perform_option(9, sequence_adn, text_widget),
            )
            calculate_codon_frequencies_button.place(relx=0.02, rely=0.68, height=50, width=400)

            mutate_dna_button = tk.Button(
                specific_window,
                text="Réaliser des mutations aléatoires sur ADN",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.perform_input_option(10, sequence_adn, text_widget, specific_window, mutate_dna_button),
            )
            mutate_dna_button.place(relx=0.02, rely=0.75, height=50, width=400)

            search_motif_button = tk.Button(
                specific_window,
                text="Chercher un motif dans ADN",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.perform_input_option(11, sequence_adn, text_widget, specific_window, search_motif_button),
            )
            search_motif_button.place(relx=0.02, rely=0.82, height=50, width=400)

            consensus_button = tk.Button(
                specific_window,
                text="Générer ADN consensus et la matrice profil",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.perform_input_option(12, sequence_adn, text_widget, specific_window, consensus_button),
            )
            consensus_button.place(relx=0.02, rely=0.89, height=50, width=400)

            save_file = tk.Button(
                specific_window,
                text="Enregistrer l'historique dans un fichier",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.save_to_file(text_widget),
            )
            save_file.place(relx=0.53, rely=0.82, height=50, width=360)

            return_button = tk.Button(
                specific_window,
                text="Retour au menu principal",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.return_to_main_menu(specific_window),
            )
            return_button.place(relx=0.53, rely=0.89, height=50, width=360)
        # Gardez une référence à l'image pour éviter la destruction par le garbage collector
        specific_canvas.image = new_background_image


    def generate_sequence_and_display(self, length_entry, submit_button, return_button, specific_window):
        length = length_entry.get()
        if length.isdigit():
            length = int(length)
            sequence_adn = generer_sequence_adn(length)
            print("Séquence ADN générée:", sequence_adn)

            # Fermer la fenêtre de génération de séquence et afficher la séquence générée
            length_entry.destroy()
            submit_button.destroy()
            return_button.destroy()

            # Ajouter le Text widget pour afficher la séquence ADN
            text_frame = tk.Frame(specific_window,
                bg="#FFEEE5",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
            )
            text_frame.place(relx=0.53, rely=0.26, height=442, width=360)
            text_widget = tk.Text(text_frame,
                wrap="word",
                bg="#FFEEE5",
                font=("Poppins", 12, "bold"),
                bd=0,
                relief=tk.FLAT,
                highlightthickness=0,
            )
            text_widget.insert(tk.END, f"Séquence ADN :\n{sequence_adn}")
            scrollbar = tk.Scrollbar(text_frame, command=text_widget.yview)
            scrollbar.pack(side="right", fill="y")
            text_widget.config(yscrollcommand=scrollbar.set)
            text_widget.pack(padx=10, pady=10, fill="both", expand=True) 

            # text_widget.insert(tk.END, f"Séquence ADN :\n\n{sequence_adn}")

            check_validity_button = tk.Button(
                specific_window,
                text="Vérifier la validité de ADN",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.perform_option(3, sequence_adn, text_widget),
            )
            check_validity_button.place(relx=0.02, rely=0.26, height=50, width=400)

            calculate_frequencies_button = tk.Button(
                specific_window,
                text="Calculer les fréquences des bases nucléiques",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.perform_option(4, sequence_adn, text_widget),
            )
            calculate_frequencies_button.place(relx=0.02, rely=0.33, height=50, width=400)

            transcribe_to_arn_button = tk.Button(
                specific_window,
                text="Transcrire ADN en une chaîne ARN",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.perform_option(5, sequence_adn, text_widget),
            )
            transcribe_to_arn_button.place(relx=0.02, rely=0.40, height=50, width=400)

            translate_to_protein_button = tk.Button(
                specific_window,
                text="Transcrire ARN en protéines",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.perform_option(6, sequence_adn, text_widget),
            )
            translate_to_protein_button.place(relx=0.02, rely=0.47, height=50, width=400)

            reverse_complement_button = tk.Button(
                specific_window,
                text="Calculer le complément inverse de ADN",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.perform_option(7, sequence_adn, text_widget),
            )
            reverse_complement_button.place(relx=0.02, rely=0.54, height=50, width=400)

            calculate_gc_content_button = tk.Button(
                specific_window,
                text="Calculer le taux de GC de la séquence ADN",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.perform_option(8, sequence_adn, text_widget),
            )
            calculate_gc_content_button.place(relx=0.02, rely=0.61, height=50, width=400)

            calculate_codon_frequencies_button = tk.Button(
                specific_window,
                text="Calculer les fréquences de codons",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.perform_option(9, sequence_adn, text_widget),
            )
            calculate_codon_frequencies_button.place(relx=0.02, rely=0.68, height=50, width=400)

            mutate_dna_button = tk.Button(
                specific_window,
                text="Réaliser des mutations aléatoires sur ADN",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.perform_input_option(10, sequence_adn, text_widget, specific_window, mutate_dna_button),
            )
            mutate_dna_button.place(relx=0.02, rely=0.75, height=50, width=400)

            search_motif_button = tk.Button(
                specific_window,
                text="Chercher un motif dans ADN",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.perform_input_option(11, sequence_adn, text_widget, specific_window, search_motif_button),
            )
            search_motif_button.place(relx=0.02, rely=0.82, height=50, width=400)

            consensus_button = tk.Button(
                specific_window,
                text="Générer ADN consensus et la matrice profil",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.perform_input_option(12, sequence_adn, text_widget, specific_window, consensus_button),
            )
            consensus_button.place(relx=0.02, rely=0.89, height=50, width=400)

            save_file = tk.Button(
                specific_window,
                text="Enregistrer l'historique dans un fichier",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.save_to_file(text_widget),
            )
            save_file.place(relx=0.53, rely=0.82, height=50, width=360)

            return_button = tk.Button(
                specific_window,
                text="Retour au menu principal",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.return_to_main_menu(specific_window),
            )
            return_button.place(relx=0.53, rely=0.89, height=50, width=360)

        else:
            error_label = tk.Label(specific_window, text="Veuillez entrer un nombre valide.", font=("Poppins", 14, "bold"), bd=2, bg="#FBE1D8", fg="#D73D3D")
            error_label.place(relx=0.498, rely=0.56, anchor=tk.CENTER)



    
    def return_to_main_menu(self, specific_window):
        # Fermez la fenêtre spécifique
        specific_window.withdraw()
        self.root.update()
        self.root.deiconify()

    def perform_option(self, option, sequence_adn, text_widget):
        # Ajoutez le code pour exécuter l'option sélectionnée
        if option == 3:
            if sequence_adn and Check_ADN_Seq(sequence_adn):
                print("La séquence ADN est valide.")
                text_widget.insert(tk.END, "\nLa séquence ADN est valide.")
            else:
                print("La séquence ADN n'est pas valide.")
                text_widget.insert(tk.END, "\nLa séquence ADN n'est pas valide.")

        elif option == 4:
            frequencies = CountNuc(sequence_adn)
            print("Fréquences des bases nucléiques:", frequencies)
            text_widget.insert(tk.END, f"\nFréquences des bases nucléiques: {frequencies}")

        elif option == 5:
            arn_sequence = Transcription(sequence_adn)
            print("Séquence ARN correspondante:", arn_sequence)
            text_widget.insert(tk.END, f"\nSéquence ARN correspondante: {arn_sequence}")

        elif option == 6:
            arn_sequence = Transcription(sequence_adn)
            text_widget.insert(tk.END, f"\nProtéine générée: {RNA_TO_PROTIEN(arn_sequence)}")

        elif option == 7:
            comp_reverse_sequence = CompReverse(sequence_adn)
            print("Complément inverse de la séquence ADN:", comp_reverse_sequence)
            text_widget.insert(tk.END, f"\nComplément inverse de la séquence ADN: {comp_reverse_sequence}")

        elif option == 8:
            gc_percentage = gc_content(sequence_adn)
            print("Taux de GC de la séquence ADN:", gc_percentage, "%")
            text_widget.insert(tk.END, f"\nTaux de GC de la séquence ADN: {gc_percentage}%")

        elif option == 9:
            codon_frequencies = calculer_frequences_codons(sequence_adn)
            print("Fréquences des codons:", codon_frequencies)
            text_widget.insert(tk.END, f"\nFréquences des codons: {codon_frequencies}")

        else:
            print("Option non valide. Veuillez choisir un nombre entre 0 et 12.")

    def perform_input_option(self, option, sequence_adn, text_widget, specific_window, button):
        if option == 10:
            button.destroy()
            input_entry_1 = tk.Entry(
                specific_window,
                font=("Poppins", 11, "bold"),
                bg="#FFEEE5",
                fg="#1C1C1C",
                bd=3,
                relief=tk.FLAT,
                borderwidth=10,
                highlightthickness=0,
            )
            input_entry_1.place(relx=0.02, rely=0.75, height=50, width=200)
            entrer_button_1 = tk.Button(
                specific_window,
                text="Entrez",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command= lambda: self.handle_entrez_button_1(input_entry_1, text_widget, entrer_button_1, specific_window, sequence_adn),
            )
            entrer_button_1.place(relx=0.28, rely=0.75, height=50, width=192)

        elif option == 11:
            button.destroy()
            input_entry_2 = tk.Entry(
                specific_window,
                font=("Poppins", 11, "bold"),
                bg="#FFEEE5",
                fg="#1C1C1C",
                bd=3,
                relief=tk.FLAT,
                borderwidth=10,
                highlightthickness=0,
            )
            input_entry_2.place(relx=0.02, rely=0.82, height=50, width=200)
            entrer_button_2 = tk.Button(
                specific_window,
                text="Entrez",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command= lambda: self.handle_entrez_button_2(input_entry_2, text_widget, entrer_button_2, specific_window, sequence_adn),
            )
            entrer_button_2.place(relx=0.28, rely=0.82, height=50, width=192)

        elif option == 12:
            button.destroy()

            def clear_entry(event, entry_widget, default_text):
                if entry_widget.get() == default_text:
                    entry_widget.delete(0, tk.END)
                    entry_widget.config(fg="black")  # Changement de couleur du texte à noir

            def restore_entry(event, entry_widget, default_text):
                if entry_widget.get() == "":
                    entry_widget.insert(0, default_text)
                    entry_widget.config(fg="grey")  # Changement de couleur du texte à gris

            input_entry_3 = tk.Entry(
                specific_window,
                font=("Poppins", 11, "bold"),
                bg="#FFEEE5",
                fg="#1C1C1C",
                bd=3,
                relief=tk.FLAT,
                borderwidth=10,
                highlightthickness=0,
            )
            input_entry_3.place(relx=0.02, rely=0.89, height=50, width=94)
            input_entry_3.insert(0, "Longueur")
            input_entry_3.config(fg="grey")  # Texte d'indicateur en gris par défaut
            input_entry_3.bind("<FocusIn>", lambda event: clear_entry(event, input_entry_3, "Longueur"))
            input_entry_3.bind("<FocusOut>", lambda event: restore_entry(event, input_entry_3, "Longueur"))

            input_entry_4 = tk.Entry(
                specific_window,
                font=("Poppins", 11, "bold"),
                bg="#FFEEE5",
                fg="#1C1C1C",
                bd=3,
                relief=tk.FLAT,
                borderwidth=10,
                highlightthickness=0,
            )
            input_entry_4.place(relx=0.15, rely=0.89, height=50, width=94)
            input_entry_4.insert(0, "Nombre")
            input_entry_4.config(fg="grey")  # Texte d'indicateur en gris par défaut
            input_entry_4.bind("<FocusIn>", lambda event: clear_entry(event, input_entry_4, "Nombre"))
            input_entry_4.bind("<FocusOut>", lambda event: restore_entry(event, input_entry_4, "Nombre"))

            entrer_button_3 = tk.Button(
                specific_window,
                text="Entrez",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.handle_entrez_button_3(input_entry_3, input_entry_4, text_widget, entrer_button_3, specific_window, sequence_adn),
            )
            entrer_button_3.place(relx=0.28, rely=0.89, height=50, width=192)

        else:
            print("Option non valide. Veuillez choisir un nombre entre 0 et 12.")

    def handle_entrez_button_1(self, input_entry, text_widget, entrer_button, specific_window, sequence_adn):
        mutations = int(input_entry.get())

        mutated_sequence = effectuer_mutations(sequence_adn, mutations)
        text_widget.insert(tk.END, f"\nSéquence ADN mutante : \n{mutated_sequence}")

        input_entry.destroy()
        entrer_button.destroy()

        mutate_dna_button = tk.Button(
                specific_window,
                text="Réaliser des mutations aléatoires sur ADN",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.perform_input_option(10, sequence_adn, text_widget, specific_window, mutate_dna_button),
            )
        mutate_dna_button.place(relx=0.02, rely=0.75, height=50, width=400)

    def handle_entrez_button_2(self, input_entry, text_widget, entrer_button, specific_window, sequence_adn):
        motif = input_entry.get()
        result = cherche_motif(sequence_adn, motif)

        if result:
            text_widget.insert(tk.END, f"\nMotif trouvé à : {result}")
        else:
            text_widget.insert(tk.END, f"\nLe motif '{motif}' n'a pas été trouvé dans la séquence.")


        input_entry.destroy()
        entrer_button.destroy()

        search_motif_button = tk.Button(
                specific_window,
                text="Chercher un motif dans ADN",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.perform_input_option(11, sequence_adn, text_widget, specific_window, search_motif_button),
            )
        search_motif_button.place(relx=0.02, rely=0.82, height=50, width=400)

    def handle_entrez_button_3(self, input_entry, alt_input_entry, text_widget, entrer_button, specific_window, sequence_adn):
       
        n = int(input_entry.get())
        m = int(input_entry.get())

        


        sequences = generer_sequences_adn2(n, m)
        matrice = calculer_profil(sequences,n)
        consensus_sequence = calculer_consensus(matrice, n)
        

        text_widget.insert(tk.END, f"\nLes sequences sont : {sequences}")
        text_widget.insert(tk.END, "\nMatrice Profil :")
        for nucleotide, occurrences in matrice.items():
            text_widget.insert(tk.END,f"\n{nucleotide} : {', '.join(map(str, occurrences))}")
        text_widget.insert(tk.END, f"\nChaîne ADN consensus : {consensus_sequence}")

        """for row in matrice:
            text_widget.insert(tk.END, f"{row}")
"""
        input_entry.destroy()
        entrer_button.destroy()
        alt_input_entry.destroy()

        consensus_button = tk.Button(
                specific_window,
                text="Générer ADN consensus et la matrice profil",
                font=("Poppins", 11, "bold"),
                bg="#FFCEB5",
                fg="#1C1C1C",
                bd=3,
                relief="solid",
                borderwidth=3,
                highlightthickness=0,
                command=lambda: self.perform_input_option(12, sequence_adn, text_widget, specific_window, consensus_button),
            )
        consensus_button.place(relx=0.02, rely=0.89, height=50, width=400)

    def save_to_file(self, text_widget):
        content = text_widget.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            initialfile="history.txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            title="Enregistrer le fichier",
        )
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)

if __name__ == "__main__":
    root = tk.Tk()
    app = DNAAnalyzerApp(root)
    root.mainloop()
