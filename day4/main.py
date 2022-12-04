from dataclasses import dataclass

@dataclass(frozen = True)
class Range:
    start: int
    end: int
    def __post_init__(self):
        assert self.start <= self.end
            
def overlap(r1: Range, r2: Range) -> bool:
    return (r1.start <= r2.end) and (r1.end >= r2.start)

def fullyContain(r1: Range, r2: Range) -> bool:
    return (r1.start <= r2.start and r1.end >=  r2.end) or \
        (r2.start <= r1.start and r2.end >=  r1.end)
    
def parseRange(s: str) -> Range:
    splitted = s.split('-', 2)
    return Range(int(splitted[0]), int(splitted[1]))

def parseLine(s: str) -> tuple[Range, Range]:
    splitted = s.split(',', 2)
    return (parseRange(splitted[0]), parseRange(splitted[1]))

def problem1_gen():
    with(open('input','r')) as file:
        for line in file.read().splitlines():
            (r1, r2) = parseLine(line)
            if fullyContain(r1,r2):
                yield 1

def problem2_gen():
    with(open('input','r')) as file:
        for line in file.read().splitlines():
            (r1, r2) = parseLine(line)
            if overlap(r1,r2):
                yield 1

def problem1():
    return sum(problem1_gen())

def problem2():
    return sum(problem2_gen())

print(problem1())
print(problem2())

