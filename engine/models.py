# -*- coding: utf-8 -*-
import random

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from model_utils.managers import InheritanceManager


class Board(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=4000, blank=True)

    # TODO: Should have currency?
    start_money = models.PositiveIntegerField()
    start_position = models.PositiveIntegerField(default=0)
    num_houses = models.PositiveIntegerField()
    num_hotels = models.PositiveIntegerField()
    turn_time = models.PositiveIntegerField()


class Space(models.Model):
    class Meta:
        unique_together = ['board', 'position']
    objects = InheritanceManager()

    board = models.ForeignKey(Board, related_name="spaces", on_delete=models.PROTECT)
    # TODO: Check entire range of positions is covered (i.e. no holes)
    position = models.PositiveIntegerField()
    name = models.CharField(max_length=100)

    def land_on(self, game, player):
        return("Landed on Space")

    def actions(self):
        return ['land_on']

    def __str__(self):
        return str(self.position) + ": " + self.name


class Buyable(Space):
    price = models.PositiveIntegerField()
    mortgage = models.PositiveIntegerField(null=True)

    def actions(self):
        return super(Buyable, self).actions() + ['buyable']

    def get_price(self):
        return self.price

    def get_mortgage(self):
        if self.mortgage is None:
            return self.price / 2
        return self.mortgage

    def land_on(self, game, player):
        return super(Buyable, self).land_on(game, player) + ("Landed on Buyable")

    def can_develop(self):
        return False

    def buyable(self):
        return True


class PropertyGroup(models.Model):
    # TODO: Use color field: https://github.com/charettes/django-colorful
    color = models.CharField(max_length=7)
    house_cost = models.PositiveIntegerField()
    hotel_cost = models.PositiveIntegerField(null=True)

    def get_house_cost(self):
        return self.house_cost

    def get_hotel_cost(self):
        if hotel_cost is None:
            return self.house_cost
        return self.hotel_cost


class RailroadGroup(models.Model):
    base_cost = models.PositiveIntegerField()


class Railroad(Buyable):
    group = models.ForeignKey(RailroadGroup, on_delete=models.PROTECT)

    def land_on(self, game, player):
        return super(Railroad, self).land_on(game, player) + ("Landed on Railroad")

    def rent(self):
        # owned_railroads = ...
        # return self.group.base_cost * 2 ** (owned_railrods - 1)
        return 0

    def can_develop(self):
        return False


class Property(Buyable):
    group = models.ForeignKey(PropertyGroup, on_delete=models.PROTECT)

    rent = models.PositiveIntegerField()
    rent_colorset = models.PositiveIntegerField(null=True)
    rent_1_house = models.PositiveIntegerField()
    rent_2_house = models.PositiveIntegerField()
    rent_3_house = models.PositiveIntegerField()
    rent_4_house = models.PositiveIntegerField()
    rent_hotel = models.PositiveIntegerField()

    def land_on(self, game, player):
        return super(Property, self).land_on(game, player) + ("Landed on Property")

    def get_rent_colorset(self):
        if self.rent_colorset is None:
            return self.rent * 2
        return self.rent

    def can_develop(self):
        return True


class TooFewPlayers(Exception):
    pass


class Game(models.Model):
    board = models.ForeignKey(Board, on_delete=models.PROTECT)

    # TODO: Check that current_player is in players
    current_player = models.ForeignKey('Player', null=True, related_name="+", on_delete=models.PROTECT)
    last_action = models.DateTimeField(null=True)

    def roll_dice(self):
        # TODO: Configurable number of dice and eyes
        # TODO: Custom event on dice?
        return random.randint(1, 6) + random.randint(1, 6)

    def start(self):
        # TODO: Run background task to timeout players
        self.last_action = timezone.now()
        # Check that enough players joined
        if self.players.count() < 2:
            raise TooFewPlayers("Must have atleast two players to start game!")
        self.current_player = self.players.all().order_by('id').first()
        # Set player money and position
        self.players.all().update(money=self.board.start_money)
        self.players.all().update(position=self.board.start_position)

        self.save()

    def turn_time_left(self):
        time_since_last_action = timezone.now() - self.last_action
        return self.board.turn_time - time_since_last_action

    # TODO: Mortgaging, building

    def go(self):
        # Roll and move
        roll = self.roll_dice()
        # TODO: divmod to flip around
        self.current_player.position = self.current_player.position + roll
        self.current_player.save()

        # Land on the square
        space = self.board.spaces.get_subclass(position=self.current_player.position)
        print(space)
        print(type(space))
        print(space.land_on(self, self.current_player))
        print(space.actions())

    def started(self):
        # Game is started if an action timer has been set
        return self.last_action is not None

    def next_player(self):
        next_player = self.player.all().order_by('id').filter(
            id__gt=self.current_player.id
        ).first()
        if next_player:
            self.current_player = next_player
        else:
            self.current_player = self.player.all().order_by('id').first()
        self.save()


class Player(models.Model):
    game = models.ForeignKey(Game, related_name="players", on_delete=models.PROTECT)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    money = models.PositiveIntegerField(default=0)
    position = models.PositiveIntegerField(default=0)
    in_jail = models.BooleanField(default=False)
    # TODO: Token, color, position


class OwnedSpace(models.Model):
    # TODO: Ensure space is in game defined by player
    space = models.ForeignKey(Buyable, on_delete=models.PROTECT)
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    # TODO: Houses, hotels
