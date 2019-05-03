import random
def babel(t):
    n=len(t)
    for j in range(n-1, 0, -1):
        for i in range(j):
            if t[i] > t[i+1]:
                t[i],t[i+1] = t[i+1],t[i]
    return t
########################
def selection(t):
    n=len(t)
    for i in range(n-1):
        k=i
        for j in range(i+1, n):
            if t[j]<t[k]:
                k=j
        t[k],t[i] = t[i], t[k]
    return t

t = []
for i in range(0,5):
    x = random.randint(0,100) #random.random() - liczba z zakresu 0-1
    t.append(x)
##############
print(t)
#babel(t)
selection(t)
print(t)


