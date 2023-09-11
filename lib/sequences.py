#!/usr/bin/env python3

def print_fibonacci(length):
   fib = []

   for i in range(length):
      if i == 0 or i == 1:
         fib.append(i)
      else:
         n = fib[len(fib)-1] + fib[len(fib)-2]
         fib.append(n)
   print(fib)

print_fibonacci(10)

