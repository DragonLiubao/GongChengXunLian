def main():
    # 用字典存放所有学生，学号作为键
    student_dict = {}
    while True:
        print("====学生成绩管理====")
        print("1.录入学生成绩")
        print("2.查询学生成绩")
        print("3.统计单科成绩")
        print("4.退出系统")
        choice = input("请输入功能序号：")

        if choice == "1":
            sno = input("输入学生学号：")
            name = input("输入学生姓名：")
            chinese = float(input("输入语文成绩："))
            math = float(input("输入数学成绩："))
            english = float(input("输入英语成绩："))
            # 单个学生信息存入字典
            info = {"姓名": name, "语文": chinese, "数学": math, "英语": english}
            student_dict[sno] = info
            print("录入完成\n")

        elif choice == "2":
            sno = input("输入要查询的学号：")
            if sno in student_dict:
                s = student_dict[sno]
                print("姓名：", s["姓名"])
                print("语文：", s["语文"])
                print("数学：", s["数学"])
                print("英语：", s["英语"])
                avg = (s["语文"] + s["数学"] + s["英语"]) / 3
                print("平均分：%.2f\n" % avg)
            else:
                print("该学生不存在\n")

        elif choice == "3":
            subject = input("选择统计科目(语文/数学/英语)：")
            score_list = []
            for data in student_dict.values():
                score_list.append(data[subject])
            if len(score_list) == 0:
                print("暂无学生数据\n")
            else:
                print("最高分：", max(score_list))
                print("最低分：", min(score_list))
                print("平均分：%.2f\n" % (sum(score_list)/len(score_list)))

        elif choice == "4":
            print("系统结束")
            break
        else:
            print("输入序号错误，请重新输入\n")

if __name__ == "__main__":
    main()