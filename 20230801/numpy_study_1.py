# 넘파이의 특징
    # 일반적인 리스트보다 속도가 빠르고 효율적인 메모리 사용이 가능
    # 반복문을 사용하지 않음
    # 다른 언어와 통합 사용 가능
# 넘파이 배열
    # 파이썬의 리스트와 같이 넘파이에서 텐서 데이터를 다루는 객체
        # 텐서(tensor) : 선형대수에서 사용하는 데이터 배열
            # 데이터 배열의 랭크에 따라 별도의 용어 존재
                # Rank 0 : 스칼라, Rank 1 : 벡터, Rank 2 : 행렬, Rank n : n차원 텐서

import numpy as np

test_1 = np.array([1, 4, 5, "8"], float)
print(test_1)

# np.array에서 m * n 크기의 배열을 만들고자 할 때, 비어있는 칸이 있으면 안 됨
# 파이썬 리스트는 메모리 주소만 순서대로 나열, 넘파이 배열은 실제 값을 연속적으로 나열
    # 파이썬 리스트는 동적 메모리 할당 가능, 넘파이 배열은 동적 메모리 할당 불가능

print(type(test_1[3]))
# <class 'numpy.float64'> => 64 : 칸 당 64비트(8바이트), 32 : 칸 당 32비트(4바이트)

print(test_1.dtype)
# dtype : 배열 전체의 데이터 타입 반환

print(test_1.shape)
# shape : 배열의 구조를 튜플 형식으로 반환, rank 2 이상일 때는 (x, y, z)형식으로 반환

print(test_1.ndim, test_1. size)
# ndim : 차원의 크기 or rank, size : 해당 넘파이 배열에 있는 모든 데이터의 개수 (x * y * z)

print(np.array([[1, 2, 3.5], [4, 5, 6.5]], dtype= int))
# dtype : dtype에 해당하는 형태로 변환

import sys
print(np.array([[1, 2, 3.5], [4, 5, 6.5]], dtype= np.float32).itemsize)
# itemsize : 각 요소의 크기 출력