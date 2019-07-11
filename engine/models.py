# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=4000, blank=True)

    start_money = models.PositiveIntegerField()
    start_position = models.PositiveIntegerField(default=0)


from model_utils.managers import InheritanceManager


class Space(models.Model):
    class Meta:
        unique_together = ['board', 'space_id']
    objects = InheritanceManager()

    board = models.ForeignKey(Board, on_delete=models.PROTECT)
    space_id = models.PositiveIntegerField()
    name = models.CharField(max_length=100)

    def land_on(self, player):
        return("Landed on Space")

    def actions(self):
        return ['land_on']

    def __str__(self):
        return self.name


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

    def land_on(self, player):
        return super(Buyable, self).land_on(player) + ("Landed on Buyable")

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



class Property(Buyable):
    group = models.ForeignKey(PropertyGroup, on_delete=models.PROTECT)

    rent = models.PositiveIntegerField()
    rent_colorset = models.PositiveIntegerField(null=True)
    rent_1_house = models.PositiveIntegerField()
    rent_2_house = models.PositiveIntegerField()
    rent_3_house = models.PositiveIntegerField()
    rent_4_house = models.PositiveIntegerField()
    rent_hotel = models.PositiveIntegerField()

    def land_on(self, player):
        return super(Property, self).land_on(player) + ("Landed on Property")

    def get_rent_colorset(self):
        if self.rent_colorset is None:
            return self.rent * 2
        return self.rent

    def can_develop(self):
        return True


class Game(models.Model):
    board = models.ForeignKey(Board, on_delete=models.PROTECT)
    

class Player(models.Model):
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    money = models.PositiveIntegerField()
    # TODO: Token, color, position
    position = models.PositiveIntegerField()


class OwnedSpace(models.Model):
    # TODO: Ensure space is in game defined by player
    space = models.ForeignKey(Buyable, on_delete=models.PROTECT)
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    # TODO: Houses, hotels


class Events(models.Model):
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    
