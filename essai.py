from colorama import Fore, Style
import inquirer
import subprocess
from tqdm import tqdm
import os
import time

# Fonction pour créer un nouveau repository GitHub
def creer_nouveau_repo(nom_projet):
    token = "Your_token"
    subprocess.run(['curl', f'-H', f'Authorization: token {token}', '-d', f'{{"name":"{nom_projet}"}}', 'https://api.github.com/user/repos'], stdout=subprocess.DEVNULL)

# Définir les styles de couleurs
Q_STYLE = f"{Fore.YELLOW}{Style.BRIGHT}"
A_STYLE = f"{Fore.YELLOW}{Style.BRIGHT}"
OPT_STYLE = f"{Fore.GREEN}{Style.BRIGHT}"
SEL_OPT_STYLE = f"{Fore.GREEN}{Style.BRIGHT}"
UNSEL_OPT_STYLE = f"{Fore.RED}{Style.BRIGHT}"

# Demander le nom du projet
questions = [inquirer.Text('nom_projet', message=f"{Q_STYLE}Quel sera le nom de votre projet ?{Style.RESET_ALL}")]
reponses = inquirer.prompt(questions)
nom_projet = reponses['nom_projet']

# Demander si un nouveau repository doit être créé
choices = [
    f"{OPT_STYLE}Oui{Style.RESET_ALL}",
    f"{UNSEL_OPT_STYLE}Non{Style.RESET_ALL}"
]
questions = [inquirer.List('nouveau_repo', message=f"{Q_STYLE}Voulez-vous créer un nouveau repository ?{Style.RESET_ALL}", choices=choices)]
reponses = inquirer.prompt(questions)
creer_repo = reponses['nouveau_repo'] == choices[0]

# Si l'utilisateur choisit de créer un nouveau repository
if creer_repo:
    # Afficher l'animation de chargement en vert
    print(f"{Fore.GREEN}Création du repository en cours...{Style.RESET_ALL}")
    for _ in tqdm(range(100), desc="Création du repository", unit="%", ncols=80):
        time.sleep(0.02)
    print(f"{Fore.GREEN}Repository créé avec succès!{Style.RESET_ALL}")

    # Appeler la fonction pour créer un nouveau repository
    creer_nouveau_repo(nom_projet)

# Appel au script Python pour sélectionner le dossier et récupérer la variable
chemin = subprocess.check_output(['python3', 'C:/create/explo.py'], universal_newlines=True).strip()

# Continuer avec le reste de votre code...

# Clone le projet GitHub en utilisant l'origine "template"
# Afficher la barre de progression pour le clonage
print(f"{OPT_STYLE}Clonage du dépôt en cours...{Style.RESET_ALL}")
# Exécuter la commande git clone avec suppression de la sortie
# Exécuter la commande git clone en arrière-plan et capturer la sortie
process = subprocess.Popen(f'git clone --origin template git@github.com:username/template.git "{chemin}/{nom_projet}"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

# Lire et afficher la sortie en temps réel
with tqdm(total=100, desc="Clonage du dépôt", unit="%", ncols=80, bar_format='{percentage:3.0f}%|{bar:80}{r_bar}') as progress_bar:
    for line in process.stdout:
        progress_bar.update(1)

# Attendre la fin du processus
process.wait()

print(f"{OPT_STYLE}Clonage du dépôt terminé!{Style.RESET_ALL}")
# Déplacer dans le dossier du projet
os.chdir(f'{chemin}/{nom_projet}')


# Remplace l'URL origin actuelle par la variable donnée en argument
subprocess.run(f'git remote set-url template git@github.com:username/{nom_projet}.git', shell=True, stdout=subprocess.DEVNULL)

# Récupère les dernières modifications du remote
subprocess.run('git pull origin main --allow-unrelated-histories', shell=True, stdout=subprocess.DEVNULL)

# Ajouter les fichiers au commit
subprocess.run('git add .', shell=True, stdout=subprocess.DEVNULL)

# Commit les changements
subprocess.run('git commit -m "start"', shell=True, stdout=subprocess.DEVNULL)

# Pousser les changements
subprocess.run('git push', shell=True, stdout=subprocess.DEVNULL)

# L'affichage du chemin
print(chemin)

# Ouvrir le projet avec idea64
subprocess.run(f'idea64.exe "{chemin}/{nom_projet}"', shell=True)

