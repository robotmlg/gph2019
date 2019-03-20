import time, string
from heapq import *
from Levenshtein import distance
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
    
    queue = []
    visited = []
    # key -> parent, action to reach
    meta = {}

    root = startWord
    meta[root] = (None, None)
    heappush(queue, (0, root))

    while queue:
        
        word = heappop(queue)[1]

        if word == endWord:
            return buildSeq(word, meta)

        uops = expandUops(word, operations)
        childrenWords = [operate(word, uop) for uop in uops]

        for (action, child) in childrenWords:
            if child in visited or len(child) <= 0 or child == word:
                continue

            if child not in queue:
                meta[child] = (word, action)
                heappush(queue, (distance(child, endWord), child))

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
    if 'PIRHANA' in operations:
        uops.append(('PIRHANA', None))
    if 'WIGGLER' in operations:
        uops.extend([('WIGGLER', i) for i in range(0, len(word))])
    if 'LAKITU' in operations:
        uops.extend([('LAKITU', i) for i in range(0, len(word))])
    if 'BILL' in operations:
        uops.extend([('BILL', l) for l in string.ascii_uppercase])
    if 'BLOOP' in operations:
        uops.extend([('BLOOP', l) for l in string.ascii_uppercase])

    return uops

def operate(word, uop):
    operation = uop[0]
    if operation == 'BOWSER':
        return ('BOWSER', bowser(word))
    elif operation == 'SHY':
        return ('SHY', shy(word))
    elif operation == 'BOO':
        return ('BOO', boo(word))
    elif operation == 'PIRHANA':
        return ('PIRHANA', pirhana(word))
    elif operation == 'WIGGLER':
        index = uop[1]
        letter = word[index]
        return ('WIGGLER ' + letter + '@' + str(index), wiggler(word, index))
    elif operation == 'LAKITU':
        index = uop[1]
        letter = word[index]
        return ('WIGGLER ' + letter + '@' + str(index), wiggler(word, index))
    elif operation == 'BILL':
        letter = uop[1]
        return ('BILL ' + letter, bill(word, letter))
    elif operation == 'BLOOP':
        letter = uop[1]
        return ('BLOOP ' + letter, bloop(word, letter))
    else:
        raise RuntimeError('Cannot do operation ' + str(uop))
        
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

def wiggler(word, index):
    letter = word[index]
    letterIdx = (ord(letter) - ord('A')) % 26
    nextLetter = chr(ord('A') + letterIdx)
    prevLetter = chr(ord('A') - letterIdx)

    return word[0:index] + nextLetter + prevLetter + word[index+1:]

def boo(word):
    temp = word.replace('A', 'ue').replace('E', 'ai').replace('I', 'eo').replace('O', 'iu').replace('U', 'oa')
    return temp.upper()

def lakitu(word, index):
    return word[index:] + word[:index]

def pirhana(word):
    index = len(word) // 2
    return word[index:] + ' ' + word[:index]

## endregion operations

def main():
    # tier 6
    print(peaches('DEMON', 'LEMON EGGNOG', ['SHY', 'BILL', 'BOO', 'PIRHANA', 'BLOOP', 'LAKITU']))
    print(peaches('SNOW', 'ASIAN SQUID', ['BILL', 'BOO', 'WIGGLER', 'PIRHANA', 'BLOOP', 'LAKITU']))
    print(peaches('DRESS', 'TONS OF NOODLES', ['SHY', 'BILL', 'BOO', 'PIRHANA', 'BLOOP', 'LAKITU']))
    print(peaches('TIGHTS', 'CRAZY EIGHT', ['BOWSER', 'SHY', 'BILL', 'WIGGLER', 'PIRHANA', 'LAKITU']))

    # tier 5
    print(peaches('EASEL', 'WATER EEL', ['BILL', 'WIGGLER', 'PIRHANA', 'BLOOP', 'LAKITU']))
    print(peaches('SHRINE', 'REFRESHROOM', ['BOWSER', 'SHY', 'BOO', 'WIGGLER', 'BLOOP', 'LAKITU']))
    print(peaches('ETHICS', 'ANISE TAHINI', ['BOWSER', 'BOO', 'WIGGLER', 'PIRHANA', 'BLOOP', 'LAKITU']))

    # tier 4
    print(peaches('HAY', 'CANDY HEN', ['SHY', 'WIGGLER', 'PIRHANA', 'BLOOP', 'LAKITU']))
    print(peaches('TURF', 'PARFAIT', ['BILL', 'BOO', 'WIGGLER', 'PIRHANA', 'LAKITU']))
    print(peaches('HERON', 'ONIGIRI', ['BOWSER', 'BOO', 'WIGGLER', 'BLOOP', 'LAKITU']))

    # tier 3
    print(peaches('MAIL', 'ECLAIR', ['BOWSER', 'SHY', 'BILL', 'WIGGLER']))
    print(peaches('GOLD', 'AIOLI', ['BOWSER', 'SHY', 'BILL', 'BOO', 'BLOOP']))

    # tier 2
    print(peaches('LARD', 'SALAD', ['BOWSER', 'SHY', 'BILL', 'BLOOP']))
    print(peaches('CLAMS', 'EGGS', ['BOWSER', 'BLOOP', 'BILL']))

    # tier 1
    print(peaches('UNAGI','UNI',['BOWSER']))

if __name__ == "__main__":
    main()
