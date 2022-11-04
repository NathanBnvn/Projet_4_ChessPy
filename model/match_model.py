#!/usr/bin/env python
# coding: utf-8

from collections import UserList
from tinydb import TinyDB, Query

class Match(UserList):
	db = TinyDB('db.json', sort_keys=False, indent=4, separators=(',', ': '))
	match_table = db.table('matchs')

	def __init__(self, player_1, player_2, score_player_1, score_player_2):
		self.player_1 = player_1
		self.player_2 = player_2
		self.score_player_1 = score_player_1
		self.score_player_2 = score_player_2

		self.match = Match(
			[player_1, score_player_1], 
			[player_2, score_player_2]
			)