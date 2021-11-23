def test (mylist):
    for i in mylist:
        yield i

for i in (test([1,2,3,4])):
    print (i)
#print ([i*i for i in [1,2,3,4]])
gen =(i*i for i in [1,2,3,4])
for i in gen:
    print(i)
# for i in range(100):
#     print(i)