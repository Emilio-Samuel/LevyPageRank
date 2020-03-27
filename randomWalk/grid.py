'''Test animation of a group of objects making a face.
'''

from graphics import *
import time
import random

def moveAll(shapeList, dx, dy):
	''' Move all shapes in shapeList by (dx, dy).'''   
	for shape in shapeList: 
		shape.move(dx, dy)
			

def moveAllOnLine(shapeList, dx, dy, repetitions, delay):
	'''Animate the shapes in shapeList along a line.
	Move by (dx, dy) each time.
	Repeat the specified number of repetitions.
	Have the specified delay (in seconds) after each repeat.
	'''
	for i in range(repetitions):
		moveAll(shapeList, dx, dy)
		time.sleep(delay)
		

def drawNxNGrid(point,n,win):

	pointX = 40
	pointY = 40
	
	for i in range(n):
		pointX = 40
		for i in range(n):
			pt = Point(pointX, pointY)
			line = Line(pt, Point(pointX+20, pointY))
			line.draw(win)
			line = Line(pt, Point(pointX-20, pointY))
			line.draw(win)
			line = Line(pt, Point(pointX, pointY-20))
			line.draw(win)
			line = Line(pt, Point(pointX, pointY+20))
			line.draw(win)
			circle = Circle(pt, 2.5)
			circle.setFill('blue')
			circle.draw(win)
			pointX += 20
		pointY += 20

		pt = Point(point[0]*20+40, point[1]*20+40)
		circle = Circle(pt, 2.5)
		circle.setFill('green')
		circle.draw(win)

def jump(point,n):
	jmp = random.random()

	if jmp <= 0.25:
		if point[0] == n-1:
			return 0,point[1]
		return point[0]+1,point[1]

	elif jmp > 0.25 and jmp <= 0.5:
		if point[1] == n-1:
			return point[0],0
		return point[0],point[1]+1

	elif jmp > 0.5 and jmp <= 0.75:
		if point[0] == 0:
			return n-1,point[1]
		return point[0]-1,point[1]

	else:
		if point[1] == 0:
			return point[0],n-1
		return point[0],point[1]-1

		

def updateGrid(oldPoint, newPoint, win):

	pt = Point(newPoint[0]*20+40, newPoint[1]*20+40)
	circle = Circle(pt, 2.5)
	circle.setFill('red')
	circle.draw(win)
	pt = Point(oldPoint[0]*20+40, oldPoint[1]*20+40)
	circle = Circle(pt, 2.5)
	circle.setFill('blue')
	circle.draw(win)

n=5
oldPoint = (random.randint(0, n-1), random.randint(0, n-1))

win = GraphWin('Back and Forth', 600, 600)
drawNxNGrid(oldPoint, n, win)

while(1):
	time.sleep(1)
	print(oldPoint)
	newPoint=jump(oldPoint,n)
	updateGrid(oldPoint, newPoint, win)
	oldPoint = newPoint
	