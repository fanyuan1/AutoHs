from card.basic_card import *


# 闪电箭
class LightingBolt(SpellPointOppo):
    spell_type = SPELL_POINT_OPPO
    bias = -2

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        spell_power = state.my_total_spell_power
        damage = 3 + spell_power
        best_delta_h = state.oppo_hero.delta_h_after_damage(damage)
        best_oppo_index = -1

        for oppo_index, oppo_minion in enumerate(state.oppo_minions):
            if not oppo_minion.can_be_pointed_by_spell:
                continue
            delta_h = oppo_minion.delta_h_after_damage(damage)
            if best_delta_h < delta_h:
                best_delta_h = delta_h
                best_oppo_index = oppo_index

        return best_delta_h + cls.bias, best_oppo_index,


# 呱
class Hex(SpellPointOppo):
    bias = -5
    keep_in_hand_bool = False

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        best_delta_h = 0
        best_oppo_index = -1

        for oppo_index, oppo_minion in enumerate(state.oppo_minions):
            if not oppo_minion.can_be_pointed_by_spell:
                continue

            delta_h = oppo_minion.heuristic_val - 1

            if best_delta_h < delta_h:
                best_delta_h = delta_h
                best_oppo_index = oppo_index

        return best_delta_h + cls.bias, best_oppo_index,


# 闪电风暴
class LightningStorm(SpellNoPoint):
    bias = -8 #kills around 3-4 minions

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        h_sum = 0
        spell_power = state.my_total_spell_power

        for oppo_minion in state.oppo_minions:
            h_sum += (oppo_minion.delta_h_after_damage(2 + spell_power) +
                      oppo_minion.delta_h_after_damage(3 + spell_power)) / 2

        return h_sum + cls.bias,


# TC130
class MindControlTech(MinionNoPoint):
    value = 0.1 #between 1 drop and 2 drop, 
    keep_in_hand_bool = False

    @classmethod
    def utilize_delta_h_and_arg(cls, state, hand_card_index):
        if state.oppo_minion_num < 4:
            return cls.value, state.my_minion_num
        else:
            h_sum = sum([minion.heuristic_val for minion in state.oppo_minions])
            h_sum /= state.oppo_minion_num
            return cls.value + h_sum + 6,


# 野性狼魂
class FeralSpirit(SpellNoPoint):
    value = 8 #between 3 and 4 drop

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        if state.my_minion_num >= 6:
            return 3, 0
        else:
            return cls.value, 0


# 碧蓝幼龙
class AzureDrake(MinionNoPoint):
    value = 11 ## 4+4+2+1
    keep_in_hand_bool = False


# 奥妮克希亚
class Onyxia(MinionNoPoint):
    value = 20
    keep_in_hand_bool = False


# 火元素
class FireElemental(MinionPointOppo):
    keep_in_hand_bool = False

    @classmethod
    def utilize_delta_h_and_arg(cls, state, hand_card_index):
        best_h = 11 + state.oppo_hero.delta_h_after_damage(3)
        best_oppo_index = -1

        for oppo_index, oppo_minion in enumerate(state.oppo_minions):
            if not oppo_minion.can_be_pointed_by_minion:
                continue

            delta_h = 11 + oppo_minion.delta_h_after_damage(3)
            if delta_h > best_h:
                best_h = delta_h
                best_oppo_index = oppo_index

        return best_h, state.my_minion_num, best_oppo_index


# 精灵弓箭手
class ElvenArcher(MinionPointOppo):
    @classmethod
    def utilize_delta_h_and_arg(cls, state, hand_card_index):
        # 不能让她下去点脸, 除非对面快死了
        best_h = 1 + state.oppo_hero.delta_h_after_damage(1)
        best_oppo_index = -1

        for oppo_index, oppo_minion in enumerate(state.oppo_minions):
            if not oppo_minion.can_be_pointed_by_minion:
                continue

            delta_h = 1 + oppo_minion.delta_h_after_damage(1)
            if delta_h > best_h:
                best_h = delta_h
                best_oppo_index = oppo_index

        return best_h, state.my_minion_num, best_oppo_index


# 大地之环先知
class EarthenRingFarseer(MinionPointMine):
    @classmethod
    def utilize_delta_h_and_arg(cls, state, hand_card_index):
        best_h = 6 + state.my_hero.delta_h_after_heal(3)
        if state.my_hero.health <= 5:
            best_h += 3
        best_my_index = -1

        for my_index, my_minion in enumerate(state.my_minions):
            delta_h = 6 + my_minion.delta_h_after_heal(3)
            if delta_h > best_h:
                best_h = delta_h
                best_my_index = my_index

        return best_h, state.my_minion_num, best_my_index


# 憎恶
class Abomination(MinionNoPoint):
    keep_in_hand_bool = True

    @classmethod
    def utilize_delta_h_and_arg(cls, state, hand_card_index):
        h_sum = 8
        for oppo_minion in state.oppo_minions:
            h_sum += oppo_minion.delta_h_after_damage(2)
        for my_minion in state.my_minions:
            h_sum -= my_minion.delta_h_after_damage(2)
        h_sum += state.oppo_hero.delta_h_after_damage(2)
        h_sum -= state.my_hero.delta_h_after_damage(2)

        return h_sum,


# 狂奔科多兽
class StampedingKodo(MinionNoPoint):
    keep_in_hand_bool = False

    @classmethod
    def utilize_delta_h_and_arg(cls, state, hand_card_index):
        h_sum = 8
        temp_sum = 0
        temp_count = 0

        for oppo_minion in state.oppo_minions:
            if oppo_minion.attack <= 2:
                temp_sum += oppo_minion.heuristic_val
                temp_count += 1
        if temp_count > 0:
            h_sum += temp_sum / temp_count

        return h_sum,


# 血骑士
class BloodKnight(MinionNoPoint):
    keep_in_hand_bool = False

    @classmethod
    def utilize_delta_h_and_arg(cls, state, hand_card_index):
        h_sum = 4 # can consider keeping

        for oppo_minion in state.oppo_minions:
            if oppo_minion.divine_shield:
                h_sum += oppo_minion.attack + 6
        for my_minion in state.my_minions:
            if my_minion.divine_shield:
                h_sum += -my_minion.attack + 6

        return h_sum,


# 末日
class DoomSayer(MinionNoPoint):
    keep_in_hand_bool = True

    @classmethod
    def utilize_delta_h_and_arg(cls, state, hand_card_index):
        # 一费别跳末日
        if state.my_total_mana == 1:
            return 0,

        # 二三费压末日就完事了
        if state.my_total_mana <= 3:
            return 1000,

        # 优势不能上末日
        if state.my_heuristic_value >= state.oppo_heuristic_value:
            return 0,

        oppo_attack_sum = 0
        for oppo_minion in state.oppo_minions:
            oppo_attack_sum += oppo_minion.attack

        if oppo_attack_sum >= 7:
            # 当个嘲讽也好
            return 1,
        else:
            return state.oppo_heuristic_value - state.my_heuristic_value,


class StormforgedAxe(WeaponCard):
    keep_in_hand_bool = True
    value = 1.5

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        # 不要已经有刀了再顶刀
        if state.my_weapon is not None:
            return 0,
        if state.my_total_mana == 2:
            for oppo_minion in state.touchable_oppo_minions:
                # 如果能提起刀解了, 那太好了
                if oppo_minion.health <= 2 and \
                        not oppo_minion.divine_shield:
                    return 2000,

        return cls.value,


# 神圣惩击
class HolySmiteClassic(SpellPointOppo):
    wait_time = 2
    bias = -2

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        spell_power = state.my_total_spell_power
        damage = 2 + spell_power
        best_delta_h = state.oppo_hero.delta_h_after_damage(damage)
        best_oppo_index = -1

        for oppo_index, oppo_minion in enumerate(state.oppo_minions):
            if not oppo_minion.can_be_pointed_by_spell:
                continue
            temp_delta_h = oppo_minion.delta_h_after_damage(damage)
            if temp_delta_h > best_delta_h:
                best_delta_h = temp_delta_h
                best_oppo_index = oppo_index

        return best_delta_h + cls.bias, best_oppo_index

# 神圣新星
class HolyNovaClassic(SpellNoPoint):
    bias = -6

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        spell_power = state.my_total_spell_power
        damage = 2 + spell_power
        damage = 2
        return cls.bias + sum([minion.delta_h_after_damage(damage)
                               for minion in state.oppo_minions])\
                        + sum([minion.delta_h_after_heal(2)
                               for minion in state.my_minions])\
                        + state.my_hero.delta_h_after_heal(2)\
                        + state.oppo_hero.delta_h_after_damage(damage),

## not working properly
class ShadowWordPain(SpellPointOppo):

    wait_time = 1.5
    bias = 0

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        best_oppo_index = -1
        best_delta_h = 0

        for oppo_index, oppo_minion in enumerate(state.oppo_minions):
            if oppo_minion.attack > 3:
                continue
            if not oppo_minion.can_be_pointed_by_spell:
                continue

            tmp = oppo_minion.heuristic_val + cls.bias
            if tmp > best_delta_h:
                best_delta_h = tmp
                best_oppo_index = oppo_index

        return best_delta_h, best_oppo_index

class PowerWordShield(SpellPointMine):
    
    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):

        try:
            if state.my_minion_num == 0:
                return -9999,
            best_delta_h = 0
            best_mine_index = -1

            for my_index, my_minion in enumerate(state.my_minions):
                if not my_minion.can_be_pointed_by_spell:
                    continue
                tmp = 2 + my_minion.delta_h_after_buff(0,2)
                if tmp > best_delta_h:
                    best_delta_h = tmp
                    best_mine_index = my_index

            return best_delta_h, best_mine_index
        except:
            return -9999,

class Banana(SpellPointMine):
    
    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):

        try:
            if state.my_minion_num == 0:
                return -9999,
            best_delta_h = 0
            best_mine_index = -1

            for my_index, my_minion in enumerate(state.my_minions):
                if not my_minion.can_be_pointed_by_spell:
                    continue
                tmp = my_minion.delta_h_after_buff(1,1)
                if tmp > best_delta_h:
                    best_delta_h = tmp
                    best_mine_index = my_index

            return best_delta_h, best_mine_index
        except:
            return -9999,

class DireWolfAlpha(MinionNoPoint):

    @classmethod
    def utilize_delta_h_and_arg(cls, state, hand_card_index):
        if state.my_minion_num == 0:
            return 2.5, #worse than 1 drop better than hp
        elif state.my_minion_num == 1:
            return 5,
        elif state.my_minion_num >= 2:
            return 6, int(state.my_minion_num/2)

class Argus(MinionNoPoint):

    @classmethod
    def utilize_delta_h_and_arg(cls, state, hand_card_index):
        if state.my_minion_num == 0:
            return 1.9, #worse than 1 drop better than hp
        elif state.my_minion_num == 1:
            return 7,
        elif state.my_minion_num >= 2:
            return 9, int(state.my_minion_num/2)

class FlameImp(MinionNoPoint):

    @classmethod
    def utilize_delta_h_and_arg(cls, state, hand_card_index):
        return 5 + state.my_hero.delta_h_after_damage(3) * 0.1,

class ShatteredSunCleric(MinionPointMine):
    @classmethod
    def utilize_delta_h_and_arg(cls, state, hand_card_index):
        if state.my_minion_num == 0:
            return 2.5, state.my_minion_num, -1 #worse than 1 drop
        
        best_delta_h = 0
        best_mine_index = -1

        for my_index, my_minion in enumerate(state.my_minions):
            delta_h = my_minion.delta_h_after_buff(1,1)
            if delta_h > best_delta_h:
                best_delta_h = delta_h
                best_my_index = my_index

        return best_delta_h + 5, state.my_minion_num, best_my_index

class SoulFire(SpellPointOppo):
    wait_time = 2
    bias = -3
    keep_in_hand_bool = False

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        adj = 0
        if state.my_hand_card_num >= 2:
            adj = -3

        spell_power = state.my_total_spell_power
        damage = 4 + spell_power
        best_delta_h = state.oppo_hero.delta_h_after_damage(damage)
        best_oppo_index = -1

        for oppo_index, oppo_minion in enumerate(state.oppo_minions):
            if not oppo_minion.can_be_pointed_by_spell:
                continue
            temp_delta_h = oppo_minion.delta_h_after_damage(damage)
            if temp_delta_h > best_delta_h:
                best_delta_h = temp_delta_h
                best_oppo_index = oppo_index

        return best_delta_h + cls.bias + adj, best_oppo_index

