a,b,c=map(float,input().split())


s=(a+b+c)/2
A=s*(s-a)*(s-b)*(s-c)
S=A**0.5
print('%.2f'%S)