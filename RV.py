from numpy import array

T = array([str] * 60)
for i in range(30):
    T[i] = "R"+str(i+1)
for i in range(30, 60):
    T[i] = "V"+str(i-29)

n = 0
while not(5<= n <=40):
    n = int(input("Enter n (5 <= n <= 40): "))

def indice(ch, T):
    for i in range(60):
        if T[i] == ch:
            return i
    return -1

f = open("livres.txt", "w")
for i in range(n):
    ch = input(f"Referece du livre {i+1} (R1-R30 ou V1-V30): ")
    ind = indice(ch, T)
    while not (ind != -1 and T[ind][-1] != "*"):
        ch = input(f"Referece du livre {i+1} invalide, reessayer: ")
        ind = indice(ch, T)
    T[ind]+= "*"
f.close()

f = open("livres.txt", "w")
for i in range(60):
    if T[i][-1] == "*":
        f.write(T[i][:-1]+"\n")
f.close()

f = open("livresIndisponibles.txt", "w")
for i in range(60):
    if T[i][-1] != "*":
        f.write(T[i]+"\n")
f.close()

print(T)
