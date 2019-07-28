from engine.models import (
    RuleSet,
    Space,
    Buyable,
    RailroadGroup,
    Railroad,
    PropertyGroup,
    Property,
    Dice
)

def seed_fair_dice():
    fair_dice, _ = Dice.objects.get_or_create(
        name="Fair dice",
        description="Two uniform randomness dice",
        dice_name="FairDice"
    )
    return fair_dice

def seed_deterministic_dice():
    deterministic_dice, _ = Dice.objects.get_or_create(
        name="All 1 die",
        description="A single die always rolls 1",
        dice_name="DeterministicDice"
    )
    return deterministic_dice

def seed_us_board():
    # Seed our dice
    fair_dice = seed_fair_dice()
    # Board
    ruleset, _ = RuleSet.objects.get_or_create(
        name="Standard (American Edition)",
        description="The start Monopoly board layout as of 2008",
        start_money=1500,
        num_houses=32,
        num_hotels=12,
        turn_time=120,
        dice=fair_dice,
    )
    # Groups
    brown_group, _ = PropertyGroup.objects.get_or_create(
        color="#9C661F",
        house_cost=50,
    )
    aqua_group, _ = PropertyGroup.objects.get_or_create(
        color="#76EEC6",
        house_cost=50,
    )
    pink_group, _ = PropertyGroup.objects.get_or_create(
        color="#FFC0CB",
        house_cost=100,
    )
    orange_group, _ = PropertyGroup.objects.get_or_create(
        color="#FF8C00",
        house_cost=100,
    )
    red_group, _ = PropertyGroup.objects.get_or_create(
        color="#FF0000",
        house_cost=150,
    )
    yellow_group, _ = PropertyGroup.objects.get_or_create(
        color="#FFFF00",
        house_cost=150,
    )
    green_group, _ = PropertyGroup.objects.get_or_create(
        color="#00FF00",
        house_cost=200,
    )
    blue_group, _ = PropertyGroup.objects.get_or_create(
        color="#0000FF",
        house_cost=200,
    )
    # Railroad
    rail_group, _ = RailroadGroup.objects.get_or_create(
        base_cost=25,
    )
    # Spaces
    Space.objects.get_or_create(
        board=ruleset,
        position=0,
        name="Start",
    )
    Property.objects.get_or_create(
        board=ruleset,
        position=1,
        name="Mediterranean Avenue",
        
        group=brown_group,

        rent=2,
        rent_1_house=10,
        rent_2_house=30,
        rent_3_house=90,
        rent_4_house=160,
        rent_hotel=250,

        price=60,
    )
    Space.objects.get_or_create(
        board=ruleset,
        position=2,
        name="Community Chest",
    )
    Property.objects.get_or_create(
        board=ruleset,
        position=3,
        name="Baltic Avenue",
        
        group=brown_group,

        rent=4,
        rent_1_house=20,
        rent_2_house=60,
        rent_3_house=180,
        rent_4_house=320,
        rent_hotel=450,

        price=60,
    )
    Space.objects.get_or_create(
        board=ruleset,
        position=4,
        name="Income Tax",
    )
    Railroad.objects.get_or_create(
        board=ruleset,
        position=5,
        name="Reading Railroad",

        group=rail_group,

        price=200,
    )
    Property.objects.get_or_create(
        board=ruleset,
        position=6,
        name="Oriental Avenue",
        
        group=aqua_group,

        rent=6,
        rent_1_house=30,
        rent_2_house=90,
        rent_3_house=270,
        rent_4_house=400,
        rent_hotel=550,

        price=100,
    )
    Space.objects.get_or_create(
        board=ruleset,
        position=7,
        name="Chance",
    )
    Property.objects.get_or_create(
        board=ruleset,
        position=8,
        name="Vermont Avenue",
        
        group=aqua_group,

        rent=6,
        rent_1_house=30,
        rent_2_house=90,
        rent_3_house=270,
        rent_4_house=400,
        rent_hotel=550,

        price=100,
    )
    Property.objects.get_or_create(
        board=ruleset,
        position=9,
        name="Connecticut Avenue",
        
        group=aqua_group,

        rent=8,
        rent_1_house=40,
        rent_2_house=100,
        rent_3_house=300,
        rent_4_house=450,
        rent_hotel=600,

        price=120,
    )
    Space.objects.get_or_create(
        board=ruleset,
        position=10,
        name="In Jail / Just Visiting",
    )
    Property.objects.get_or_create(
        board=ruleset,
        position=11,
        name="St. Charles Place",
        
        group=pink_group,

        rent=10,
        rent_1_house=50,
        rent_2_house=150,
        rent_3_house=450,
        rent_4_house=625,
        rent_hotel=750,

        price=140,
    )
    Buyable.objects.get_or_create(
        board=ruleset,
        position=12,
        name="Electric Company",

        price=150,
    )
    Property.objects.get_or_create(
        board=ruleset,
        position=13,
        name="States Avenue",
        
        group=pink_group,

        rent=10,
        rent_1_house=50,
        rent_2_house=150,
        rent_3_house=450,
        rent_4_house=625,
        rent_hotel=750,

        price=140,
    )
    Property.objects.get_or_create(
        board=ruleset,
        position=14,
        name="Virginia Avenue",
        
        group=pink_group,

        rent=12,
        rent_1_house=60,
        rent_2_house=180,
        rent_3_house=500,
        rent_4_house=700,
        rent_hotel=900,

        price=160,
    )
    Railroad.objects.get_or_create(
        board=ruleset,
        position=15,
        name="Pennsylvania Railroad",

        group=rail_group,

        price=200,
    )
    Property.objects.get_or_create(
        board=ruleset,
        position=16,
        name="St. James Place",
        
        group=orange_group,

        rent=14,
        rent_1_house=70,
        rent_2_house=200,
        rent_3_house=550,
        rent_4_house=750,
        rent_hotel=950,

        price=180,
    )
    Property.objects.get_or_create(
        board=ruleset,
        position=17,
        name="Tennessee Avenue",
        
        group=orange_group,

        rent=14,
        rent_1_house=70,
        rent_2_house=200,
        rent_3_house=550,
        rent_4_house=750,
        rent_hotel=950,

        price=180,
    )
    Space.objects.get_or_create(
        board=ruleset,
        position=18,
        name="Community Chest",
    )
    Property.objects.get_or_create(
        board=ruleset,
        position=19,
        name="New York Avenue",
        
        group=orange_group,

        rent=16,
        rent_1_house=80,
        rent_2_house=220,
        rent_3_house=600,
        rent_4_house=800,
        rent_hotel=1000,

        price=200,
    )
    Space.objects.get_or_create(
        board=ruleset,
        position=20,
        name="Free Parking",
    )
    Property.objects.get_or_create(
        board=ruleset,
        position=21,
        name="Kentucky Avenue",
        
        group=red_group,

        rent=18,
        rent_1_house=90,
        rent_2_house=250,
        rent_3_house=700,
        rent_4_house=875,
        rent_hotel=1050,

        price=220,
    )
    Space.objects.get_or_create(
        board=ruleset,
        position=22,
        name="Chance",
    )
    Property.objects.get_or_create(
        board=ruleset,
        position=23,
        name="Indiana Avenue",
        
        group=red_group,

        rent=18,
        rent_1_house=90,
        rent_2_house=250,
        rent_3_house=700,
        rent_4_house=875,
        rent_hotel=1050,

        price=220,
    )
    Property.objects.get_or_create(
        board=ruleset,
        position=24,
        name="Illinois Avenue",
        
        group=red_group,

        rent=20,
        rent_1_house=100,
        rent_2_house=300,
        rent_3_house=750,
        rent_4_house=925,
        rent_hotel=1100,

        price=240,
    )
    Railroad.objects.get_or_create(
        board=ruleset,
        position=25,
        name="B&O Railroad",

        group=rail_group,

        price=200,
    )
    Property.objects.get_or_create(
        board=ruleset,
        position=26,
        name="Atlantic Avenue",
        
        group=yellow_group,

        rent=22,
        rent_1_house=110,
        rent_2_house=330,
        rent_3_house=800,
        rent_4_house=975,
        rent_hotel=1150,

        price=260,
    )
    Property.objects.get_or_create(
        board=ruleset,
        position=27,
        name="Ventnor Avenue",
        
        group=yellow_group,

        rent=22,
        rent_1_house=110,
        rent_2_house=330,
        rent_3_house=800,
        rent_4_house=975,
        rent_hotel=1150,

        price=260,
    )
    Buyable.objects.get_or_create(
        board=ruleset,
        position=28,
        name="Water Works",

        price=150,
    )
    Property.objects.get_or_create(
        board=ruleset,
        position=29,
        name="Marvin Gardens",
        
        group=yellow_group,

        rent=24,
        rent_1_house=120,
        rent_2_house=360,
        rent_3_house=850,
        rent_4_house=1025,
        rent_hotel=1200,

        price=280,
    )
    Space.objects.get_or_create(
        board=ruleset,
        position=30,
        name="Go To Jail",
    )
    Property.objects.get_or_create(
        board=ruleset,
        position=31,
        name="Pacific Avenue",
        
        group=green_group,

        rent=26,
        rent_1_house=130,
        rent_2_house=390,
        rent_3_house=900,
        rent_4_house=1100,
        rent_hotel=1275,

        price=300,
    )
    Property.objects.get_or_create(
        board=ruleset,
        position=32,
        name="North Carolina Avenue",
        
        group=green_group,

        rent=26,
        rent_1_house=130,
        rent_2_house=390,
        rent_3_house=900,
        rent_4_house=1100,
        rent_hotel=1275,

        price=300,
    )
    Space.objects.get_or_create(
        board=ruleset,
        position=33,
        name="Community Chest",
    )
    Property.objects.get_or_create(
        board=ruleset,
        position=34,
        name="Pennsylvania Avenue",
        
        group=green_group,

        rent=28,
        rent_1_house=150,
        rent_2_house=450,
        rent_3_house=1000,
        rent_4_house=1200,
        rent_hotel=1400,

        price=320,
    )
    Railroad.objects.get_or_create(
        board=ruleset,
        position=35,
        name="Short Line",

        group=rail_group,

        price=200,
    )
    Space.objects.get_or_create(
        board=ruleset,
        position=36,
        name="Chance",
    )
    Property.objects.get_or_create(
        board=ruleset,
        position=37,
        name="Park Place",
        
        group=blue_group,

        rent=35,
        rent_1_house=175,
        rent_2_house=500,
        rent_3_house=1100,
        rent_4_house=1300,
        rent_hotel=1500,

        price=350,
    )
    Space.objects.get_or_create(
        board=ruleset,
        position=38,
        name="Luxury Tax",
    )
    Property.objects.get_or_create(
        board=ruleset,
        position=39,
        name="Broadwalk",
        
        group=blue_group,

        rent=50,
        rent_1_house=200,
        rent_2_house=600,
        rent_3_house=1400,
        rent_4_house=1700,
        rent_hotel=2000,

        price=400,
    )
    return ruleset
