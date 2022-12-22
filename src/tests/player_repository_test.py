import unittest
from repositories.player_repository import player_repository

class TestPlayerRepository(unittest.TestCase):
    def setUp(self):
        player_repository.delete_all()
        self.name = "matti"
        self.turns = 1
        self.name2 = "teppo"
    
    def test_create_player(self):
        player_repository.create_player(self.name, self.turns)
        players = player_repository.find_all()
        self.assertEqual(len(players), 1)
        self.assertEqual(players[0], self.name)
    
    def test_find_all(self):
        player_repository.create_player(self.name, self.turns)
        player_repository.create_player(self.name2, self.turns)
        players = player_repository.find_all()
        self.assertEqual(len(players), 2)
        self.assertEqual(players[0], self.name)
        self.assertEqual(players[1], self.name2)
    
    def test_find_by_name(self):
        player_repository.create_player(self.name, self.turns)
        player = player_repository.find_by_name(self.name)
        self.assertEqual(player, self.name)