#encoding:utf-8
import removeRepeat
res = removeRepeat.removeInFile("./src/normal_require.txt","./src/payload.txt")
print "正常数量"
print len(res['normal'])
print "payload数量"
print len(res['payload'])