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
# 
# def countdown():
#     for i in range(10,-1,-1):
#         print(i)
# countdown()
# def countdown(n):
#     if n <= 0:  # Base case
#         print("Blast off!")
#     else:
#         print(n)
#         countdown(n - 1)  # Recursive call
# countdown(5)
# def calc():
#     list=[10,15,52,85,80]
#     total=sum(list)
#     avrage=total/len(list)
#     print(f"sum is {total},and Average is {avrage} ")
# calc()
# def sum_and_average(numbers):
#     total = sum(numbers)              # Calculate sum
#     avg = total / len(numbers) if numbers else 0  # Avoid division by zero
#     return total, avg                 # Return both values as a tuple

# # Example usage:
# nums = [10, 20, 30, 40]
# result = sum_and_average(nums)

# print("Sum:", result[0])
# print("Average:", result[1])
# def T_marks(*marks):
#     return sum(marks)
# total=T_marks(10,20,50,90,60,30,40,70)
# print("total marks",total)                    
# numbers = [1, 2, 3, 4, 5]
# squares = [n**2 for n in numbers]
# print(squares)   # Output: [1, 4, 9, 16, 25]
# [expression for item in iterable if condition]
# expression → what to put in the list

# item → variable representing each element

# iterable → source (list, range, etc.)

# condition → optional filter