from model.ActionType import ActionType
from model.Building import Building
from model.BuildingType import BuildingType
from model.Bonus import Bonus
from model.BonusType import BonusType
from model.Faction import Faction
from model.Game import Game
from model.LaneType import LaneType
from model.Minion import Minion
from model.MinionType import MinionType
from model.Move import Move
from model.Player import Player
from model.PlayerContext import PlayerContext
from model.Projectile import Projectile
from model.ProjectileType import ProjectileType
from model.Unit import Unit
from model.Wizard import Wizard
from model.World import World

import random


class MyStrategy:
    # constants section
    WAYPOINT_RADIUS = 100
    LOW_HP_FACTOR = 0.25

    # get modules initialised
    lane = LaneType()
    waypoints = []

    def move(self, me: Wizard, world: World, game: Game, move: Move):
        self.initialize_strategy(game)
        self.initialize_tick(world, game, me, move)

        # add strafe_speed
        if self.me.life < self.me.max_life * self.LOW_HP_FACTOR:
            self.goto(self.get_previous_waypoint())





    # ------ helper functions ---------------------------------------
    def initialize_strategy(self, game):
        random.seed(game.random_seed)
        map_size = game.map_size
        print('Map size %s' % map_size)

        # TOP lane waypoints
        self.waypoints.append([100, map_size - 100])
        self.waypoints.append([100, map_size - 400])
        self.waypoints.append([200, map_size - 800])
        self.waypoints.append([200, map_size * 0.75])
        self.waypoints.append([200, map_size * 0.5])
        self.waypoints.append([200, map_size * 0.25])
        self.waypoints.append([200, 200])
        self.waypoints.append([map_size * 0.25, 200])
        self.waypoints.append([map_size * 0.5, 200])
        self.waypoints.append([map_size * 0.75, 200])
        self.waypoints.append([map_size - 200, 200])
        print('Waypoints')
        print(self.waypoints)

        self.lane = LaneType.TOP

    def initialize_tick(self, world, game, me, move):
        self.world = world
        self.game = game
        self.me = me
        self.move = move

    def get_next_waypoint(self):
        last_waypoint_index = len(self.waypoints) - 1
        last_waypoint = self.waypoints[last_waypoint_index]

        for waypoint_index in range(0, last_waypoint_index):
            waypoint = self.waypoints[waypoint_index]

            if self.me.get_distance_to(waypoint) <= self.WAYPOINT_RADIUS:
                return waypoint[waypoint_index + 1]
            if last_waypoint.get_distance_to(waypoint) < self.me.get_distance_to(last_waypoint): # 1!!
                return waypoint

    def get_previous_waypoint(self):
        first_waypoint = self.waypoints[0]
        for waypoint_index in range(len(self.waypoints) - 1, 0, -1):
            waypoint = self.waypoints[waypoint_index]
            if self.me.get_distance_to(waypoint) <= self.WAYPOINT_RADIUS:
                return self.waypoints[waypoint_index - 1]
            if first_waypoint.get_distance_to(first_waypoint) < self.me.get_distance_to(first_waypoint): # 1!!
                return waypoint

    def goto(self, waypoint):
        angle = self.me.get_angle_to(waypoint[0], waypoint[1])

        self.move.turn(angle)

        if abs(angle) < self.game.staff_sector / 4:
            self.move.speed = self.game.wizard_forward_speed


    # @staticmethod
    # def goto_farm_place(me, world, game):
    #     print('Function: goto_farm_place')
    #     building_list = []
    #     for building in world.buildings:
    #         building_list.append([building.x, building.y])
    #         print('Building coordinates: x: %s, y: %s. Building type: %s' % (building.x, building.y, building.type))
    #
    #     if me.faction == Faction.ACADEMY:
    #         target_location_t2 = {'x': 50, 'y': 2693}
    #         target_location_t1 = {'x': 350, 'y': 1656}
    #
    #
    #
    #
    #
    #
    # @staticmethod
    # def get_top_tower_t1_coords(me, world):
    #     print('Function: get_top_tower_t1_coords')
    #     building_list = []
    #     print('My fraction: %s' % me.faction)
    #     for building in world.buildings:
    #         building_list.append([building.x, building.y])
    #         print('Building coordinates: x: %s, y: %s. Building type: %s' % (building.x, building.y, building.type))
    #
    #     t1_tower = {'x': building_list[0][0], 'y': building_list[0][1]}
    #     if me.faction == Faction.ACADEMY:
    #         for pos in range(1, len(building_list)):
    #             if t1_tower['y'] > building_list[pos][1]:
    #                 t1_tower['x'], t1_tower['y'] = building_list[pos][0], building_list[pos][1]
    #     elif me.faction == Faction.RENEGADES:
    #         for pos in range(1, len(building_list)):
    #             if t1_tower['x'] > building_list[pos][0]:
    #                 t1_tower['x'], t1_tower['y'] = building_list[pos][0], building_list[pos][1]
    #
    #     print('T1 tower is : x %s, y %s' % (t1_tower['x'], t1_tower['y']))
    #     print('')
    #     return t1_tower

