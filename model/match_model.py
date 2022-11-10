#!/usr/bin/env python
# coding: utf-8

from collections import UserList
from tinydb import TinyDB, Query

class Match(UserList):
	db = TinyDB('db.json', indent=4, separators=(',', ': '))
	match_table = db.table('matchs')

	def __init__(self, player_1, player_2, score_player_1, score_player_2):
		self.match = ([player_1, score_player_1], [player_2, score_player_2])
	

	def serializer(self, match):
		player_one = match[0]
		player_two = match[1]
		
		match = Match(
			player_1=player_one[0],
			score_player_1=player_one[1],
			player_2=player_two[0],
			score_player_2=player_two[1],
		)

		serialized_match = {
			'player_1': match.player_1,
			'score_player_1': match.score_player_1,
			'player_2': match.player_2,
			'score_player_2': match.score_player_2
        }

		print(serialized_match)
		return serialized_match