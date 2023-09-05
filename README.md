Guide d'utilisation du script de création de projet GitHub
Ce guide explique comment utiliser le script Bash fourni pour créer un nouveau projet GitHub en utilisant le terminal. Le script automatisera plusieurs étapes, telles que la création d'un référentiel GitHub, le clonage du modèle de projet, et la configuration du référentiel local pour votre projet personnalisé.

Prérequis
Avant de commencer, assurez-vous que vous avez les éléments suivants:

Accès à un compte GitHub.
Un jeton d'authentification GitHub avec les autorisations nécessaires. Vous pouvez générer un token en suivant ces instructions.
Git installé sur votre système.
Étapes
Téléchargez le script

Assurez-vous que le script Bash est présent sur votre système. Si ce n'est pas le cas, vous pouvez le copier-coller dans un fichier, par exemple create_project.sh, et lui donner les droits d'exécution avec la commande chmod +x create_project.sh.

Exécutez le script

Ouvrez votre terminal et exécutez le script en utilisant la commande suivante :

./create_project.sh
Nommez votre projet

Vous serez invité à donner un nom à votre projet. Entrez le nom souhaité et appuyez sur Entrée.

Créez un référentiel GitHub

Le script créera un nouveau référentiel GitHub avec le nom que vous avez choisi en utilisant le jeton d'authentification GitHub que vous avez fourni dans le script.

Clonez le modèle de projet

Le script clonera le modèle de projet préexistant (probablement un modèle que vous avez configuré) depuis le référentiel GitHub samyns/template dans le répertoire local avec le nom que vous avez choisi.

Accédez au répertoire du projet

Le script se déplacera dans le répertoire de votre projet nouvellement créé.

Vérifiez la configuration du référentiel

Le script configurera l'URL du référentiel "template" pour qu'il pointe vers votre référentiel GitHub nouvellement créé. Il affichera également les URL des référentiels pour vérification.

Récupérez les dernières modifications

Le script récupérera les dernières modifications du référentiel GitHub pour vous assurer que vous travaillez sur la dernière version.

Ajoutez, commitez et poussez vos modifications

Vous êtes maintenant prêt à travailler sur votre projet. Ajoutez, commitez et poussez vos modifications comme d'habitude en utilisant les commandes Git standards.

Votre projet est maintenant configuré et prêt à être développé. Vous pouvez personnaliser le modèle de projet cloné selon vos besoins.

N'oubliez pas de conserver votre jeton d'authentification GitHub en sécurité, car il permet d'accéder à votre compte GitHub. Assurez-vous également de ne pas partager de données sensibles dans votre référentiel public.
