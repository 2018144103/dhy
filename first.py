import  os
path=os.getcwd()
print(path)
 #print('hello word')
string = 'hello word'
f = open('hello,txt','w')
f.write(string)
f.close()

曲靖528=['翁晨生','谢立冬','段皓洋']
曲靖528.append('李仙荣')
for i in 曲靖528:
    print(i)



import math
a = -1.5
res = abs(a)
print(a)
q=math.sin(res)
print(q)

all_in_list=[12,'翁畜生',True,'姁漂亮']
w = all_in_list[0:2]
x = all_in_list[-1]
print(x)

all_in_list.append('hello maxu')
all_in_list.insert(0,'dhy')
all_in_list.remove(12)
del all_in_list[0:1]
print(all_in_list[-1])

for i in range(10):
    print(i)

c = [i for i in range(1,11)]
b=[i**2 for i in range(1,11) if i%2==0]
print(c)
print(b)



import math
n=10
width=2*math.pi/n
#方法一：
x=[]
y=[]
for i in range(n):
    x.append(i*width)
for i in x:
    y.append(abs(math.sin(i)))
p=sum(y)*width
print(p)
#方法二
s=[ abs(math.sin(width*i))*width for i in range(n)]
print(sum(s))
