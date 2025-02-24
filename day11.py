from traceback import print_tb

import numpy as np

v = np.array([1,3,-5,7])
print(v,v.ndim,v.shape,v.dtype)
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b,b.ndim,b.shape,b.dtype,b.strides)
c=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(c,c.ndim)
#ndim:배열의 차원 수
#shape:배열의 차원과 크기를 나타내는 튜플 형태의 속성
#dtype:배열 요소들의 데이터 타입을 나타내는 속성
#strides:배열 요소들 사이의 간격(ex.1차원에서 원소들 사이 간격,2차원에서 배열 사이의,3차원에서 면사이의)
print(c,c.ndim,c.shape)