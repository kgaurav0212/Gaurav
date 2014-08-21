'''
Created on 21-Aug-2014

@author: lokesh
'''


#! /usr/bin/env python
from infos import filein2
from infos import fileout2
from infos import COL_VARS

import math
from pandas import read_csv
import numpy
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model



A=read_csv(filein2)

print type(A)

A=A.values
X=A[:,2:COL_VARS+2]
Y= A[:,COL_VARS+2]

#print X

# print type( X[0][0] )
# sum2 = 0.0
# print type( sum2 )
# print sum2+X[0][0]


for j in range(0,COL_VARS ):
    array1=[]
    for i in range (0, len(X)):
        if  math.isnan( X[i][j] ) is False :
            array1.append( X[i][j] )
    value = numpy.mean(array1)        
    for i in range (0, len(X)):
        if( math.isnan( X[i][j]) ):
            X[i][j] =value 
 
 
test=read_csv(fileout2)
test=test.values
test = test[:,2:COL_VARS+2]
 
             
for j in range(0, COL_VARS ):
    array1=[]
    for i in range (0,len(test)):
        if  math.isnan( test[i][j]) is False :
            array1.append( test[i][j] )
    value = numpy.mean(array1) 
    for i in range (0,len(test)):
        if( math.isnan( test[i][j]) ):
            test[i][j] = value
            
 
clf = RandomForestClassifier(n_estimators=10)
#clf = linear_model.LinearRegression()
   
clf = clf.fit(X, Y)
   
result = clf.predict(test)


f = open("files/crim2.csv", "w")
f.write("title\n")


for i in range(0, len(result)):
     f.write("%d\n"% result[i] )


#numpy.savetxt("files/crim2.csv",result, fmt ="%f")
f.close()
print "sucess!!"
