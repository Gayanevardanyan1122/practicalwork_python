def same_parity(n:int, *args:int):
        '''this function returns the list that consists of the arguments of
        this function that are divided to n.'''
        lst = []
        for num in args:
             if num % n == 0:
                 lst.append(num)
        return lst 

print(same_parity(11, 20, 44, 48))
