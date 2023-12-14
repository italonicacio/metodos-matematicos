using DataFrames
using Plots


# Dados Iniciais
# Como termo geral da sequencia, o valor de M, o valor de K
# E um valor inicial N ⋜ Nmax
a(n) = (-1)^(n)
M = 2
K = -2
N = 1
Nmax = 10

an_s = []
n_s = []
for i = 1:Nmax
   append!(an_s, a(i))
   append!(n_s, i)
end

df = DataFrame(n = n_s, an = an_s)
print(df)
x = N: 1 : Nmax
y_M = [M for i = x]
y_K = [K for i = x]
y_an = [a(i) for i = x]
Y = [y_M, y_K, y_an]

plot(x, Y, label=["M" "N" "an"], lw=5, ls=[:solid :solid :dot])