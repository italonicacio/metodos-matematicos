using DataFrames
using Plots


# Dados Iniciais
# Como termo geral da sequencia, o ϵ o valor L
a(n) = n/(n+1)
L = 1
ϵ = 1e-6
Nmax = 20
N = 1/ϵ - 1

an_s = []
n_s = []
for i = 1:Nmax
   append!(an_s, a(i))
   append!(n_s, i)
end

df = DataFrame(n = n_s, an = an_s)
print(df)
x = N: 0.5 : N+Nmax
y = [L for i = N:0.5:N+20]
y_min = [L - ϵ for i = N:0.5:N+20]
y_max = [L + ϵ for i = N:0.5:N+20]
Y = [y_min, y,y_max]

p = plot(x, Y,label = ["L - ϵ" "L" "L + ϵ"], lw=5)




