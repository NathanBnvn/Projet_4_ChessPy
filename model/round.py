#!/usr/bin/env python
# coding: utf-8

from .match import Match

class Round:
	
	def __init__(self, name, match, start_time, end_time):
		self.name = name
		self.match = Match()
		self.start_time = start_time
		self.end_time = end_time