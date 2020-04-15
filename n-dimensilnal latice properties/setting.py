
import numpy as np

def initialize(dim,num, side):

    inicio=[]
    for i in range(dim):
        inicio.append(np.random.randint(0,side-1))
        
    return inicio
    
def distanceMatrix(dim, n, size):

    nodoi = np.array([ 0 for i in range(dim)])
    nodoj = np.array([ 0 for i in range(dim)])
    fila = []
    columna = []
    icount = 0
    jcount = 0   
    for j in range(n):
        aux = format(jcount, '03b')
        nodoj = np.array([int(d) for d in aux])
        
        for i in range(n):
            aux = format(icount, '03b')
            nodoi = np.array([int(d) for d in aux])
            fila.append(np.sum(abs(nodoj-nodoi)))
            icount+=1
            
        icount=0
        columna.append(fila)
        fila=[]
        jcount+=1
            
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