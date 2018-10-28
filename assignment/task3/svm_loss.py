#!/usr/bin/python
#
# jopin edit for task3 of cs231n
# this is learn for linear
# test svm


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

class linear_classfy:

    def __init__(self,loss='svm'):
        self.lossfun = loss
        self.Xtr = None
        self.ytr = None

    def svm_loss(self, x, y, W):
        scores = x.dot(W)
        margins = np.maximum(0, scores - np.array(scores[y] + 1))
        margins[y] = 0
        #print(y)
        #print(margins)
        return np.sum(margins)

    def fit(self, Xtr, Ytr):
        self.Xtr = Xtr
        self.ytr = Ytr

    def calc_loss(self,num=None,W=None,lable_n=10):
        if not num:
            num = self.Xtr.shape[0]
        if type(W).__name__ == 'NoneType':
            W = np.random.randn(self.Xtr.shape[1],lable_n)
        loss = 0
        for i in range(num):
            loss += self.svm_loss(self.Xtr[i], self.ytr[i], W)
        loss = float(loss)/float(num)

        #print('test %d number loss is %2f'%(num, loss))
        return loss

    def evaluate_gradient(self, loss_fun, W=None, lable_n=10):
        if type(W).__name__ == 'NoneType':
            W = np.random.randn(self.Xtr.shape[1],lable_n)
        grad = np.zeros([self.Xtr.shape[1],lable_n])
        temp1 = loss_fun(W=W)
        print("loss now is %2f"%temp1)
        for i in range(self.Xtr.shape[1]):
            for j in range(lable_n):
                W2 = W.copy()
                W2[i,j]+=0.0001
                temp2 = loss_fun(W=W2)
                grad[i,j]=(temp2-temp1)/0.0001
        return grad

    def train(self, W=None, number=2, step=0.01, lable_n=10):
        if type(W).__name__ == 'NoneType':
            W = np.random.randn(self.Xtr.shape[1],lable_n)
        for loop in range(number):
            W_grad = self.evaluate_gradient(W=W, loss_fun=self.calc_loss)
            W += -(step*W_grad)
            loss = self.calc_loss(W=W)
            print("now loss %d is %2f"%(loop,loss))
        
        

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

def mian():
    trainfile = os.path.join(cifa10_path, train_file[0])
    data = unpickle(trainfile)
    train_x = data[b'data']
    train_y = data[b'labels']
    liner = linear_classfy()
    liner.fit(train_x,np.array(train_y))
    L1_loss = liner.calc_loss(num = 1, lable_n=10)
    print('test L1_loss is %2f'%L1_loss)
    liner.train()
    

if __name__ == '__main__':
    print('svm test')
    mian()
        