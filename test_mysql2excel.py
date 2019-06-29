#!/usr/bin/env python
import pymysql              

#创建连接
def getCon():
    # conn = pymysql.connect(host = '127.0.0.1',user='root',passwd='123456',db='movies')
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="mysql",
                           database="superMarket", charset="utf8")
    return conn


#查看数据
def searchALL():
    lt =[]               #建立空列表，用于后面插入excel中时使用
    conn = getCon()
    sql = "select * from vip_list"
    cur=conn.cursor()
    cur.execute(sql)
    all = cur.fetchall()   #查看所有数据

    # print(all)
    for i in all:           #通过遍历查看
        lt.append(i)         #将数据放到空列表中
    # print('-------------')
    # print(lt)
    '''
    [(4, 'bobo', '15912351123', 0, b'\x00'),
    (5, 'hsb', '18520395753', 0, b'\x00'),
     (6, '小定', '13710121111', 0, b'\x00')]
    '''
    return lt


#调用涵数
searchALL()     

# 第二步为将数据插入到EXCEL中---------------------------------
import xlrd         #导入需要的模块
import xlwt


wbk = xlwt.Workbook()
sheet=wbk.add_sheet('test01.xlsx')
# print('len:%s'%len(searchALL()))
#计算列表的长度就是计算有多少行
for i in range(len(searchALL())):
    #由于该表最后的字段is_delete为bytes类型，会报错，故先不写入
    for j in range(len(searchALL()[0])-1):     #计算列表中的第一个列表中的数据的长度就是有多少列
        # 通过索引写入数据
        sheet.write(i,j,searchALL()[i][j])

'''for i in range(len(searchALL())):            #计算列表的长度就是计算有多少行
    for j in range(len(searchALL()[0])):     #计算列表中的第一个列表中的数据的长度就是有多少列
        sheet.write(i,j,searchALL()[i][j])   #通过索引写入数据'''

wbk.save('test01.xlsx')                   #保存

# #查看是否成功
# wk = xlrd.open_workbook('test01.xlsx')
# sheet = wk.sheet_by_index(0)
# nrows = sheet.nrows
# ncols = sheet.ncols
#     #查看行值
# for i in range(nrows):
#     myrowvalue = sheet.row_values(i)
#     # print(myrowvalue)
#     #查看列值
# for j in range(ncols):
#     mycolvalue = sheet.col_values(j)
#     # print(mycolvalue)
#
# #查看单元格的值
# for i in range(nrows):
#     for j in range(ncols):
#         mycellvalue = sheet.cell(i,j).value
#         print(mycellvalue,end='\t')
#     print()
#
#






# #--------------------------
# #创建数据表
# def createALL():
#     conn = getCon()
#     ###sql ='''create ###table test01(                     #这一段为sql语句，创建数据表
#     moviename varchar(255) not null primary key,
#     boxoffice float not null,
#     percent float not null,
#     days int(11) not null,
#     totalboxoffice float not null)
#     '''
#     cur = conn.cursor()
#     cur.execute(sql)
#     conn.commit()
# #调用函数，调用完成及时注释掉，避免多次调用报错
# # createALL()
#
# #修改字段属性
# def alterALL():
#     conn = getCon()
#     sql = "alter table test01 modify percent varchar(255) not null "           #将percent的列属性改成varchar(255)
#     cur  = conn.cursor()
#     cur.execute(sql)
# # alterALL()
#
# #插入数据
# def insertALL(data):
#     conn = getCon()
#     sql ="insert into test01 values('%s','%f','%s','%d','%f')"           #占位符使用时注意列类型的区分d：整数s：字符串f：浮点小数
#     cur =conn.cursor()
#     cur.execute(sql%data)
#     conn.commit()


# data =('21克拉',1031.92,'15.18%',2,2827.09)
# data2 =('狂暴巨兽',2928.28 ,'43.07%',9    ,57089.2)
# data3 =('起跑线',161.03   ,'2.37%',18    ,19873.43)
# data4 = ('头号玩家',   1054.87    ,'15.52%',23,127306.41)
# data5 =('红海行动',    45.49, '0.67%',65,    364107.74)
# data6=('犬之岛',  617.35,    '9.08%',2, 1309.09)
# data7=('湮灭',   135.34 ,'1.99%',9,    5556.77)