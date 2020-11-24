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

hist1, bins1 = np.histogram(x1.ravel(), 255, range=[0, 255])
hist2, bins2 = np.histogram(x2.ravel(), 9, range=[0, 9])
print(hist1)
print(bins1)
print(hist2)
print(bins2)

print(np.max(hist1))
print(np.amax(hist2))
print(np.where(hist1 == np.amax(hist1)))
print(np.where(hist2 == np.amax(hist2)))
bin1_max = np.where(hist1 == hist1.max())
print('maxbin1', bins1[bin1_max[0][0]])
bin2_max = np.where(hist2 == np.amax(hist2))
print('maxbin2', bins2[bin2_max[0][0]])

unique, counts = np.unique(x2.ravel(), return_counts=True)
print(dict(zip(unique, counts)))

# g1 = plt.figure(1)
# arr1 = plt.hist(x1.ravel(), bins=256, range=[0, 255])
# for i in range(256):
#     strData=""
#     if arr1[0][i] > 1.0:
#         print(arr1[0][i])
#         strData = str(arr1[0][i])
#     plt.text(arr1[1][i], arr1[0][i], strData)
# g2 = plt.figure(2)
# arr2 = plt.hist(x2.ravel(), bins=9, range=[1, 9])
# print(arr2)
# for i in range(9):
#     strData=str(arr2[0][i])
#     # if arr2[0][i] > 1.0:
#     #     strData = str(arr2[0][i])
#     #else ""
#     plt.text(arr2[1][i], arr2[0][i], strData)
# plt.show()


# cv2.imwrite('img1.png', x1)
# cv2.imshow("image", np.uint8(x1))
# cv2.waitKey()
