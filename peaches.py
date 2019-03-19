import time, string
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
    return peaches_impl(startWord, endWord, operations, [])


def peaches_impl(startWord, endWord, operations, stepsSoFar):

    if len(startWord) == 0:
        return None
    if startWord == endWord:
        return stepsSoFar
    if len(stepsSoFar) >= 10:
        return None

    '''
    print(startWord + ' ' + endWord + ' ' + str(stepsSoFar))
    time.sleep(0.25)
    '''

    newOperations = operations.copy()
    ## disallow two Bullet Bills in a row
    if len(stepsSoFar) > 0 and stepsSoFar[-1][0].startswith('BILL'):
        newOperations.remove('BILL')
    ## disallow two Shy Guys in a row
    if (len(stepsSoFar) > 0 and stepsSoFar[-1][0].startswith('SHY')) or ('L' not in startWord and 'R' not in startWord):
        newOperations.remove('SHY')

    uops = expandUops(startWord, newOperations)
    
    for op in uops:
        result = operate(startWord, op)
        newSteps = stepsSoFar.copy()
        newSteps.append(result)
        
        ans = peaches_impl(result[1], endWord, operations, newSteps)

        if ans is not None:
            return ans

    return None


def expandUops(word, operations):
    uops = []
    if 'BOWSER' in operations:
        uops.append(('BOWSER', None))
    if 'SHY' in operations:
        uops.append(('SHY', None))
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


## endregion operations

# print(peaches('UNAGI','UNI',['BOWSER']))
print(peaches('LARD', 'SALAD', ['BOWSER', 'SHY', 'BILL', 'BLOOP']))

