import numpy as np

# indexing : 리스트에 있는 값에 접근하기 위해 이 값의 상대적인 주소(offset)를 사용하는 것
    # 파이썬이랑 같음

x = np.array([[1, 2, 3], [4, 5, 6]], dtype= int)
print(x[0][0], x[0, 2])
# x[0, 2]도 정상적으로 출력됨, x[0][2]와 같음

x[0, 1] = 100
print(x)
# 배열 안의 값도 변경 가능

# slicing : 리스트의 인덱스를 사용해 전체 리스트에서 일부를 잘라내어 반환하는 것
    # 차원의 구분은 반점(,)으로 하는 것 말고는 파이썬 슬라이싱과 같음

y = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]], int)
print(y[:, 2:])     # 전체 행, 2열 이상
print(y[1, 1:3])    # 1행, 1~2열
print(y[1:3])       # 1~2행, 전체 열
print(y[:, ::2])    # 전체 행, 전체 열에서 2단계씩만