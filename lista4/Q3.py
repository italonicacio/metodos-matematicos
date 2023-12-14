import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# Termo geral da serie
def a(n):
    return 1/(np.sqrt(n+1)*np.sqrt(n)*(np.sqrt(n+1)+np.sqrt(n)))


# Dados iniciais
Kmin = 1
Kmax = 15

k = []
Sk = []
Sk_total = 0

for n in range(Kmin, Kmax+1):
    Sk_total += a(n) 
    k.append(n)
    Sk.append(Sk_total)


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


