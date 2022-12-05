#!/usr/bin/env python
# coding: utf-8

from tinydb import TinyDB, Query
from .match_model import Match
import datetime

class Round:
	db = TinyDB('db.json', indent=4, separators=(',', ': '))
	round_table = db.table('rounds')

	def __init__(self, name, match, start_time, end_time):
		self.name = name
		self.match = match
		self.start_time = start_time
		self.end_time = end_time
	
	def serializer(self, round):
		round = Round(
			name=round[0],
			match=round[1],
			start_time=datetime.datetime.now(),
			end_time=round[2]
		)