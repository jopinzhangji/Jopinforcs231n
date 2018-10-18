#!/usr/bin/python
#
# jopin edit for task2 of cs231n
# this is learn for knn
# now it is very lower accuracy


import numpy as np
import pickle
import os

cifa10_path = os.path.dirname(os.getcwd())+'/resorce_down/cifar-10-batches-py'
train_file = ['data_batch_1',
             'data_batch_2',
             'data_batch_3',
             'data_batch_4',
             'data_batch_5']
test_file = ['test_batch']

class knn_classfy:

    dis_config='L1'
    # k = 1

    def __init__(self, kernel='L1'):
        self.dis_config=kernel
        self.Xtr = None
        self.ytr = None

    def dis_L2(self,X,Y):
        return np.pow(np.sum(np.pow((X - Y),2)), 0.5)

    def dis_L1(self,X): 
        return np.sum(np.abs(self.Xtr-X))

    def train(self, X, y):
        self.Xtr = X
        self.ytr = y

    def predict(self, X):
        y_pre = np.zeros(X.shape[0], dtype = self.ytr.dtype)
        for i in range(X.shape[0]):
            print('start predict num: %d'%i)
            dis = self.dis_L1(X[i,:])
            min = np.argmin(dis)
            y_pre[i] = self.ytr[min]
        return y_pre

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

def mian():
    trainfile = os.path.join(cifa10_path, train_file[0])
    testfile = os.path.join(cifa10_path, test_file[0])
    data = unpickle(trainfile)
    testd_data = unpickle(testfile)
    train_x = data[b'data']
    train_y = data[b'labels']
    test_x = testd_data[b'data']
    test_y = testd_data[b'labels'] 
    knn = knn_classfy()
    knn.train(train_x,np.array(train_y))
    pre_y = knn.predict(test_x)
    self_t = float(np.sum((test_y == pre_y)))/float(len(test_y))
    print('test is %2f'%self_t)
    

if __name__ == '__main__':
    print('knn test')
    mian()

