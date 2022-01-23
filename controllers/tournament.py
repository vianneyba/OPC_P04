from models.linktracking import LinkTracking
from models.match import Match
from models.round import Round
from controllers.validation import Validation as Vld
from controllers.player import PlayerController
from services.services import PlayerManagement, RoundManagement
from services.services import MatchManagement, TournamentManagement
from models.tournament import Tournament
from config import DEFAULT_NBR_PLAYER


class TournamentController:
    lnk = LinkTracking()

    def __init__(self, view=None):
        self.view = view

    def select_tournament(self):
        tournaments = Tournament.all_tournaments
        self.view.display_list_tournament_online(tournaments)
        t_id = self.view.display_select_tournament()

        try:
            t_id = int(t_id)-1
            if t_id < len(tournaments):
                return tournaments[t_id]
            else:
                return None
        except ValueError:
            return None

    def field_place(self, txt=None):
        if txt:
            message = f'Nouveau Lieu ({txt}): '
        else:
            message = 'Entrer le lieu du tournoi: '
        return self.form(self.view, message, Vld.tournament_place)

    def field_ctr_time(self, txt=None):
        if txt:
            message = (
                '[1] Bullet, [2] Blitz, [3] Coup rapide '
                f'(actuelle = {txt}): '
            )
        else:
            message = (
                'Côntrole du temps '
                '([1] Bullet, [2] Blitz, [3] Coup rapide): '
            )
        ctr_time = self.form(self.view, message, Vld.tournament_ctr_time)
        return self.get_ctr_time(ctr_time)

    def field_description(self, txt=None):
        if txt:
            message = f'Entrer la nouvelle description ({txt}): '
        else:
            message = 'Entrer une description: '
        return self.form(self.view, message, Vld.tournament_description)

    def field_name(self, txt=None):
        if txt:
            message = f'Entrer le nouveau nom du tournoi [{txt}]: '
        else:
            message = 'Entrer le nom du tournoi: '
        return self.form(self.view, message, Vld.tournament_name)

    def field_start_date(self, txt=None):
        if txt:
            message = f'Changer la date de début ({txt}): '
        else:
            message = 'Entrer la date du début du tournoi (jj/mm/yyyy): '
        return self.form(self.view, message, Vld.tournament_date_start)

    def field_nbr_days(self, txt=None):
        if txt:
            message = f'Durée du tournoi ({txt}): '
        else:
            message = 'Combien de jour durera la tournoi [1]: '
        return self.form(self.view, message, Vld.tournament_duration)

    def field_nbr_rounds(self, txt=None):
        if txt:
            message = f'Nombre de tours ({txt}): '
        else:
            message = 'Nombre de tours [4]: '
        return self.form(self.view, message, Vld.tournament_rounds)

    def save(self, tournament):
        for player in tournament.players:
            PlayerManagement.save(player.serialize())
        for round_t in tournament.rounds:
            RoundManagement.save(round_t.serialize())
            for match in round_t.matches:
                MatchManagement.save(match.serialize())

        TournamentManagement.save(tournament.serialize())

    def add_player(self, tournament: Tournament, view, add=False) -> str:
        pc = PlayerController(self.view)
        select = ''
        while select not in ['q', 'n']:
            if select == 'y' or add:
                add = False
                new_player = pc.add_player(
                    tournament.count_players()+1
                )
                tournament.add_player(new_player)
            if tournament.count_players() < DEFAULT_NBR_PLAYER:
                select = view.display_add_player()
            else:
                select = 'q'

    def create_round(self, tournament: Tournament, name='round 1', first=True):
        my_round = RoundController.create_round(
            tournament.get_players(), name, first)
        tournament.add_round(my_round)

    def add_tournament(self):
        tournament = Tournament()

        self.view.display_tournament_new()

        tournament.name = self.field_name()
        tournament.place = self.field_place()
        tournament.set_start_date(self.field_start_date())
        tournament.nbr_days = self.field_nbr_days()
        tournament.nbr_rounds = self.field_nbr_rounds()
        tournament.ctr_time = self.field_ctr_time()
        tournament.description = self.field_description()

        self.add_player(tournament, self.view)

        return tournament

    def import_all_tournament(self):
        tournaments = TournamentManagement.get_all()
        for tournament in tournaments:
            t = Tournament()
            t.id = tournament['id']
            t.name = tournament['name']
            t.place = tournament['place']
            t.set_start_date(tournament['start_date'])
            t.nbr_days = tournament['nbr_days']
            t.nbr_rounds = tournament['nbr_rounds']
            t.ctr_time = tournament['ctr_time']
            t.description = tournament['description']

            for player_id in tournament['players']:
                t.add_player(PlayerController.get_by_id(player_id))

            for round_id in tournament['rounds']:
                round_dic = RoundController.get_by_id(round_id)
                my_round = Round(round_dic)
                for match_id in round_dic['matches']:
                    match = MatchManagement.get_by_id(match_id)
                    new_match = Match(match)
                    for tuple_player in match['players']:
                        new_match.add_player(
                            PlayerController.get_by_id(
                                tuple_player[0]), tuple_player[1]
                        )
                    my_round.add_match(new_match)
                t.add_round(my_round)

    def view_tournaments(self):
        if len(Tournament.all_tournaments) > 0:
            tournaments = Tournament.all_tournaments
            self.view.display_list_tournament_online(tournaments)

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
            response = validation(response, self.lnk)
            if self.lnk.next is True:
                return response

    def close_round(self, my_round):
        matches = my_round.matches

        for match in matches:
            continu = True
            p_one = match.player_one
            p_two = match.player_two
            self.view.display_list_players([p_one, p_two])

            while continu:
                select = self.view.finish_match(p_one, p_two)
                if select in ['1', '2', '3']:
                    MatchController.add_point(int(select), match)
                    continu = False

            my_round.finish()

    def change_player_rating(self, players):
        pc = PlayerController(self.view)
        for player in players:
            txt = f'{player.firstname} {player.lastname} ({player.points} pts)'
            print(self.view.headings(txt))
            player.rating = pc.field_rating(
                player.rating
            )


class RoundController:

    @classmethod
    def create_round(self, players_list, name, first=True):
        round_one = Round({'name': name})
        players_list = sorted(players_list, key=lambda x: x.rating)
        if first:
            half = len(players_list)//2
            list_one = players_list[:half]
            list_two = players_list[half:]
            while len(list_one) > 1 or len(list_two):
                player_one = list_one.pop(0)
                player_two = list_two.pop(0)
                match = Match()
                match.add_player(player_one)
                match.add_player(player_two)
                round_one.add_match(match)
        else:
            players_list = sorted(
                players_list, key=lambda x: x.points, reverse=True)
            while len(players_list) > 1:
                player_one = players_list.pop(0)
                player_two = players_list.pop(0)
                match = Match()
                match.add_player(player_one)
                match.add_player(player_two)
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

    @classmethod
    def add_point(cls, player_selected: int, match: Match):
        if player_selected == 1:
            match.player_one.add_points(1)
            pts = 1
        elif player_selected == 2:
            match.player_two.add_points(1)
            pts = 1
        elif player_selected == 3:
            match.player_one.add_points(0.5)
            match.player_two.add_points(0.5)
            pts = 0.5

        match.add_point(player_selected, pts)
