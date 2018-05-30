a = int(input())
b = [a,a*2,a*4]
if a % 2 == 0:
    raise Exception('bushijishu', b)
a = a - 1
print(a)