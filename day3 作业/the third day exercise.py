import warnings
warnings.filterwarnings("ignore")
import numpy as np

# 定义全局列表存储学生姓名和成绩
name_list = []
score_list = []

def show_menu():
    print("-" * 40)
    print("        成绩分析系统")
    print("-" * 40)
    print("1. 输入成绩数据")
    print("2. 查看成绩统计")
    print("3. 查看成绩排名")
    print("4. 查看成绩分布")
    print("5. 查询学生成绩")
    print("6. 退出系统")
    print("-" * 40)

def input_score():
    # 录入学生姓名和成绩
    name_list.clear()
    score_list.clear()
    num = int(input("请输入学生人数："))
    for i in range(num):
        name = input(f"请输入第{i+1}个学生姓名：")
        score = int(input(f"请输入成绩："))
        name_list.append(name)
        score_list.append(score)
    print("成绩录入完成！")

def stat_score():
    # 成绩统计，用numpy计算
    arr = np.array(score_list)
    print("\n====成绩统计信息====")
    print(f"平均分：{np.mean(arr):.2f}")
    print(f"最高分：{np.max(arr)}")
    print(f"最低分：{np.min(arr)}")
    print(f"方差：{np.var(arr):.2f}")
    print(f"标准差：{np.std(arr):.2f}")

def sort_score():
    # 成绩从高到低排名
    arr = np.array(score_list)
    # 把姓名和成绩打包，按成绩降序排序
    stu_data = list(zip(name_list, score_list))
    stu_data.sort(key=lambda x: x[1], reverse=True)
    print("\n====成绩排名（从高到低）====")
    for i in range(len(stu_data)):
        print(f"第{i+1}名  {stu_data[i][0]}  {stu_data[i][1]}分")

def score_distribute():
    # 成绩等级划分
    arr = np.array(score_list)
    excellent = np.sum(arr >= 90)
    good = np.sum((arr >= 80) & (arr < 90))
    medium = np.sum((arr >= 60) & (arr < 80))
    fail = np.sum(arr < 60)
    total = len(arr)
    print("\n====成绩等级分布====")
    print(f"优秀(90~100)：{excellent}人，占比{excellent/total*100:.1f}%")
    print(f"良好(80~89)：{good}人，占比{good/total*100:.1f}%")
    print(f"及格(60~79)：{medium}人，占比{medium/total*100:.1f}%")
    print(f"不及格(0~59)：{fail}人，占比{fail/total*100:.1f}%")

def search_stu():
    # 查询单个学生成绩
    search_name = input("请输入要查询的学生姓名：")
    if search_name in name_list:
        idx = name_list.index(search_name)
        print(f"\n{search_name} 的成绩为：{score_list[idx]}")
    else:
        print("该学生不存在！")

# 主程序循环
while True:
    show_menu()
    choice = int(input("请选择："))
    if choice == 1:
        input_score()
    elif choice == 2:
        stat_score()
    elif choice == 3:
        sort_score()
    elif choice == 4:
        score_distribute()
    elif choice == 5:
        search_stu()
    elif choice == 6:
        print("系统退出！")
        break
    else:
        print("输入错误，请重新选择！")