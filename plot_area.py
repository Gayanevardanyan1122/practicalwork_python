def area(lenght: float, wight:float):
    return lenght * wight
    
x = float(input("Insert lenght: "))
y = float(input("insert wight: "))
print(f'the area of plot is {area(x, y)} pound = {area(x,y)/43560} acre')
