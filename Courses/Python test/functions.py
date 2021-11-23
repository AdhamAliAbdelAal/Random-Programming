"""def func1(st,n='ali'):#like declaration
    pass
print(func1)#print the adress of the func1
print(func1("s"))"""#print the return type of the func1
def func1(st,n='ali'):
    print("func1") 
    return "{} {}".format(st,n)
print(func1)#print the adress of the func1
print(func1('adham'))#print the return type of the func1
def func2(x=4,y=1):
    return x,y
print(func2(x=1,y=2))
k=func2(x=1,y=2)
print(k[0])
#k[0]=1