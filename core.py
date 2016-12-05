#encoding:utf-8
# ------------------引入公共库-------------------------
from operator import *
# numpy
import numpy as np
# 区分测试集和训练集
from sklearn.cross_validation import train_test_split
# svm
from sklearn import svm
# knn
from sklearn.neighbors import KNeighborsClassifier
# 交叉验证
from sklearn.cross_validation import cross_val_score


# ----------------------引入自己的库-----------------------
import wordProcess as wp
import removeRepeat as rr

# ------------------获取正常请求和payload-------------------
res = wp.getWords(0)
norm_list = res['normal']
pl_list = res['payload']


# -----------获取正常请求和payload 并且去重-----------------
# res = rr.removeInFile("./src/normal_require.txt","./src/payload.txt")
# norm_list = res['normal']
# pl_list = res['payload']

# ------------------文本预处理-----------------------------
# 处理后的payload
payloads = []
for pl in pl_list:
    payloads.append(wp.changePayload(pl))
# 处理后的正常请求
requires = []
for req in norm_list:
    requires.append(wp.changePayload(req))



# -------------------处理后的文本转化为向量-------------------
# 创建向量
vec_list = wp.createDocVec(payloads,requires)
payloads_vec = []
requires_vec = []
# 为每个文本进行转化
for payload in payloads:
    payloads_vec.append(wp.wordToVec(vec_list,payload))
for require in requires:
    requires_vec.append(wp.wordToVec(vec_list,require))
# numpy处理一下
payloads_vec = np.array(payloads_vec)
requires_vec = np.array(requires_vec)



# ---------------------生成X和Y用于训练------------------------
# 生成X
X = np.concatenate((payloads_vec,requires_vec))
# 生成Y
Y = []
for i in range(0,len(payloads_vec)):
    Y.append(1)
for i in range(0,len(requires_vec)):
    Y.append(0)



# ----------------------包括svm的交叉验证----------------------------

# 设置算法
clf = svm.SVC()

# 用测试集预测 
scores = cross_val_score(clf, X,Y, cv=10, scoring='accuracy')
print scores
print scores.mean()

# ----------------------训练SVM并看看哪个分错了----------------------
# # 设置算法
# clf = svm.SVC(gamma=0.001)
# # 训练
# clf.fit(X,Y)
# # 查看分类错了的样本
# for i in range(len(X)):
#     temp = np.array(X[i]).reshape((1,-1))
#     if(clf.predict(temp)[0] != Y[i]):
#         # 如果预测错误，打印出原文
#         if i < len(pl_list):
#             print "payload 分类错误"
#             print pl_list[i]
#             print payloads[i]
#         else:
#             print "正常请求分类错误"
#             print norm_list[(i-len(pl_list))]
#             print requires[(i-len(pl_list))]
#         print "\n"
