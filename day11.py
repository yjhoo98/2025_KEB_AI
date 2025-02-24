# from statistics import LinearRegression
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
import pandas as pd
import matplotlib.pyplot as plt
ls =pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
# print(ls)
X=ls[["GDP per capita (USD)"]].values
y=ls[["Life satisfaction"]].values
# print(y)
# ls.plot(kind='scatter',grid=True,
#         x="GDP per capita (USD)",y="Life satisfaction")
# plt.axis([23_500,62_500,4,9])
# plt.show()
# model=LinearRegression()
model=KNeighborsRegressor(n_neighbors=3)
model.fit(X,y)

X_new=[[37655.2]]
print(model.predict(X_new))
#LinearRegression 6.30