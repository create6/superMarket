'''1-仓库管理员
权限：产品数量进行管理
'''
# 导入产品类中的Produces类
from superMarket.produce import Produces

class RepertoryMS():
    def __init__(self):
        self.menu_dict = {'1': self.add_new_vip,
                          '2': self.view_all,
                          '3': self.seach_single,
                          '4': self.del_vip,
                          '5': self.modify_vip,
                          '0': self.my_exit}
        self.prod_dict = {}  # 会员字典  #延用此名

    # 启动
    def start(self):
        # 加入异常处理
        try:
            str_0 = open('produces_data.txt','r')
        except Exception:
            print('没有原始数据')
        else:
            # 加载数据
            self.load_data()
        finally:
            str_0.close()

        while True:
            self.print_menu()
            self.select_menu()

    # 打印菜单
    def print_menu(self):
        print('*' * 30 + '\n' + '欢迎进入产品管理系统\n' + '1:添加产品\n' + '2:查看全部产品\n'
              + '3:查询产品\n' + '4:删除产品\n' + '5:修改产品\n'+ '0:退出系统')

    # 选择菜单
    def select_menu(self):
        num = input('请输入需要的服务:')

        if num in self.menu_dict.keys():
            self.menu_dict[num]()
        else:
            print('无此服务')

    # 加载数据库
    def load_data(self):
        # 异常 新用系统时会文件
        str_0 = open('produces_data.txt','r')      # -------------------产品数据库
        stu = str_0.readlines()
        for each in stu:
            # 把each 装入中间字典
            dict_0 = eval(each)
            new_prod = Produces(dict_0['product_name'], dict_0['product_price'], dict_0['product_num'])
            self.prod_dict[dict_0['product_name']] = new_prod
        str_0.close()

    # 1-添加会员
    def add_new_vip(self):
        product_name = input('请输入商品名称:')
        product_price = input('请输入单价:')
        product_num = input('请输入数量:')
        self.prod_dict[product_name] = Produces(product_name,product_price,product_num)
        self.save_file()

    # 2-查看所有会员
    def view_all(self):
        for each in self.prod_dict.values():  # 加载更新后的vip字典
            print('-' * 30)
            # print(1)
            # tplt = '{0:^10}\t{1:^10}\t{2:^10}'
            # print(tplt.format(each.p_name, each.p_price, each.p_num,chr(12288)))
            # 显示
            print("%s%s%s"%(each.p_name.center(15), each.p_price.center(10), each.p_num.center(15)))

    # 3-查找单个会员
    def seach_single(self):
        name = input('请输入商品名:')
        if name in self.prod_dict.keys():
            self.display_single(name)
        else:
            print('未查到')

    # 3-1 显示单个会员
    def display_single(self, name):  # 功能函数里面不能加if 判断，当其加入到其他函数中，会出现不执行的情况
            print('-' * 30)
            print(self.prod_dict[name].p_name.ljust(10), self.prod_dict[name].p_price.ljust(15),self.prod_dict[name].p_num.ljust(10))

    # 3-2 读取价格接口 ,接口很好用
    def read_price(self, name):
        self.load_data()  # 加载数据，  【要完成read_price 功能，需要把加载数据放在函数里面，放外面会报'keyError'
        return float(self.prod_dict[name].p_price)  # 由str转成浮点型
        # print(self.prod_dict[name].p_price)

    # 4-删除会员
    def del_vip(self):
        name = input('请输入需要删除的商品:')
        if name in self.prod_dict.keys():
            self.display_single(name)
            isok = input('1:确认\n0:取消')
            if isok == '1':
                del (self.prod_dict[name])
            else:
                # break  # 回到开头 break用在循环体，用return 无用
                print('已取消')
        else:
            print('未查到')

    # 5-修改会员信息（很少用）
    def modify_vip(self):
        name = input('请输入需要修改的商号:')
        if name in self.prod_dict.keys():
            self.display_single(name)
            price = input('新单价:')
            num = input('新数量')
            self.prod_dict[name] = Produces(name, price, num)
        else:
            print('未查到')

    # 5-1修改会员积分，外接
    def modify_vip_point(self, product_name, product_price, product_num):
        self.prod_dict[product_name] = Produces(product_name, product_price, product_num)
        # 保存数据
        self.save_file()

    # 保存数据
    def save_file(self):
        file = open('produces_data.txt', 'w')
        for each in self.prod_dict.values():
            dict = {}
            dict['product_name'] = each.p_name
            dict['product_price'] = each.p_price
            dict['product_num'] = each.p_num
            dict = str(dict) + '\n'
            file.write(dict)
        file.close()

    # 退出系统
    def my_exit(self):
        self.save_file()
        print('退出系统')
        exit(0)