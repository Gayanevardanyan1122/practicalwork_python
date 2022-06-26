def is_growing(lst):
        for ind in range(len(lst)):
              for ind1 in range(ind + 1, len(lst)):
                     if lst[ind] >= lst[ind1]:
                           return False
        return True

def is_decreacing(lst):
        for ind in range(len(lst)):
              for ind1 in range(ind + 1, len(lst)):
                    if lst[ind] <= lst[ind1]:
                           return False
        return True 

lst = [3, 10, 30, 88]
if is_growing(lst) or is_decreacing(lst):
        print("Your list is regulated!")
else:
        print("your list is NOT regulated!")
