print ('Hello, sparta')
a = 3
print (a)
b = a
print (b)
a = a+1
print(a)
print(b)
num = a*b
print(num)
b = 4
print(a*b)
print(num)

name = '조용현'
print(name)
number = '33'
print(number)
print(number+str(a))
print(number+name)
print(int(number)+a)

is_true = True
print(is_true)

a_list = []
a_list.append(1)
print(a_list)
a_list.append(2)
print(a_list)
a_list.append(3)
print(a_list)
a_list.append([4,5,6])
print(a_list)

a_dict = {'name':'조용현','age':27}
print(a_dict)
a_dict['level'] = 5
print(a_dict)
a_list.append(a_dict)
print(a_list)

b_list =[]
b_dict ={'name': 'ashely','age': 27}
b_list.append(b_dict)
print(b_list)
b_dict['level'] = 7
print(b_list)

#b_list = None
if b_list is not None:
    print(b_list)


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

result = is_even(19)
print(result)


def sum_all(a,b,c):
    return a+b+c
print(sum_all(3,4,5))


def is_adult(num):
    if num >= 20:
        return True
    else:
        return False
print(is_adult(29))

def check_generation(num):
    if num >= 40:
        return 'x세대'
    elif num <= 20:
        return 'gen Z'
    else:
        return '밀레니얼'

print(check_generation(18))
print(check_generation(46))
 # 자바스크립트의 {}는 파이썬에서 :로, else if 는 elif 로!

fruits =['apple','pear','cherry','mandarin','cherry']
for fruit in fruits:
    print(fruit)


def count_fruits(name):
    count = 0
    for fruit in fruits:
        if fruit == name:
            count += 1
    return count

print(count_fruits('cherry'))
cherry_count=count_fruits('cherry')
print(cherry_count)

