'''会员管理系统
#-*- coding : utf-8 -*-

'''

# coding: utf-8

from member_vip import Vip
import pymysql

conn1 = pymysql.connect(host="localhost", port=3306, user="root",password="mysql",
                        database="superMarket",charset="utf8")



class VipSys(object):

    def __init__(self):
        self.menu_dict = {'1':self.add_new_vip,
                          '2':self.view_all,
                          '3':self.seach_single,
                          '4':self.del_vip,
                          '5':self.modify_vip,
                          '0':self.my_exit}
        self.vip_dict = {}  # 会员字典

    # 启动
    def start(self):
        # 自动加载数据,由于数据来源改为mysql先不使用自动加载数据功能
        # self.load_data()
        while True:
            self.print_menu()
            self.select_menu()

    # 打印菜单
    def print_menu(self):
        print('*'*30+'\n'+ '欢迎进入会员管理系统\n'+'1:添加会员\n'+'2:查看全部会员\n'+ '3:查询会员\n'
              + '4:删除会员\n' + '5:修改会员\n'+'0:退出系统')

    # 选择菜单
    def select_menu(self):
        num = input('请输入需要的服务:')

        if num in self.menu_dict.keys():
            self.menu_dict[num]()
        else:
            print('无此服务')

    # 加载数据
    def load_data(self):
        file = open('vip_list.txt', 'r')
        # file = open('vip_list.txt', 'rb')
        str_vip = file.readlines()
        # 加入到会员字典
        for each in str_vip:
            dict = eval(each)
            # 实例对象
            v1 = Vip(dict['phone'],dict['name'],dict['points'])

            self.vip_dict[dict['phone']] = v1
        file.close()

    # 1-添加会员
    def add_new_vip(self):
        name = input('请输入会员姓名:')
        phone = input('请输入手机号:')
        points = 0 #default 0
        print(phone)
        # 数据库操作1：新增：
        cs = conn1.cursor()
        sql = "insert into vip_list(name,phone,points) values (\'%s\',\'%s\',%d);" % (name, phone, points)
        print('slq:%s'%sql)
        cs.execute(sql)
        conn1.commit()  #提交
        # data = cs.fetchall()  # 是一个元组
        cs.close()
        conn1.close()
        # print(data)


        # self.vip_dict[v_phone] = Vip(v_phone,v_name,'0') # 会员初始积分为0分，积分数据类型 int
        # self.save_file()

    # 2-查看所有会员
    def view_all(self):
        cs = conn1.cursor()
        sql = "select *from vip_list"
        cs.execute(sql)
        data = cs.fetchall()  # 是一个元组
        cs.close()
        conn1.close()
        # print(data)
        for each in data:
            print(each[1].ljust(10), each[2].ljust(15), str(each[3]).ljust(10))
            '''
            (4, 'bobo', '15912351123', 0, b'\x00')
            (5, 'hsb', '18520395753', 0, b'\x00')
            (6, '小定', '13710121111', 0, b'\x00')'''
    # 3-查找单个会员
    def seach_single(self):
        phone = input('请输入手机号:')
        data=self.display_single(phone)
        print(data[0][1].ljust(10), data[0][2].ljust(15), str(data[0][3]).ljust(10))

    # 3-1 显示单个会员
    def display_single(self,phone):

        print('-'*30)
        # 数据库操作2：查找单个数据
        cs = conn1.cursor()
        sql = "select * from vip_list where phone=\'%s\';" % (phone)
        cs.execute(sql)
        data = cs.fetchall()  # 是一个元组
        cs.close()
        conn1.close()
        # print(data[0])  (1, '波', '18520395753', 200, b'\x00')
        return data

    # 3-2 查询积分接口
    def display_point(self,phone):
        # 加载数据，  【要完成read_price 功能，需要把加载数据放在函数里面，放外面会报'keyError
        # self.load_data()
        # 可以加入判断是否是会员】
        # 数据库操作2：查找单个数据

        data = self.display_single(phone)
        print('-'*30)
        # print(data[0][3])
        return data[0][3]

    # 4-删除会员
    def del_vip(self):
        phone = input('请输入需要删除的会员手机号:')

        cs = conn1.cursor()
        sql = "delete from vip_list where phone=\'%s\';" % phone
        cs.execute(sql)
        conn1.commit()  # 提交
        cs.close()
        conn1.close()

        # try:
        #     cs = conn1.cursor()
        #     sql = "drop * from vip_list where phone=\'%s\';" % phone
        #     cs.execute(sql)
        #     conn1.commit()  # 提交
        #     cs.close()
        #     conn1.close()
        # except Exception:
        #     print("无此用户")


        # if phone in self.vip_dict.keys():
        #     self.display_single(phone)
        #     isok = input('1:确认\n0:取消')
        #     if isok == '1':
        #         del(self.vip_dict[phone])
        #     else:
        #         return # 回到开头
        # else:
        #     print('无此用户')

    # 5-修改会员信息（很少用）
    def modify_vip(self):
        phone = input('请输入需要修改的会员手机号:')
        if phone in self.vip_dict.keys():
            self.display_single(phone)
            name = input('新姓名:')
            point = input('新积分')
            self.vip_dict[phone] = Vip(phone, name, point)
        else:
            print('无此用户')

    # 5-1修改会员积分，外接
    def modify_vip_point(self,v_phone,v_name,point):
        self.vip_dict[v_phone] = Vip(v_phone, v_name, point)
        #保存数据
        self.save_file()

    # 保存数据
    def save_file(self):
        file = open('vip_list.txt','w')
        for each in self.vip_dict.values():
            dict = {}
            dict['phone'] = each.v_phone
            dict['name'] = each.v_name
            dict['points'] =each.v_points
            dict = str(dict) + '\n'
            file.write(dict)

        file.close()

    # 退出系统
    def my_exit(self):
        self.save_file()
        print('退出系统')
        exit(0)

if __name__ == '__main__':
    VipSys().start()
    # VipSys().seach_single()
    #18520395753