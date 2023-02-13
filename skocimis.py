x,y,z = input().split()

x = int(x)
y = int(y)
z = int(z)

a = z-y
b = y-x

if(a > b):
    print(a-1)
else:
    print(b-1)
