import random
num=[]
aux=0
for i in range (10):
    aleatorios=random.randrange(1,30)
    num.append(aleatorios)
print (num)

for i in range (9):
    for j in range(9):
        if num[j] > num[j+1]:
            aux=num[j]
            num[j]= num[j+1]
            num[j+1]= aux

print (num)