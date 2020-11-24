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

print(np.amax(x1))
print(np.amax(x2))


def neighbors(a, radius, rowNumber, columnNumber):
    return [[a[i][j] if i >= 0 and i < len(a) and j >= 0 and j < len(a[0]) else 0
             for j in range(columnNumber - 1 - radius, columnNumber + radius)]
            for i in range(rowNumber - 1 - radius, rowNumber + radius)]

def maxFilter(arr):
    height = arr.shape[0]
    width = arr.shape[1]
    tmp = arr.copy()
    for i in range(height):
        for j in range(width):
            neighborArr = neighbors(arr,1,i+1,j+1)

            tmp[i][j] = np.amax(neighborArr)
    return tmp
#
print(maxFilter(x1))
print(maxFilter(x2))
# print(neighbors(x2,1,7,7))