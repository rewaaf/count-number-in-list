lst = [[1,1],[1,1],[1,0],[1,1],[1,0,1,1],[0,1],[0,0,1]]
counter_one = 0
for item in lst:
    counter_one += item.count(1)
print('number of ones in: ',str(lst),'is: ',str(counter_one))
