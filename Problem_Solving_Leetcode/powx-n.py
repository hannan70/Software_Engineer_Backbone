def myPow(x:float, n:int):
     temp = n
     n = abs(n)
     res = 1.0
     while n > 0:
         if n%2 == 1:
             res *= x
         x*=x
         n //= 2

     if temp < 0:
         res = 1.0 / res

     return res


x = 2.10000
n = 3
print(myPow(x, n))
