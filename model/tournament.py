#!/usr/bin/env python
# coding: utf-8

from tinydb import TinyDB
from collections import UserList
# from .match import Match
# from .round import Round
# from .player import Player

class Tournament:
        
        def __init__(self, name, place, start_date, end_date, round_count, time_check, description):
                self.name = name
                self.place = place
                self.start_date = start_date
                self.end_date = end_date
                self.round_count = round_count
                self.round_list = round_list
                self.player = player
                self.time_check = time_check
                self.description = description
