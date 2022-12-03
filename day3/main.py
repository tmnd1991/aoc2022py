def range_char(start, stop):
    return (chr(n) for n in range(ord(start), ord(stop) + 1))

def chain(*iterables):
    for it in iterables:
        for element in it:
            yield element
priorities = {c: i+1 for i, c in enumerate(list(chain(range_char('a', 'z'), range_char('A','Z'))))}
def problem1():
    return sum(oneline_problem1())

def oneline_problem1(): #7581
    with(open('input','r')) as file:
        for line in file.read().splitlines():
            l = len(line)
            compartiment_1 = line[:int(l/2)]
            compartiment_2 = line[int(l/2):]
            weights = map(lambda e: priorities[e], list(set(compartiment_1).intersection(set(compartiment_2))))
            yield sum(weights)

def problem2():
    return sum(oneline_problem2())

def oneline_problem2(): #2525
    total = 0
    with(open('input','r')) as file:
        lines = file.read().splitlines()
        while lines:
            e1,e2,e3 = set(lines.pop(0)), set(lines.pop(0)), set(lines.pop(0))
            badge = e1.intersection(e2).intersection(e3).pop()
            yield priorities[badge]

print(problem1())
print(problem2())
