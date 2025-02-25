#assignment
#v0.9 day12 파일의 결측치 값->산술평균으로 채우기

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

df=pd.DataFrame(
    {
        'A':[1,2,np.nan,4],
        'B':[np.nan,2,3,4],
        'C':[1,2,3,4]
    }
)
print(df)