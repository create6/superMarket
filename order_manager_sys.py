'''2收银系统
调用策略类，调用会员系统
【订单号】
'''
from superMarket.produce import Order
from superMarket.strategy import Strategies
from superMarket.repertory_manager_sys import RepertoryMS

class OrderManager(object):
    def __init__(self):
        self.prod_dict = {} # 购物清单字典
        self.performance_dict = {} # 业绩字典，【同名的键 的值进行累计，而非覆盖】


    def start(self):
        while True:
            sum_price, finally_sum_price =self.operate()
            self.shopingList(sum_price, finally_sum_price)

    # 运作中心
    def operate(self):
        isVip = input('是否是会员\n1.是\n0.否\n9.退出系统')
        if isVip == '1':  # 会员
            # 会员 ，调用会员策略
            phone = input('您注册会员的手机号:')
            discount_coupon, v_point = Strategies().member_points(phone)
            print('您的积分是%s 可抵扣%s元'%(v_point,discount_coupon))
            sum_price, finally_sum_price = self.sumPrice()  # 调用总价处理（含非会员策略，基础优惠）
            isok = input('请问是否使用优惠卷:\n1:是\n0:否')
            if isok == '1': # 默认全部抵扣（积分最大化兑换）
                finally_sum_price -= discount_coupon
                return sum_price, finally_sum_price
            else:
                return sum_price, finally_sum_price
            # 此处return 可以调整
        # 退出系统
        elif isVip == '9':
            self.my_exit()
        # 非会员
        else:
            sum_price, finally_sum_price = self.sumPrice()
            return sum_price, finally_sum_price     # 可以写 ？ return self.sumPrice()

    # 总价处理 ，接收self.plus_product()的初始总价及件数；调用策略，接收优惠券金额
    def sumPrice(self):
        # 调用统计后的总价与件数
        sum_price, count = self.plus_product()
        # print('原价:%d'%sum_price)
        # 调用策略，传入优惠券金额
        discount_coupon = Strategies().c_minus(sum_price, count)
        # print('现价:%d'%sum_price)
        finally_sum_price = sum_price - discount_coupon
        return sum_price, finally_sum_price  # 返回总价及优惠价

    # 打印购物清单  由self.operate() 传入参数
    def shopingList(self,sum_price,finally_sum_price):  # 此处要接收 operate 传过来的参数，sum_price,finally_sum_price # 返回总价及优惠价
        # 1 打印表头  商品 单价 数量
        print('名称'.ljust(10)+'单价'.ljust(10) + '数量'.ljust(10))
        # 2 打印具体项目
        for each in self.prod_dict.values():
            # 注意要打印数据时要注意数据类型，只有str 可以进行ljust之类的字符串操作
            # print(each.p_name.ljust(1)+ str(each.p_price).ljust(1)+ str(each.c_buyNum).ljust(1))# 是否需要加\n,不需要。
            print('%s%s%s'%(each.p_name.ljust(10), str(each.p_price).ljust(10),str(each.c_buyNum).ljust(10)))
        # 调用 operate 的返回值，可以打印 总价及折后总价
        # sum_price, finally_sum_price = self.operate()  # 直接用传参，不调用数据
        print('-'*30)# 打印分行符
        print('原价:%d   优惠价:%d'%(sum_price,finally_sum_price))
        # 打印清单结束后，清空购物清单字典
        self.prod_dict = {}

    # 统计，返原始总价，件数
    def plus_product(self):
        sum_price = 0
        count = 0
        while True:
             # 件数初始值为0
            isOk = input('是否统计完成\n1.是\n0.否')  # 此处可以改进，不要总是询问，默认继续扫描物品(调用硬件-扫描枪)
            if isOk == '0': # 未统计完成
                c_product = input('产品名:')
                c_num = int(input('数量:'))  # 转成整型  , 散称的件也是整数，一个袋子为一件
                c_price = RepertoryMS().read_price(c_product)  # 调用接口函数
                sum_price += c_price * c_num   # c_price需要调用价目表中数据
                count += c_num
                product_num = 0  # 此处不读取商品库存情况，后续可完善
                # 客户对象
                # 实际购物时同类产品不一定一起扫描，c_num不一定真实，即需要对同商品购买数量进行累计
                # c_order = Order(c_product,c_price,product_num,c_num)
                # 加入清单字典，以商品为键，以订单类Order为值，加入一个判断【加多一个判断，相同产品，数量相加】
                if c_product in self.prod_dict.keys():
                    c_num += self.prod_dict[c_product].p_num

                # 产品出现过与未出现过都要执行：
                c_order = Order(c_product, c_price, product_num, c_num)
                self.prod_dict[c_product] = c_order
            #统计完成，返回总价，件数
            else:
                return sum_price,count

    # 保存报表  ,(总表。分表：日报表，周表，月表，季度表，半年表，年表)
    def write_priceList(self):
        pass

    def my_exit(self):
        self.write_priceList()
        exit(0)
