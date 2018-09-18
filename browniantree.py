
#Emily Kolb kolb0148
#I understand this is a graded, individual examination that may not be
#discussed with anyone. I also understand that obtaining solutions or
#partial solutions from outside sources, or discussing any aspect of the exam
#with anyone is academic misconudct and will result in failing the course.
#I further certify that this program represents my own work and that none of
#it was obtained from any other souce than material presented as part of the
#course.




import turtle
import random
import math

def getNumber():
    return(int(turtle.textinput("","How many particles?")))

def makeGrid(): #makes a grid
    grid = []
    counter = 0


    while counter < 200:

        nestedlist = []
        counter2 = 0

        while counter2 < 200:
            nestedlist.append(False)
            counter2 += 1
        grid.append(nestedlist)
        counter += 1

    grid [100][100] = True
    return(grid)


def randomWalk(t1,grid,particles):
    radius = 0
    stepcounter = 0
    location = t1.pos()
    (x,y) = location
    col = int(x)
    row = int(y)

    while particles > 0:
        randomangle = (random.random()*2*3.14159) #multiplies a random number by 2pi
        t1.goto(100 + ((radius + 1)*math.cos(randomangle)), 100 + ((radius + 1)*math.sin(randomangle)))
        location = t1.pos()
        (x,y) = location
        col = int(x)
        row = int(y)




        while hasNeighbor(grid,row,col) == False and stepcounter < 200: ##sends the particle on the walk and returns row/col
            number = random.randint(1,4)
            stepcounter += 1

            if number == 1:
                row = row + 1
            if number == 2:
                row = row - 1
            if number == 3:
                col = col + 1
            if number == 4:
                col = col - 1

        if stepcounter < 200: #this stops the randomwalk when we take 200 steps
            t1.goto(row,col)
            t1.dot(10,"blue")
            if grid[row][col] == False:
                particles -= 1
                grid[row][col] = True #updates grid
                print(particles)
            distance = math.sqrt(((row-100)**2) + ((col - 100)**2)) #determines radius by checking hypoteneuse
            if distance > radius: #if radius is bigger than previous radius, radius becomes this distance
                radius = int(distance)

        stepcounter = 0


    return(grid,row,col)




def hasNeighbor(grid,row,col):

    if inGrid(row) and inGrid(col): #asks if the row,col we're looking at is in the grid, otherwise stay false
        isit = False


        for x in range(row - 1, row + 2):
            if inGrid(x) == True:

                for y in range(col - 1, col + 2):
                    if inGrid(y) == True:

                        isit = isit or grid[x][y] #returns true if row/col has neighbor in grid
        grid[row][col] = isit

        return(grid[row][col])
    else:
        return(False) #returns false if row/col is not in grid


def inGrid(n):
    if n >= 0 and n <= 199:
        return(True)





def main():
    t1 = turtle.Turtle()
    t1.getscreen()
    t1.showturtle()
    turtle.setworldcoordinates(0, 0, 199, 199)
    t1.hideturtle()
    t1.speed(0)
    t1.penup()
    particles = getNumber()

    t1.goto(100,100)
    t1.dot(10,"blue")






    grid = makeGrid()



    (grid,row,col) = randomWalk(t1,grid,particles)





if __name__ == '__main__':
    main()
