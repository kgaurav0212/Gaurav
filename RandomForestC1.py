'''
Created on 21-Aug-2014

@author: lokesh
'''


#! /usr/bin/env python
from infos import COL_VARS
from infos import filein1
from infos import fileout1
from scipy import optimize

import pylab as P
import math
import matplotlib.pyplot as plt
from pandas import read_csv
import numpy 
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model



A = read_csv(filein1)

print type(A)

A = A.values
X = A[:, 2:COL_VARS + 2]
Y = A[:, COL_VARS + 2]

for j in range(0, COL_VARS):
    array1 = []
    for i in range (0, len(X)):
        if  math.isnan(X[i][j]) is False :
            array1.append(X[i][j])
             
    value = numpy.mean(array1)        
    for i in range (0, len(X)):
        if(math.isnan(X[i][j])):
            X[i][j] = -1
            
            
print len(X)
X= X.T
for i in range(0, len(X)):
    #for j in range (0, len(X[i])):
     #   X[i][j] = int(X[i][j])
     
    plt.plot(X[i],linewidth=0.1)
    plt.savefig(`i` + '.png',dpi=800)
    plt.clf()

# print type(X)
# 
# print COL_VARS
# # X.append()
# 
# # print X
# 
# # print type( X[0][0] )
# # sum2 = 0.0
# # print type( sum2 )
# # print sum2+X[0][0]
# 
#   
#  
# for j in range(0, COL_VARS):
#     array1 = []
#     for i in range (0, len(X)):
#         if  math.isnan(X[i][j]) is False :
#             array1.append(X[i][j])
#             
#     value = numpy.mean(array1)        
#     for i in range (0, len(X)):
#         if(math.isnan(X[i][j])):
#             X[i][j] = value
#  
#  
#  
# test = read_csv(fileout1)
# test = test.values
# test = test[:, 2:COL_VARS + 2]
#  
#              
# for j in range(0, COL_VARS):
#     array1 = []
#     for i in range (0, len(test)):
#         if  math.isnan(test[i][j]) is False :
#             array1.append(test[i][j])
#     value = numpy.mean(array1) 
#     for i in range (0, len(test)):
#         if(math.isnan(test[i][j])):
#             test[i][j] = value
#             
# # clf= optimize.brent()
# clf = RandomForestClassifier(n_estimators=20)
# # clf = linear_model.LinearRegression()
# 
# clf = clf.fit(X, Y)
#    
# result = clf.predict(test)
# 
# 
# f = open("files/crim1.csv", "w")
# f.write("title\n")
# 
# 
# for i in range(0, len(result)):
#     f.write("%d\n" % result[i])
# 
# 
# # numpy.savetxt("files/crim2.csv",result, fmt ="%f")
# f.close()
print "sucess!!"
