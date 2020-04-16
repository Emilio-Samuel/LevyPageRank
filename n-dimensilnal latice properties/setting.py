
import numpy as np
from numpy import linalg as LA


#function that starts the simulation in a random point, i.e. initializes the lattice 
#with an uniformly random probability.
def initialize(dim, side):

    inicio=[]
    for i in range(dim):
        inicio.append(np.random.randint(0,side-1))
        
    return inicio
    
def distanceMatrix(dim, n, size):
    print(size)
    
    nodoi = np.zeros(dim)
    nodoj = np.zeros(dim)
    fila = []
    columna = []
    
    for j in range(n):
        iteratorj=0
        
        for i in range(n):
            print(nodoi)
            print(nodoj)
            
            fila.append(np.sum(abs(nodoj-nodoi)))
            iteratori=0
            
            while nodoi[iteratori]==size-1 and iteratori<dim-1:
                nodoi[iteratori]=0
                iteratori+=1
            nodoi[iteratori]+=1
            
        columna.append(fila)
        fila=[]
        nodoi = np.zeros(dim)
        while nodoj[iteratorj]==size-1 and iteratorj<dim-1:
            nodoj[iteratorj]=0
            iteratorj+=1
        nodoj[iteratorj]+=1        
    return np.array(columna)
                
def transitionMatrix(D,alpha):
    fila = []
    columna = []
    for i in range(len(D)):
        for j in range(len(D)):
            if i==j:
                fila.append(0)
                continue
                
            dij = np.power(1/float(D[i][j]),alpha)
            s=np.sum(np.power(1/D[i][D[i]!=0].astype(float),alpha))
            fila.append(round(float(dij)/s,3))
        columna.append(fila)
        fila = []
    return np.array(columna)
    
    
def getEigenthings(W):
    return LA.eig(W)
    
#def getProbT(INode, evals, evect):
     




    
    