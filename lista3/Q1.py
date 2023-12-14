import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#OBS:   existe um erro número onde a sequencia começa a partir de 0, pensei em colocar para começar de vez fazer um floor, como é mostrado na linha 16
#       Com o Nmin decidi deixar assim mesmo e podendo desconsiderar o primeiro apenas por desconhecer como tratar o erro.


# Questão 1
# (e) (n**2)/(n+1) - (n**2)/(n+2)
def a(n):
    return (n**2)/(n+1) - (n**2)/(n+2)

L = 1.0 # Foi usado 1.0 para essa expressão pois fica melhor para o computador float com outros floats do que um inteiro com floats
epsilon = 1e-3 # Epsilon
Nmin = int(abs((1/2)*( (np.sqrt(epsilon*(8+epsilon)))/(epsilon - 1) - ((3*epsilon)/(epsilon -1) ))))# Nmin
Nmax = int(Nmin+10) # É feito dessa forma para Nmax ser os 10 numeros posteriores a Nmin

an_s = [] # Array que armazena os valores de a(n)
n_s = [] # Array com os indices de n correspodentes a a(n)


# Construindo os dados para fazer a tabela e o plot dos graficos
for i in range(Nmin, Nmax+1):
    an_s.append(a(i))
    n_s.append(i)

# Construção da tabela utilizando o pandas
# OBS: fica melhor visivel a tabela utilizando um ambiente jupyter como o colab ou o proprio jupyter
data = [n_s, an_s] #Dados da tabela
columns = ["a(n)"] # Nomenclatura da coluna com os termos de a(n)
df = pd.DataFrame(data = an_s, columns=columns, index=n_s) 
# index é para definir os indicies de a(n) como n a partir de n min, 
# se n por padrão vai de 0 até o tamanho da lista
print(df) # Print da tabela no terminal


# Construção do Grafico
x = np.arange(Nmin, Nmax, 1)
y = [L for i in x]
y_min = [L - epsilon for i in x]
y_max = [L + epsilon for i in x]
legend = ['L + epsilon', 'L', 'L - epsilon']

plt.scatter(x=x, y=y_min)
plt.scatter(x=x, y=y)
plt.scatter(x=x, y=y_max)
plt.legend(legend)
plt.show()


