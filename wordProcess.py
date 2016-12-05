#encoding:utf-8
# 文件操作
from operator import *
# 读取关键词列表
f_key = open('src/key_list.txt')

# 把关键词生成数组
key_list = []
for line in f_key.readlines():
    line=line.strip('\n')
    key_list.append(line)

# 定义转化函数
def changePayload(payload):
    p_list = []
    # 无关单词转化,key保留
#     for word.lower() in payload:
#         # 在key list中的敏感词
#         if word in key_list:
#             p_list.append(word)
#         # 非敏感词
#         elif ("normal_word" not in p_list):
#             p_list.append("normal_word")
#         else:
#             continue



    for word in key_list:
        if word in payload.lower():
            p_list.append(word)
        elif("normal_word" in payload):
            p_list.append("normal_word")
        else:
            continue
            
            

    # 特殊字符转化
    for i in payload:
        ascii = ord(i)
        if(ascii<48 or ascii>57 and ascii<65 or ascii>90 and ascii < 95 or ascii>95 and ascii<97 or ascii>122):
            if(('ascii'+ str(ascii)) not in p_list):
               p_list.append('ascii'+str(ascii))
            if(i != " "):
                payload = payload.replace(i," ")
    # 16进制转化
    payload = payload.split(" ")
    for word in payload:
        if(word[0:2] == "0x"):
            p_list.append("16hex")
            payload.remove(word)
    
    return p_list

# 函数：为每一个训练样本生成一个向量，词集模型
def wordToVec(vecList,doc):
    returnVec = [0] * len(vecList)
    for word in doc:
        # 如果
        if(word in vecList):
            returnVec[vecList.index(word)] = 1
        else:
            print("word is not contained:  " + word)
    return returnVec

# 创建文本训练集向量
def createDocVec(payloads,requires):
    vec = set([])
    for doc in payloads:
        vec = vec | set(doc)
    for doc in requires:
        vec = vec | set(doc)
    return list(vec)

def getWords(separateLength):
	# 多长的文本之下单独处理
	# payload
	f_pl = open('src/payload.txt')
	# normal requrire
	f_norm = open('src/normal_require.txt')
	# 数组化
	pl_list = []
	# 短的单独处理
	pl_list_short = []
	for line in f_pl.readlines():
		line=line.strip('\n')
		if(len(line)>separateLength):
		    pl_list.append(line)
		else:
			pl_list_short.append(line)
	# 正常请求
	norm_list = []
	# 短的单独处理
	norm_list_short = []
	for line in f_norm.readlines():
	    line=line.strip('\n')
	    if(len(line)>separateLength):
	        norm_list.append(line)
	    else:
	        norm_list_short.append(line)
	return {
		'normal':norm_list,
		'payload':pl_list,
		'normal_shot':norm_list_short,
		'payload_shot':pl_list_short
	}
