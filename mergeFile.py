'''
Created on 21-Aug-2014

@author: lokesh
'''
from pandas.io.parsers import read_csv

COL_VARS = 40

A  = read_csv("files/crim1.csv")
A =A.values

B = read_csv("files/crim2.csv")
B=B.values

########################################

C1 = read_csv('files/trainingC1.csv')
C2 = read_csv('files/trainingC2.csv') 

# C1 = read_csv('files/leaderC1.csv')
# C2 = read_csv('files/leaderC2.csv')

C1 = C1.values
C2 = C2.values


#######################################

Ids1 = C1[:, 0]
Ids2 = C2[:, 0]

Values1 = C1[:, COL_VARS+2 ]
Values2 = C2[:, COL_VARS+2 ]
 
f = open('files/mergedOutput.csv', 'w')


diff_count=0


print len(A)+len(B)
print len(Ids1)

for i in range(0, len(Ids1)):
    f.write( "%s,%s, %d\n" %(Ids1[i][4: len( Ids1[i]) ], Ids1[i], A[i] ) )
    if( A[i] != Values1[i]):
        diff_count+=1
        
for i in range(0, len(Ids2)):
    f.write( "%s,%s, %d\n" % ( Ids2[i][4: len( Ids2[i]) ],Ids2[i], B[i]) )
    if( B[i] != Values2[i]):
        diff_count+=1
        
print("Diff_count")
print(diff_count) 

f.close()
