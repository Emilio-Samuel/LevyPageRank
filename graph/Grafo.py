import numpy as np
from numpy.linalg import inv

class Grafo(object):
	"""docstring for ClassName"""
	def __init__(self, n):
		super(Grafo, self).__init__()
		self.nodos = []
		self.adjacencyMatrix = np.zeros((n, n))
		self.degreeMatrix = np.zeros((n, n))


	def addNode(self,nodo):
		self.nodos.append(nodo)



	def addEdge(self,pareja):
		self.adjacencyMatrix[pareja[0].name][pareja[1].name] = 1
		self.adjacencyMatrix[pareja[1].name][pareja[0].name] = 1
		pareja[0].addNeightbour(pareja[1])
		pareja[1].addNeightbour(pareja[0])
		self.degreeMatrix[pareja[0].name][pareja[0].name] += 1
		self.degreeMatrix[pareja[1].name][pareja[1].name] += 1


	def showAdjacencyMatrix(self):
		print('\n\nAdjacency matrix:\n')
		print('   ', end = '')
		for i in range(len(self.nodos)):
			print(' '+str(i), end = '')
		print('\n', end = '')
		for i in range(len(self.nodos)):
			print(str(i)+' |', end = '')
			for j in range(len(self.nodos)):
				print(' '+ str(int(self.adjacencyMatrix[i][j])), end = '')
			print(' |\n', end = '')

	def showDegreeMatrix(self):
		print('\n\nDegree matrix:\n')
		print('   ', end = '')
		for i in range(len(self.nodos)):
			print(' '+str(i), end = '')
		print('\n', end = '')
		for i in range(len(self.nodos)):
			print(str(i)+' |', end = '')
			for j in range(len(self.nodos)):
				print(' '+ str(int(self.degreeMatrix[i][j])), end = '')
			print(' |\n', end = '')

