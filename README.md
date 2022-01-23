# Fonctionnalités

Application permettant de gérer des tournois d'échecs.

# Utilisation

## Création de l'environnement virtuel

taper: *python -m venv env*

activer l'environement: *source env/bin/activate*

installer les dependance: *pip install -r requirements.txt*

## Lancement du script

pour lancer l'application

*python3 main.py*

1. Créer un tournoi
2. Joueur
    1. Ajouter un joueur
    2. Liste des joueurs par nom
    3. liste des joueurs par classement
    4. modifier joueur
    5. import joueur 
    6. Quitter
3. Tournoi
    1. Créer un tournoi
    2. Liste des tournois
        1. Fin de round (mise à jour des scores): 
        2. changer le nom
        3. changer la description
        4. changer le controlle du temps
        5. changer la localisation
        6. changer la date du début de tournoi
        7. changer la durée du tournoi
        8. Ajouter des joueurs
        9. Creer le round
        10. Quitter
    3. Quitter
4. Rapports
    1. Liste des Joueurs
    2. Liste des joueurs d'un tournoi
    3. liste des tournois
    4. liste des tours d'un tournoi
    5. liste des matchs d'un tournoi
    6. Quitter
6. Chargement
7. Sauvegarde
8. rapport flake8
9. Quitter

## Créer un tournoi
Le menu "1 Créer un tournoi" ou "3-1 Créer un tournoi" permet de crée un tournoi après avoir rempli les champs suivant:

*Entrer le nom du tournoi: tournoi du 20/01/2022*
*Entrer le lieu du tournoi: lille*
*Entrer la date du début du tournoi (jj/mm/yyyy): 20/01/2022*
*Combien de jour durera la tournoi [1]: *
*Nombre de tours [4]: *
*Côntrole du temps ([1] Bullet, [2] Blitz, [3] Coup rapide): 1*
*Entrer une description: a la maire de wazemme*

il est aussi possible d'ajouter les 8 participants au tournoi dans cette section.

## Ajouter un joueur
Le menu "2-1 Ajouter un joueur" permet d'ajouter des joueurs sans les lier a un tournoi.
Avec le menu "3-2-8 Ajouter des joueurs" il est aussi possible d'ajouter des joueurs directement dans le tournoi précédemment selectionné.

*entrer son prénom: bruno*
*entrer son nom: armant*
*date de naissance (jj/mm/yyyy): 16/08/1963*
*entrer son sexe (H/F): h*
*entrer son classement: 20*

## Clôturer un tour
Le menu "3-2-1 Fin de round (mise à jour des scores)" permet de d'indiquer le gagnant sur tous les matches du tour. en validant les matches un nouveau tour est généré.

## Exporter des données
En quittant l'application les données ne seront pas automatiquement sauvegarder il faudra passer par le menu "7 Sauvegarde".

## Importer des données
Le menu "6 Chargement" permet de charger les données précédemment sauvegarder.