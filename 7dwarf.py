dwarf_list=[]*9
for i in range(9):
    dwarf_list.append(int(input())) 

dwarf_list.sort()

sum_all=sum(dwarf_list)


#전체 index는 0부터 8까지 있음
one=0
two=0
for i in range(0,8):#0부터 7까지
    for j in range(i+1,9):
        new_sum=sum_all-dwarf_list[i]-dwarf_list[j]
        if new_sum==100:
            one = dwarf_list[i]
            two = dwarf_list[j]
        
dwarf_list.remove(one)
dwarf_list.remove(two)
            
for i in dwarf_list:
    print(i)


