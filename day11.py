from traceback import print_tb

import numpy as np
ones=np.ones((3,4))
print(ones)
# zeros=np.zeros((3,4))
zeros=np.zeros((3,4),dtype=np.int16)
print(zeros)
zeros2=np.zeros((2,3,4))
print(zeros2,zeros2.dtype)
# a=np.arange(5,11,2)
# print(a,a.ndim,a.shape,a.size)
# a=np.arange(2.0,11.8,0.2)
# print(a,a.ndim,a.shape,a.size)
a=np.arange(2.0,11.8,2.0,dtype=np.int16)
print(a,a.ndim,a.shape,a.size)
#linsapce():지정된 범위 내에서 균등하게 분할된 숫자가 담긴 배열을 생성하는 함수
#reshape():배열의 모양(shpae)을 변경하는 메서드로,새로운 모양에 맞게 요소들을 재배열
