import sys
from collections import defaultdict
from copy import copy, deepcopy

board = []
players = []
num_elves = 0

class Player:
    def __init__(self, type, x, y, health, attack):
        self.type = type
        self.x = x
        self.y = y
        self.health = health
        self.attack = attack

for line in open(sys.argv[1]):
    row = []
    for c in line.strip():
        row.append(c)
    board.append(row)

for j in range(len(board)):
    for i in range(len(board[0])):
        if board[i][j] == 'G':
            players.append(Player('G',i,j,200,3))
        elif board[i][j] == 'E':
            players.append(Player('E',i,j,200,3))
            num_elves += 1

initial_board = deepcopy(board)
initial_players = deepcopy(players)

def isNotFinished():
    global players
    elves = 0
    goblins = 0
    for player in players:
        if player.type == 'E':
            elves = 1
        else:
            goblins = 1
    if elves and goblins:
        return True
    return False

def print_player(player):
    print(player.type, player.x, player.y, player.health)

def arrange_players():
    global players
    coords = []
    for player in players:
        coords.append((player.x,player.y))
    coords.sort()
    arranged = []
    for coord in coords:
        for player in players:
            if (player.x,player.y) == coord:
                arranged.append(player)
    players = arranged

def determineMove(player):
    global players
    range = []
    range.append((player.x-1,player.y))
    range.append((player.x,player.y-1))
    range.append((player.x,player.y+1))
    range.append((player.x+1,player.y))
    return_range = []
    for person in players:
        if person.type != player.type and (person.x,person.y) in range:
            return_range.append((person.x,person.y))
    if len(return_range):
        return 1, return_range
    for coord in range:
        if board[coord[0]][coord[1]] == '.':
            return_range.append(coord)
    return 0, return_range

def performAttack(player, range):
    global players
    global board
    possible_attacks = []
    for person in players:
        if (person.x,person.y) in range:
            possible_attacks.append(person)

    to_attack = Player('G',0,0,201,3)
    if len(possible_attacks) == 1:
        to_attack = possible_attacks[0]
    else:
        for person in possible_attacks:
            if person.health < to_attack.health:
                to_attack = person

    to_attack.health -= player.attack
    if to_attack.health < 1:
        board[to_attack.x][to_attack.y] = '.'
        players.remove(to_attack)

def movePlayer(player, range):
    others_range = []
    for person in players:
        if person.type != player.type:
            others_range.append((person.x-1,person.y))
            others_range.append((person.x,person.y-1))
            others_range.append((person.x,person.y+1))
            others_range.append((person.x+1,person.y))

    new = []
    for coord in others_range:
        x = coord[0]
        y = coord[1]
        if board[x][y] == '.':
            new.append(coord)
    others_range = new
    if not len(others_range):
        return 0
    lowest_dist = 999999
    destinations = []
    for coord in range:
        dist, dest = bfs(coord,others_range)
        if dist == lowest_dist:
            destinations += dest
        if dist < lowest_dist:
            lowest_dist = dist
            destinations = []
            destinations += dest
    if not len(destinations):
        return
    target = [sorted(destinations)[0]]
    lowest_dist = 999999
    best_coord = []
    for coord in range:
        dist, dest = bfs(coord,target)
        if dist == lowest_dist:
            best_coord.append(coord)
        if dist < lowest_dist:
            lowest_dist = dist
            best_coord = []
            best_coord.append(coord)
    final = sorted(best_coord)[0]
    board[player.x][player.y] = '.'
    player.x = final[0]
    player.y = final[1]
    board[player.x][player.y] = player.type

def bfs(coord, destinations):
    global board
    if coord in destinations:
        return 0, [coord]
    seen = [coord]
    to_visit = [coord]
    success = []
    i = 0
    while not len(success):
        i += 1
        next_visit = []
        for coord in to_visit:
            x = coord[0]
            y = coord[1]
            for x2,y2 in ((x-1,y), (x,y-1), (x,y+1), (x+1,y)):
                if (x2,y2) in destinations:
                    success.append((x2,y2))
                if (x2,y2) not in seen and board[x2][y2] == '.':
                    seen.append((x2,y2))
                    next_visit.append((x2,y2))
        if not len(next_visit):
            return 99999,[]
        to_visit = next_visit
    return i, success

def print_board():
    for line in board:
        c = ""
        for x in line:
            c += x
        print(c)

def doTurn():
    global turns
    global players
    turns += 1
    arrange_players()
    curr = copy(players)
    for player in curr:
        if player in players:
            if not isNotFinished():
                return
            move, range = determineMove(player)

            if move == 1:
                performAttack(player, range)
            else:
                movePlayer(player, range)
                move, range = determineMove(player)
                if move == 1:
                    performAttack(player,range)

#part 1
turns = 0
while isNotFinished():
    doTurn()

def determineOutcome():
    global turns
    global players
    turns -= 1
    health_left = 0
    for player in players:
        health_left += player.health
    print(turns * health_left)

determineOutcome()

#part2
def part2NotComplete():
    global players
    remaining = []
    for player in players:
        if player.type == 'G':
            return True
        else:
            remaining.append(player)
    return not len(remaining) == num_elves

while part2NotComplete():
    turns = 0
    players = deepcopy(initial_players)
    board = deepcopy(initial_board)
    for player in initial_players:
        if player.type == 'E':
            player.attack += 1
    while isNotFinished():
        doTurn()

determineOutcome()
