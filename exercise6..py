def sum(num:int):
     sum = 0
     for number in range(num):
         sum += number
     return  sum
  
n = int(input("insert the number: "))
print(f'the sum of integers in interval 0 to {n} is equal: {sum(n)}')
