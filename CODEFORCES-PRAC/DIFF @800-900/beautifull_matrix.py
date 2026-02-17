import numpy as np
arr = np.array[(5,5)]
print(arr)
for i in range(5):
    for j in range(5):
        arr[i][j] = map(int,input().split())