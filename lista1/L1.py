import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def a(n):
    return n/(n+1)

L = 1.0
epsilon = 1e-6
Nmax = 20
N = 1/epsilon - 1

an_s = []
n_s = []

for i in range(1, Nmax+1):
    an_s.append(a(i))
    n_s.append(i)

data = [n_s, an_s]
columns = ["a(n)"]
df = pd.DataFrame(data = an_s, columns=columns, index=n_s)
print(df)

x = np.arange(N, N+Nmax, 0.5)
y = [L for i in x]
y_min = [L - epsilon for i in x]
y_max = [L + epsilon for i in x]
legend = ['L + epsilon', 'L', 'L - epsilon']

plt.scatter(x=x, y=y_min)
plt.scatter(x=x, y=y)
plt.scatter(x=x, y=y_max)
plt.legend(legend)
plt.show()


