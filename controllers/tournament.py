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

        self.lnk.init()
        while self.lnk.next is False:
            message = 'entrer le nom du tournoi: '
            tournament.name = view.field_text(self.lnk, message)
            Vld.tournament_name(tournament.name, self.lnk)

        self.lnk.init()
        while self.lnk.next is False:
            message = 'entrer le lieu du tournoi: '
            tournament.place = view.field_text(self.lnk, message)
            Vld.tournament_place(tournament.place, self.lnk)

        self.lnk.init()
        while self.lnk.next is False:
            message = 'entrer la date du début du tournoi (jj/mm/yyyy): '
            new_date = view.field_text(self.lnk, message)
            tournament.start_date = Vld.tournament_date_start(new_date, self.lnk)

        self.lnk.init()
        while self.lnk.next is False:
            message = 'combien de jour durera la tournoi [1]: '
            nbr_days = view.field_text(self.lnk, message)
            tournament.nbr_days = Vld.tournament_duration(nbr_days, self.lnk)

        self.lnk.init()
        while self.lnk.next is False:
            message = 'combien de tours [4]: '
            nbr_rounds = view.field_text(self.lnk, message)
            tournament.nbr_rounds = Vld.tournament_rounds(nbr_rounds, self.lnk)

        self.lnk.init()
        while self.lnk.next is False:
            message = 'côntrole du temps ([1] Bullet, [2] Blitz, [3] Coup rapide): '
            ctr_time = view.field_text(self.lnk, message)
            tournament.ctr_time = Vld.tournament_ctr_time(ctr_time, self.lnk)

        self.lnk.init()
        while self.lnk.next is False:
            message = 'entrer une description: '
            tournament.description = view.field_text(self.lnk, message)
            Vld.tournament_description(tournament.description, self.lnk)

        self.lnk.init()
        while self.lnk.next is False:
            while tournament.count_players() < DEFAULT_NBR_PLAYER:
                new_player = PlayerController.add_player(view, tournament.count_players()+1)
                tournament.add_player(new_player)

            self.lnk.next = True

        my_round = RoundController.create_round(tournament.export_players(), 'round 1')
        tournament.add_round(my_round)
        return tournament


class RoundController:

    @classmethod
    def create_round(self, players_list, name):
        round_one = Round(name)
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
