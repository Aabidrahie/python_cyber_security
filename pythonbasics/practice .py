size = int(input("Enter the size of a list: "))
lst = []
temp = 0
for i in range(size):
	element = input("Enter the value of the list element:	")
	lst.append(element)
print(lst)

for j in range(0,len(lst)//2):
	temp = lst[j]
	lst[j] = lst[size-j-1]
	lst[size-j-1] = temp
print(lst)
