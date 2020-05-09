#coding:utf-8

st = 'Life is short You need python'
upst = st.upper().split(' ')
print('大写',upst)

lowst = st.lower().split(' ')
print('小写',lowst)

#longdist = {}
#for i in upst:
#    longdist[i] = len(i)

longdist = {k:v for k,v in zip(upst,[len(i) for i in upst])}
print(longdist)