'''订单类，产品名，单价，数量
'''
# 产品类 物价
class Produces(object):
    # 产品名，单价，产品数量
    def __init__(self,product_name,product_price,product_num):
        self.p_name = product_name
        self.p_price =product_price
        self.p_num = product_num

# 订单类
class Order(Produces):
    # 产品名，单价，产品数量(用于更新库存信息，收银员不调用此信号，【内部同步更新或者定时更新】)，客户购买某产品件数
    def __init__(self,product_name,product_price,product_num,client_buyNum):
        Produces.__init__(self,product_name,product_price,product_num)
        self.c_buyNum = client_buyNum
