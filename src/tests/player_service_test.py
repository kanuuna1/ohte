import unittest
from services.player_service import(PlayerService, NameExistsError)

class FakePlayerRepository:
    def __init__(self, players=None):
        self.players = players or []

    def delete_all(self):
        self.players = []

    def find_all(self):
        return self.players

    def create_player(self, name, turns):
        t = [name, turns]
        self.players.append(t)

    def find_by_name(self, name):
        matching_players = filter(
            lambda player: player[0] == name,
            self.players
        )

        matching_players_list = list(matching_players)

        return matching_players_list[0] if len(matching_players_list) > 0 else None
    

class TestPlayerService(unittest.TestCase):
    def setUp(self):
        self.player_service = PlayerService(FakePlayerRepository())
        self.name = "matti"
        self.turns = 1

    def test_find_all(self):
        self.player_service.create_player(self.name, self.turns)
        players = self.player_service.find_all()
        self.assertEqual(len(players), 1)

    def test_find_by_name(self):
        self.player_service.create_player(self.name, self.turns)
        players = self.player_service.find_by_name(self.name)
        self.assertEqual(len(players), 2)

    def test_create_player_with_non_existing_username(self):
        self.player_service.create_player(self.name, self.turns)
        players = self.player_service.find_all()
        self.assertEqual(len(players), 1)
        self.assertEqual(players[0][0], self.name)

    def test_create_user_with_existing_username(self):
        self.player_service.create_player(self.name, self.turns)
        
        self.assertRaises(
            NameExistsError,
            lambda: self.player_service.create_player(self.name, self.turns)
        )

    
    