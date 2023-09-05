Script d'automatisation de création de projet sur GitHub
Ce script automatisé a été développé pour simplifier la création de nouveaux projets GitHub en utilisant un modèle existant et en réduisant au maximum les étapes manuelles. Il permet de :

Créer un nouveau dépôt GitHub à partir du nom de projet saisi par l'utilisateur.
Cloner le modèle GitHub dans le répertoire de projet local.
Configurer automatiquement l'URL du dépôt GitHub pour faciliter la synchronisation.
Prérequis
Avant d'utiliser ce script, assurez-vous d'avoir les éléments suivants installés sur votre système :

Bash (Bourne-Again Shell) : Le script principal est écrit en Bash. Assurez-vous d'avoir Bash installé sur votre système.

Python 3 : Le script Python est utilisé pour sélectionner le répertoire de destination du projet. Vous devez avoir Python 3 installé.

Git : Le système de contrôle de version Git est utilisé pour cloner le modèle et gérer le dépôt GitHub. Assurez-vous d'avoir Git installé.

GitHub Token : Vous devez générer un token GitHub personnel avec des autorisations de création de dépôts. Remplacez "<Your_Token>" par votre propre token d'autorisation dans le script.

Utilisation
Clonez ce dépôt ou copiez les scripts Bash et Python sur votre système.

Exécutez le script Bash en utilisant la commande suivante :

bash
Copy code
./votre_script.sh
Suivez les instructions à l'écran :

Entrez le nom de votre projet.
Sélectionnez le répertoire de destination où vous souhaitez que le projet soit cloné.
Attendez que le script termine le processus d'initialisation du projet GitHub.

Votre nouveau projet est maintenant prêt. Vous pouvez commencer à travailler et à pousser des modifications vers votre dépôt GitHub.

N'oubliez pas de personnaliser votre modèle GitHub en fonction de vos besoins spécifiques avant d'utiliser ce script.

Pour créer une commande à partir de votre script Bash afin qu'il puisse être exécuté comme une commande système (c'est-à-dire en utilisant un nom de commande personnalisé), vous pouvez suivre ces étapes :

Choisir un nom de commande : Choisissez un nom court et descriptif pour votre commande personnalisée. Assurez-vous qu'il est unique et ne risque pas de conflit avec d'autres commandes système.

Créer un répertoire pour vos commandes personnalisées : Vous pouvez créer un répertoire dans votre système où vous stockerez vos commandes personnalisées. Par exemple, vous pouvez créer un répertoire ~/bin s'il n'existe pas déjà.


mkdir -p ~/bin
Ajouter le répertoire à votre PATH : Pour que votre système reconnaisse les commandes dans ce répertoire, vous devez ajouter ~/bin (ou le chemin du répertoire que vous avez choisi) à votre variable d'environnement PATH. Vous pouvez le faire en ajoutant la ligne suivante à votre fichier .bashrc (ou .bash_profile si vous êtes sur macOS) :


export PATH="$PATH:$HOME/bin"
Assurez-vous de recharger votre profil shell ou de relancer votre terminal pour que les modifications prennent effet :


source ~/.bashrc
Renommer votre script Bash : Renommez le script Bash que vous avez écrit en utilisant le nom de commande que vous avez choisi. Par exemple, si vous avez choisi le nom de commande create-github-project, renommez votre script en create-github-project.


mv votre_script.sh create-github-project
Ajouter un en-tête : Assurez-vous que votre script commence par un en-tête de script Bash valide, comme ceci :

#!/bin/bash
Déplacer le script vers le répertoire des commandes personnalisées : Déplacez le script renommé dans le répertoire que vous avez créé pour vos commandes personnalisées (~/bin dans cet exemple).


mv create-github-project ~/bin/
Donner les droits d'exécution au script : Rendez le script exécutable en utilisant la commande chmod :


chmod +x ~/bin/create-github-project
Utilisation : Vous pouvez maintenant utiliser votre nouvelle commande personnalisée dans n'importe quel terminal en tapant simplement :


create-github-project
Votre script sera exécuté comme s'il s'agissait d'une commande système.

Assurez-vous de respecter les règles de sécurité lors de l'exécution de scripts personnalisés, en particulier si ces scripts effectuent des opérations sensibles sur votre système.


N'hésitez pas à personnaliser davantage ce README en ajoutant des informations spécifiques à votre projet ou en fournissant des détails supplémentaires sur son fonctionnement.