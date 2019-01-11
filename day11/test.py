print(eval('1+2+x',{'x':3},{'x':30})) #返回33
print(exec('1+2+x',{'x':3},{'x':30})) #返回None

# print(eval('for i in range(10):print(i)'))
#语法错误，eval不能执行表达式
print(exec('for i in range(10):print(i)'))