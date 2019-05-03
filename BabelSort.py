import random
def babel(t):
    n=len(t)
    for j in range(n-1, 0, -1):
        for i in range(j):
            if t[i] > t[i+1]:
                t[i],t[i+1] = t[i+1],t[i]
    return t
########################
t = []
for i in range(0,5):
    x = random.randint(0,100) #random.random() - liczba z zakresu 0-1
    t.append(x)
##############
print(t)
babel(t)
print(t)


