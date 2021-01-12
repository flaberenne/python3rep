"""
transformDiagMatDemo: demo for transfDiagMagDemo
- source:https://github.com/flaberenne/python3rep/transformDiagMatDemo.py
- author:flaberenne
"""

import transformDiagMat as f

a=[[1 ,2 ,3, 4,5],[6 ,7 ,8 ,9, 10 ],[ 11 ,12 ,13,14,15],[16 ,17,18,19,20],[21,22,23,24,25]]

print("*************")
print("Original matrix")
print("*************")

for matLine in a:
    print(*matLine)
    
print("\n")
print("*************")
print("Data on diagonal NE => SW")
print("*************")

r=f.transformDiagMat(a,0)

for matLine in r:
    print(*matLine)

print("\n")
print("*************")
print("Data on diagonal SW => NE")
print("*************")

r=f.transformDiagMat(a,1)

for matLine in r:
    print(*matLine)
