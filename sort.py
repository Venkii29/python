len_list = int(input("enter the len the lists : "))
list = []
for i in range (len_list):
    element  = int(input(f"enter num {i+1} : "))
    list.append(element)
print("unsorted list",list)
for i in range (len_list):
    for j in range (len_list):
        if list[i+j] > list[j+1]:
            list[i+j],list[j+1]=list[j+1],list[i+j]
print("sorted list",list)
