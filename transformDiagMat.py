"""
transformDiagMat: rewrite square matrix elements on the diagonals of a new matrix
not to be confused with matrix diagonalization
See demo in  https://github.com/flaberenne/python3rep/transformDiagMatDemo.py
- source:https://github.com/flaberenne/python3rep/transformDiagMat.py
- author:flaberenne
"""


def transformDiagMat(m):
    r=[[0 for x in range(len(m))] for y in range(len(m[0]))]
    res=[[0 for x in range(len(m))] for y in range(len(m[0]))]
    i=0
    j=0
    for t in range(len(m)*2):
        for v in range(t+1):
            if v<=len(m)-1 and t-v<=len(m)-1:
                res[v][t-v]=m[i][j]
                j+=1
                if j==5:
                    i+=1
                    i=i%5
                j=j%5

    return res

