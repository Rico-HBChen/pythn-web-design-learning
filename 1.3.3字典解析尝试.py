#coding:utf-8
import collections.abc

d = {'book':['python','datascience'],'author':'rico','publisher':'phei'}
#下面为尝试时的错误答案
#dd = {v : K for k,v in d.items() if isinstance(v,collections.abc.Hashable) else v:k for tuple(k),v in d.items()}
#下面为参考答案
dd = {v if isinstance(v,collections.abc.Hashable) else tuple(v):k for k,v in d.items()}
print('original',d)
print('change',dd)