#!/usr/bin/env python
# coding: utf-8

from tinydb import TinyDB


class Round:
    db = TinyDB('db.json', indent=4, separators=(',', ': '))
    round_table = db.table('rounds')

    def __init__(self, name, matchs, start_time, end_time):
        self.name = name
        self.matchs = matchs
        self.start_time = start_time
        self.end_time = end_time

    def serializer(self, round):
        round = Round(
            name=round[0]['name'],
            matchs=round[0]['round'],
            start_time=round[0]['start_at'],
            end_time=round[0]['finish_at']
        )
        serialized_round = {
            'name': round.name,
            'matchs': round.matchs,
            'start_time': round.start_time,
            'end_time': round.end_time
        }
        return serialized_round

    def save(self, round):
        serialized_round = self.round_model.serializer(self, round)
        self.round_model.round_table.insert(serialized_round)
