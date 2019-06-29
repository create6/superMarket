'''主程序
接口1 管理员入口，可以进入修改策略，员工系统会同步新策略，可以进入会员系统
接口2 收营入口，直接工作模式，没有修改权限'''
from order_manager_sys import OrderManager
from vip_sys import VipSys
from repertory_manager_sys import RepertoryMS
# 【加强:当用input 传入数据时，可以加一些判断，防止未按规范输入，防止报错】
# 【加强:当要读取数据库数据时，也要加入异常处理】
# 【注意:对参数进行运算时注意各参数的数据类型是否是int、float，在使用字符串的相关方法，要注意数据类型是否全是 str】
# {加强点：加入多任务。现实应用中收银系统是多个收银员在使用的。。。加入业绩报表}

if __name__ == '__main__':
    # 【可以直接在入口出加入权限判断，收银员，管理员，库管】
    def c_start():
        while True:
            print('*'*30)
            num = input('欢迎进入超市系统\n请输入需要的服务:\n1:收银系统\n2:会员系统\n3:产品系统\n0:退出系统')
            if num == '2':
                password = input('请输入密码:')
                if password == 'admin':
                    VipSys().start()
                else:
                    print('密码错误!')
            elif num == '1':
                OrderManager().start()
            elif num == '3':
                RepertoryMS().start()
            elif num == '0':
                exit(0)
            else:
                print('请重新输入')
    c_start()

#  测试读取价格，产品名--》价格
    def test_price():
        c_product = '饼干'
        c_price = RepertoryMS().read_price(c_product)
        print(c_price)
        # RepertoryMS().read_price(c_product)
        c_product = 'kao'
        c_price = RepertoryMS().read_price(c_product)
        print(c_price)
    # test_price()