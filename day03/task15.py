'''
n1 =int(input("Enter the starting number : "))
n2 =int(input("Enter the ending  number : "))


for i in reversed(range(n2,n1+1,3)):
    print(i)
    '''
print("strating :")
n1=int(input())
print("ending :")
n2=int(input())
while n1>=n2:
    print(n1)
    n1=n1-3