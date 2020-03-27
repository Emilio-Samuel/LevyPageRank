import numpy as np
from numpy.linalg import inv

class randomWalk(object):
	"""docstring for ClassName"""
	def __init__(self, grafo):
		super(randomWalk, self).__init__()
		self.grafo = grafo
		self.walkMatrix = np.matmul(self.grafo.adjacencyMatrix,inv(self.grafo.degreeMatrix))
		self.p0=np.array([i.prob for i in self.grafo.nodos ]).T
		self.pi=np.array([ self.grafo.degreeMatrix[i.name][i.name]/np.sum(self.grafo.degreeMatrix.diagonal()) for i in self.grafo.nodos ]).T

	def showWalkMatrix(self):
		np.set_printoptions(precision=3)
		print('\n\nWalk matrix:\n')
		print('   ', end = '')
		for i in range(len(self.grafo.nodos)):
			print(' '+str(i), end = '')
		print('\n', end = '')
		for i in range(len(self.grafo.nodos)):
			print(str(i)+' |', end = '')
			for j in range(len(self.grafo.nodos)):
				print(' %.2f' % self.walkMatrix[i][j], end = '')
			print(' |\n', end = '')

	def showp0(self):
		print(self.p0)


	def showpi(self):
		print(self.pi)

	def getStationaryState(self):
		aux = self.p0
		for i in range(1000):
			old = aux
			aux = np.matmul(self.walkMatrix, aux)
			print(np.sum(aux-self.pi))
			if np.array_equal(old, aux):
				print(i)
				break
		return aux
		
