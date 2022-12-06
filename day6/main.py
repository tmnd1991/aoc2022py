def sliding_window(elements, window_size):
    if len(elements) <= window_size:
        yield elements
    for i in range(len(elements)):
        if len(elements) >= i+window_size:
            yield elements[i:i+window_size]

def problem1():
    with(open('input','r')) as file:
        for i,w in enumerate(sliding_window(file.read(),4)):
            if len(set(w)) == 4:
                return i + 4
def problem2():
    with(open('input','r')) as file:
        for i,w in enumerate(sliding_window(file.read(),14)):
            if len(set(w)) == 14:
                return i + 14
            
print(problem1())
print(problem2())