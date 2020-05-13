#coding:utf-8
print("习题4-1答案",[i for i in [2,4,-7,19,-2,-1.45] if i<0 ])

score = {'python':89,'java':58,'physics':65,'math':49
,'Chinese':78}
averageScore = sum(score.values()) / len(score)
print("习题4-2答案：",{k:v for k,v in score.items() if v>averageScore})
print("习题4-3答案：",sum(i**2 for i in range(1,100)))