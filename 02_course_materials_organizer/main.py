import sys
import argparse
from pathlib import Path
# 自动识别模块路径，彻底解决 No module 报错
sys.path.append(str(Path(__file__).parent))

from course_organizer.core import organize_files

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=str, required=True)
    parser.add_argument("--target", type=str, required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--mode", type=str, default="copy", choices=["copy", "move"])
    args = parser.parse_args()

    source_path = Path(args.source)
    target_path = Path(args.target)

    if not source_path.exists():
        print("源文件夹不存在！")
        return

    organize_files(source_path, target_path, args.dry_run, args.mode)
    if not args.dry_run:
        print("文件整理完成，已生成整理报告！")

if __name__ == "__main__":
    main()