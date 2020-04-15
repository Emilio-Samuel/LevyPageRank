#this program has as objetive to calculate all the properties given a D-dimensional lattice with N nodes.

from setting import *
import argparse

parser = argparse.ArgumentParser(description='Please enter the dimension and size of the lattice.')
parser.add_argument('d', type=int,
                    help='dimension of the lattice')
parser.add_argument('n', type=int,
                    help='number of nodes')
parser.add_argument('alpha', type=int,
                    help='number of nodes')                    
                    



if __name__ == '__main__':
    args = parser.parse_args()
    dim = args.d
    num = args.n
    alpha = args.alpha
    side = int(np.floor(np.power(num, 1.0/dim)))
    print(side)
    inicio=initialize(dim,num,side)

    print(inicio)
    D=distanceMatrix(dim,num,side)
    W=transitionMatrix(D, alpha)
    print(D)
    print(W)