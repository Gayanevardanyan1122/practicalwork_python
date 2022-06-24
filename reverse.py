number= int(input("insert a number: "))
reverse_num = 0
while number != 0:
     reverse_num *= 10
     reverse_num += number % 10
     number = number // 10
print (f'your reverse number is equal:{reverse_num}' )    
