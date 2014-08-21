'''
Created on 21-Aug-2014

@author: lokesh
'''


#! /usr/bin/env python
import math
from pandas import read_csv
import numpy
from sklearn.ensemble import RandomForestClassifier

COL_VARS = 40

A=read_csv('files/trainingC2.csv')

print type(A)

A=A.values
X=A[:,2:COL_VARS+2]
Y= A[:,COL_VARS+2]

#print X

# print type( X[0][0] )
# sum2 = 0.0
# print type( sum2 )
# print sum2+X[0][0]

  
 
for i in range(0,len(X) ):
    sum1=0
    count=0
    for j in range (0, COL_VARS):
        if  math.isnan( X[i][j] ) is False :
            sum1=sum1+X[i][j]
            count=count+1
    for j in range (0, COL_VARS):
        if( math.isnan( X[i][j]) ):
            X[i][j] = (sum1/count)
 
 
 
test=read_csv('files/trainingC2.csv')
test=test.values
test = test[:,2:COL_VARS+2]
 
             
for i in range(0,len(test) ):
    sum1=0.0
    count=0
    for j in range (0, COL_VARS):
        if  math.isnan( test[i][j]) is False :
            sum1=sum1+test[i][j]
            count=count+1
    for j in range (0, COL_VARS):
        if( math.isnan( test[i][j]) ):
            test[i][j] = (sum1/count)
            
 
clf = RandomForestClassifier(n_estimators=10)
   
clf = clf.fit(X, Y)
   
result = clf.predict(test)


f = open("files/crim2.csv", "w")
f.write("title\n")


for i in range(0, len(result)):
     f.write("%d\n"% result[i] )


#numpy.savetxt("files/crim2.csv",result, fmt ="%f")
f.close()
print "sucess!!"
