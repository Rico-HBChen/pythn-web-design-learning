#coding:utf-8
'''
题干：三角形三边分别为3、7、9，计算三个角度的读数
（1）在三角形ABC中,设AB=c,BC=a,CA=b,且a、b、c所对的内角分别是A、B、C,则：
cosA=[b²＋c²－a²]/(2bc)
cosB=[a²＋c²－b²]/(2ac)
cosC=[a²＋b²－c²]/(2ab)
（2）角度=180°×弧度÷π
（3）>>> help(math.acos)
Help on built-in function acos in module math:
acos(...)
    acos(x)
    
    Return the arc cosine (measured in radians) of x.
(END)

'''
import math

#下列程序运行后，会提醒依次输入三条边，然后自动输出每条边对应弧度，并验算对应角度和并输出。
print("请输入第1条边长度，然后按下回车键")
a = float(input())
print("第一条边：a = " + str(a))
print("请输入第2条边长度，然后按下回车键")
b = float(input())
print("第二条边：b = " + str(b))
print("请输入第3条边长度，然后按下回车键")
c = float(input())
print("第三条边：c = " + str(c))
aAngle = math.acos((b**2+c**2-a**2)/(2*b*c))
bAngle = math.acos((a**2+c**2-b**2)/(2*a*c))
cAngle = math.acos((a**2+b**2-c**2)/(2*a*b))
print("第1条边对面角的弧度为：" + str(round(aAngle,3)))
print("第2条边对面角的弧度为：" + str(round(bAngle,3)))
print("第3条边对面角的弧度为：" + str(round(cAngle,3)))
print("验算三内角和为：" + str(round((aAngle+bAngle+cAngle)*180/3.1415,1)))