
import turtle
import random

class Cell:
    def __init__(self,xmin=0,ymin=0,width=1,height=1):
        self.__xmin = xmin
        self.__ymin = ymin
        self.__xmax = self.__xmin + width
        self.__ymax = self.__ymin + height
        self.__t = turtle.Turtle()
        self.__t.hideturtle()
        self.__t.speed(0)
        self.__bomb = False
        self.__cleared = False


    def isIn(self,x,y):
        if x > self.__xmin and x < self.__xmax and y > self.__ymin and y < self.__ymax:
            return True

        else:
            return False

    def setBomb(self):
        self.__bomb = True

    def isBomb(self):
        return self.__bomb


    def clear(self):
        self.__cleared = True
        self.draw()

    def isCleared(self):
        return self.__cleared


    def showcount(self,c):
        centerx = (self.__xmax + self.__xmin)/2
        centery = (self.__ymax + self.__ymin)/2
        self.__t.penup()
        self.__t.goto(centerx,centery)
        self.__t.write(c,align="center", font=("Arial",10,"normal"))

    def draw(self):
        self.__t.hideturtle()
        self.__t.penup()
        self.__t.goto(self.__xmin,self.__ymin)

        if self.isBomb():
            self.__t.pendown()
            self.__t.fillcolor("red")
            self.__t.begin_fill()
            self.__t.goto(self.__xmax,self.__ymin)
            self.__t.goto(self.__xmax,self.__ymax)
            self.__t.goto(self.__xmin,self.__ymax)
            self.__t.goto(self.__xmin,self.__ymin)
            self.__t.end_fill()
            self.__t.penup()
            centerx = (self.__xmax + self.__xmin)/2
            centery = (self.__ymax + self.__ymin)/2
            self.__t.goto(centerx,centery)
            self.__t.write("*",font=("Arial",10,"normal"))


        elif self.isCleared():
            self.__t.pendown()
            self.__t.fillcolor("gray")
            self.__t.begin_fill()
            self.__t.goto(self.__xmax,self.__ymin)
            self.__t.goto(self.__xmax,self.__ymax)
            self.__t.goto(self.__xmin,self.__ymax)
            self.__t.goto(self.__xmin,self.__ymin)
            self.__t.end_fill()


        else:
            self.__t.pendown()
            self.__t.fillcolor("green")
            self.__t.begin_fill()
            self.__t.goto(self.__xmax,self.__ymin)
            self.__t.goto(self.__xmax,self.__ymax)
            self.__t.goto(self.__xmin,self.__ymax)
            self.__t.goto(self.__xmin,self.__ymin)
            self.__t.end_fill()



class Minesweeper:
    def __init__(self,rows=14,columns=14,mines=15,bombsvis=False):
        self.__grid = []
        self.__t = turtle.Turtle()
        self.__s = self.__t.getscreen()
        self.__t.speed(0)
        self.__s.onclick(self.__mouseClick)
        self.__s.listen()
        self.__s.tracer(1000,0)
        self.__s.update()
        scale = 10*max(rows,columns)
        turtle.setworldcoordinates(-.5*scale,-.5*scale,3/2*scale,3/2*scale)
        #scales the grid based on how many rows/columns there are - grid always takes up same amount of screen space.
        self.__t.hideturtle()


        counter1 = 0
        gridcolumns = []
        y = 0
        x = 0


        while counter1 < rows: #making a nested list of cells
            width = 10
            height = 10
            counter1 += 1
            x = 0
            counter2 = 0

            while counter2 < columns:
                newcell = Cell(x,y,width,height)
                gridcolumns.append(newcell)
                counter2 += 1
                x += width
                newcell.draw()
            self.__s.update()
            self.__grid.append(gridcolumns)
            y += height
            gridcolumns = []


        remainingmines = 0
        while remainingmines < mines: #sets # of mines based on given argument
            newminex = random.randint(0,columns-1)
            newminey = random.randint(0,rows-1)
            if self.__grid[newminey][newminex].isBomb() == False:
                self.__grid[newminey][newminex].setBomb()
                remainingmines += 1


        if bombsvis:
            counter1 = 0
            while counter1 < columns:
                counter2 = 0
                while counter2 < rows:
                    if self.__grid[counter1][counter2].isBomb():
                        self.__grid[counter1][counter2].draw()
                    counter2 += 1
                counter1 +=1

    def countBombs(self,row,col):
        numberofbombs = 0
        for y in range(row - 1, row + 2):
            for x in range(col - 1, col + 2):
                if self.__grid[y][x].isBomb():
                    numberofbombs += 1
        return numberofbombs

    def cellsRemaining(self):
        cellsnum = 0
        for a in range(0,len(self.__grid)):
            for b in range(0,len(self.__grid[0])):
                if not self.__grid[a][b].isCleared() and not self.__grid[a][b].isBomb():
                    cellsnum += 1
        return(cellsnum)


    def getRowCol(self,x,y):
        if x/10 < len(self.__grid) and x/10 > 0 and y/10 < len(self.__grid[0]) and y/10 > 0:
            return (x/10),(y/10)
        else:
            return (-1,-1)


    def __mouseClick(self,x,y):
        (x,y) = self.getRowCol(x,y)
        row = int(y)
        col = int(x)

        if x != -1 and y != -1: #to make sure clicking outside grid doesn't clear cell [-1,-1]
            if not self.__grid[row][col].isCleared():

                if self.__grid[row][col].isBomb():
                    self.__t.penup()
                    self.__t.goto(25,-20)
                    self.__t.pendown()
                    self.__t.write("You lose, loser", font=("Arial",45,"normal"),align="center") #plz don't be offended i just thought this was funny
                    self.__t.penup()
                    self.__t.goto(25,-30)
                    self.__t.pendown()
                    self.__t.write("Click mouse to exit", font=("Arial",25,"normal"),align="center")

                    counter1 = 0
                    while counter1 < len(self.__grid):
                        counter2 = 0
                        while counter2 < len(self.__grid[0]):
                            if self.__grid[counter1][counter2].isBomb():
                                self.__grid[counter1][counter2].draw()
                            counter2 += 1
                        counter1 +=1
                    self.__s.update()
                    self.__s.exitonclick()

                else:
                    self.clearCell(row,col)

                    if self.cellsRemaining() == 0:
                        self.__t.penup()
                        self.__t.goto(25,-20)
                        self.__t.pendown()
                        self.__t.write("You win, winner!", font=("Arial",45,"normal"),align="center")
                        self.__t.penup()
                        self.__t.goto(25,-30)
                        self.__t.pendown()
                        self.__t.write("Click mouse to exit", font=("Arial",25,"normal"),align="center")


                        counter1 = 0
                        while counter1 < len(self.__grid):
                            counter2 = 0
                            while counter2 < len(self.__grid[0]):
                                if self.__grid[counter1][counter2].isBomb():
                                    self.__grid[counter1][counter2].draw()
                                counter2 += 1

                            counter1 +=1
                        self.__s.exitonclick()




    def clearCell(self,row,col):

        self.__grid[row][col].clear()


        if self.hasneighborMine(row,col) == 0:
            for a in range(row-1,row+2):
                if a >= 0 and a < len(self.__grid):
                    for b in range(col-1,col+2):
                        if b >= 0 and b < len(self.__grid[0]):
                            if not self.__grid[a][b].isCleared():
                                self.__s.update() #had to update in here to avoid glitchiness for the cell clearing, bit slower but smoother animation - you can keep playing as it clears
                                self.clearCell(a,b)






    def hasneighborMine(self,row,col): #added method that checks for neighbors for the recursive clear cell
        minenumber = 0
        for y in range(row-1,row+2):
            if y >= 0 and y < len(self.__grid):
                for x in range(col-1,col+2):
                    if x >= 0 and x < len(self.__grid[0]):
                        if self.__grid[y][x].isBomb():

                            minenumber += 1
        if minenumber > 0:
            self.__grid[row][col].showcount(minenumber)
        return minenumber






def main():

    newgame = Minesweeper(15,15,14)

if __name__ == '__main__':
    main()
