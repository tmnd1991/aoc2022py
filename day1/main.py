with open('input', 'r') as inputFile:
    lines = inputFile.readlines()
    
    elves=[0]
    i=0
    # Strips the newline character
    for line in lines:
        if line.strip() == '':
            i = i + 1
            elves.append(0)
        else:
            elves[i] = int(line.strip())+ elves[i]
    elves.sort(reverse=True)
    print("problem 1: " + str(elves[0]))
    print("problem 2: " + str(sum(elves[0:3])))