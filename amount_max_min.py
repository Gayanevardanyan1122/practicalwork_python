def max_min(lst):
    max = lst[0]
    min = lst[0]
    for num in lst:
        if num > max:
            max = num
        if num < min:
            min = num
    sum = min + max 
    return sum

lst = [1, 4, 6, 10]   
print(max_min(lst))
