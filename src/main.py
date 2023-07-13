import sys
from collections import defaultdict
categoryfile = sys.argv[1]
inputfile = sys.argv[2]
outputpath = sys.argv[3]

# define the FSA
fsa = {
    0: [('V1', 1), ('C1', 2)],
    1: [('C1', 2)],
    2: [('C2', 3), ('V2', 4), ('T', 5), ('V3', 6), ('C3', 9), ('V1', 7), ('C1', 8)],
    3: [('V2', 4), ('T', 5), ('V3', 6), ('C3', 9)],
    4: [('T', 5), ('V3', 6), ('C3', 9), ('V1', 7), ('C1', 8)],
    5: [('V3', 6), ('C3', 9), ('V1', 7), ('C1', 8)],
    6: [('C3', 9), ('V1', 7), ('C1', 8)],
    7: 1,
    8: 2,
    9: 0
    }

# instantiate data structures
convertor = defaultdict(int)
segmented = ''
current_state_index = 0

# dictionary mapping category to its members
with open(categoryfile, 'r', encoding='utf8') as d:
    content = d.readlines()
    for line in content:
        splitup = line.split()
        convertor[splitup[0]] = splitup[1:]


with open(inputfile, 'r', encoding='utf8') as f:
    lines = f.readlines()

# segment text
for line in lines:
    for char in line:
        for (category, to_state_index) in fsa[current_state_index]:
            if char in convertor[category]:
                # set the current state index to the to-state index
                current_state_index = to_state_index
                break

        if current_state_index == 7 or current_state_index == 8:
            # add break before the char
            segmented += ' ' + char

            # move to the next state for free
            current_state_index = fsa[current_state_index]

        elif current_state_index == 9:
            # add the break after the char
            segmented += char + ' '

            # move to the next state for free
            current_state_index = fsa[current_state_index]

        else:
            # for all other states, simply add the character
            segmented += char

# write segmented text to the output file
with open(outputpath, 'w', encoding='utf8') as g:
    g.write(segmented)