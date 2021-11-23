
def takeinput(s):
    index =s.find(' ')
    if index!=-1:
        temp=int(s[:index])   
        s=s[index+1:]
    else:
        temp=int(s)
    return temp,s
n=int(input())
string=[]
for i in range(0,n,1):
    string.append(input())
for i in range(0,n,1):
    num1,string[i]=takeinput(string[i])
    num2,string[i]=takeinput(string[i])
    min1,string[i]=takeinput(string[i])
    min2,string[i]=takeinput(string[i])
    dec,string[i]=takeinput(string[i])
    num1t=num1
    num2t=num2
    if(num1t-dec>=min1):
        num1t-=dec
    else:
        num1t=min1
    if(num2t-dec>=min2):
        num2t-=dec
    else:
        num2t=min2
    if(num1t<=num2t):
        if(num1-dec>=min1):
            num1-=dec
            dec=0
        else:
            dec=dec-(num1-min1)
            num1=min1
            if num2-dec>=min2:
                num2-=dec
                dec=0
            else:
                num2=min2
    else:
        if(num2-dec>=min2):
            num2-=dec
            dec=0
        else:
            dec=dec-(num2-min2)
            num2=min2
            if num1-dec>=min1:
                num1-=dec
                dec=0
            else:
                num1=min1
    print(num1*num2)