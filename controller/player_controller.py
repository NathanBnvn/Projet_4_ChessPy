#!/usr/bin/env python
# coding: utf-8

from turtle import update
from controller.manager_controller import ManagerController
from view.manager_view import ManagerView
from rich.table import Table

class PlayerController:
	def __init__(self, model, view):
		self.player_model = model
		self.player_view = view
		self.manager_view = ManagerView
		self.manager_controller = ManagerController
		self.error_message = "Commande non valide. Veuillez réessayer."
	
	def start_player_menu(self):
		self.player_view.show_player_menu(self)
		menu_message = "Choisissez une option : "

		while True:
			user_choice = self.manager_view.prompt_command(self, menu_message)

			if user_choice == '1':
				self.create_player()
			elif user_choice == '2':
				self.update_player()
			elif user_choice == '3':
				return
			else:
				self.manager_view.show_message(self, self.error_message)
			
			self.start_player_menu()
			return

	def create_player(self):
		input_player = [
            "le nom du joueur/joueuse : ",
            "le prénom du joueur/joueuse : ",
            "la date de naissance du joueur/joueuse (jj/mm/aaaa) : ",
            "sélectionnez le sexe du joueur/joueuse",
            "la place du joueur/joueuse dans le classement : ",
        ]
		message = input_player[4]
		choices = ["masculin", "féminin"]
		player = self.manager_controller.check_user_input(
			self, input_player, message, choices
			)
		sucessfully_created_message = "Votre joueur/joueuse à bien été crée."

		if player:
			if len(player) < len(input_player):
				while len(player) < len(input_player):
					player.append(None)
			self.player_model.save(self, player)
			self.manager_view.show_message(self, sucessfully_created_message)
		return player


	def add_player_to_tournament(self):
		tournament_players = []
		max_player_count = 7
		player_count = 0
		add_player_message = "Souhaitez-vous ajouter 8 joueurs aux tournois ? (oui/non) : "
		add_player_response = self.manager_view.prompt_command(self, add_player_message)
		if add_player_response == "oui":
			while player_count <= max_player_count:
				tournament_player = self.player_controller.create_player(self)
				tournament_players.append(tournament_player)
				player_count += 1
			# Les joueurs dans la table tournois correspondent 
			# à la liste des indices
			# des instances du joueur stockées en mémoire.
			return tournament_players


	def update_player(self):
		select_id = "Veuillez sélectionner l'ID du joueur que vous souhaitez mettre à jour : "
		select_category = "Quelle propriété souhaitez vous éditer ?"
		value_message = "Veuillez entrer la nouvelle valeur : "
		success_message = "Le joueur/la joueuse a bien été mis à jour"
		cannot_save_message = "Les données n'ont pas pu être enregistrées"
		categories = []
		players = self.player_model.get_all(self)
		# @TODO implement view function
		print(players)
		selected_id = self.manager_view.prompt_command(self, select_id)
		if selected_id.isdigit():
			player_id = int(selected_id)
		else:
			self.manager_view.show_message(self, self.error_message)
		player = self.player_model.get(self, player_id)
		# @TODO implement view function
		print(player)
		for key in player:
			categories.append(key)
		category = self.manager_view.select_command(self, select_category, categories)
		new_value = self.manager_view.prompt_command(self, value_message)
		update_player = self.player_model.update(self, category, new_value, player_id)
		if player_id in update_player:
			self.manager_view.show_message(self, success_message)
		else:
			self.manager_view.show_message(self, cannot_save_message)
