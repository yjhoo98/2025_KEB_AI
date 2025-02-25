#assignment
#v1.0 day12 파일의 결측치 값->산술평균으로 채우기(without sklearn)

import numpy as np
import pandas as pd
# from sklearn.impute import SimpleImputer

df=pd.DataFrame(
    {
        'A':[1,2,np.nan,4],
        'B':[np.nan,2,3,4],
        'C':[1,2,3,4]
    }
)
# i=SimpleImputer(strategy='mean')
# df[['A','B']]=i.fit_transform(df[['A','B']])


df.fillna({'A': df['A'].mean()}, inplace=True)

df.fillna({'B': df['B'].mean()}, inplace=True)
print(df)