import math

# 加法
def add(num1, num2):
    return num1 + num2

# 减法
def sub(num1, num2):
    return num1 - num2

# 乘法
def mul(num1, num2):
    return num1 * num2

# 除法
def div(num1, num2):
    return num1 / num2

# 幂和开方运算
def power_sqrt(num1, num2, opt):
    if opt == "**":
        return num1 ** num2
    elif opt == "sqrt":
        return math.sqrt(num1)

# 写入计算记录到文件
def save_record(text):
    f = open("record.txt", "a", encoding="utf‑8")
    f.write(text + "\n")
    f.close()

# 读取历史记录
def show_history():
    try:
        f = open("record.txt", "r", encoding="utf‑8")
        content = f.read()
        f.close()
        print("====历史记录====")
        print(content)
    except FileNotFoundError:
        print("暂无历史记录")

def main():
    while True:
        print("\n====简易计算器====")
        print("1.加法  2.减法  3.乘法  4.除法")
        print("5.幂运算  6.开方  7.查看历史  8.退出")
        op = input("请选择功能序号：")
        try:
            if op in ["1", "2", "3", "4", "5"]:
                n1 = float(input("输入第一个数字："))
                n2 = float(input("输入第二个数字："))
                res = 0
                if op == "1":
                    res = add(n1, n2)
                    record = f"{n1} + {n2} = {res}"
                elif op == "2":
                    res = sub(n1, n2)
                    record = f"{n1} - {n2} = {res}"
                elif op == "3":
                    res = mul(n1, n2)
                    record = f"{n1} × {n2} = {res}"
                elif op == "4":
                    res = div(n1, n2)
                    record = f"{n1} ÷ {n2} = {res}"
                elif op == "5":
                    res = power_sqrt(n1, n2, "**")
                    record = f"{n1} ** {n2} = {res}"
                print("计算结果：", res)
                save_record(record)

            elif op == "6":
                n1 = float(input("输入需要开方的数字："))
                res = power_sqrt(n1, 0, "sqrt")
                record = f"sqrt({n1}) = {res}"
                print("计算结果：", res)
                save_record(record)

            elif op == "7":
                show_history()

            elif op == "8":
                print("计算器结束")
                break
            else:
                print("序号输入错误")
        except ZeroDivisionError:
            print("错误：除数不能为0")
        except ValueError:
            print("错误：请输入有效数字")

if __name__ == "__main__":
    main()