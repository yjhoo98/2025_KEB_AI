#assignment
#v1.0 day12 파일의 결측치 값->산술평균으로 채우기(without sklearn)
from statistics import median

import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
# from sklearn.impute import SimpleImputer
import seaborn as sns

titanic=sns.load_dataset('titanic')

median_age = titanic['age'].median()  # 나이 중앙값 산출
titanic_fill_row = titanic.fillna({'age' : median_age})  # 결측치 처리

X = titanic_fill_row[['age']]  # 독립 변수 설정
y = titanic_fill_row[['survived']]  # 종속 변수 설정
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=KNeighborsRegressor(n_neighbors=10)
model.fit(X_train,y_train)
# print(type(titanic))
y_pred=model.predict(X_test)
# print(titanic.head())
#시각화
plt.figure(figsize=(5,2))
plt.scatter(X_test,y_test,color='blue',label='Real')
plt.scatter(X_test,y_pred,color='red',label='Predicted')
plt.title('KNeighborRegressor: Real vs Predicted')
plt.xlabel('Age')
plt.ylabel('Survived')
plt.show()