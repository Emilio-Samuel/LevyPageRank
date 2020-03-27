
class Nodo(object):
	"""docstring for Nodo"""
	def __init__(self, name, prob = 0):
		super(Nodo, self).__init__()
		self.name = name
		self.prob = prob
		self.neightbours = []
		
	def addNeightbour(self, nodo):
		self.neightbours.append(nodo)