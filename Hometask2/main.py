day=int(input())
perc=int(input())
sum=float(input())
for i in range(day):
    sum+=3
sum=(sum/100*perc)+sum
print(sum)