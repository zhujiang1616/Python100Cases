'''
def Fib(n):
    return 1 if n<=2 else Fib(n-1)+Fib(n-2)
print(Fib(int(input())))
    

target=int(input())
res=0
a,b=1,1
for i in range(target-1):
    a,b=b,a+b
print(a)
'''
'''
# def fib(max):
#     i,a,b = 0,1,1
#     while i < max:
#         print(b)
#         a,b = b, a+b
#         i +=1
#     return 'done'
# f = fib(12)
# print(f)
'''
'''
# def fib(max):
#     i,a,b = 0,1,1
#     while i < max:
#         yield b
#         a,b = b, a+b
#         i +=1
#     return 'done'
# for n in fib(8):
#     print(n)
'''
