from models.linktracking import LinkTracking
from models.match import Match
from models.round import Round
from models.player import Player
from controllers.validation import Validation as Vld
from controllers.player import PlayerController
from services.services import PlayerManagement, RoundManagement
from services.services import MatchManagement, TournamentManagement
from models.tournament import Tournament
from config import DEFAULT_NBR_PLAYER


class TournamentController:
    lnk = LinkTracking()

    @classmethod
    def save(self, tournament):
        for player in tournament.players:
            PlayerManagement.save(player.serialize())

        for round_t in tournament.rounds:
            RoundManagement.save(round_t.serialize())
            for match in round_t.matchs:
                MatchManagement.save(match.serialize())

        TournamentManagement.save(tournament.serialize())

    @classmethod
    def add_tournament(self, view):
        tournament = Tournament()

        view.display_tournament_new()

        message = 'Entrer le nom du tournoi: '
        tournament.name = self.form(
            self, view, message, Vld.tournament_name
        )

        message = 'Entrer le lieu du tournoi: '
        tournament.place = self.form(self, view, message, Vld.tournament_place)

        message = 'Entrer la date du début du tournoi (jj/mm/yyyy): '
        tournament.start_date = self.form(
            self, view, message, Vld.tournament_date_start
        )

        message = 'Combien de jour durera la tournoi [1]: '
        tournament.nbr_days = self.form(
            self, view, message, Vld.tournament_duration
        )

        message = 'Nombre de tours [4]: '
        tournament.nbr_rounds = self.form(
            self, view, message, Vld.tournament_rounds
            )

        message = 'Côntrole du temps ([1] Bullet, [2] Blitz, [3] Coup rapide): '
        ctr_time = self.form(
            self, view, message, Vld.tournament_ctr_time
        )
        tournament.ctr_time = self.get_ctr_time(self, ctr_time)

        message = 'Entrer une description: '
        tournament.description = self.form(
            self, view, message, Vld.tournament_description
        )

        self.lnk.init()
        while self.lnk.next is False:
            while tournament.count_players() < DEFAULT_NBR_PLAYER:
                new_player = PlayerController.add_player(
                    view, tournament.count_players()+1
                )
                tournament.add_player(new_player)

            self.lnk.next = True

        my_round = RoundController.create_round(
            tournament.export_players(), 'round 1'
        )
        tournament.add_round(my_round)
        return tournament

    @classmethod
    def import_all_tournament(self):
        Tournament.all_tournaments = []
        tournaments = TournamentManagement.get_all()
        for tournament in tournaments:
            t = Tournament()
            t.id = tournament['id']
            t.name = tournament['name']
            t.place = tournament['place']
            t.start_date = tournament['start_date']
            t.nbr_days = tournament['nbr_days']
            t.nbr_rounds = tournament['nbr_rounds']
            t.ctr_time = tournament['ctr_time']
            t.description = tournament['description']

            for player_id in tournament['players']:
                t.add_player(PlayerController.get_by_id(player_id))

            for round_id in tournament['rounds']:
                round_dic = RoundController.get_by_id(round_id)
                my_round = Round(round_dic)
                for match_id in round_dic['matchs']:
                    match = MatchManagement.get_by_id(match_id)
                    new_match = Match(match)
                    for tuple_player in match['players']:
                        new_match.add_player(
                            PlayerController.get_by_id(tuple_player[0]), tuple_player[1]
                        )
                    my_round.add_match(new_match)
                t.add_round(my_round)

    @classmethod
    def view_tournaments(self, view):
        for index, tournament in enumerate(Tournament.all_tournaments):
            view.display_list_tournament(tournament, index+1)
        return view.choice_tournament()

    def get_ctr_time(self, ctr_time):
        if ctr_time == '1':
            return 'bullet'
        elif ctr_time == '2':
            return 'blitz'
        elif ctr_time == '3':
            return 'coup rapide'
        elif ctr_time.lower() in ['bullet', 'blitz', 'coup rapide']:
            return ctr_time.lower()

    def form(self, view, message, validation):
        self.lnk.init()
        while self.lnk.next is False:
            response = view.field_text(self.lnk, message)
            validation(response, self.lnk)
            if self.lnk.next is True:
                return response

    @classmethod
    def menu_edit_tournament(self, view, tournament):
        select = '0'

        while select != 'q':
            select = view.display_edit_tournament_menu()
            if select == '2':
                message = f'Entrer le nouveau nom du tournoi [{tournament.name}]: '
                tournament.name = self.form(
                    self, view, message, Vld.tournament_name
                )
            if select == '3':
                self.lnk.init()
                while self.lnk.next is False:
                    message = 'Entrer la nouvelle description: '
                    tournament.description = self.form(
                        self, view, message, Vld.tournament_ctr_time
                    )
            if select == '4':
                message = 'Côntrole du temps ([1] Bullet, [2] Blitz, [3] Coup rapide): '
                ctr_time = self.form(
                    self, view, message, Vld.tournament_ctr_time
                )
                tournament.ctr_time = self.get_ctr_time(self, ctr_time)
        self.lnk.init()


class RoundController:

    @classmethod
    def create_round(self, players_list, name):
        round_one = Round({'name': name})
        players_list = sorted(players_list, key=lambda x: x['rating'])
        half = len(players_list)//2
        list_one = players_list[:half]
        list_two = players_list[half:]
        while len(list_one) > 1 or len(list_two):
            player_one = list_one.pop(0)
            player_two = list_two.pop(0)
            match = Match()
            match.add_player(Player(player_one))
            match.add_player(Player(player_two))
            round_one.add_match(match)
        return round_one

    @classmethod
    def import_all_rounds(self, players_list, name):
        return RoundManagement.get_all()

    @classmethod
    def get_by_id(cls, my_id):
        return RoundManagement.get_by_id(my_id)


class MatchController:

    @classmethod
    def import_all_matches(self):
        return MatchManagement.get_all()

    @classmethod
    def get_by_id(cls, my_id):
        return MatchManagement.get_by_id(my_id)
