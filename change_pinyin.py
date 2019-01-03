#coding=utf-8
def trans_pinyin(key,value):
	f = open("/home/wujie/方言统计/方言汉字.txt",'r')
	ff =f.read()
	dic = eval(ff)
	while 1:
		s1 = {}
		if u'\u4e00'<= key <= u'\u9fff':
			s1[key] = value
			break
		else:
			print(" '%s':'%s' 输入参数有误" % (key,value))
			return 0
			
	
	for key in s1.keys():	
		if key in dic.keys():
			print(" '%s':'%s' 在陕西方言中的发音：%s" % (key,s1[key],dic[key]))
			return dic[key]
		else:
			print(" '%s':'%s' 没有陕西方言发音" % (key,s1[key]))
			return 0
 
print(trans_pinyin('2','da4'))
