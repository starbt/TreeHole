#coding:utf-8
import urllib.request
import re
class TreeHole:
	def __init__(self):
		self.weibo = []
		self.name_dic = {}
	# 得到树洞所有在pages数量的段子
	def getPages(self,pages):
		for i in range(pages):
			url = "http://www.openstu.com/?p="+str(i)
			#print(url)
			response = urllib.request.urlopen(url)
			date = response.read()
			date = date.decode('utf-8','ignore')
			patter = re.compile(r'<a href="http://weibo.com/n/汕大TreeHole"  wb_screen_name="汕大TreeHole">汕大TreeHole</a>：(.*)<br/>')
			response = re.findall(patter,date)
			return response
	def getNames(self,pages):
		weibo_name = []
		name_dic = {}
		for i in range(pages):
			url = "http://www.openstu.com/?p="+str(i)
			print(url)
			response = urllib.request.urlopen(url)
			date = response.read()
			date = date.decode('utf-8','ignore')
			patter = re.compile( r'<a href="javascript:ajaxDelV2\(\'(.*?)\',\'t_(.*?)\'\);" class="tips">删除</a>',re.S)
			result = re.findall(patter,date)
			for item in result:
				url = "http://www.openstu.com/comment.php?id="+item[1]+"&parent="+item[0]+"&type=comments"
				response = urllib.request.urlopen(url)
				date = response.read()
				date = date.decode('utf-8','ignore')
				patter = re.compile( r'<div style="float:left;width: 400px;padding-left:5px;padding-bottom: 2px;">.*?@(.*?)：',re.S)
				result1 = re.findall(patter,date)
				if result1:
					weibo_name.extend(result1)
		# print(len(weibo_name))
		name_set = set(weibo_name)
		for name in name_set:
			name_dic[name] = weibo_name.count(name)
		# print(len(name_dic))
		name_dic = sorted(name_dic.items(),key=lambda d:d[1],reverse = True)
		return name_dic
tree_hole = TreeHole()
tree_hole.getPages(1)
names = tree_hole.getNames(1)
print(names)
