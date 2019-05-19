'''策略'''

from superMarket.vip_sys import VipSys
class Strategies(object):
    # 满减
    def c_minus(self,sum_price,count):  # 数量与总价方面都可以写进去
        discount_coupon = 0
        if sum_price >= 500 :
            discount_coupon = 80
            # return discount_coupon
        elif count >=8 and sum_price >= 300: # 把优惠力度大的放在上面，满足后就会返回参数，不进行其他判断
            discount_coupon = 50
            # return discount_coupon
        return discount_coupon
            # 最终都是返回 sum_price 可以把return 与 if 对齐，不用每个条件后都return】，不过每个条件下写return也是有其用处
    # 积分抵扣 [会员], 调用vip接口
    def member_points(self,v_phone):
        v_point = int(VipSys().display_point(v_phone))    # 【将积分由str 转为int】# 类名后要加括号
        num = v_point // 1000   # 进行计算时注意数据类型
        discount_coupon = num * 10  # discount_coupon 为优惠券
        return discount_coupon, v_point   # 返回优惠金额与积分值给客户看




if __name__ == '__main__':
    sum_price = 300
    count = 3
    discount_coupon = Strategies().c_minus(sum_price,count)
    print(discount_coupon)
