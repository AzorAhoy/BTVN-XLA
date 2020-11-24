import numpy as np
from matplotlib import pyplot as plt
import cv2

x1 = np.array([[62, 79, 23, 119, 120, 105, 4, 0],
               [10, 10, 9, 62, 12, 78, 34, 0],
               [10, 58, 197, 46, 46, 0, 0, 48],
               [176, 135, 5, 188, 191, 68, 0, 49],
               [2, 1, 1, 29, 26, 37, 0, 77],
               [0, 89, 144, 147, 187, 102, 62, 208],
               [255, 252, 0, 166, 123, 62, 0, 31],
               [166, 63, 127, 17, 1, 0, 99, 30]])

x2 = np.array([[9, 7, 1, 1, 1, 2, 2, 1],
               [8, 9, 9, 7, 1, 1, 1, 1],
               [7, 8, 9, 7, 1, 2, 1, 1],
               [8, 9, 9, 9, 9, 1, 1, 2],
               [8, 9, 9, 7, 7, 2, 1, 3],
               [9, 9, 9, 9, 8, 2, 2, 1],
               [9, 9, 8, 8, 7, 1, 2, 1],
               [8, 9, 8, 6, 5, 1, 1, 3]])

def f1(arr,a, alpha):
    height = arr.shape[0]
    width = arr.shape[1]
    # alpha=0.1
    # a=13
    tmp = arr.copy()
    for i in range(height):
        for j in range(width):
            if arr[i][j] < alpha:
                arr[i][j]=0
            else:
                arr[i][j]= round(alpha*arr[i][j])
    return arr

def f2(arr,L, a,b,beta):
    height = arr.shape[0]
    width = arr.shape[1]
    # alpha=0.1
    # a=13
    tmp = arr.copy()
    for i in range(height):
        for j in range(width):
            if arr[i][j] < L and arr[i][j] >= b:
                arr[i][j]=round(beta*(b-a))
            elif arr[i][j] < b and arr[i][j] >= a:
                arr[i][j] = round(beta*(arr[i][j]-a))
            else:
                arr[i][j] = 0
    return arr

# print(f1(x1,13,0.1))
# print(f1(x2,5,0.3))

print(f2(x1,256,23,67,0.2))
print(f2(x2,9,2,7,0.5))