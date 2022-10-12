from model.tournament import Tournament
from view.tournament import TournamentView
from datetime import datetime

class TournamentController:

    def create_tournament(self):
        self.tournament = Tournament
        self.tournament_view = TournamentView
        tournament = self.tournament_view.prompt_tournament(self)
        if not tournament:
            return
            tournament = Tournament(
			tournament[0], 
			tournament[1], 
			tournament[2], 
			tournament[3], 
			tournament[4], 
			tournament[5], 
			tournament[6], 
			)