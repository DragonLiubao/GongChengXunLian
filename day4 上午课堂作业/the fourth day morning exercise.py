import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: f'{x:.2f}')

# 数据准备
orders = pd.DataFrame({
    'order_id': [f'O{number}' for number in range(1001, 1019)],
    'region': ['华东','华北','华南','华东','西南','华北','华南','华东','西南','华北','华东','华南','西南','华东','华北','华南','华东','西南'],
    'product': ['机械键盘','无线鼠标','显示器','扩展坞','机械键盘','显示器','无线鼠标','显示器','扩展坞','机械键盘','显示器','无线鼠标','扩展坞','显示器','机械键盘','扩展坞','显示器','无线鼠标'],
    'category': ['外设','外设','显示设备','配件','外设','显示设备','外设','显示设备','配件','外设','外设','配件','显示设备','外设','配件','显示设备','外设','外设'],
    'quantity': [2,3,1,4,5,2,6,1,3,2,8,2,1,3,5,2,4,6],
    'unit_price': [289,129,1299,399,289,1299,129,1299,399,289,129,399,1299,289,399,1299,129,289],
    'member_level': ['金卡','普通','银卡','金卡','银卡','普通','金卡','银卡','普通','金卡','银卡','金卡','普通','金卡','普通','银卡','金卡','银卡'],
    'coupon_rate': [0.05,0.00,0.08,0.10,0.05,0.00,0.12,0.05,0.00,0.08,0.10,0.05,0.00,0.08,0.00,0.12,0.05,0.10],
    'salesperson': ['小林','小周','小陈','小林','小赵','小周','小陈','小林','小赵','小周','小林','小陈','小赵','小林','小周','小陈','小林','小赵']
})
print(orders)

# ======================任务1=====================
# 1.输出行数、列数、列名
print("1.数据行列信息")
print(f"数据行数：{orders.shape[0]}，数据列数：{orders.shape[1]}")
print("全部列名：")
print(orders.columns.tolist())

# 2.取出单列，打印类型
ser_region = orders["region"]
df_part = orders[["order_id","product","quantity"]]
print("\n2.列数据类型")
print("region单列类型：",type(ser_region))
print("多列数据类型：",type(df_part))

# 3.iloc取第4~8行，前4列
print("\n3.iloc截取4‑8行，前4列")
print(orders.iloc[3:8, 0:4])

# 4.loc筛选华东订单，展示指定列
print("\n4.华东地区订单")
print(orders.loc[orders["region"]=="华东", ["order_id","product","member_level"]])

# 5.简答
print("\n5.简答：loc是按标签名称匹配，代码可读性高，列顺序变动不会出错，适合长期维护。")

# ======================任务2=====================
# 构建新表analysis，新增4列
analysis = orders.copy()

# 1.商品总金额
analysis["gross_amount"] = analysis["quantity"] * analysis["unit_price"]

# 2.会员折扣 金卡10%，银卡5%，普通0%
analysis["member_discount"] = np.where(analysis["member_level"]=="金卡",0.10,
                             np.where(analysis["member_level"]=="银卡",0.05,0))

# 3.优惠后应付金额
analysis["payable_amount"] = analysis["gross_amount"] * (1 - analysis["member_discount"]) * (1 - analysis["coupon_rate"])

# 4.运费
analysis["shipping_fee"] = np.where(analysis["payable_amount"] >= 1000, 0, 20)

# 5.最终实付
analysis["final_amount"] = analysis["payable_amount"] + analysis["shipping_fee"]

# 展示前8行
print("\n=====任务2 新增指标前8行=====")
print(analysis[["gross_amount","member_discount","payable_amount","shipping_fee","final_amount"]].head(8))

# ======================任务3=====================
# 定义3个布尔条件
cond1 = (analysis["region"] == "华东") | (analysis["region"] == "华南")
cond2 = analysis["final_amount"] >= 700
cond3 = (analysis["quantity"] >= 2) | (analysis["member_level"] == "金卡")

# 合并条件，括号不能省略，&和|优先级高于比较运算符
mask = cond1 & cond2 & cond3

# 筛选，按金额降序
focus_ord = analysis.loc[mask, ["order_id","region","product","quantity","member_level","final_amount"]]
focus_ord = focus_ord.sort_values("final_amount", ascending=False)

print("\n=====任务3 重点跟进订单=====")
print(focus_ord)
print("说明：&、|优先级高于>=、==，不加括号会出现逻辑错误。")

# ======================任务4=====================
# 定义函数，不能修改原表
def add_order_level(df):
    df1 = df.copy()
    df1["order_level"] = np.where(df1["final_amount"] >= 2000, "战略大客户",
                         np.where(df1["final_amount"] >= 1000, "重点订单","普通订单"))
    return df1

# 使用pipe调用
leveled_orders = analysis.pipe(add_order_level)

# 统计各级订单数量
level_count = leveled_orders["order_level"].value_counts()
print("\n=====任务4 订单等级统计=====")
print(level_count)

# ======================任务5=====================
# 链式方法
region_report = (analysis
                 .pipe(add_order_level)
                 .query("final_amount >= 500")
                 .groupby(["region","order_level"])
                 .agg(
                     order_count=("order_id","count"),
                     quantity_sum=("quantity","sum"),
                     revenue_sum=("final_amount","sum"),
                     revenue_mean=("final_amount","mean")
                 )
                 .sort_values("revenue_sum", ascending=False)
                )

print("\n=====任务5 地区经营报表=====")
print(region_report)

# ======================任务6=====================
# 1.哪位销售人员总成交最高
sale_total = analysis.groupby("salesperson")["final_amount"].sum()
top_sale_name = sale_total.idxmax()
top_sale_total = sale_total.max()

# 2.该销售人员成交最高的地区
person_data = analysis[analysis["salesperson"] == top_sale_name]
region_sale = person_data.groupby("region")["final_amount"].sum()
top_region = region_sale.idxmax()
top_region_val = region_sale.max()

# 3.地区占比
rate = top_region_val / top_sale_total

print("\n=====任务6 经营诊断=====")
print(f"销售人员：{top_sale_name}")
print(f"总成交金额：{top_sale_total:.2f}")
print(f"核心地区：{top_region}")
print(f"核心地区金额：{top_region_val:.2f}")
print(f"地区贡献占比：{rate:.2%}")
print("业务结论：该销售人员业绩主要依靠单一核心地区，业务集中度偏高。")