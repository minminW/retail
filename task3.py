
#接下来要对每台售货机的饮料类商品贴标签
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
task1A = pd.read_csv(r'C:\Users\A\Desktop\practice\task1-1A.csv',encoding = 'gbk')
task1B = pd.read_csv(r'C:\Users\A\Desktop\practice\task1-1B.csv',encoding = 'gbk')
task1C = pd.read_csv(r'C:\Users\A\Desktop\practice\task1-1C.csv',encoding = 'gbk')
task1D = pd.read_csv(r'C:\Users\A\Desktop\practice\task1-1D.csv',encoding = 'gbk')
task1E = pd.read_csv(r'C:\Users\A\Desktop\practice\task1-1A.csv',encoding = 'gbk')
data2 = pd.read_csv(r'C:\Users\A\Desktop\practice\data2.csv',encoding = 'gbk')

def monthsplit(examdata):
    examdata['支付时间'] = pd.to_datetime(examdata['支付时间'],format = '%Y-%m-%d',errors = 'coerce') #将错误信息删除，项目结束后思考如何提取出错误信息
    examdata['month'] = [i.month for i in examdata['支付时间']]
    examdata['day'] = [i.day for i in examdata['支付时间']]
    examdata['hour'] = [i.hour for i in examdata['支付时间']]
    return examdata


#定义热销、正常、滞销
#通过绘制直方图来观察整体的销售情况
'''def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2, 1.003*height, '%s' % float(height),ha = 'center',va = 'bottom')
        
temp = aim_data.groupby('商品').count().sort_values(by="订单号" , ascending=False)
data_figure = temp['订单号']  
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(25, 25), dpi=80)
a = plt.bar(range(len(data_figure.index)), data_figure.values, tick_label=data_figure.index)  
plt.xlabel('商品类别')# 设置横轴标签
plt.ylabel('销售量')# 设置纵轴标签
plt.title('六月销售量排名前五')# 添加标题
autolabel(a)
plt.show()'''
#通过观察图决定，销量超过100定义为热销，小于100大于30定义为正常，小于10定义为滞销
def biaoqian(data):
    ##两个excel数据的合并
    data_data2 = pd.merge(data,data2,on = '商品')
    aim_data = data_data2.groupby('大类').get_group('饮料')
    sorted_data = aim_data.groupby('商品').count().sort_values(by="订单号" , ascending=False) #按照订单量的多少，对商品进行排
    rexiao = sorted_data.loc[sorted_data['订单号'] >= 100]['订单号']
    rexiao = pd.DataFrame(rexiao)
    rexiao['标签'] = '热销'
    zhixiao = sorted_data.loc[sorted_data['订单号'] <30]['订单号']
    zhixiao = pd.DataFrame(zhixiao)
    zhixiao['标签'] = '滞销'
    zhengchang = sorted_data.drop(index = rexiao.index )
    zhengchang = zhengchang.loc[sorted_data['订单号'] >= 30]['订单号']
    zhengchang = pd.DataFrame(zhengchang)
    zhengchang['标签'] = '正常'

    rexiao_zhengchang= pd.DataFrame.append(rexiao,zhengchang)
    task3 = pd.DataFrame.append(rexiao_zhengchang,zhixiao)
    task3.rename(columns={'商品':'饮料类商品','订单号':'销量'}, inplace=True)
    return task3
task3A = biaoqian(task1A).drop('销量',axis =1)
task3B = biaoqian(task1B).drop('销量',axis =1)
task3C = biaoqian(task1C).drop('销量',axis =1)
task3D = biaoqian(task1D).drop('销量',axis =1)
task3E = biaoqian(task1E).drop('销量',axis =1)
task3A.to_csv(r'C:\Users\A\Desktop\practice\task3-1A.csv',encoding = 'gbk')
task3B.to_csv(r'C:\Users\A\Desktop\practice\task3-1B.csv',encoding = 'gbk')
task3C.to_csv(r'C:\Users\A\Desktop\practice\task3-1C.csv',encoding = 'gbk')
task3D.to_csv(r'C:\Users\A\Desktop\practice\task3-1D.csv',encoding = 'gbk')
task3E.to_csv(r'C:\Users\A\Desktop\practice\task3-1E.csv',encoding = 'gbk')
print('任务3.1完成！')

#标签拓展，在3.1的基础上贴上其它标签，生成完整的画像
#定义0-4.5为便宜，4.5-6.5为适中，6.5以上为贵
def jiage_biaoqian(data):
    data2 = pd.read_csv(r'C:\Users\A\Desktop\practice\data2.csv',encoding = 'gbk')
    data_data2 = pd.merge(data,data2,on = '商品')
    aim_data = data_data2.groupby('大类').get_group('饮料')
    sorted_data = aim_data.groupby('商品').mean().sort_values(by="应付金额" , ascending=False) #按照价格的多少，对商品进行排
    gui = sorted_data.loc[sorted_data['应付金额'] >= 6.5]['应付金额']
    gui = pd.DataFrame(gui)
    gui['价格标签'] = '价格贵'
    pianyi = sorted_data.loc[sorted_data['应付金额'] <30]['应付金额']
    pianyi = pd.DataFrame(pianyi)
    pianyi['价格标签'] = '价格便宜'
    zhengchang = sorted_data.drop(index = gui.index )
    zhengchang = zhengchang.loc[sorted_data['应付金额'] >= 4.5]['应付金额']
    zhengchang = pd.DataFrame(zhengchang)
    zhengchang['价格标签'] = '价格适中'

    gui_zhengchang= pd.DataFrame.append(gui,zhengchang)
    task3 = pd.DataFrame.append(gui_zhengchang,pianyi)
    task3.rename(columns={'商品':'饮料类商品','应付金额':'单价'}, inplace=True)
    return task3
task3A2 = pd.merge(task3A,jiage_biaoqian(task1A),on = '商品').drop('单价',axis =1)
task3B2 = pd.merge(task3A,jiage_biaoqian(task1B),on = '商品').drop('单价',axis =1)
task3C2 = pd.merge(task3A,jiage_biaoqian(task1C),on = '商品').drop('单价',axis =1)
task3D2 = pd.merge(task3A,jiage_biaoqian(task1D),on = '商品').drop('单价',axis =1)
task3E2 = pd.merge(task3A,jiage_biaoqian(task1E),on = '商品').drop('单价',axis =1)

#定义0-300为销售额少，300-800为总销售额适中，800以上为总销售额多
def xiaoshoue_biaoqian(data):
    data_data2 = pd.merge(data,data2,on = '商品')
    aim_data = data_data2.groupby('大类').get_group('饮料')
    sorted_data = aim_data.groupby('商品').sum().sort_values(by="实际金额" , ascending=False) #按照总销售额的多少，对商品进行排
    gao = sorted_data.loc[sorted_data['实际金额'] >= 800]['实际金额']
    gao = pd.DataFrame(gao)
    gao['总销售额标签'] = '总销售额高'
    shao = sorted_data.loc[sorted_data['实际金额'] <300]['实际金额']
    shao = pd.DataFrame(shao)
    shao['总销售额标签'] = '总销售额低'
    zhengchang = sorted_data.drop(index = gao.index )
    zhengchang = zhengchang.loc[sorted_data['实际金额'] >= 300]['实际金额']
    zhengchang = pd.DataFrame(zhengchang)
    zhengchang['总销售额标签'] = '总销售额适中'

    gao_zhengchang= pd.DataFrame.append(gao,zhengchang)
    task3 = pd.DataFrame.append(gao_zhengchang,shao)
    task3.rename(columns={'商品':'饮料类商品','实际金额':'总销售额'}, inplace=True)
    return task3
task3A2 = pd.merge(task3A2,xiaoshoue_biaoqian(task1A),on = '商品').drop('总销售额',axis =1)
task3B2 = pd.merge(task3A2,xiaoshoue_biaoqian(task1B),on = '商品').drop('总销售额',axis =1)
task3C2 = pd.merge(task3A2,xiaoshoue_biaoqian(task1C),on = '商品').drop('总销售额',axis =1)
task3D2 = pd.merge(task3A2,xiaoshoue_biaoqian(task1D),on = '商品').drop('总销售额',axis =1)
task3E2 = pd.merge(task3A2,xiaoshoue_biaoqian(task1E),on = '商品').drop('总销售额',axis =1)

task3A2.to_csv(r'C:\Users\A\Desktop\practice\task3-2A.csv',encoding = 'gbk')
task3B2.to_csv(r'C:\Users\A\Desktop\practice\task3-2B.csv',encoding = 'gbk')
task3C2.to_csv(r'C:\Users\A\Desktop\practice\task3-2C.csv',encoding = 'gbk')
task3D2.to_csv(r'C:\Users\A\Desktop\practice\task3-2D.csv',encoding = 'gbk')
task3E2.to_csv(r'C:\Users\A\Desktop\practice\task3-2E.csv',encoding = 'gbk')
print('任务3.2完成')






#业务预测
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

def pre(data):
    data_data2 = pd.merge(data,data2,on = '商品')
    data_data2 = monthsplit(data_data2)
    aim_data = data_data2[['设备ID','应付金额','商品','大类','month']]
    m_index = aim_data.groupby('month').size().index
    fei_yinliao = []
    yinliao = []
    for i in m_index:
        a = aim_data.groupby(['month','大类'])['应付金额'].sum()[i]
        yinliao.append(a['饮料'])
        fei_yinliao.append(a['非饮料'])

    m_index = np.array(m_index).reshape(-1,1)

    # Create linear regression object 创建线性回归的对象
    fei_regr = linear_model.LinearRegression()
    regr = linear_model.LinearRegression()
    # Train the model using the training sets 训练模型
    fei_regr.fit(m_index, fei_yinliao)
    regr.fit(m_index,yinliao)
    print('饮料Coefficients: \n', regr.coef_)
    print('非饮料Coefficients: \n', fei_regr.coef_)
    # Make predictions using the testing set 将测试集输入训练好的模型中
    yinliao_pred = regr.predict(m_index)
    feiyinliao_pred = fei_regr.predict(m_index)
    # The mean squared error 均方误差
    print("饮料Mean squared error: %.2f"% mean_squared_error(yinliao, yinliao_pred))
    print("非饮料Mean squared error: %.2f"% mean_squared_error(fei_yinliao, feiyinliao_pred))
    # Explained variance score: 1 is perfect prediction 拟合优度最大值为1
    print('饮料Variance score: %.2f' % r2_score(yinliao, yinliao_pred))
    print('非饮料Variance score: %.2f' % r2_score(fei_yinliao, feiyinliao_pred))
    print('饮料预测：\n',yinliao_pred)
    print('非饮料预测：\n',feiyinliao_pred)
    
    plt.figure(figsize=(10,10), dpi=80)
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False
    plt.subplot(211)
    plt.scatter(m_index,yinliao,  color='black')
    plt.plot(m_index, yinliao_pred, color='blue', linewidth=3)
    plt.title('%s饮料'%aim_data.groupby('设备ID').count().index)
    plt.subplot(212)
    plt.scatter(m_index,fei_yinliao,  color='black')
    plt.plot(m_index, feiyinliao_pred, color='blue', linewidth=3)
    plt.title('%s非饮料'%aim_data.groupby('设备ID').count().index)
    plt.savefig(r'C:\Users\A\Desktop\practice\%s回归预测.png'%aim_data.groupby('设备ID').count().index)
    plt.show()
    

a = [task1A,task1B,task1C,task1D,task1E]
for i in a:
    pre(i)