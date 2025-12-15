#내풀이 
def Fibo(n):
   if n==1:
      result=0
   elif n==2:
      result=1
   elif n>0:
      result=Fibo(n-1)+Fibo(n-2)
   return result

n=int(input())
print(Fibo(n+1))

#chatgpt의 답변
'''
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = 10
fib_n = fibonacci(n)
print(f"The {n}-th Fibonacci number is {fib_n}.")
'''
