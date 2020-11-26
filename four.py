#函数自定义
def sum(x,y):
    return x+y
res=sum(1,2)
print(res)

i = lambda x:x**2
re = i(5)
print(re)

#自定义序列求偶数的个数
def xu(x):
    z=0
    for i in x:
        if i%2==0:
            z=z+1
    return z
p=xu([1,2,3,4,5])
print(p)

#面向对象
class Human:
    def __init__(self,sex=None,age=None):
        self.sex=sex
        self.age=age

    def sq(self,x):
        return x**2

zhangfei=Human(age=23,sex="男")
res=zhangfei.sq(10)
res=zhangfei.sex
print(res)

