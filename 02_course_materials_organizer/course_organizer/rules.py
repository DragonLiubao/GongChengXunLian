homework_keywords = ["作业", "练习", "实验", "任务"]

suffix_rule = {
    "slides": [".ppt", ".pptx", ".key"],
    "code": [".py", ".ipynb", ".c", ".cpp", ".java"],
    "data": [".csv", ".xlsx", ".json"],
    "documents": [".pdf", ".doc", ".docx", ".txt", ".md"],
    "images": [".png", ".jpg", ".jpeg", ".gif"],
    "others": []
}

def get_target_folder(filename, suffix):
    for word in homework_keywords:
        if word in filename:
            return "homework"
    for folder, suf_list in suffix_rule.items():
        if suffix in suf_list:
            return folder
    return "others"