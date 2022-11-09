number1 = int(input("insert first number"))
number2 = int(input("insert second number"))
print(f'sum of your numbers is equal: {number1 + number2}')
print(f'subtraction of number is equal: {number1 - number2 }'}
print(f'multiplication of your numbers is equal to: {number1 * number2}')
print(f'integer division of your numbers is equal to: {num1ber // number2}')
print(f'residual division of your numbers is equal to: {number1 % number2}')
print(f'division of your numbers is equal to: {number1 / number2}')
      
      def lg(num:int):
      if num == 1: 
           return 0
      res = 1
      count = 0
      while res < num:
          res *= 10
          count += 1
      return count

print(f' lga of your numbers is equal to: {lg(number1)}')      
