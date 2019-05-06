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
########################
def insertion(t):
    n=len(t)
    for i in range(1,n):
        pom = t[i]
        k = i - 1
        while k >= 0 and t[k] > pom:
            t[k+1] = t[k]
            k -= 1
        t[k+1] = pom
    return t
######################
def line_sort(t,m):
    n=len(t)
    P= []
    for i in range(m):
        P.append(0); ### może szybciej?
    for i in t:
        P[i]+=1;
    k = 0
    for i in range(m):
        for j in range(P[i],0,-1):
            t[k]=i
            k+=1
    return t
######################
def quickSort(t,lewy,prawy):
    n=len(t)
    i,j=lewy,prawy
    v = t[(lewy+prawy)//2]
    while i<=j:
        while t[i] < v:
            i+=1
        while t[j] > v:
            j-=1
        if i <= j:
            t[i],t[j] = t[j],t[i]
            i,j=i+1,j-1
    if lewy<j:
        quickSort(t,lewy,j)
    if prawy>i:
        quickSort(t,i,prawy)
######################
t = []
for i in range(0,10):
    x = random.randint(0,100) #random.random() - liczba z zakresu 0-1
    t.append(x)
##############
print(t)
#babel(t)
#selection(t)
#insertion(t)
#line_sort(t,100)
quickSort(t,0,9)
print(t)


