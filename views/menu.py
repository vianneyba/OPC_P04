from config import DEFAULT_NBR_PLAYER
from math import floor


class MenuView:

    def __init__(self):
        self.longeur = 90
        self.response = ''

    def headings(self, texte):
        texte = f' {texte} '
        self.response = '\n'
        self.response += f'{texte:-^{self.longeur}}\n'
        self.response += '\n'

    def format_title(self, texte):
        texte = f' {texte} '
        print(f'{"":-^{self.longeur}}')
        print(f'{texte:-^{self.longeur}}')
        print(f'{"":-^{self.longeur}}')

    def display(self, list_menu):
        for item in list_menu:
            self.response += f'[{item[0]}] {item[1]}\n'
        self.response += '[Q] Quitter'
        return self.response

    def display_menu(self):
        self.headings('menu')
        menu = [
            ('1', 'Créer un tournoi'),
            ('2', 'Joueur'),
            ('3', 'Tournoi'),
            ('4', 'Rapports'),
            ('8', 'Chargement'),
            ('9', 'Sauvegarde')
        ]
        return self.display(menu)

    def display_menu_player(self):
        self.headings('menu joueur')
        menu = [
            ('1', 'Ajouter un joueur'),
            ('2', 'Liste des joueurs par nom'),
            ('3', 'liste des joueurs par classement'),
            ('4', 'modifier joueur')
        ]
        return self.display(menu)

    def display_edit_player(self):
        self.headings('Edition Joueur')
        menu = [
            ('1', 'modifer le prénom'),
            ('2', 'modifer le nom'),
            ('3', 'modfier la date de naissance'),
            ('4', 'modifer le classement')
        ]
        return self.display(menu)

    def field_text(self, linktracking, message):
        if linktracking.error is True:
            print(f'!!!!!==> {linktracking.message} !!!!!<==')
        return input(message)

    def display_player_new(self, nbr=1):
        self.format_title('ajout nouveau joueur {}'.format(nbr))

    def display_list_players(self, players):
        print(f'{"":-^{self.longeur}}')
        print(f'{" Liste des Joueurs ":-^{self.longeur}}')
        print(f'{"":-^{self.longeur}}')
        div = 6
        print(
            f'{"index":^{floor(self.longeur/div)}}'
            f'{"prénom":^{floor(self.longeur/div)}}'
            f'{"nom":^{floor(self.longeur/div)}}'
            f'{"genre":^{floor(self.longeur/div)}}'
            f'{"place":^{floor(self.longeur/div)}}'
            f'{"points":^{floor(self.longeur/div)}}'
        )
        for i, player in enumerate(players):
            print(
                f'{i+1:^{floor(self.longeur/div)}}'
                f'{player.firstname:^{floor(self.longeur/div)}}'
                f'{player.lastname:^{floor(self.longeur/div)}}'
                f'{player.gender:^{floor(self.longeur/div)}}'
                f'{player.rating:^{floor(self.longeur/div)}}'
                f'{player.points:^{floor(self.longeur/div)}}'
            )
        # input('continue')

    def select_player(self):
        return input('Quel joueur modifier?: ')

    def display_list_tournament(self, tournament, index):
        print(f'{"":-^{self.longeur}}')
        print(f'  [{index}] index du tournoi')
        print(f'Nom: {tournament.name}')
        print(f'Lieu: {tournament.place}')
        print(f'Date du début: {tournament.start_date}')
        print(f'Date de fin: {tournament.end_date()}')
        print(f'Côntrole du temps: {tournament.ctr_time}')
        print(f'Description: {tournament.description}')
        nbr_rounds = f'{len(tournament.rounds)}/{tournament.nbr_rounds}'
        print(f'Nombre de tour: {nbr_rounds}')
        nbr_players = f'{len(tournament.players)}/{DEFAULT_NBR_PLAYER}'
        print(f'Nombre de joueur: {nbr_players}')

    def select_tournament(self):
        return input('Taper l\'index du tournoi a modifier:')

    def display_edit_tournament_menu(
                self, is_close=False, end_player=True, nb_round=0):
        self.headings('Edition d\'un tournoi')
        menu = [
            ('1', 'Fin de round (mise à jour des scores): '),
            ('2', 'changer le nom'),
            ('3', 'changer la description'),
            ('4', 'changer le controlle du temps'),
            ('5', 'changer la localisation'),
            ('6', 'changer la date du début de tournoi'),
            ('7', 'changer la durée du tournoi'),
            ('8', 'Ajouter des joueurs'),
            ('9', 'Creer le round'),
            ('10', 'Modifier le classement'),
        ]
        delete = []
        for i, el in enumerate(menu):
            if is_close and el[0] == '1':
                delete.append(i)
            if end_player is True and el[0] == '8':
                delete.append(i)
            if (end_player is False or nb_round > 0) and el[0] == '9':
                delete.append(i)
            if is_close is False and el[0] == '10':
                delete.append(i)

        delete.sort(reverse=True)
        for i in delete:
            menu.pop(i)

        return self.display(menu)

    def display_tournament_new(self):
        self.format_title('ajout nouveau tournoi')

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

    def display_add_player(self):
        return input('Ajouter un joueur [y/n]: ')

    def display_menu_rapport(self):
        self.headings('Rapports')
        menu = [
            ('1', 'Liste des Joueurs'),
            ('2', 'Liste des joueurs d\'un tournoi'),
            ('3', 'liste des tournois'),
            ('4', 'liste des tours d\'un tournoi'),
            ('5', 'liste des matchs d\'un tournoi')
        ]
        return self.display(menu)

    def display_menu_order(self):
        self.headings('Rapports')
        menu = [
            ('1', 'Ordre de classement'),
            ('2', 'Ordre alphabétique')
        ]
        return self.display(menu)

    def display_list_tournament_online(self, tournaments):
        print(f'{"":-^{self.longeur}}')
        print(f'{" Liste des tournois ":-^{self.longeur}}')
        print(f'{"":-^{self.longeur}}')
        div = 4
        print(
            f'{"index":^{floor(self.longeur/div)}}'
            f'{"nom":^{floor(self.longeur/div)}}'
            f'{"date début":^{floor(self.longeur/div)}}'
            f'{"date fin":^{floor(self.longeur/div)}}'
        )
        for i, tournament in enumerate(tournaments):
            print(
                f'{i+1:^{floor(self.longeur/div)}}'
                f'{tournament.name:^{floor(self.longeur/div)}}'
                f'{tournament.start_date:^{floor(self.longeur/div)}}'
                f'{tournament.end_date():^{floor(self.longeur/div)}}'
            )
        print()

    def display_round(self, name, rounds):
        print(f'{"":-^{self.longeur}}')
        print(f'{" tournoi: "+name+" - rounds ":-^{self.longeur}}')
        print(f'{"":-^{self.longeur}}')
        div = 3
        print(
            f'{"nom":^{floor(self.longeur/div)}}'
            f'{"date début":^{floor(self.longeur/div)}}'
            f'{"date fin":^{floor(self.longeur/div)}}'
        )
        for my_round in rounds:
            name = my_round.name
            start_date = my_round.get_start_date_to_txt()
            end_date = my_round.get_end_date_to_txt()
            print(
                f'{name:^{floor(self.longeur/div)}}'
                f'{start_date:^{floor(self.longeur/div)}}'
                f'{end_date:^{floor(self.longeur/div)}}'
            )
            self.display_list_match(my_round.matches)
        print()

    def display_select_tournament(self):
        return input('Choisir le tournoi: ')

    def display_list_match(self, matches):
        div = 4
        print(f'{"":-^{self.longeur}}')
        print(f'{" match ":-^{self.longeur}}')
        print(f'{"":-^{self.longeur}}')
        print(
            f'{"Joueur 1":^{floor(self.longeur/div)}}'
            f'{"Score J1":^{floor(self.longeur/div)}}'
            f'{"Joueur 2":^{floor(self.longeur/div)}}'
            f'{"Score J2":^{floor(self.longeur/div)}}'
        )
        for match in matches:
            p_one = f'{match.player_one.firstname} {match.player_one.lastname}'
            p_two = f'{match.player_two.firstname} {match.player_two.lastname}'
            print(
                f'{p_one:^{floor(self.longeur/div)}}'
                f'{match.player_one_pt:^{floor(self.longeur/div)}}'
                f'{p_two:^{floor(self.longeur/div)}}'
                f'{match.player_two_pt:^{floor(self.longeur/div)}}'
            )
        print()
