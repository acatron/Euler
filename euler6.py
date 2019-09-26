def sum_square(num):
  s = 0
  for i in range(1, num + 1):
        s += i ** 2
  return s

def sum_of_squares(num):
  s = 0
  for i in range(1, num + 1):
        s += i
  return s**2 

print (sum_of_squares(100)-sum_square(100))