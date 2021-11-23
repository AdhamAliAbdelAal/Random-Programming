List=["adham",2,3,"mohy"]
print(List)
print(len(List))
print (List[-1])#access the last element in list
print(List[-2])
#print(List[-5]) error in index
print(List[-4])
print(List[:3])
List.append("adding")
print(List)
List.insert(len(List)+5,"Adding2")
print(List)
list2=["one","two"]
List.extend(list2)
print(List)
List.remove("one")#don't return value
message=List.pop()#return deleted obj
print(message)
print(List)
List.reverse()
print(List)
num1=[34556,2434,2311]
num2=[1,2,3]
num1.sort()#change the base list
num2.sort(reverse=True)
print(num1)
print(num2)
num3=sorted(num2)#don't change the base list
print(num3)
print(sum(num3))
print(max(num3))
print(List.index("mohy"))
print("hdfsg" in List)
for i in List:
    print(i)
    print(i) 
for i in enumerate(List):
    print(i)
    print(i) 
for i,j in enumerate(List):
    print(i,j)
    print(i,j) 
for i,j in enumerate(List,start=1):
    print(i,j)
    print(i,j)
k=["Adham","Ali","Sayes"] 
d=' - '.join(k)#k must be list to string only
print(d)
k2=d.split('A')
print(k2)
print(d)
list_1=["a",'b','c']
list_2=list_1
list_1[0]=9
print(list_1,list_2)
tup1=('a',4,4,4,4,4,4,4,'b','c')
tup2=tup1#
print(tup1)
#tup1[0]=9 error
print(tup1,tup2)
set1={1,2,3}
print(tup1.count(4))
#set1[0]=7 error
set2=set1
print(set1.intersection(set2))
print(set1.difference(tup1))
print(dir(tuple))
#tup1.extend(tup2) error
ad=[1,2,3,4]
sub=[5,6,7]
#ad.insert(0,sub)
#ad.extend(sub)
#print(ad[0][0])
#print(ad.find(0))
#for i in enumerate(ad,start=0,step=2):
  #  print(ad[i])
for i,j in enumerate(ad,start=0):
    print(i,j)
ab=['adham','mo','hamza']
ad=ab
aa=ab
print(len(ad))
ab=' - '.join(ab)
ad.append('mariam')
print(ab)
print(aa)
print(ad)
gg={1,2,3}
hh={1,2,4}
uu=gg.union(hh)
print(uu)
print(gg.intersection(hh))
ooo=777 in ad
print(ooo)
for i in range(1,5,2):
    print("h")