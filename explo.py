import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()  # Cacher la fenêtre principale de tkinter

chemin = filedialog.askdirectory()
if chemin:
    print(chemin)
else:
    print("Aucun dossier sélectionné.")

root.destroy()  # Fermer la fenêtre principale de tkinter proprement

# Vous pouvez maintenant utiliser la variable folder_path pour accéder au chemin du dossier sélectionné
