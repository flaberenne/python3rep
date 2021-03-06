"""
transformDiagMat: rewrite square matrix elements on the diagonals of a new matrix
not to be confused with matrix diagonalization
parameters:
    - m : square matrix
    - s : direction for the elements writing
        - 0 : SW from top right to bottom left
        - 1 : NE from top left from bottom right
        - 2 : alternate NE and SW
See demo in  https://github.com/flaberenne/python3rep/transformDiagMatDemo.py
- source:https://github.com/flaberenne/python3rep/transformDiagMat.py
- author:flaberenne
"""


def transformDiagMat(m,s):
    # input m original square matrix
    #       s  0:NE=>SW else SW =>NE
    r=[[0 for x in range(len(m))] for y in range(len(m[0]))]
    res=[[0 for x in range(len(m))] for y in range(len(m[0]))]
    i=0
    j=0
    a=1
    for t in range(len(m)*2):
        for v in range(t+1):
            if v<=len(m)-1 and t-v<=len(m)-1:
                if s==1:
                    res[v][t-v]=m[i][j]
                elif s==0:
                    res[t-v][v]=m[i][j]
                elif s==2:
                    if a==1:
                        res[v][t-v]=m[i][j]
                    else:
                        res[t-v][v]=m[i][j]
                j+=1
                if j==5:
                    i+=1
                    i=i%5
                j=j%5
                if t+v==m:
                    a*=-1

    return res


