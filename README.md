\# DNA Sequence Analysis Toolkit 🧬



Ce projet est une application Python développée dans le cadre du module "Système et Programmation de Scripts" du Master 1 Bio-Informatique (USTHB). Il fournit une boîte à outils complète pour l'analyse de séquences d'ADN, accessible via une interface graphique (GUI) ou une interface en ligne de commande (CLI).



\## ✨ Captures d'écran de l'Interface Graphique



L'application offre une expérience utilisateur intuitive grâce à son interface construite avec Tkinter.



\*\*Menu Principal :\*\*

!\[Menu Principal de l'application](./screenshots/01.png)



\*\*Fenêtre d'Analyse :\*\*

!\[Fenêtre d'analyse](./screenshots/02.png)



\## 🚀 Fonctionnalités



L'application permet de réaliser un large éventail d'opérations sur des séquences d'ADN, qu'elles soient générées aléatoirement ou lues depuis un fichier.



\- \*\*Gestion de Séquence :\*\*

&nbsp; - Générer une chaîne ADN aléatoire d'une longueur donnée.

&nbsp; - Charger une séquence ADN depuis un fichier (`.fasta`, `.txt`, etc.).

&nbsp; - Vérifier la validité d'une séquence (contient uniquement A, C, G, T).



\- \*\*Analyses Fondamentales :\*\*

&nbsp; - \*\*Fréquence des bases :\*\* Calculer le nombre d'occurrences de chaque nucléotide (A, C, G, T).

&nbsp; - \*\*Taux de GC :\*\* Calculer le pourcentage de bases G et C dans la séquence.

&nbsp; - \*\*Transcription :\*\* Convertir une séquence d'ADN en sa correspondante d'ARN.

&nbsp; - \*\*Traduction :\*\* Traduire une séquence d'ARN en sa séquence de protéines (acides aminés).

&nbsp; - \*\*Complément Inverse :\*\* Générer la séquence complémentaire inverse.

&nbsp; - \*\*Fréquence des codons :\*\* Calculer la fréquence de chaque codon de trois nucléotides.



\- \*\*Fonctionnalités Avancées :\*\*

&nbsp; - \*\*Mutation Ponctuelle :\*\* Introduire un nombre spécifié de mutations par substitution.

&nbsp; - \*\*Recherche de Motif :\*\* Trouver toutes les occurrences d'un sous-motif dans la séquence.

&nbsp; - \*\*Séquence Consensus :\*\* À partir d'un ensemble de séquences, générer la matrice de profil et la chaîne ADN consensus.



\- \*\*Utilitaire :\*\*

&nbsp; - Sauvegarder l'historique des analyses et des résultats dans un fichier texte.



\## 🔧 Comment l'utiliser



1\.  \*\*Clonez ce dépôt :\*\*

&nbsp;   ```bash

&nbsp;   git clone https://github.com/VOTRE\_NOM\_UTILISATEUR/DNA-Sequence-Analyzer.git

&nbsp;   cd DNA-Sequence-Analyzer

&nbsp;   ```



2\.  \*\*(Optionnel mais recommandé) Créez un environnement virtuel :\*\*

&nbsp;   ```bash

&nbsp;   python -m venv env

&nbsp;   # Sur Windows

&nbsp;   .\\env\\Scripts\\activate

&nbsp;   # Sur macOS/Linux

&nbsp;   source env/bin/activate

&nbsp;   ```



3\.  \*\*Installez les dépendances nécessaires :\*\*

&nbsp;   ```bash

&nbsp;   pip install -r requirements.txt

&nbsp;   ```



4\.  \*\*Lancez l'application de votre choix :\*\*



&nbsp;   - \*\*Pour l'interface graphique (GUI) :\*\*

&nbsp;     ```bash

&nbsp;     python App.py

&nbsp;     ```

&nbsp;   - \*\*Pour l'interface en ligne de commande (CLI) :\*\*

&nbsp;     ```bash

&nbsp;     python Menu.py

&nbsp;     ```



\## 📂 Structure du Projet



Le code est organisé de manière modulaire pour une meilleure lisibilité et maintenance :

\- `App.py`: Point d'entrée de l'application graphique (Tkinter).

\- `Menu.py`: Point d'entrée de l'application en ligne de commande.

\- `ADN\_\*.py`, `Count\_\*.py`, etc. : Modules contenant chacun une fonction bio-informatique spécifique.

\- `/assets` : Contient les images utilisées par l'interface graphique.

\- `/sample\_data` : Contient des fichiers d'exemples de séquences.

\- `enonce\_projet.pdf` : Le document original décrivant le projet.

