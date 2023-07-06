import turtle
import math


def bezier(tur, controlPoints):
    i = 0
    while i <= 1:
        x = math.pow(1 - i, 3) * controlPoints[0][0] + 3 * math.pow(1 - i, 2) * i * controlPoints[1][0] + 3 * (
                1 - i) * math.pow(i, 2) * controlPoints[2][0] + math.pow(i, 3) * controlPoints[3][0]

        y = math.pow(1 - i, 3) * controlPoints[0][1] + 3 * math.pow(1 - i, 2) * i * controlPoints[1][1] + 3 * (
                1 - i) * math.pow(i, 2) * controlPoints[2][1] + math.pow(i, 3) * controlPoints[3][1]

        tur.goto(x, y)
        i += 0.01


def getControlPoints():
    controlPoints = [[], [], [], []]
    for i in range(0, 4):
        x = float(input(f"Coordenada x{i + 1}: "))
        y = float(input(f"Coordenada y{i + 1}: "))
        controlPoints[i] = [x, y]
    return controlPoints


def main():
    myTurtle = turtle.Turtle()
    controlPoints = getControlPoints()
    window = turtle.Screen()
    myTurtle.penup()
    myTurtle.goto(controlPoints[0])
    myTurtle.pendown()
    myTurtle.width(5)
    bezier(myTurtle, controlPoints)
    turtle.done()


if __name__ == '__main__':
    main()
