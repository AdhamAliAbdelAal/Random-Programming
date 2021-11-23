if True :
    print("Ahahha true")
x=8
y=6#578543
if x>y:
    print("X>y\n")
elif y>x:
    print("X<y\t")
else:
    print("Ana ana")
if x>y:
    print("X>y\n")
    if y>x:
        print("X<y\t")
    else:
        print("Ana ana")
print(3 and 4)
print(3 or 4)
print(not 4)
if False or True and False:
    print("Welcome Back To My Home")
if True or True and False:
    print("Welcome Back To My Home")
l1=[1,2,3]
l2=[1,2,3]
print(l1==l2)
print(id(l1))
print(id(l2))
print(l1 is l2)#is l1 alias to l2 or not
#aliasing
#x1=8
#x2=x1
#x2=5
#print(x1,x2)
#print(x1 is x2)
l2=l1
print(id(l1))
print(id(l2))
print(l1 is l2)