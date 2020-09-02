import numpy as np
import matplotlib.pyplot as plt

def norm(x):
    return np.sqrt(np.sum(np.square(x)))


m1 = np.array((2, -1, 1)).reshape(3, 1)
m2 = np.array((3, -5, 2)).reshape(3, 1)
m1xm2 = np.cross(m1.T, m2.T).reshape(3,1)


A1 = np.array((1, 1, 0)).reshape(3, 1)
A2 = np.array((2, 1, -1)).reshape(3, 1)
diff_A = A2-A1

norm_m1xm2 = norm(m1xm2)

dist = (np.matmul(diff_A.T, m1xm2))/norm_m1xm2
print("The shortest distance between the 2 lines is",str(dist[0][0]))
