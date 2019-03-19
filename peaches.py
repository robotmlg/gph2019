import time, string
from collections import deque
# operations
#
# Bowser	    destroys alphabetically first letter
# Shy Guy	    changes L to R, R to L
# Bullet Bill	change the first leter to your choice
# Blooper	    adds the letter of your choice to 2nd and 2nd to last pos.
# Wiggler	    Change the letter of your choice to the two letters after and before
# Boo	        replaces all vowels with the vowels before and after
# Lakitu	    Rotate the word so your chosen letter is first
# Pirhana	    Swap the first and second halves, adding a space

def peaches(startWord, endWord, operations):
    
    queue = deque()
    visited = []
    # key -> parent, action to reach
    meta = {}

    root = startWord
    meta[root] = (None, None)
    queue.append(root)

    while queue:
        
        word = queue.popleft()

        if word == endWord:
            return buildSeq(word, meta)

        uops = expandUops(word, operations)
        childrenWords = [operate(word, uop) for uop in uops]

        for (action, child) in childrenWords:
            if child in visited or len(child) <= 0 or child == word:
                continue

            if child not in queue:
                meta[child] = (word, action)
                queue.append(child)

        visited.append(word)
                

def buildSeq(word, meta):
    actions = []

    curr = word
    while meta[curr][0] is not None:
        prev = meta[curr]
        actions.append(prev)
        curr = prev[0]

    actions.reverse()
    return actions


def expandUops(word, operations):
    uops = []
    if 'BOWSER' in operations:
        uops.append(('BOWSER', None))
    if 'SHY' in operations:
        uops.append(('SHY', None))
    if 'BOO' in operations:
        uops.append(('BOO', None))
    if 'BILL' in operations:
        for letter in string.ascii_uppercase:
            uops.append(('BILL', letter))
    if 'BLOOP' in operations:
        for letter in string.ascii_uppercase:
            uops.append(('BLOOP', letter))

    return uops

def operate(word, uop):
    operation = uop[0]
    if operation == 'BOWSER':
        return ('BOWSER', bowser(word))
    elif operation == 'SHY':
        return ('SHY', shy(word))
    elif operation == 'BOO':
        return ('BOO', boo(word))
    elif operation == 'BILL':
        letter = uop[1]
        return ('BILL ' + letter, bill(word, letter))
    elif operation == 'BLOOP':
        letter = uop[1]
        return ('BLOOP ' + letter, bloop(word, letter))
        
## region operations

def bowser(word):
    letters = ''.join(sorted(word))
    letter = letters[0]
    return word.replace(letter, '')

def shy(word):
    temp = word.replace('R', '$').replace('L', '%')
    return temp.replace('$', 'L').replace('%', 'R')

def bill(word, letter):
    letters = list(word)
    letters[0] = letter
    return ''.join(letters)

def bloop(word, letter):
    letters = list(word)
    letters.insert(1, letter)
    letters.insert(-1, letter)
    return ''.join(letters)

def boo(word):
    temp = word.replace('A', 'ue').replace('E', 'ai').replace('I', 'eo').replace('O', 'iu').replace('U', 'oa')
    return temp.upper()

## endregion operations

# print(peaches('UNAGI','UNI',['BOWSER', 'SHY', 'BILL', 'BLOOP']))
# print(peaches('LARD', 'SALAD', ['BOWSER', 'SHY', 'BILL', 'BLOOP']))
# print(peaches('GOLD', 'AIOLI', ['BLOOP', 'BOWSER', 'BILL']))
print(peaches('CLAMS', 'EGGS', ['BOWSER', 'BLOOP', 'BILL']))

