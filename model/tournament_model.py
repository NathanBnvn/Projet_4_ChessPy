#!/usr/bin/env python
# coding: utf-8

from tinydb import TinyDB, Query
from collections import UserList
# from .match import Match
# from .round import Round
# from .player import Player

class Tournament:
        db = TinyDB('db.json', indent=4, separators=(',', ': '))
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
                tournament = Tournament(
                        name=tournament[0],
                        place=tournament[1],
                        start_date=tournament[2],
                        end_date=tournament[3],
                        round_count=tournament[4],
                        rounds=tournament[5],
                        players=tournament[6],
                        time_control=tournament[7],
                        description=tournament[8]
                )
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
                serialized_tournament = self.tournament_model.serializer(self, tournament)
                self.tournament_model.tournament_table.insert(serialized_tournament)


        def update(self, category, new_value, tournament_id):
                updated_tournament = self.tournament_model.tournament_table.update(
                        {category: new_value}, 
                        doc_ids = [tournament_id]
                        )
                return updated_tournament


        def get(self, tournament_id):
                tournament = self.tournament_model.tournament_table.get(doc_id=tournament_id)
                return tournament


        def get_all(self):
                registered_tournament = self.tournament_model.tournament_table.all()
                return registered_tournament
