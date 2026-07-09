from pathlib import Path
import shutil
from .rules import get_target_folder

def organize_files(source_dir, target_dir, dry_run, mode):
    source = Path(source_dir)
    target = Path(target_dir)
    plan_list = []
    count_dict = {}

    for file in source.iterdir():
        if file.is_dir():
            continue
        filename = file.name
        suffix = file.suffix
        folder_name = get_target_folder(filename, suffix)

        target_folder = target / folder_name
        target_file = target_folder / filename
        num = 1
        while target_file.exists():
            new_name = file.stem + f"_{num}"
            target_file = target_folder / (new_name + suffix)
            num += 1

        plan_list.append((str(file), str(target_file)))
        if folder_name not in count_dict:
            count_dict[folder_name] = 0
        count_dict[folder_name] += 1

    if dry_run:
        print("=====预运行模式，整理计划=====")
        for src, dst in plan_list:
            print(f"{src}  -->  {dst}")
        return plan_list, count_dict

    for src, dst in plan_list:
        dst_folder = Path(dst).parent
        dst_folder.mkdir(parents=True, exist_ok=True)
        if mode == "copy":
            shutil.copy(src, dst)
        elif mode == "move":
            shutil.move(src, dst)

    report_path = target / "整理报告.txt"
    with open(report_path, "w", encoding="utf-8") as f:
        if mode == "copy":
            f.write("本次执行方式：复制文件，原文件保留\n")
        else:
            f.write("本次执行方式：移动文件，原文件转移\n")
        f.write(f"总共整理文件数量：{len(plan_list)}\n\n")
        f.write("文件迁移明细：\n")
        for src, dst in plan_list:
            f.write(f"{src}  -->  {dst}\n")
        f.write("\n各类文件统计：\n")
        for folder, num in count_dict.items():
            f.write(f"{folder}：{num}个\n")

    return plan_list, count_dict