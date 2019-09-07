import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#导入数据、观察数据大小、数据类型、数据大致样子
data = pd.read_csv(r'C:\Users\A\Desktop\practice\data1.csv',encoding = 'gbk')
data2 = pd.read_csv(r'C:\Users\A\Desktop\practice\data2.csv',encoding = 'gbk')
print('数据大小：\n',data.shape)
print('------------------------')
print('数据类型：\n',data.dtypes)
print('------------------------')
data.head()

#数据预处理
##清洗数据
examdata = data.copy()
###去重
#print(examdata.duplicated()) #判断是否有重复行，重复的显示为TRUE。data.duplicated('设备ID'),则是按照那一列来判断重复行
#print('--------------------------')
examdata.drop_duplicates(inplace = True) #去掉重复行,原始数据不改变。
#项目完成以后思考，如果有重复行，如何知道哪些重复了，重复了几次
###缺失值处理
#print(examdata.isnull().any()) #判断每一列是否有缺失值，如果有显示为True
#print('-------------------------')
examdata.head()

#观察数据，想分离出不同设备的信息
examdata_gp_id = data.groupby("设备ID")
examdata_gp_id.count().head() #观察一下分组后的情况
lenth = len(examdata_gp_id.count()) #获取有多少个ID
id_name = examdata_gp_id.size().index #获取每个ID的设备号。.value是代表获取值
ID = []
for i in id_name:
    ID.append(examdata_gp_id.get_group(i))#get_group(index) 按照分类的记号提取出每一个类
#将每一个设备的信息分别存入不同的文件
ID[0].to_csv(r'C:\Users\A\Desktop\practice\task1-1A.csv',encoding = 'gbk')
ID[1].to_csv(r'C:\Users\A\Desktop\practice\task1-1B.csv',encoding = 'gbk')
ID[2].to_csv(r'C:\Users\A\Desktop\practice\task1-1C.csv',encoding = 'gbk')
ID[3].to_csv(r'C:\Users\A\Desktop\practice\task1-1D.csv',encoding = 'gbk')
ID[4].to_csv(r'C:\Users\A\Desktop\practice\task1-1E.csv',encoding = 'gbk')

#观察数据，想按时间的月份来分离信息,因为要重复操作，所以定义monthsplit函数
def monthsplit(examdata):
    examdata['支付时间'] = pd.to_datetime(examdata['支付时间'],format = '%Y-%m-%d',errors = 'coerce') #将错误信息删除，项目结束后思考如何提取出错误信息
    examdata['month'] = [i.month for i in examdata['支付时间']]
    examdata['day'] = [i.day for i in examdata['支付时间']]
    examdata['hour'] = [i.hour for i in examdata['支付时间']]
    return examdata

#想按月，计算出所有设备每个月的总订单量，总实际交易额，平均实际交易额,总日均订单量
examdata = monthsplit(examdata)
examdata_gp_m = examdata.groupby("month")
#examdata_gp_m.count().head() #观察一下分组后的情况

#想生成一个表格，横向是月份，纵向是（总交易额，总订单量，总平均交易额，总日均订单量，设备1交易额，设备1订单量...）
temp = pd.DataFrame(np.arange(1,13),columns =[ '月份'])
temp['总订单量'] = examdata_gp_m['订单号'].count().values
temp['总交易额'] = examdata_gp_m['实际金额'].sum().values
temp['总平均交易额'] = examdata_gp_m['实际金额'].mean().values
m_day = [31,28,31,30,31,30,31,31,30,31,30,31]
temp['总日均订单量'] = temp['总订单量']/m_day
temp['总每月交易额均值'] = temp['总交易额']/m_day
temp.head()

ID[0] = monthsplit(ID[0])
ID0_gp_m = (ID[0]).groupby("month")
temp[id_name[0]+'订单量'] = ID0_gp_m['订单号'].count().values
temp[id_name[0]+'交易额'] = ID0_gp_m['实际金额'].sum().values
temp[id_name[0]+'平均交易额'] = ID0_gp_m['实际金额'].mean().values
temp[id_name[0]+'日均订单量'] = temp['总订单量']/m_day

ID[1] = monthsplit(ID[1])
ID1_gp_m = (ID[1]).groupby("month")
temp[id_name[1]+'订单量'] = ID1_gp_m['订单号'].count().values
temp[id_name[1]+'交易额'] = ID1_gp_m['实际金额'].sum().values
temp[id_name[1]+'平均交易额'] = ID1_gp_m['实际金额'].mean().values
temp[id_name[1]+'日均订单量'] = temp['总订单量']/m_day

ID[2] = monthsplit(ID[2])
ID2_gp_m = (ID[2]).groupby("month")
temp[id_name[2]+'订单量'] = ID2_gp_m['订单号'].count().values
temp[id_name[2]+'交易额'] = ID2_gp_m['实际金额'].sum().values
temp[id_name[2]+'平均交易额'] = ID2_gp_m['实际金额'].mean().values
temp[id_name[2]+'日均订单量'] = temp['总订单量']/m_day

ID[3] = monthsplit(ID[3])
ID3_gp_m = (ID[3]).groupby("month")
temp[id_name[3]+'订单量'] = ID3_gp_m['订单号'].count().values
temp[id_name[3]+'交易额'] = ID3_gp_m['实际金额'].sum().values
temp[id_name[3]+'平均交易额'] = ID3_gp_m['实际金额'].mean().values
temp[id_name[3]+'日均订单量'] = temp['总订单量']/m_day

ID[4] = monthsplit(ID[4])
ID4_gp_m = (ID[4]).groupby("month")
temp[id_name[4]+'订单量'] = ID4_gp_m['订单号'].count().values
temp[id_name[4]+'交易额'] = ID4_gp_m['实际金额'].sum().values
temp[id_name[4]+'平均交易额'] = ID4_gp_m['实际金额'].mean().values
temp[id_name[4]+'日均订单量'] = temp['总订单量']/m_day

temp.to_csv(r'C:\Users\A\Desktop\practice\task1.csv',encoding = 'gbk')
print('任务一完成！')


