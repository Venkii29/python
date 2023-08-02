len_list = int(input("enter the len the lists : "))
list = []
for i in range (len_list):
    element  = int(input(f"enter num {i+1} : "))
    list.append(element)
print("unsorted list",list)
for i in range (len_list):
    for j in range (i+1,len_list):
        if list[i] > list[j]:
            list[i],list[j]=list[j],list[i]
print("sorted list",list)
