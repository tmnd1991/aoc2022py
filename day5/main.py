import re
from dataclasses import dataclass
from collections import deque

@dataclass
class Stacks:
    lines: list[deque[str]]

@dataclass
class Move:
    amount: int
    f: int
    t: int

def doMove(stacks: Stacks, move: Move) -> Stacks:
    for i in range(move.amount):
        stacks.lines[move.t - 1].appendleft(stacks.lines[move.f - 1].popleft())
    return stacks

def doMove2(stacks: Stacks, move: Move) -> Stacks:
    toMove = deque([])
    for i in range(move.amount):
        toMove.appendleft(stacks.lines[move.f - 1].popleft())
    stacks.lines[move.t - 1].extendleft(toMove)
    return stacks

def parseLine(line: str, stacks: Stacks) -> Stacks:
    for i in range(0, len(line), 4):
        char=line[i+1].strip()
        if char:
            stacks.lines[int(i/4)].append(char)
    return stacks

def problem1():
    with(open('input','r')) as file:
        initialStackLines=[]
        lines = file.read().splitlines()
        for line in lines:
            if line.strip():
                initialStackLines.append(line)
            else:
                break
        size=int(re.split('\s+',initialStackLines[-1].strip())[-1])
        initialStacks=[]
        for i in range(size):
            initialStacks.append(deque([]))
        stacks=Stacks(initialStacks)
        for line in initialStackLines[:-1]:
            stacks=parseLine(line, stacks)
        for line in lines:
            m = re.match(r"move (\d+) from (\d+) to (\d+)", line)
            if m:
                move = Move(int(m.group(1)), int(m.group(2)), int(m.group(3)))
                stacks=doMove(stacks, move)
        for crate in stacks.lines:
            yield crate[0]

def problem2():
    with(open('input','r')) as file:
        initialStackLines=[]
        lines = file.read().splitlines()
        for line in lines:
            if line.strip():
                initialStackLines.append(line)
            else:
                break
        size=int(re.split('\s+',initialStackLines[-1].strip())[-1])
        initialStacks=[]
        for i in range(size):
            initialStacks.append(deque([]))
        stacks=Stacks(initialStacks)
        for line in initialStackLines[:-1]:
            stacks=parseLine(line, stacks)
        for line in lines:
            m = re.match(r"move (\d+) from (\d+) to (\d+)", line)
            if m:
                move = Move(int(m.group(1)), int(m.group(2)), int(m.group(3)))
                stacks=doMove2(stacks, move)
        for crate in stacks.lines:
            yield crate[0]

print("".join(list(problem1())))
print("".join(list(problem2())))