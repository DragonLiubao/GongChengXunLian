import pandas as pd

# 读取数据集，使用pandas内置在线数据
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print("=====1.原始数据基本信息=====")
print("数据行列大小：", df.shape)
print("\n每列缺失值统计：")
print(df.isnull().sum())

print("\n=====2.重复值处理=====")
# 检测重复行
duplicate_num = df.duplicated().sum()
print(f"重复行数：{duplicate_num}")
# 本例无重复，若有则执行 df = df.drop_duplicates()

print("\n=====3.缺失值三种处理方式=====")
# 方式1：直接删除缺失过多的行（删除船舱Cabin缺失行）
df1 = df.dropna(subset=["Cabin"])
print(f"删除Cabin缺失后数据量：{df1.shape[0]}")

# 方式2：均值填充（年龄Age用平均值填充）
df["Age"].fillna(df["Age"].mean(), inplace=True)
print(f"\nAge列填充后缺失数量：{df['Age'].isnull().sum()}")

# 方式3：插值填充（船票费用）
df["Fare"] = df["Fare"].interpolate()
print(f"Fare插值填充后缺失数量：{df['Fare'].isnull().sum()}")

# 4.类别字段填充，众数填充登船港口
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

print("\n=====4.数据类型转换=====")
df["Pclass"] = df["Pclass"].astype("str")   # 舱位转为字符串类别型
df["Survived"] = df["Survived"].astype("bool")
print("转换后各列数据类型：")
print(df.dtypes)

print("\n=====5.异常值处理（票价异常）=====")
# 筛选票价大于300的异常数据
abnormal = df[df["Fare"] > 300]
print("票价异常行数：\n", abnormal[["Name","Fare"]])
# 剔除异常行
df = df[df["Fare"] <= 300]

print("\n=====6.清洗完成，保存清洗后数据=====")
df.to_csv("titanic_clean_data.csv", index=False, encoding="utf‑8")
print("清洗完毕，已保存为 titanic_clean_data.csv")