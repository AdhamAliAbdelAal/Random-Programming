temp=input()
index=temp.find(" ")
n=int(temp[:(index+1)])
m=4*60-int(temp[index:])
if n>=1:
    sum=int(n/2*(n+1))
else:
    sum=0
totalMin=5*sum
numOfQ=n
for i in range(n,0,-1):
    if totalMin>m:
        totalMin-=(5*i)
        numOfQ=i-1
print(numOfQ)


    