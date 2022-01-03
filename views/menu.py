from models.player import Player

class MenuView:

    def headings(self, texte):
        print()
        print(f'------ {texte} ------')
        print()

    def display(self, list_menu):
        i = 1
        for item in list_menu:
            print(f'[{i}] {item}')  
            i += 1

        print('[Q] Quitter')
        return input('entrer le numéro du menu:')
        
    def display_menu(self, ):
        self.headings('menu')
        menu= ['Créer un tournoi', 'Joueur', 'Tournoi']
        return self.display(menu)

    def display_menu_player(self):
        self.headings('menu joueur')
        menu= ['Ajouter un joueur', 'Liste des joueurs par nom', 'liste des joueurs par classement']
        return self.display(menu)

    # ----- *** MENU PLAYER *** -----
    def display_player_new(self, nbr=1):
        print(f'------------------------------------------------------')
        print(f'-------------- ajout nouveau joueur {nbr} ------------')
        print(f'------------------------------------------------------')

    def display_list_players(self, players):
        print(f'------------------------------------------------------')
        print(f'-------------- Liste des Joueurs ------------')
        print(f'------------------------------------------------------')
        for player in players:
            new_player = {'firstname': player['firstname'],
                            'lastname': player['lastname'],
                            'gender': player['gender'],
                            'rating': player['rating']}
            print(f'{new_player["firstname"]} {new_player["lastname"]} ({new_player["gender"]}) #{new_player["rating"]}')
    def display_add_player(self):
        sexe= input('les informations sont\'elle correct [Y/n]: ')
        continu= print('voulez vous créer un autre joueur [y/N]? ')

    def display_player(self, player):
        print(f'Prénom: {player.firstname}')
        print(f'Nom: {player.lastname}')
        print(f'Sexe: {player.gender}')
        print(f'classement: {player.rating}')

    def display_player_first_name(self, error):
        if error.error == True:
            print(f'\t==>{error.message}')
        return input('entrer son prénom: ')

    def display_player_birthday(self, error):
        if error.error == True:
            print(f'\t==>{error.message}')
        return input('date de naissance (jj/mm/yyyy): ')

    def display_player_last_name(self, error):
        if error.error == True:
            print(f'\t==>{error.message}')
        return input('entrer son nom: ')
    
    def display_player_gender(self, error):
        if error.error == True:
            print(f'\t==>{error.message}')
        return input('entrer son sexe (H/F): ')

    def display_player_rating(self, error):
        if error.error == True:
            print(f'\t==>{error.message}')
        return input('entrer son classement: ')