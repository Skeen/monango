# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model

from engine.fixture import seed_us_board
from engine.models import (
    Player,
    Game,
)


class AnimalTestCase(TestCase):

    def seed_players(self, game, num_players):
        for x in range(num_players):
            user = get_user_model().objects.create_user(
                username='player' + str(x),
                email='player' + str(x) + "@example.org",
                password='password1',
            )
            Player.objects.create(
                game=game,
                user=user,
            )

    def seed_game(self, board):
        return Game.objects.create(
            board=board,
        )

    def setUp(self):
        self.num_players = 4
        board = seed_us_board()
        self.game = self.seed_game(board)
        players = self.seed_players(self.game, self.num_players)

    def test_start(self):
        self.assertIsNone(self.game.last_action)
        self.assertIsNone(self.game.current_player)
        for player in self.game.players.all():
            self.assertEqual(player.money, 0)
            self.assertEqual(player.position, 0)
            self.assertFalse(player.in_jail)
        self.assertFalse(self.game.started())
        
        self.game.start()

        self.assertLessEqual(self.game.last_action, timezone.now())
        self.assertEqual(self.game.current_player, self.game.players.first())
        for player in self.game.players.all():
            self.assertEqual(player.money, 1500)
            self.assertEqual(player.position, 0)
            self.assertFalse(player.in_jail)
        self.assertTrue(self.game.started())

    def test_playing(self):
        self.game.start()
        self.assertEqual(self.game.players.first().position, 0)
        # TODO: Monkey-patch random.randint
        self.game.go()
        self.assertGreater(self.game.players.first().position, 0)
