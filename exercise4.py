def money(x,y):
    return x*0.10 + y*0.25

x = float(input("1 liter and less: "))

y = float(input("more than a liter"))
print(f'your money is {money(x, y)}$')
