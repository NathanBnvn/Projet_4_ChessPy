#!/usr/bin/env python
# coding: utf-8

from tinydb import TinyDB, Query
from collections import UserList
# from .match import Match
# from .round import Round
# from .player import Player

class Tournament:
        db = TinyDB('db.json', sort_keys=True, indent=4, separators=(',', ': '))
        tournament_table = db.table('tournaments')

        def __init__(self, name, place, start_date, end_date, round_count, rounds, players, time_control, description):
                self.name = name
                self.place = place
                self.start_date = start_date
                self.end_date = end_date
                self.round_count = round_count
                self.rounds = rounds
                self.players = players
                self.time_control = time_control
                self.description = description


        def serializer(self, tournament):
                serialized_tournament = {
                        'name': tournament.name,
                        'place': tournament.place,
                        'start_date': tournament.start_date,
                        'end_date': tournament.end_date,
                        'round_count': tournament.round_count,
                        'rounds': tournament.rounds,
                        'players': tournament.players,
                        'time_control': tournament.time_control,
                        'description': tournament.description
                }
                return serialized_tournament


        def save(self, tournament):
                serialized_tournament = self.serializer(tournament)
                self.tournament_table.insert(serialized_tournament)


        def update(self, tournament):
                self.tournament_table.update()
                pass


        def get(self, tournament_name):
                self.tournament_table.get()
                pass

        def get_all(self):
                registered_tournament = self.tournament_model.player_table.all()
                return registered_tournament