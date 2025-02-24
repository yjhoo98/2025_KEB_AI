#assignment:최근접 이웃 모델을 커스텀 클래스로 설계

# from sklearn.linear_model import LinearRegression

from yjhlearn import KNeighborRegressor
import pandas as pd
import matplotlib.pyplot as plt
ls =pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")

X=ls[["GDP per capita (USD)"]].values
y=ls[["Life satisfaction"]].values

ls.plot(kind='scatter',grid=True,
        x="GDP per capita (USD)",y="Life satisfaction")
plt.axis([23_500,62_500,4,9])
plt.show()
model=KNeighborRegressor(n_neighbors=3)

model.fit(X,y)

X_new=[[37655.2]]
print(model.predict(X_new))
#LinearRegression 6.30