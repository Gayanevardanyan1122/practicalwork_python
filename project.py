def num1(tpl):
    m = len(tpl) - 1
    d=0
    for num in tpl:
        d+= num * 10**m
        m-=1
    return d
tpl = (1, 2, 3)   
print(f' number is: {num1(tpl)}' )
        
