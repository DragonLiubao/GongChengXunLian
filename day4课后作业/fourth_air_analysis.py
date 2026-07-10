import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

data_text = """year,month,day,hour,PM2.5,PM10,SO2,NO2,CO,O3
2014,1,1,0,85,117,28,54,1.2,37
2014,1,1,1,86,121,27,56,1.3,34
2014,1,1,2,88,123,29,58,1.3,32
2014,2,5,12,72,95,22,47,1.0,45
2014,2,6,13,76,99,24,49,1.1,42
2014,3,12,14,55,73,18,38,0.8,56
2014,3,15,15,52,70,17,36,0.7,58
2014,6,20,14,22,35,7,20,0.4,79
2014,6,22,15,20,33,6,19,0.3,82
2014,11,8,16,92,128,31,60,1.4,30
2014,11,10,17,95,131,33,62,1.5,28
2014,12,5,18,102,140,36,65,1.6,26
2014,12,8,19,105,143,38,67,1.7,24
"""
df = pd.read_csv(StringIO(data_text))

df["datetime"] = pd.to_datetime(df[["year","month","day","hour"]])
df.set_index("datetime", inplace=True)

print("=====1.基础统计信息=====")
print(df[["PM2.5","PM10","SO2","NO2","CO","O3"]].describe())

print("\n=====2.污染物相关性分析=====")
corr_data = df[["PM2.5","PM10","SO2","NO2","CO","O3"]].corr()
print(corr_data)

month_pm25 = df.groupby(df.index.month)["PM2.5"].mean()

plt.figure(figsize=(12,9))

plt.subplot(2,2,1)
month_pm25.plot(color="#c82423")
plt.title("PM2.5月度时间变化趋势")
plt.ylabel("PM2.5浓度")

plt.subplot(2,2,2)
month_pm25.plot(kind="bar", color="#2878b5")
plt.title("1‑12月PM2.5月均浓度")
plt.xlabel("月份")

plt.subplot(2,2,3)
plt.scatter(df["PM2.5"], df["PM10"], alpha=0.6, color="#38a169")
plt.title("PM2.5与PM10相关性散点图")
plt.xlabel("PM2.5")
plt.ylabel("PM10")

plt.subplot(2,2,4)
im = plt.imshow(corr_data, cmap="RdYlBu")
plt.colorbar(im)
plt.xticks(range(len(corr_data.columns)), corr_data.columns, rotation=45)
plt.yticks(range(len(corr_data.columns)), corr_data.columns)
plt.title("污染物相关性热力图")

plt.tight_layout()
plt.savefig("air_quality_figure.png", dpi=300)
plt.show()

print("\n=====3.季节性规律总结=====")
print("1.秋冬季节(11、12、1、2月)PM2.5浓度明显偏高，污染较重。")
print("2.夏季6‑8月降水多，空气流动性强，污染物浓度最低。")
print("3.PM2.5和PM10相关性很高，变化趋势基本同步。")