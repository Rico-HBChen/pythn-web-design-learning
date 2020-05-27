#coding:utf-8
import itertools

def floatRange(start,end = None,step = 1.0):
    if end is None:
        end = float(start)
        start = 0.0

    for i in itertools.count():
        nxt = start + i * step
        if(step > 0 and nxt >= end) or (step <0 and nxt <=end):
            break
        yield nxt

f = floatRange(1.5,9,1.3)
print(f.__next__())
print(f.__next__())
print(list(f))