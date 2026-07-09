# 课程资料整理器
## 运行指令
1. 预运行（仅输出计划，不生成文件夹）
python main.py --source sample_materials --target organized_materials --dry-run

2. 正式整理，复制文件
python main.py --source sample_materials --target organized_materials

3. 拓展：移动文件模式
python main.py --source sample_materials --target organized_materials --mode move

## 知识点简答
1.Path为面向对象路径写法，自动适配Windows系统；普通字符串路径需要手动处理斜杠，兼容性差。
2.argparse接收终端命令参数，不用修改代码即可切换整理目录。
3.先输出整理计划，核对无误再操作文件，防止文件丢失。
4.字典存储后缀分类规则，后期新增文件类型直接修改字典即可。
5.程序拆分为主程序入口、核心逻辑、分类规则，模块化清晰，便于维护。

## Python作用
通过Python实现自动化批量整理文件，完成重复的手工归类任务，提升文件管理效率。
项目已托管至GitHub仓库，完成一次代码版本提交。
项目地址：https://github.com/DragonLiubao/GongChengXunLian