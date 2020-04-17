
import operator
import numpy as np
from numpy import linalg as LA
from numpy.linalg import matrix_power

#function that starts the simulation in a random point, i.e. initializes the lattice 
#with an uniformly random probability.
def initialize(dim, side):

    inicio=[]
    for i in range(dim):
        inicio.append(np.random.randint(0,side-1))
        
    return inicio

    
def distanceMatrix(dim, n, size):
    nodoi = np.zeros(dim)
    nodoj = np.zeros(dim)
    fila = []
    columna = []


    for j in range(n):
        iteratorj=0


        for i in range(n):
            
            
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
            dij = np.power(1/float(D[i,j]),alpha)
            s=np.sum(np.power(1/D[i,:][D[i]!=0].astype(float),alpha))
            fila.append(float(dij)/s)
        columna.append(fila) 
        fila = []
    return np.array(columna)
    
    
def getEigenthings(W):
    eigenval, eigenvect = LA.eig(W)
    '''
    for i in range(len(eigenval)):
        sorted[i][0]=i
    '''
    invZ=eigenvect.transpose()
    return eigenval, eigenvect, invZ

def getProbT(eigenvals, Z, invZ, t):
    # N=len(Z)
    # for i in range(N):
        # if eigenvals[i] > 0.99:
            # eigenvals[i]=1
            # break
    # P = np.zeros([N,N])
    # vector1=0
    # vector2=0
    # pij=0
    # for j in range(N):
        # for i in range(N):
            # pij=0
            # for h in range(N):
                # vector1 =  Z[:,h]
                # vector2 = Z[h,:]
                # print(vector1[i])
                # print(vector2[j])
                
                # pij+= np.power(eigenvals[h],t)*vector1[i]*vector2[j]
                # print(eigenvals[h])
            # print('**************************************************')
            # P[i,j]=pij
    # print(P)
    diag = np.diag(eigenvals)
    print(matrix_power(diag,t))
    P=np.matmul(np.matmul(Z, matrix_power(diag,t)),invZ)

    return P    
    

    
    