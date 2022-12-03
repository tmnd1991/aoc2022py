ROCK=1
PAPER=2
SCISSORS=3

def winner(p1,p2):
    if (p1 == p2):
        return 0
    elif (p1 == ROCK and p2 == PAPER):
        return 1
    elif (p1 == ROCK and p2 == SCISSORS):
        return -1
    elif (p1 == PAPER and p2 == SCISSORS):
        return 1
    else:
        return -winner(p2,p1)

def pointsForMe(you,me):
    who_win=winner(you,me)
    if who_win == 0:
        return me + 3
    elif who_win == -1:
        return me
    else:
        return me + 6

def parseLine1(line):

    you = None
    me = None
    splitted=line.split(' ',2)
    if (splitted[0] == 'A'):
        you=ROCK
    elif (splitted[0] == 'B'):
        you=PAPER
    elif (splitted[0] == 'C'):
        you=SCISSORS

    if (splitted[1].strip() == 'X'):
        me=ROCK
    elif (splitted[1].strip() == 'Y'):
        me=PAPER
    elif (splitted[1].strip() == 'Z'):
        me=SCISSORS
    
    return (you, me)

def toLose(you):
    if you == PAPER:
        return ROCK
    elif you == SCISSORS:
        return PAPER
    else: return SCISSORS

def toWin(you):
    if you == PAPER:
        return SCISSORS
    elif you == SCISSORS:
        return ROCK
    else: return PAPER

def toDraw(you):
    return you


def parseLine2(line):

    you = None
    me = None
    splitted=line.split(' ',2)
    if (splitted[0] == 'A'):
        you=ROCK
    elif (splitted[0] == 'B'):
        you=PAPER
    elif (splitted[0] == 'C'):
        you=SCISSORS

    if (splitted[1].strip() == 'X'):
        me=toLose(you)
    elif (splitted[1].strip() == 'Y'):
        me=toDraw(you)
    elif (splitted[1].strip() == 'Z'):
        me=toWin(you)
    
    return (you, me)

def problem1():
    with open('input', 'r') as file:
        lines = file.readlines()
        sum=0
        for line in lines:
            you, me = parseLine1(line)
            sum = sum + pointsForMe(you, me)
    return sum

def problem2():
    with open('input', 'r') as file:
        lines = file.readlines()
        sum=0
        for line in lines:
            you, me = parseLine2(line)
            sum = sum + pointsForMe(you, me)
    return sum

print(problem1())
print(problem2())