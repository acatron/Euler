def prime_iteration():

  max = 110000 //set ceiling for number iteration
  min = 1
  count = 0 //set count

  print("Prime numbers between",min,"and",max,"are:")

  for num in range (min, max +1):
    if num > 1:
      for i in range (2, num):
        if (num % i) == 0:
          break
      else:
        count = count + 1 // add to count
        print(num, "Count is: ", count) // print prime number and count
        

print(prime_iteration()) //used to help solve euler problem 7