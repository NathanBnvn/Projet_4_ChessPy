#!/usr/bin/env python
# coding: utf-8

from collections import UserList

class Match(UserList):

	def __init__(self, player_1, player_2, score_player_1, score_player_2):
		self.player_1 = player_1
		self.player_2 = player_2
		self.score_player_1 = score_player_1
		self.score_player_2 = score_player_2

		self.match = Match(
			[player_1, score_player_1], 
			[player_2, score_player_2]
			)