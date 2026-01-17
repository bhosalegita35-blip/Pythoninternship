# def fib(n):
#     if n<=1:
#         return n
#     return fib(n-1)+fib(n-2)
# n=5
# for i in range(n):
#      print(fib(i),end="")
# def factorial(n):
#     if n == 0:
#         return 1   # Base Case
#     else:
#         return n * factorial(n - 1) # Recursive Case
#     print(factorial)
# n=int(input("Enter a number:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print("factorial is",fact)
# n=int(input ("Enter a number:"))
# i=1
# fact=1
# while i<=n:
#     fact=fact*i
#     i+=1
# print("factorial is ",fact)
# s=input("Enter a string:")
# count=0
# for v in "aeiouAEIOU":
#     count+=s.count(v)
# print(count)
def count_V(s):
    count=0
    for ch in s:
        if ch.lower()in "aeiou":
            count+=1
    return count
text=input("Enter a string:")
print(count_V(text))