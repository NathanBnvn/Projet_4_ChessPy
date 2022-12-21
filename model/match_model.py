#!/usr/bin/env python
# coding: utf-8

from collections import UserList
from tinydb import TinyDB


class Match(UserList):
    db = TinyDB('db.json', indent=4, separators=(',', ': '))
    match_table = db.table('matchs')

    def __init__(self, player_one, score_one, player_two, score_two):
        self.player_one = player_one,
        self.score_one = score_one,
        self.player_two = player_two,
        self.score_two = score_two

    def serializer(self, match_instance):
        match = Match(
            match_instance[0][0],
            match_instance[0][1],
            match_instance[1][0],
            match_instance[1][1],
        )
        serialized_match = {
            'player_one': match.player_one,
            'score_player_one': match.score_one,
            'player_two': match.player_two,
            'score_player_two': match.score_two
        }
        return serialized_match

    def save(self, match):
        serialized_match = self.match_model.serializer(self, match)
        self.match_model.match_table.insert(serialized_match)
