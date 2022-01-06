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

    # ----- *** MENU PLAYER *** -----
    def display_player_new(self, nbr=1):
        self.format_title(' ajout nouveau joueur {} '.format(nbr))

    def display_list_players(self, players):
        print('{0:-^43}'.format(''))
        print('{0:-^43}'.format(' Liste des Joueurs '))
        print('{0:-^43}'.format(''))
        print('{:^12} | {:^12} | {:^5} | {:^5}'.format("prénom", "nom", "genre", "place"))
        for player in players:
            new_player = {
                'firstname': player.firstname,
                'lastname': player.lastname,
                'gender': player.gender,
                'rating': player.rating}
            print('{:^12} | {:^12} | {:^5} | {:^5}'.format(new_player["firstname"], new_player["lastname"], new_player["gender"], new_player["rating"]))

    def display_player(self, player):
        print(f'Prénom: {player.firstname}')
        print(f'Nom: {player.lastname}')
        print(f'Sexe: {player.gender}')
        print(f'classement: {player.rating}')

# ----- *** MENU TOURNOI *** -----
    def display_tournament_new(self):
        self.format_title(' ajout nouveau tournoi ')

    def display_menu_tournament(self):
        self.headings('menu tournoi')
        menu = ['Créer un tournoi', 'Liste des tournois']
        return self.display(menu)
