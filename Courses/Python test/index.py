def DeleteChar(s,i):
   # temp=s[:i]+s[i+1:]
    return s[:i]+s[i+1:]
print('Adham\'s World')
print("Adham's World")
#print("Adham"Ali")
#print('Adham'Ali')
print('Adham"Ali')
#message=""adham testing Multiple ""
#LINE string""
message="""adham testing ""Multiple
LINE string"""
print(message)
print (len(message))
#print (message[330]) index error
print(message[0:1])#means not include the second index
print(message[:3])
print(message[1:])
print (message.upper())
print(message.count("\""))#how many time of appearance
print(message.find("\""))#index
pmessage=message.replace("adham","Doooooom")
print (pmessage)
print (message)#replace don't act at the base
fn ="Adham"
fn=fn.join("r")
print(fn)
ln="Osman"
name=fn+" "+ln
print(name)
name="{} {}".format(fn,ln)#better than concat
print(name)
name=f'{fn.lower()} {ln.  upper()}'
print(name)
#print(dir(str))
#print(help(str))
print(help(str.join))
print(help(str.replace))
dod="hassan"
print(ord("h"))
t="uuuuu"
p=t
t="jjj"
#print(t,p)
"""def test(op):
    op=6
    return op"""
#t=test(t)
#print(t)
t=DeleteChar(t,0)
print(t)
for i in range (0,5):
    print(i)
    i-=1
q=(1,"ggg")
es,me=q
print(es,me)
if(1==1):
    scope=1
    print("test")
print(scope)