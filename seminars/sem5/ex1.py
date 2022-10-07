#  HOД

def FindMnoj(n):
    spisok_mnoj = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            spisok_mnoj.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        spisok_mnoj.append(n)
    return spisok_mnoj


n=list(map(int,input('Введите пару чисел через пробел: ').split()))
n1 = FindMnoj(n[0])
n2 = FindMnoj(n[1])
r =[]
print (n1, n2)
for i in range(len(n1)):
    if max(n1) in n2:
        r.append(max(n1))
    n1.pop(len(n1)-1)
print (r)
res=1
for i in range(len(r)):
    res*=r[i]
print(res)