from graphics import *
import copy
def main():
    win = GraphWin("Triangles", 800, 800)
    print("Click three times in the graphics window.")
    colors = ['red', 'green', 'blue', 'orange']
    for color in range(4):
        point1 = win.getMouse()
        circle = Circle(point1, 5)
        circle.setFill('red')
        circle.draw(win)     
        point2 = win.getMouse()
        c = Circle(point2, 5)
        c.setFill('red')
        c.draw(win)
        point3 = win.getMouse()
        a = Circle(point3, 5)
        a.setFill('red')
        a.draw(win)
        triangle = Polygon(point1, point2, point3)
        triangle.setFill(colors[color])
        triangle.draw(win)

    win.getMouse()
    

main()
