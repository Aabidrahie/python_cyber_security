lst = [3,4,1,5,2]

for i in range(5):
    temp = 0
    for j in range(i+1,5):
        if lst[i]>lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
print(lst)