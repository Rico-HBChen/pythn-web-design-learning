#coding:utf-8
'''
判断自己技术是否在技术栈范围内。
技术栈：skills = {'Python','R','SQL','Git',
'Tableau','SAS'}
自己技术：mySkills = {'Python','R'}
实现思路：最简单的是直接用集合关系运算，但是考虑
到实际项目中可能存在大小写问题，所以先将其转化为列表
然后转化为字符串，然后将其统一小写，转化为列表、列表
再转化为集合，使用集合的isuperset方法判断。
'''
skills = {'Python','R','SQL','Git','Tableau','SAS'}
mySkills = {'python','R'}
#如下部分为避免因大小写不同而误判的程序
lskills = list(skills)
lmyskils = list(mySkills)
stlSkills = " ".join(lskills)
stlMyskills = " ".join(lmyskils)
lowSkills = stlSkills.lower()
lowmyskills = stlMyskills.lower()
lskills = lowSkills.split(' ')
lmyskils = lowmyskills.split(' ')
#如下为最终判断并输出结果的程序
result = set(lskills).issuperset(set(lmyskils))
print(result)
