import numpy as np
import pandas as pd
# List the parameters to be featured in the grid
paramList=['nestim','eta','max_depth','alpha','gamma','esr','colsample_bytree']
# Generate the grid
paramData=np.array(np.meshgrid([800,1000],[0.01,0.03,0.1,0.3],[2,4,6,8],[0.3,0.5,0.7],[0,0.3,0.5,1],[10,30,50,60],[1])).T.reshape(-1,7) 
grid=pd.DataFrame(data=paramData,columns=paramList) 
grid.head(10)
