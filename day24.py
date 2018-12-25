import sys
import re
from copy import deepcopy

def print_group(group):
    print(group.type, group.units, group.health, group.immunities, group.weaknesses, group.attack_damage, group.attack_type,group.initiative)

class Group:
    def __init__(self,type,units,health,immunities,weaknesses,attack_damage,attack_type,initiative):
        self.type = type
        self.units = units
        self.health = health
        self.immunities = immunities
        self.weaknesses = weaknesses
        self.attack_damage = attack_damage
        self.attack_type = attack_type
        self.initiative = initiative

def parse_input():
    groups = []
    curr_type = "immune"
    for line in open(sys.argv[1]):
        if line == "\n":
            continue
        if "Immune" in line:
            continue
        if "Infection" in line:
            curr_type = "infection"
            continue
        nums = [int(s) for s in re.findall(r'\d+', line)]
        attack_type = re.findall(r'(\w*) damage', line)[0]
        immunities = []
        weaknesses = []
        if '(' in line:
            weak_and_immune = line.split('(')[1].split(')')[0]
            immune = ""
            weak = ""
            if ';' in weak_and_immune:
                fields = weak_and_immune.split(';')
                if "immune" in fields[0]:
                    immune = fields[0].split('to ')[1]
                    weak = fields[1].split('to ')[1]
                else:
                    immune = fields[1].split('to ')[1]
                    weak = fields[0].split('to ')[1]
            else:
                if "immune" in weak_and_immune:
                    immune = weak_and_immune.split('to ')[1]
                else:
                    weak = weak_and_immune.split('to ')[1]
            if immune:
                immunities = immune.split(', ')
            if weak:
                weaknesses = weak.split(', ')
        groups.append(Group(curr_type,nums[0],nums[1],immunities,weaknesses, nums[2], attack_type,nums[3]))
    return groups

def orderGroups(groups):
    effective_powers = {}
    for group in groups:
        eff_pwr = group.units * group.attack_damage
        effective_powers[eff_pwr,group.initiative] = group
    sorted_groups = []
    for key in sorted(effective_powers.keys(), reverse=True):
        sorted_groups.append(effective_powers[key])
    return sorted_groups

def findAttack(attacking, groups, being_attacked):
    best_group = 0
    highest_dmg = 0
    for group in groups:
        if group.type != attacking.type and group not in being_attacked:
            anticipated_damage = attacking.units * attacking.attack_damage
            if attacking.attack_type in group.immunities:
                continue
            elif attacking.attack_type in group.weaknesses:
                anticipated_damage *= 2
            if anticipated_damage > highest_dmg:
                highest_dmg = anticipated_damage
                best_group = group
            elif anticipated_damage and anticipated_damage == highest_dmg:
                eff1 = best_group.units * best_group.attack_damage
                eff2 = group.units * group.attack_damage
                if eff1 == eff2:
                    init1 = best_group.initiative
                    init2 = group.initiative
                    if init2 > init1:
                        best_group = group
                elif eff2 > eff1:
                    best_group = group
    return best_group

def performAttack(group, attacked):
    anticipated_damage = group.units * group.attack_damage
    if group.attack_type in attacked.immunities:
        return
    elif group.attack_type in attacked.weaknesses:
        anticipated_damage *= 2
    num_killed = anticipated_damage//attacked.health
    attacked.units -= num_killed
    if attacked.units < 1:
        return 1
    return 0

def keepGoing(groups):
    immune = 0
    infection = 0
    for group in groups:
        if group.type == 'immune':
            immune += 1
        else:
            infection += 1
    if immune == 0 or infection == 0:
        return 1
    return 0


def do_game(groups):
    while 1:
        ordered_groups = orderGroups(groups)
        being_attacked = []
        attacks = {}
        for group in ordered_groups:
            attacked = findAttack(group, groups, being_attacked)
            if attacked:
                attacks[group.initiative,group] = attacked
                being_attacked.append(attacked)
        for group in sorted(attacks.keys(),reverse=True):
            if group[1] in groups:
                killed = performAttack(group[1], attacks[group])
                if killed:
                    groups.remove(attacks[group])
        stop = keepGoing(groups)
        if stop:
            return groups

groups = parse_input()
part2_groups = deepcopy(groups)
final = do_game(groups)

remaining_units = 0
for group in final:
    remaining_units += group.units
print(remaining_units)

#part2
boost = 45
while 1:
    boost += 1
    groups = deepcopy(part2_groups)
    for group in groups:
        if group.type == "immune":
            group.attack_damage += boost
    final = do_game(groups)
    remaining_units = 0
    finished = 1
    for group in final:
        if group.type == "infection":
            finished = 0
        else:
            remaining_units += group.units
    if finished:
        print(remaining_units)
        break
