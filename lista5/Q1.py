import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math



# Termo geral da serie
def a(n):
    return 1/n**2
    # return 1/(np.sqrt(n+1)*np.sqrt(n)*(np.sqrt(n+1)+np.sqrt(n)))

def approximation(p, m):
    return ((10**m)/(p-1))**(1/(p-1))

# Dados iniciais
Kmin = 1
Kmax = 15
k = []
Sk = []
Sk_total = 0


# Dados iniciais serie P e o teste da integral
serie_p = True # Colocar true ou falso caso a serie seja ou não P
m = 3
p = 2

for n in range(Kmin, Kmax+1):
    Sk_total += a(n) 
    k.append(n)
    Sk.append(Sk_total)

if serie_p:
    print("K = ", math.ceil(approximation(2, m)))

# Abaixo temos como printar os dados em uma tabela
# # Por padrão vou deixar comentando essa parte
# columns = ["a(n)"] # Nomenclatura da coluna com os termos de a(n)

# # Abaixo estamos criando um objeto do tipo dataframe, onde é passado os dados sendo Sk
# # e o indices senod k
# df = pd.DataFrame(data = Sk, columns=columns, index=k) 

# print(df)

# Plot do Grafico da sequencia
legend = ['Sk']

plt.scatter(x=k, y=Sk)
plt.legend(legend)
plt.show()


