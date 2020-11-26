hours = int(input("请输入时长:"))
rate = int(input("请输入速率:"))
Money=hours*rate
if hours>40:
    Money+=0.5*rate*(hours-40)
    print(Money)
else:print(Money)


score=float(input("请输入您的分数:"))
if score<0 or score>1:
    print("输入错误")
elif score<0.6:
    print('F')
elif score<0.7:
    print('D')
elif score<0.8:
    print('C')
elif score<0.9:
    print('B')
else:print('A')