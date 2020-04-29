#coding:utf-8

lst = list("python")
lst.extend(list("rust"))
print(lst)
print("列表升序排列如下：")
lst.sort()
print(lst)

#使用空列表记录重复元素的后一个的索引
idxlst = []
for i in range(len(lst)-1):
    if lst[i] == lst[i+1]:
        idxlst.append(i+1)
#判断是否有重复元素，如果有，就删掉
if idxlst:
    n = 0
    for i in range(len(idxlst)):
        lst.remove(lst[idxlst[i-n]])
        n = n + 1

print("删除列表重复元素后如下")
print(lst)