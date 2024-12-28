def blocks():
    with open('day1.txt') as f:
        for line in f.readlines():
            movements = (line.replace(' ','').split(','))
    x,y = 0,0
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    destinations = []
    secondanswer = []
    currentdirec = 0
    for movement in movements:
        direc,steps = movement[0],int(movement[1::])
        if direc == "R":
            currentdirec += 1
        else:
            currentdirec -=1
        for step in range(steps):
            x = x + directions[currentdirec % 4][0]
            y = y + directions[currentdirec % 4][1]
            destinations.append((x,y))
            if destinations.count((x,y)) > 1:
                secondanswer.append((x,y))
    answer = abs(x) + abs(y)
    print(abs(secondanswer[0][0]) + abs(secondanswer[0][1]))
    print(answer)
blocks()
