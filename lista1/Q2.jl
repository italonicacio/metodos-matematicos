using DataFrames
using Plots


# Dados Iniciais
# Como termo geral da sequencia, o valor de M e a formula para achar N
a(n) = n^2
M = 36
N = M
Nmax = N+N

an_s = []
n_s = []
for i = 1:Nmax
   append!(an_s, abs(a(i)))
   append!(n_s, i)
end

df = DataFrame(n = n_s, an = an_s)
print(df)
x = N: 1 : Nmax
y = [M for i = x]
y_2 = [i for i = x]
Y = [y, y_2]

plot(x, Y,label=["M" "(n, |an|)"], lw=5, ls=[:solid :dot])