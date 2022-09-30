#!/usr/bin/env python
# coding: utf-8

from tinydb import TinyDB

class Player:
        
        def __init__(self, last_name, first_name, birth_date, gender, ranking):
                self.last_name = last_name
                self.first_name = first_name
                self.birth_date = birth_date
                self.gender = gender
                self.ranking = ranking