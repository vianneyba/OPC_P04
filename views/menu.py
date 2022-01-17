class MenuView:

    def headings(self, texte):
        print()
        print(f'------ {texte} ------')
        print()

    def format_title(self, texte):
        print(f'{"":-^44}')
        print(f'{texte:-^44}')
        print(f'{"":-^44}')

    def display(self, list_menu):
        for item in list_menu:
            print(f'[{item[0]}] {item[1]}')

        print('[Q] Quitter')
        return input('entrer le numéro du menu:')

    def display_menu(self, ):
        self.headings('menu')
        menu = [
            ('1', 'Créer un tournoi'),
            ('2', 'Joueur'),
            ('3', 'Tournoi'),
            ('8', 'Chargement'),
            ('9', 'Sauvegarde')]
        return self.display(menu)

    def display_menu_player(self):
        self.headings('menu joueur')
        menu = [
            ('1', 'Ajouter un joueur'),
            ('2', 'Liste des joueurs par nom'),
            ('3', 'liste des joueurs par classement')]
        return self.display(menu)

    def field_text(self, linktracking, message):
        if linktracking.error is True:
            print(f'!!!!!==> {linktracking.message} !!!!!<==')
        return input(message)

    def display_list_tournaments(self, players):
        print('{0:-^43}'.format(''))
        print('{0:-^43}'.format(' Liste des Jouer du tournoi '))
        print('{0:-^43}'.format(''))
        print('{:^12} | {:^12} | {:^5} | {:^5} | {:^5}'.format(
            "prénom", "nom",
            "genre", "place",
            "points"
        ))
        for player in players:
            print('{:^12} | {:^12} | {:^5} | {:^5} | {:^5}'.format(
                player.firstname, player.lastname,
                player.gender, player.rating,
                player.points
            ))

    # ----- *** MENU PLAYER *** -----
    def display_player_new(self, nbr=1):
        self.format_title(' ajout nouveau joueur {} '.format(nbr))

    def display_list_players(self, players):
        print('{0:-^43}'.format(''))
        print('{0:-^43}'.format(' Liste des Joueurs '))
        print('{0:-^43}'.format(''))
        print('{:^12} | {:^12} | {:^5} | {:^5} | {:^5}'.format(
            "prénom", "nom",
            "genre", "place",
            "points"
        ))
        for player in players:
            print('{:^12} | {:^12} | {:^5} | {:^5} | {:^5}'.format(
                player.firstname, player.lastname,
                player.gender, player.rating,
                player.points
            ))

    def display_player(self, player):
        print(f'Prénom: {player.firstname}')
        print(f'Nom: {player.lastname}')
        print(f'Sexe: {player.gender}')
        print(f'classement: {player.rating}')

    def display_list_tournament(self, tournament, index):
        print('{0:-^43}'.format(''))
        print(f'index du tournoi: {index}')
        print(f'Nom: {tournament.name}')
        print(f'Lieu: {tournament.place}')
        print(f'Date du début: {tournament.start_date}')
        print(f'Date de fin: {tournament.start_date}')
        print(f'Côntrole du temps: {tournament.ctr_time}')
        print(f'Description: {tournament.description}')
        nbr_rounds = f'{len(tournament.rounds)}/{tournament.nbr_rounds}'
        print(f'Nombre de tour: {nbr_rounds}')

    def choice_tournament(self):
        return input('Taper l\'index du tournoi a modifier:')

    def display_edit_tournament_menu(self):
        self.headings('Edition d\'un tournoi')
        menu = [
            ('1', 'Fin de round (mise à jour des scores): '),
            ('2', 'change le nom'),
            ('3', 'changer la description'),
            ('4', 'changer le controlle du temps'),
            ('5', 'changer la localisation'),
            ('6', 'changer la date du début de tournoi'),
            ('7', 'changer la durée du tournoi')
        ]
        return self.display(menu)

    # ----- *** MENU TOURNOI *** -----
    def display_tournament_new(self):
        self.format_title(' ajout nouveau tournoi ')

    def display_menu_tournament(self):
        self.headings('menu tournoi')
        menu = [
            ('1', 'Créer un tournoi'),
            ('2', 'Liste des tournois')
        ]
        return self.display(menu)

    def finish_match(self, p_one, p_two):
        print(f'[1] si le Joueur {p_one.firstname} {p_one.lastname} a gagné')
        print(f'[2] si le Joueur {p_two.firstname} {p_two.lastname} a gagné')
        print('[3] pour une égalité')
        return input('votre choix: ')
