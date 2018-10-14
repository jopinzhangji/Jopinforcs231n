#!/usr/bin/python
#
# jopin edit for task1 of cs231n
# sample: multiplication(X,Y)

# only use class and list
# import numpy as np

DEBUG = False

class data_input:
    #support = ['list', 'tuple']
    support = ['list']
    data = None
    def __init__(self):
        self.data = None

    def data_check(self,input):
        data_type = type(input).__name__
        if data_type not in self.support:
            print('only support input type:'%self.support)
            return False
        num = len(input[0])
        for data_raw in input:
            if len(data_raw) != num:
                print('this data is not the standard data [0]:%d!=[*]:%d'%(num, len(data_raw)))
                return False
        self.data = input
        return True

    def mult_check(self,X,Y):
        i = len(X[0])
        j = len(Y)
        if DEBUG: print('mult_check X[0]:%d Y:%d'%(i,j))
        if i == j:
            return True
        else:
            print('X and Y can not multi!: X[0]:%d Y:%d'%(i,j))
            return False

    def get_zero_out_list(self,X,Y):
        Z = []
        for i in range(len(X)):
            Z.append(len(Y[0])*[0])
        if DEBUG: print('out Z init: ',Z)
        return Z

def multiplication(X,Y):
    Z = []
    data_op = data_input()
    if not data_op.data_check(X) or not data_op.data_check(Y):
        print('err out..')
        return Z
    if not data_op.mult_check(X,Y):
        print('err out..')
        return Z
    Z = data_op.get_zero_out_list(X,Y)
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(X[0])):
                Z[i][j] += (X[i][k] * Y[k][j])
                if DEBUG: print('now add: X %d Y %d Z[%d,%d]:%d'%(X[i][k],Y[k][j],i,j,Z[i][j]))
    if DEBUG: print('out Z after multi: ',Z)
    return Z


if __name__ == '__main__':
    DEBUG = True
    print('this is a noraml test:')
    X = [[0,1,2],[2,3,4]]
    Y = [[2,3],[4,5],[6,7]]
    print('input-X: ',X)
    print('input-Y: ',Y)
    Z = multiplication(X,Y)
    print('noraml test done!')
    print('this is a error occer test:')
    X = [[0,1,2],[2,3]]
    Y = [[2,3],[4,5],[6,7]]
    print('input-X: ',X)
    print('input-Y: ',Y)
    Z = multiplication(X,Y)
    print('error test done')

