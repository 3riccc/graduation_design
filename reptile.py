# 引入requests
import requests

# 即将访问的域名
domains = ["http://yz.chsi.com.cn/","http://pvp.qq.com/"]
# 已经访问过的域名
visitedDomains = []
# 积累的链接
links = []

# 只要有域名，就不停循环
while (len(domains) > 0):
	lastDomain = domains.pop()
	getThisDomain(lastDomain)
	visitedDomains.append(lastDomain)

# 获取一个域名
def getThisDomain(domain):
	thisDomainLink = []
	links = getPageLink(domain,domain)
	

	return

# 获取一个页面
def getPageLink(domain,page):
	if !ifBelong(domain,page):
		return
	else:

# 判断一个页面是否属于某个域名下
def ifBelong(domain,page):
	return true