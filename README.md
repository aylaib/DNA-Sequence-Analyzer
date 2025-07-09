# DNA Sequence Analysis Toolkit 🧬
This project is a Python application developed as part of the "Systems and Script Programming" module of the Master 1 Bioinformatics (USTHB). It provides a comprehensive toolkit for DNA sequence analysis, accessible via a graphical interface (GUI) or a command-line interface (CLI).
## ✨ Graphical Interface Screenshots
The application offers an intuitive user experience through its interface built with Tkinter.
**Main Menu:**
![Application Main Menu](./screenshots/01.png)
**Analysis Window:**
![Analysis window](./screenshots/02.png)
## 🚀 Features
The application allows performing a wide range of operations on DNA sequences, whether randomly generated or read from a file.
- **Sequence Management:**
  - Generate a random DNA string of a given length.
  - Load a DNA sequence from a file (`.fasta`, `.txt`, etc.).
  - Verify the validity of a sequence (contains only A, C, G, T).
- **Fundamental Analyses:**
  - **Base frequency:** Calculate the number of occurrences of each nucleotide (A, C, G, T).
  - **GC content:** Calculate the percentage of G and C bases in the sequence.
  - **Transcription:** Convert a DNA sequence to its corresponding RNA.
  - **Translation:** Translate an RNA sequence to its protein sequence (amino acids).
  - **Reverse Complement:** Generate the reverse complementary sequence.
  - **Codon frequency:** Calculate the frequency of each three-nucleotide codon.
- **Advanced Features:**
  - **Point Mutation:** Introduce a specified number of mutations by substitution.
  - **Motif Search:** Find all occurrences of a sub-motif in the sequence.
  - **Consensus Sequence:** From a set of sequences, generate the profile matrix and consensus DNA string.
- **Utility:**
  - Save analysis history and results to a text file.
## 🔧 How to Use
1.  **Clone this repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/DNA-Sequence-Analyzer.git
    cd DNA-Sequence-Analyzer
    ```
2.  **(Optional but recommended) Create a virtual environment:**
    ```bash
    python -m venv env
    # On Windows
    .\env\Scripts\activate
    # On macOS/Linux
    source env/bin/activate
    ```
3.  **Install required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Launch the application of your choice:**
    - **For the graphical interface (GUI):**
      ```bash
      python App.py
      ```
    - **For the command-line interface (CLI):**
      ```bash
      python Menu.py
      ```
## 📂 Project Structure
The code is organized modularly for better readability and maintenance:
- `App.py`: Entry point for the graphical application (Tkinter).
- `Menu.py`: Entry point for the command-line application.
- `ADN_*.py`, `Count_*.py`, etc.: Modules each containing a specific bioinformatics function.
- `/assets`: Contains images used by the graphical interface.
- `/sample_data`: Contains example sequence files.
- `enonce_projet.pdf`: The original document describing the project.
