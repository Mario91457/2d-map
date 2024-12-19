
mapa = []

directions = { # y, x
    "up": [1, 0, "^"],
    "down": [-1, 0, "v"],
    "left": [0, -1, "<"],
    "right": [0, 1, ">"]
}

def customInput(info):
    while True:
        newInput = input(info)

        try:
            newInput = int(newInput)

            if newInput <= 0:
                raise ValueError
            
            return newInput
        except ValueError:
            print("integer please")

def pMap():
    print("Y")

    for i in reversed(mapa):
        print(f"┃{" ".join(i)}")
    
    print(f"┗{"━"*sizeX*2} X")

sizeX = customInput("map size X: ")
sizeY = customInput("map size Y: ")

mapa = [
    ["." for _ in range(sizeX)] for _ in range(sizeY)
]

x = customInput("pos in X: ")
y = customInput("pos in Y: ")

currentPos = [0, 0] # y, x

if x in range(1,sizeX+1) and y in range(1,sizeY+1):
    mapa[y-1][x-1] = "^" 
    currentPos = [y-1, x-1]
    pMap()

while True:
    goTo = input("up, down, left, right: ")

    if goTo in directions:
        newY = currentPos[0] + directions[goTo][0]
        newX = currentPos[1] + directions[goTo][1]

        print(f"{newX=}, {newY=}")

        if newX in range(sizeX) and newY in range(sizeY):
            mapa[currentPos[0]][currentPos[1]] = "."

            mapa[newY][newX] = directions[goTo][2]
            currentPos = [newY, newX] 

            pMap()
        else:
            pMap()
            print("Out of range")