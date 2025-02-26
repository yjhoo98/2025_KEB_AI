import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
data=[1,7,5,2,8,3,6,4]
bins =[0,3,6,9]
labels=['low','mid','high']
cat=pd.cut(data,bins,True,labels=labels)
print(cat)