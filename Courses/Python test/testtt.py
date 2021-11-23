def any(**f):
    print(f["n"])
def any2(*adham):
    print(sum(adham))
#any(n=1,d=2,g=3,t=4)
#any2(1,2,3,4)
string=""
x=[]
n=int(input())
for i in range(0,n):
    x.append(int(input()))
for i in range(0,n):
    if(x[i]>45):
        print(-1)
    else:
        for j in range(9,-1,-1):
            if(x[i]-j>=0):
                string+=(str(j))
                x[i]-=j
            else:
                string+=(str(x[i]))
                break
        string="".join(sorted(string))
        if string[0]=="0":
           print(string[1:]) 
        else:
            print(string)
        string=""

