

BOARD_SIZE = 11

# adjust for Pearl using a 1-indexed grid
def pearlAdjust(x,y):
    return (x-1, y-1)

def genWord(startX, startY, direction, length):
    if startX < 0 or startX > 11 or startY < 0 or startY > 11:
        raise RuntimeError('word coördinate (' + startX + ', ' + startY + ')  out of range!')

    squares = []
    currX, currY = pearlAdjust(startX, startY)
    while length > 0:
        squares.append((currX, currY))

        if 'N' in direction:
            currX -= 1
        if 'E' in direction:
            currY += 1
        if 'S' in direction:
            currX += 1
        if 'W' in direction:
            currY -= 1

        currX %= BOARD_SIZE
        currY %= BOARD_SIZE

        length -= 1

    return squares

def g(x,y,d,l):
    return genWord(x,y,d,l)

l = len('MACKENZIE')
mackenzie = [g(2,3,'S',l), g(10,1,'SW',l)]
l = len('ABBOTT')
abbott = [g(2,2,'SE',l), g(11,4,'NE',l), g(9,6,'NW',l)]
l = len('BOWELL')
bowell = [g(6,1,'NW',l), g(7,10,'NW',l), g(8,8,'NE',l), g(9,6,'NW',l), g(10,4,'NW',l)]
l = len('LAURIER')
laurier = [g(8,6,'NW',l),g(5,7,'E',l),g(2,8,'SW',l),g(10,9,'N',l),g(7,10,'SE',l),
g(4,11,'W',l),g(1,1,'NE',l)]
l = len('BENNETT')
bennett = [g(5,6,'NW',l),g(7,2,'SW',l),g(9,9,'SE',l),g(11,5,'NE',l),g(2,1,'NW',l),
g(4,8,'SW',l),g(6,4,'SE',l),g(8,11,'NE',l),g(10,7,'NW',l),g(1,3,'SW',l),g(3,10,'SE',l)
]
l = len('DIEVENBAKER')
dievenbaker = [g(8,4,'E',l),g(5,8,'S',l),g(2,1,'W',l),g(10,5,'N',l),g(7,9,'E',l),
g(4,2,'S',l),g(1,6,'W',l),g(9,10,'N',l),g(6,3,'E',l),g(3,7,'S',l),g(11,11,'W',l),
g(8,4,'N',l),g(5,8,'E',l)
]
l = len('TURNER')
turner = [g(7,9,'S',l),g(3,3,'SE',l),g(10,8,'E',l),g(6,2,'NE',l),g(2,7,'N',l),
g(9,1,'NE',l),g(5,6,'W',l),g(1,11,'SW',l),g(8,5,'S',l),g(4,10,'SE',l),g(11,4,'E',l),
g(7,9,'NE',l),g(3,3,'N',l),g(10,8,'NW',l),g(6,2,'W',l),g(2,7,'SW',l),g(9,1,'S',l)
]
l = len('CAMPBELL')
campbell = [g(5,3,'N',l),g(11,11,'SE',l),g(6,8,'W',l),g(1,5,'NE',l),g(7,2,'S',l),
g(2,10,'NW',l),g(8,7,'E',l),g(3,4,'SW',l),g(9,1,'N',l),g(4,9,'SE',l),g(10,6,'W',l),
g(5,3,'NE',l),g(11,11,'S',l),g(6,8,'NW',l),g(1,5,'E',l),g(7,2,'SW',l),g(2,10,'N',l),
g(8,7,'SE',l),g(3,4,'W',l)
]
l = len('TRUDEAU')
trudeau = [g(2,9,'W',l),g(9,2,'NW',l),g(5,6,'N',l),g(1,10,'NE',l),g(8,3,'E',l),
g(4,7,'SE',l),g(11,11,'S',l),g(7,4,'SW',l),g(3,8,'W',l),g(10,1,'NW',l),g(6,5,'N',l),
g(2,9,'NE',l),g(9,2,'E',l),g(5,6,'SE',l),g(1,10,'S',l),g(8,3,'SW',l),g(4,7,'W',l),
g(11,11,'NW',l),g(7,4,'N',l),g(3,8,'NE',l),g(10,1,'E',l),g(6,5,'SE',l),g(2,9,'S',l)
]

pms = [(mackenzie, 2), (abbott, 3), (bowell, 5), (laurier, 7), (bennett, 11), 
       (dievenbaker, 13), (turner, 17), (campbell, 19), (trudeau, 23)]

def main():

    bestcount = BOARD_SIZE ** 2
    bestpuzzle = 0

    for i in range(0, 99999999):
        covered = set()

        for pm in pms:
            modulo = pm[1]
            puzzleindex = i % modulo

            pmsquares = pm[0][puzzleindex]
            covered.update(pmsquares)

        if len(covered) < bestcount:
            bestcount = len(covered)
            bestpuzzle = i

    print(bestpuzzle)

if __name__ == '__main__':
    main()
