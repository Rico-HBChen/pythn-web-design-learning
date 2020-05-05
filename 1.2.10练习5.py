#coding:utf-8

#下面为课中暂停尝试所写程序
songs = '''You raise my up so I can stand on mountains You raise my up to walk on stormy seas I am strong when I am on your shoulders You raise me up to more than I can be'''

dictionary = list(set(songs.lower().split(' ')))
print(dictionary)
searchData = input("请输入要统计出现次数的单词：")
print(searchData + "出现了" + str(songs.lower().count(searchData.lower())) + "次")