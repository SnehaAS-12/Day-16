#Create a lambda function that multiplies argument x with argument y
a= lambda x, y : x * y
print("Result : ",a(100, 3))


#Python program to create Fibonacci series to n using Lambda
from functools import reduce
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2), [0, 1])
print("\nFibonacci series :")
print(fib_series(10))


#Python program that multiply each number of given list with a given number 
nums = [2, 4, 6, 9 , 11]
n = 2
print("\nOriginal list : ", nums)
print("Given number : ", n)
filtered_numbers=list(map(lambda number:number*n,nums))
print("Result : ")
print(' '.join(map(str,filtered_numbers)))


#Python program to find numbers divisible by 9 from a list of numbers 
my_list = [2,10,24,12,35,27,54,34]
result = list(filter(lambda x: (x % 9 == 0), my_list))
print("\nNumbers divisible by 9 are : ",result)


#Python program to count the even numbers in a given list of integers 
list1= [3,2,4,5,7,6,1,8,0,9]
even = len(list(filter(lambda x: (x%2 == 0) , list1)))
print("\nNumber of even numbers in the given list : ", even)