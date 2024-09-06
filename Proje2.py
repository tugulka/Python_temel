
l=[[1, 2], [3, 4], [5, 6, 7],8]
def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst)):
        if isinstance(lst[len(lst)-i-1], list):
            l=reverse_list(lst[len(lst)-i-1])
            reversed_list.append(l)
        else:  
            reversed_list.append(lst[len(lst)-i-1])
    return reversed_list
print(reverse_list(l))