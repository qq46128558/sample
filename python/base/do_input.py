# 输入和输出
# print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出：
# print()会依次打印每个字符串，遇到逗号“,”会输出一个空格
print ('welcome','back','kate!')
print('100 * 6 =',100*6)

# 输入是Input，输出是Output，因此，我们把输入输出统称为Input/Output，或者简写为IO。
name=input('Please input a name:')
print('welcome back',name+'.')

age=input('Please input you age:');
if int(age)>=18:
    print('Adult.')
else:
    print('Teenager.')