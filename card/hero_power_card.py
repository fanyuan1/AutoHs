import click
from card.basic_card import *


class TotemicCall(HeroPowerCard):
    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        if not state.my_hero_power.exhausted \
                and state.my_minion_num < 7:
            return 3,
        else:
            return 0,

    @classmethod
    def use_with_arg(cls, state, card_index, *args):
        click.use_skill_no_point()
        time.sleep(1)


class LesserHeal(HeroPowerCard):
    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        if state.my_hero_power.exhausted:
            return 0,
        best_index = -1
        best_delta_h = state.my_hero.delta_h_after_heal(2)

        for my_index, my_minion in enumerate(state.my_minions):
            delta_h = my_minion.delta_h_after_heal(2)
            if delta_h > best_delta_h:
                best_delta_h = delta_h
                best_index = my_index

        return best_delta_h, best_index

    @classmethod
    def use_with_arg(cls, state, card_index, *args):
        click.use_skill_point_mine(args[0], state.my_minion_num)
        time.sleep(1)

class BallistaShot(HeroPowerCard):
    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        return 2,-1

    @classmethod
    def use_with_arg(cls, state, card_index, *args):
        click.use_skill_no_point()
        time.sleep(1)

class DemonClaws(HeroPowerCard):
    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        return 1,-1

    @classmethod
    def use_with_arg(cls, state, card_index, *args):
        print('[恶魔之爪][use_with_arg]')
        click.use_skill_point_oppo(args[0], len(state.oppo_minions), state.oppo_locations_pos)
        time.sleep(1)

class Fireblast(HeroPowerCard):
    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        print('使用[火焰冲击]')
        if state.my_hero_power.exhausted:
            return 0
        best_index = -2
        best_delta_h = 0

        for my_index, enemy_minion in enumerate(state.oppo_minions):
            delta_h = enemy_minion.delta_h_after_damage(1)
            if delta_h > best_delta_h:
                best_delta_h = delta_h
                best_index = my_index


        return best_delta_h, best_index

    @classmethod
    def use_with_arg(cls, state, card_index, *args):
        print('[火焰冲击][use_with_arg]')
        click.use_skill_point_oppo(args[0], len(state.oppo_minions), state.oppo_locations_pos)
        time.sleep(1)

class GhoulCharge(HeroPowerCard):
    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        if state.my_minion_num >= 7:
            return -1,-1
        else:
            return 3,-1

    @classmethod
    def use_with_arg(cls, state, card_index, *args):
        click.use_skill_no_point()
        time.sleep(1)