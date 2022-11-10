#!/usr/bin/env python
# coding: utf-8

from tinydb import TinyDB, Query

class Player:
        db = TinyDB('db.json', indent=4, separators=(',', ': '))
        player_table = db.table('players')
        player_query = Query()

        def __init__(self, last_name, first_name, birth_date, gender, ranking):
                self.last_name = last_name
                self.first_name = first_name
                self.birth_date = birth_date
                self.gender = gender
                self.ranking = ranking


        def serializer(self, player):
                player = Player(
                        last_name=player[0], 
                        first_name=player[1], 
                        birth_date=player[2],
                        gender=player[3],
                        ranking=player[4],
                )
                serialized_player = {
                        'last_name': player.last_name,
                        'first_name': player.first_name,
                        'birth_date': player.birth_date,
                        'gender': player.gender,
                        'ranking': player.ranking
                }
                return serialized_player


        def save(self, player):
                serialized_player = self.player_model.serializer(self, player)
                self.player_model.player_table.insert(serialized_player)


        def update(self, category, new_value, player_id):
                updated_player = self.player_model.player_table.update(
                        {category: new_value}, 
                        doc_ids = [player_id]
                        )
                return updated_player


        def get(self, player_id):
                player = self.player_model.player_table.get(doc_id=player_id)
                return player


        def get_all(self):
                saved_players = self.player_model.player_table.all()
                return saved_players


        def get_ranked_player(self):
                ranked_player = self.player_model.player_table.search(
                        self.player_model.player_query.ranking != None
                        )
                return ranked_player
