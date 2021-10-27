def getNums(list):
    max_val=None
    for i in list:
        if max_val==None or i>max_val:
            max_val=i
    return max_val

lst=[1,2,3,4,8,5,6]
nums=getNums(lst)
print(nums)