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


#数据可视化

##六月销量前五的商品柱状图
data_6m = examdata_gp_m.get_group(6) #获取六月份的数据
data_6m_gp_t = data_6m.groupby('商品')
sale_6m = data_6m_gp_t.count()
sort_sale_6m = sale_6m.sort_values(by="订单号" , ascending=False) #降序排序，从大到小
data_figure = sort_sale_6m['订单号'][0:5]
#print(data_figure)
#绘图数据准备好以后，开始绘图
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(8, 5), dpi=80)
a = plt.bar(range(len(data_figure.index)), data_figure.values, tick_label=data_figure.index)  
plt.xlabel('商品类别')# 设置横轴标签
plt.ylabel('销售量')# 设置纵轴标签
plt.title('六月销售量前五商品')# 添加标题
#在顶部添加数据
#定义函数来显示柱状上的数值
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2, 1.003*height, '%s' % float(height),ha = 'center',va = 'bottom')
autolabel(a)
plt.savefig(r'C:\Users\A\Desktop\practice\六月销量前五商品柱状图.png')
plt.show() 



##每台售货机交易额月环比增长率柱状图
###画图数据的准备
jiaoyie_m0 = ID0_gp_m.sum()['实际金额'].values
huanbi0 = []
for i in range(0,11):
    huanbi0.append(jiaoyie_m0[i+1]/jiaoyie_m0[i])
huanbi0 = np.array(huanbi0)

jiaoyie_m1 = ID1_gp_m.sum()['实际金额'].values
huanbi1 = []
for i in range(0,11):
    huanbi1.append(jiaoyie_m1[i+1]/jiaoyie_m1[i])
huanbi1 = np.array(huanbi1)

jiaoyie_m2 = ID2_gp_m.sum()['实际金额'].values
huanbi2 = []
for i in range(0,11):
    huanbi2.append(jiaoyie_m2[i+1]/jiaoyie_m2[i])
huanbi2 = np.array(huanbi2)

jiaoyie_m3 = ID3_gp_m.sum()['实际金额'].values
huanbi3 = []
for i in range(0,11):
    huanbi3.append(jiaoyie_m3[i+1]/jiaoyie_m3[i])
huanbi3 = np.array(huanbi3)

jiaoyie_m4 = ID4_gp_m.sum()['实际金额'].values
huanbi4 = []
for i in range(0,11):
    huanbi4.append(jiaoyie_m4[i+1]/jiaoyie_m4[i])
huanbi4 = np.array(huanbi4)

#id_name[0]月环比柱状图
plt.figure(figsize=(8, 5), dpi=80)
b = plt.bar(range(len(huanbi0)), huanbi0, tick_label=['2月/1月','3月/2月','4月/3月','5月/4月','6月/5月','7月/6月','8月/7月','9月/8月','10月/9月','11月/10月','12月/11月'])  
plt.xticks(rotation =25)
plt.ylabel('比率')# 设置纵轴标签
plt.title(id_name[0]+'交易月环比增长率')# 添加标题
autolabel(b)
plt.savefig(r'C:\Users\A\Desktop\practice\id_name[0]月环比.png')
plt.show()
#id_name[1]月环比柱状图
plt.figure(figsize=(8, 5), dpi=80)
b = plt.bar(range(len(huanbi1)), huanbi1, tick_label=['2月/1月','3月/2月','4月/3月','5月/4月','6月/5月','7月/6月','8月/7月','9月/8月','10月/9月','11月/10月','12月/11月'])  
plt.xticks(rotation =25)
plt.ylabel('比率')# 设置纵轴标签
plt.title(id_name[1]+'交易月环比增长率')# 添加标题
autolabel(b)
plt.savefig(r'C:\Users\A\Desktop\practice\id_name[1]月环比.png')
plt.show()
#id_name[2]月环比柱状图
plt.figure(figsize=(8, 5), dpi=80)
b = plt.bar(range(len(huanbi2)), huanbi2, tick_label=['2月/1月','3月/2月','4月/3月','5月/4月','6月/5月','7月/6月','8月/7月','9月/8月','10月/9月','11月/10月','12月/11月'])  
plt.xticks(rotation =25)
plt.ylabel('比率')# 设置纵轴标签
plt.title(id_name[2]+'交易月环比增长率')# 添加标题
autolabel(b)
plt.savefig(r'C:\Users\A\Desktop\practice\id_name[2]月环比.png')
plt.show()
#id_name[3]月环比柱状图
plt.figure(figsize=(8, 5), dpi=80)
b = plt.bar(range(len(huanbi3)), huanbi3, tick_label=['2月/1月','3月/2月','4月/3月','5月/4月','6月/5月','7月/6月','8月/7月','9月/8月','10月/9月','11月/10月','12月/11月'])  
plt.xticks(rotation =25)
plt.ylabel('比率')# 设置纵轴标签
plt.title(id_name[3]+'交易月环比增长率')# 添加标题
autolabel(b)
plt.savefig(r'C:\Users\A\Desktop\practice\id_name[3]月环比.png')
plt.show()
#id_name[4]月环比柱状图
plt.figure(figsize=(8, 5), dpi=80)
b = plt.bar(range(len(huanbi4)), huanbi4, tick_label=['2月/1月','3月/2月','4月/3月','5月/4月','6月/5月','7月/6月','8月/7月','9月/8月','10月/9月','11月/10月','12月/11月'])  
plt.xticks(rotation =25)
plt.ylabel('比率')# 设置纵轴标签
plt.title(id_name[4]+'交易月环比增长率')# 添加标题
autolabel(b)
plt.savefig(r'C:\Users\A\Desktop\practice\id_name[4]月环比.png')
plt.show()


##每台售货机每月总交易额折线图
plt.figure(figsize=(15, 8), dpi=80)
x = [1,2,3,4,5,6,7,8,9,10,11,12]
plt.plot(x,jiaoyie_m0, marker='o', color = 'b',label=id_name[0])
plt.plot(x,jiaoyie_m1, marker='o', color = 'r',label=id_name[1])
plt.plot(x,jiaoyie_m2, marker='o', color = 'g',label=id_name[2])
plt.plot(x,jiaoyie_m3, marker='o', color = 'c',label=id_name[3])
plt.plot(x,jiaoyie_m4, marker='o', color = 'k',label=id_name[4])
plt.legend()  # 让图例生效
plt.xticks(x, rotation=1)
plt.title('每月总交易额折线图')# 添加标题
plt.xlabel('月份') #X轴标签
plt.ylabel("销售额") #Y轴标签
plt.savefig(r'C:\Users\A\Desktop\practice\每月总交易额折线图.png')
plt.show()


##绘制每台售货机毛利润占总利润比例的饼图
data_data2 = pd.merge(data,data2,on = '商品') #将两个dataframe合并，按照‘商品’列进行合并
id0_data2 = pd.merge(ID[0],data2,on = '商品')
id1_data2 = pd.merge(ID[1],data2,on = '商品')
id2_data2 = pd.merge(ID[2],data2,on = '商品')
id3_data2 = pd.merge(ID[3],data2,on = '商品')
id4_data2 = pd.merge(ID[4],data2,on = '商品')

#计算毛利润的函数
def maolirun(data):
    gp_lei = data.groupby('大类').sum()
    gp_lei['毛利润比例'] = [0.2,0.25]
    gp_lei['毛利润'] = gp_lei['实际金额']*gp_lei['毛利润比例']
    lirun = gp_lei['毛利润'].sum() 
    return lirun

zong_lirun = maolirun(data_data2)
id0_lirun = maolirun(id0_data2)
id1_lirun = maolirun(id1_data2)
id2_lirun = maolirun(id2_data2)
id3_lirun = maolirun(id3_data2)
id4_lirun = maolirun(id4_data2)

lirun_bili = (np.array([id0_lirun,id1_lirun,id2_lirun,id3_lirun,id4_lirun]))/zong_lirun

plt.figure(figsize=(8,8), dpi=80)
plt.title('每台售货机毛利润占总毛利润比例')
plt.pie(lirun_bili,labels = id_name,autopct='%.2f')
plt.legend()
plt.savefig(r'C:\Users\A\Desktop\practice\毛利润比例.png')
plt.show()


##每月交易额均值气泡图
y = np.array(data_data2.groupby('二级类')['实际金额'].sum().index)
#先按月切割数据
data_data2_split = monthsplit(data_data2)
data_data2_gp_m = data_data2_split.groupby('month')
data_data2_m = data_data2_gp_m.size().index 
data_data2_split_m = []
for i in data_data2_m:
    data_data2_split_m.append(data_data2_gp_m.get_group(i))#get_group(index) 按照分类的记号提取出每一个类
jiaoyie_sum = []
for i in range(12):
    lei_sum = data_data2_split_m[11-i].groupby('二级类')['实际金额'].sum()
    lei_sum_pd = pd.DataFrame(lei_sum)
    lei_sum_pd.rename(columns={'实际金额':'%d月'%(12-i)}, inplace = True)
    jiaoyie_sum.append(lei_sum_pd)

#构建一个新的dataframe，列名为：二级类目，1，2，...
new_data = pd.DataFrame(y,columns =[ '二级类'])
for i in range(12):
    new_data = pd.merge(jiaoyie_sum[i],new_data,on = '二级类',how = 'outer')
new_data.fillna(0, inplace=True)
new_data.drop(['二级类'],axis=1,inplace= True)
qipaotu_data = new_data/m_day
qipaotu = qipaotu_data.copy()
qipaotu['二级类'] = y
qipaotu['分类'] = np.arange(20)
qipaotu.head()
#绘制气泡图
plt.figure(figsize=(20,10), dpi=80)
plt.title('每月交易额均值气泡图')
x = np.zeros((20,12))
for i in range(20):
    x[i] = [1,2,3,4,5,6,7,8,9,10,11,12]
size = qipaotu_data.rank()
n = 20
color={0:'red',1:'blue',2:'orange',3:'black',4:'yellow',5:'cyan',6:'navy',7:'pink',8:'tan',9:'wheat',10:'aliceblue',11:'chocolate',12:'darkorchid',13:'dimgray',14:'gold',15:'green',16:'indigo',17:'lightsalmon',18:'mediumturquoise',19:'moccasin'}
plt.scatter(x,qipaotu_data,color=[color[i] for i in qipaotu['分类']],s=size*n,alpha=0.6) 
plt.savefig(r'C:\Users\A\Desktop\practice\每月均值交易额气泡图.png')
plt.show()


##绘制订单量的热力图
#每月的数据被分离开，我们需要的6、7、8月是[5][6][7]
data_figure = []
m_name = examdata_gp_m.size().index 
for i in m_name:
    a = examdata_gp_m.get_group(i)
    data_figure.append(a)
data_figure[5].head()

#绘制热力图所需的数据
def relitu_struct(data):
    relitu_data = []
    month_index = data.groupby('day').size().index
    for i in month_index:
        lie_data = data.groupby(['day','hour'])['订单号'].count()[i]
        lie_data = pd.DataFrame(lie_data)
        lie_data.rename(columns={'订单号':'%d天'%(i)}, inplace = True)
        relitu_data.append(lie_data)
    #接下来进行拼接
    relitu = relitu_data[0]
    i =0
    while i < (len(relitu_data)-1):
        relitu = pd.merge(relitu,relitu_data[i+1], how='outer', on='hour')
        i = i+1
    relitu.fillna(0, inplace=True)
    return relitu
m_6 = relitu_struct(data_figure[5])
m_7 = relitu_struct(data_figure[6])
m_8 = relitu_struct(data_figure[7])

# 绘图
import seaborn as sns
plt.figure(figsize=(18,15), dpi=80)
ax = sns.heatmap(m_6, # 指定绘图数据
                 cmap=plt.cm.Blues, # 指定填充色
                 linewidths=.1, # 设置每个单元方块的间隔
                 annot=True # 显示数值
                )
ax.set_title('六月销量热力图')
plt.xlabel('天') #X轴标签
plt.ylabel("小时") #Y轴标签
plt.savefig(r'C:\Users\A\Desktop\practice\六月销售热力图.png')
plt.show()

# 绘图
import seaborn as sns
plt.figure(figsize=(18,15), dpi=80)
ax = sns.heatmap(m_7, # 指定绘图数据
                 cmap=plt.cm.Blues, # 指定填充色
                 linewidths=.1, # 设置每个单元方块的间隔
                 annot=True # 显示数值
                )
ax.set_title('七月销量热力图')
plt.xlabel('天') #X轴标签
plt.ylabel("小时") #Y轴标签
plt.savefig(r'C:\Users\A\Desktop\practice\七月销售热力图.png')
plt.show()

# 绘图
import seaborn as sns
plt.figure(figsize=(18,15), dpi=80)
ax = sns.heatmap(m_8, # 指定绘图数据
                 cmap=plt.cm.Blues, # 指定填充色
                 linewidths=.1, # 设置每个单元方块的间隔
                 annot=True # 显示数值
                )
ax.set_title('八月销量热力图')
plt.xlabel('天') #X轴标签
plt.ylabel("小时") #Y轴标签
plt.savefig(r'C:\Users\A\Desktop\practice\八月销售热力图.png')
plt.show()
print('任务二完成！')