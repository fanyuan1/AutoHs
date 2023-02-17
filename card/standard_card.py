from card.basic_card import *


# 护甲商贩
class ArmorVendor(MinionNoPoint):
    value = 4
    keep_in_hand_bool = True


# 神圣惩击
class HolySmite(SpellPointOppo):
    wait_time = 2
    # 加个bias,一是包含了消耗的水晶的代价，二是包含了消耗了手牌的代价
    bias = -2

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        best_oppo_index = -1
        best_delta_h = 0
        spell_power = state.my_total_spell_power
        damage = 2 + spell_power

        for oppo_index, oppo_minion in enumerate(state.oppo_minions):
            if not oppo_minion.can_be_pointed_by_spell:
                continue
            temp_delta_h = oppo_minion.delta_h_after_damage(damage)
            if temp_delta_h > best_delta_h:
                best_delta_h = temp_delta_h
                best_oppo_index = oppo_index

        return best_delta_h + cls.bias, best_oppo_index


# 倦怠光波
class WaveOfApathy(SpellNoPoint):
    wait_time = 2
    bias = -4

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        tmp = 0

        for minion in state.oppo_minions:
            tmp += minion.attack - 1

        return tmp + cls.bias,


# 噬骨殴斗者
class BonechewerBrawler(MinionNoPoint):
    value = 5
    keep_in_hand_bool = True


# 暗言术灭
class ShadowWordDeath(SpellPointOppo):
    wait_time = 1.5
    bias = -6

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        best_oppo_index = -1
        best_delta_h = 0

        for oppo_index, oppo_minion in enumerate(state.oppo_minions):
            if oppo_minion.attack < 5:
                continue
            if not oppo_minion.can_be_pointed_by_spell:
                continue

            tmp = oppo_minion.heuristic_val + cls.bias
            if tmp > best_delta_h:
                best_delta_h = tmp
                best_oppo_index = oppo_index

        return best_delta_h, best_oppo_index


# 神圣化身
class Apotheosis(SpellPointMine):
    bias = -6

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        best_delta_h = 0
        best_mine_index = -1

        for my_index, my_minion in enumerate(state.my_minions):
            if not my_minion.can_be_pointed_by_spell:
                continue

            tmp = cls.bias + 3 + my_minion.delta_h_after_buff(3,5)
            if my_minion.can_attack_minion:
                tmp += my_minion.attack / 2
            if tmp > best_delta_h:
                best_delta_h = tmp
                best_mine_index = my_index

        return best_delta_h, best_mine_index


# # 亡首教徒
# class DeathsHeadCultist(MinionNoPoint):
#     value = 1
#     keep_in_hand_bool = True


# 噬灵疫病
class DevouringPlague(SpellNoPoint):
    wait_time = 4
    bias = -4  # 把吸的血直接算进bias

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        curr_h = state.heuristic_value

        delta_h_sum = 0
        sample_times = 5

        for i in range(sample_times):
            tmp_state = state.copy_new_one()
            for j in range(4):
                tmp_state.random_distribute_damage(1, [i for i in range(tmp_state.oppo_minion_num)], [])

            delta_h_sum += tmp_state.heuristic_value - curr_h

        return delta_h_sum / sample_times + cls.bias,


# 狂傲的兽人
class OverconfidentOrc(MinionNoPoint):
    value = 8
    keep_in_hand_bool = True


# 神圣新星
class HolyNova(SpellNoPoint):
    bias = -8

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        return cls.bias + sum([minion.delta_h_after_damage(2)
                               for minion in state.oppo_minions]),


# 狂乱
class Hysteria(SpellPointOppo):
    wait_time = 5
    bias = -9  # 我觉得狂乱应该要能力挽狂澜
    keep_in_hand_bool = False

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        best_delta_h = 0
        best_arg = 0
        sample_times = 10

        if state.oppo_minion_num == 0 or state.oppo_minion_num + state.my_minion_num == 1:
            return 0, -1

        for chosen_index, chosen_minion in enumerate(state.oppo_minions):
            if not chosen_minion.can_be_pointed_by_spell:
                continue

            delta_h_count = 0

            for i in range(sample_times):
                tmp_state = state.copy_new_one()
                tmp_chosen_index = chosen_index

                while True:
                    another_index_list = [j for j in range(tmp_state.oppo_minion_num + tmp_state.my_minion_num)]
                    another_index_list.pop(tmp_chosen_index)
                    if len(another_index_list) == 0:
                        break
                    another_index = another_index_list[random.randint(0, len(another_index_list) - 1)]

                    # print("another index: ", another_index)
                    if another_index >= tmp_state.oppo_minion_num:
                        another_minion = tmp_state.my_minions[another_index - tmp_state.oppo_minion_num]
                        if another_minion.get_damaged(chosen_minion.attack):
                            tmp_state.my_minions.pop(another_index - tmp_state.oppo_minion_num)
                    else:
                        another_minion = tmp_state.oppo_minions[another_index]
                        if another_minion.get_damaged(chosen_minion.attack):
                            tmp_state.oppo_minions.pop(another_index)
                            if another_index < tmp_chosen_index:
                                tmp_chosen_index -= 1

                    if chosen_minion.get_damaged(another_minion.attack):
                        # print("h:", tmp_state.heuristic_value, state.heuristic_value)
                        tmp_state.oppo_minions.pop(tmp_chosen_index)
                        break

                    # print("h:", tmp_state.heuristic_value, state.heuristic_value)

                delta_h_count += tmp_state.heuristic_value - state.heuristic_value

            delta_h_count /= sample_times
            # print("average delta_h:", delta_h_count)
            if delta_h_count > best_delta_h:
                best_delta_h = delta_h_count
                best_arg = chosen_index

        return best_delta_h + cls.bias, best_arg


# 暗言术毁
class ShadowWordRuin(SpellNoPoint):
    bias = -8
    keep_in_hand_bool = False

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        return cls.bias + sum([minion.heuristic_val
                               for minion in state.oppo_minions
                               if minion.attack >= 5]),


# 除奇致胜
class AgainstAllOdds(SpellNoPoint):
    bias = -9
    keep_in_hand_bool = False

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        return cls.bias + \
               sum([minion.heuristic_val
                    for minion in state.oppo_minions
                    if minion.attack % 2 == 1]) - \
               sum([minion.heuristic_val
                    for minion in state.my_minions
                    if minion.attack % 2 == 1]),

# 灵魂之镜
class SoulMirror(SpellNoPoint):
    wait_time = 5
    bias = -16
    keep_in_hand_bool = False

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        copy_number = min(7 - state.my_minion_num, state.oppo_minion_num)
        h_sum = 0
        for i in range(copy_number):
            h_sum += state.oppo_minions[i].heuristic_val

        return h_sum + cls.bias,

# grave strength
class GraveStrength(SpellNoPoint):
    bias = -0.01

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        multiplier = 1
        if state.my_corpses < 5:
            multiplier = 1
        elif state.my_corpses >= 5:
            multiplier = 3
        return cls.bias + state.my_minion_num*multiplier,

# grave strength
class MagicShell(SpellNoPoint):
    bias = -0.01

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        return cls.bias + state.my_minion_num*2.5,

class PlaguedGrain(SpellNoPoint):
    wait_time = 3

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        return 0.1, #use if i have 1 mana left

class TombGuardians(SpellNoPoint):
    wait_time = 3

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        val = 4.5
        if state.my_minion_num >= 7:
            val = -1
        elif state.my_minion_num == 6:
            if state.my_corpses >= 4:
                val = 4.5
        elif state.my_minion_num <=5:
            if state.my_corpses >= 4:
                val = 12
            else:
                val = 4.5
        if state.my_hero.health <= 10:
            val *= 1.5
        return val,

# astalor based on 精灵弓箭手
class Astalor(MinionPointOppo):
    @classmethod
    def utilize_delta_h_and_arg(cls, state, hand_card_index):

        if state.my_total_mana < 5:
            return 4, state.my_minion_num, -1
        # 不能让她下去点脸, 除非对面快死了

        best_h = 4 + state.oppo_hero.delta_h_after_damage(2)
        best_oppo_index = -1

        for oppo_index, oppo_minion in enumerate(state.oppo_minions):
            if not oppo_minion.can_be_pointed_by_minion:
                continue

            delta_h = 4 + oppo_minion.delta_h_after_damage(2) #most likely will use on turn 5
            if delta_h > best_h:
                best_h = delta_h
                best_oppo_index = oppo_index

        return best_h, state.my_minion_num, best_oppo_index

class Astalor1(MinionNoPoint):

    @classmethod
    def utilize_delta_h_and_arg(cls, state, hand_card_index):
            if state.my_total_mana < 8:
                return 7,
            else:
                return 12, #5 drop with upside

class Astalor2(MinionNoPoint):

    @classmethod
    def utilize_delta_h_and_arg(cls, state, hand_card_index):
            if state.my_total_mana < 10:
                return 8, #slightly better than 3 drop rather play 4 drop at less than 10 mana, save for later
            else:
                return 25, #mega busted at 10 mana

# Boneflinger based on 精灵弓箭手 doesnt know if undead minion died
class BoneFlinger(MinionPointOppo):
    @classmethod
    def utilize_delta_h_and_arg(cls, state, hand_card_index):
        # how do i check if this minion is active??
        best_h = 5 + state.oppo_hero.delta_h_after_damage(2)
        best_oppo_index = -1

        for oppo_index, oppo_minion in enumerate(state.oppo_minions):
            if not oppo_minion.can_be_pointed_by_minion:
                continue

            delta_h = 5 + oppo_minion.delta_h_after_damage(2)
            if delta_h > best_h:
                best_h = delta_h
                best_oppo_index = oppo_index

        return best_h, state.my_minion_num, best_oppo_index

# plaguestrike
class PlagueStrike(SpellPointOppo):
    wait_time = 2
    bias = 1
    #killed off minion hval*OPPO Factor, at least 5 hval

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        if state.my_minion_num >= 7:
            bias_local = -7
        else:
            bias_local = cls.bias
        best_oppo_index = -1
        best_delta_h = 0
        spell_power = state.my_total_spell_power
        damage = 3 + spell_power

        for oppo_index, oppo_minion in enumerate(state.oppo_minions):
            if not oppo_minion.can_be_pointed_by_spell:
                continue
            temp_delta_h = oppo_minion.delta_h_after_damage(damage) + bias_local ##classic dmg
            if temp_delta_h > best_delta_h:
                best_delta_h = temp_delta_h
                best_oppo_index = oppo_index

        return best_delta_h, best_oppo_index

# VrykulNecrolyte based on 大地之环先知
class VrykulNecrolyte(MinionPointMine):
    @classmethod
    def utilize_delta_h_and_arg(cls, state, hand_card_index):

        best_h = 0.01
        best_my_index = -1

        for my_index, my_minion in enumerate(state.my_minions):
            delta_h = 5 + 1/my_minion.heuristic_val
            if delta_h > best_h:
                best_h = delta_h
                best_my_index = my_index

        return best_h, state.my_minion_num, best_my_index

class PriestDeceased(MinionNoPoint):
    #discourages play if not infused
    value = 0.01
class PriestDeceasedt(MinionNoPoint):
    value = 13 #better than the 6 drop i will run...

class NerubianSwarmguard(MinionNoPoint):
    @classmethod
    def utilize_delta_h_and_arg(cls, state, hand_card_index):
        if state.my_minion_num <= 4:
            return 12, #standard 4 drop
        elif state.my_minion_num == 5:
            if state.my_hand_card_num <= 2:
                return 12,
            else:
                return 4, #let's hold this card, play 2 2 drops instead
        elif state.my_minion_num == 6:
            return 4,
        else:
            return 12,

class Genn(MinionNoPoint):
    @classmethod
    def utilize_delta_h_and_arg(cls, state, hand_card_index):
        if state.my_minion_num == 6:
            return 11, #i rather play astalor on 8 mana instead
        elif state.my_hand_card_num >= 3:
            return 4, #rather play more minions
        else:
            return 9, #some better 4-5 drops i will play instead,..

class DarkTransformation(SpellPointMine):

    bias = 10

    @classmethod
    def best_h_and_arg(cls, state, hand_card_index):
        best_delta_h = -1
        best_mine_index = -1
        
        for my_index, my_minion in enumerate(state.my_minions):
            if not my_minion.can_be_pointed_by_spell:
                continue
            if not my_minion.race == 'UNDEAD':
                continue
            tmp = cls.bias - my_minion.heuristic_val #breakeven if minion is 2/3 or 3/2

            #two drop 2, three drop 2.5, four drop 3
            if tmp >= best_delta_h: #right most minion gets the buff, more like to target hp
                best_delta_h = tmp
                best_mine_index = my_index
        return best_delta_h, best_mine_index

class ManaFeederHP(MinionNoPoint):
    @classmethod
    def utilize_delta_h_and_arg(cls, state, hand_card_index):
        if state.my_hero_power.exhausted:
            return 7, #equivalent to 3 drop
        else:
            return 3, #save if there are other 2 drops

class BoneDigger(MinionNoPoint):
    @classmethod
    def utilize_delta_h_and_arg(cls, state, hand_card_index):
        if state.my_corpses >= 1:
            return 7, #equivalent to 3 drop
        else:
            return 4,

class BattlefieldNecromancer(MinionNoPoint):
    @classmethod
    def utilize_delta_h_and_arg(cls, state, hand_card_index):
        if state.my_corpses >= 1:
            return 8, #slightly better than 3 drop
        else:
            return 4,