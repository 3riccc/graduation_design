#encoding:utf-8
# 文件操作
from operator import *
# 正则表达式
import re
# url解码用的
import urllib
# 判断类型
import types
# 打开文件
f = open('src/ff_12011805.html')
# 链接们
links = []
# 正则
linkPattern = re.compile(r'(href=".*?\")')
# # 取到连接
for line in f.readlines():
	links = linkPattern.findall(line)
# 参数值们
paras = []
# 用正则从链接中匹配参数值
paraPattern = re.compile(r'(\=.*?&amp;)')
# 链接修剪并匹配
for link in links:
    # 修剪
	link = link[6:-1]
    # 匹配
	paraList = paraPattern.findall(link)
	for para in paraList:
#         paras.append(unicode(para[1:-5],'utf-8'))
		paras.append(para[1:-5])
print len(paras)


# 写入文件
output = open('src/ff_temp.txt','w')
# 开始写入
for para in paras:
	if(len(para) > 0):
	    output.write(urllib.unquote(para))
    	output.write('\n')
output.close()
f.close()