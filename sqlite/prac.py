lst1 = ['a','b','a','c','c','d','c','d']
lst2 = []
for mem in lst1:
    if mem not in lst2:
        lst2.append(mem)
    else:
        pass
   
dic = {}
for mem in lst2:
    dic[mem] = lst1.count(mem)
tuplist = dic.items()
print(tuplist)

