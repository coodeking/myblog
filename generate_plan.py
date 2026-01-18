
import json
import datetime
import os

# Configuration
start_date = datetime.date(2026, 1, 19)
total_weeks = 48
student_name = "汪桑"

# Tasks data
math_schedule = [
    # Phase 1: Basic (Week 1-16)
    (1, 2, "高数基础", "张宇基础三十讲 高数第1-7讲 (函数极限/数列极限/一元函数连续性) + 课后题"),
    (3, 4, "高数基础", "张宇基础三十讲 高数第8-15讲 (一元函数微分/中值定理/泰勒公式/导数应用) + 课后题"),
    (5, 6, "高数基础", "张宇基础三十讲 高数第16-23讲 (一元函数积分/定积分应用/微分方程) + 课后题"),
    (7, 8, "高数基础", "张宇基础三十讲 高数第24-30讲 (多元函数微分/二重积分) + 课后题 (注: 数二不考无穷级数/空间解析几何/三重积分/曲线曲面积分，请核对章节)"),
    (9, 9, "高数基础", "张宇1000题基础篇 - 极限与连续 (约80题)"),
    (10, 10, "高数基础", "张宇1000题基础篇 - 一元函数微分学 (约80题)"),
    (11, 11, "高数基础", "张宇1000题基础篇 - 一元函数积分学 (约80题)"),
    (12, 12, "高数基础", "张宇1000题基础篇 - 多元函数微积分 + 微分方程 (约80题)"),
    (13, 13, "线代基础", "整理高数错题 + 张宇基础三十讲线代部分 第1-3讲 (行列式/矩阵)"),
    (14, 14, "线代基础", "张宇基础三十讲线代部分 第4-6讲 (向量/方程组/特征值/二次型)"),
    (15, 15, "线代基础", "张宇1000题基础篇 - 线代 (行列式/矩阵/向量)"),
    (16, 16, "线代基础", "张宇1000题基础篇 - 线代 (方程组/特征值/二次型)"),
    
    # Phase 2: Reinforcement (Week 17-28)
    (17, 18, "高数强化", "澄箫宇大观系列 1-2 (高数极限/中值定理) - 两天一个，先做后听"),
    (19, 20, "高数强化", "澄箫宇大观系列 3-4 (一元微积分)"),
    (21, 22, "高数强化", "澄箫宇大观系列 5-6 (多元函数/微分方程)"),
    (23, 23, "线代强化", "澄箫宇大观系列 7 (线性代数)"),
    (24, 26, "基础速刷", "660题一阶题速刷 (330题左右) - 2分钟没思路直接跳，每周约110题"),
    (27, 28, "强化总结", "整理660错题 + 针对薄弱环节看B站知识点讲解视频"),
    
    # Phase 3: True Questions (Week 29-40)
    (29, 36, "真题攻坚", "《真题一本通》(于文涛) - 按章节刷题 (87-23年真题) - 重点计算题，制作章节错题本"),
    (37, 38, "二刷巩固", "二刷澄箫宇大观系列 (倍速回顾，重点看之前没懂的)"),
    (39, 40, "查漏补缺", "复习真题一本通错题本 + 攻克薄弱章节真题"),
    
    # Phase 4: Sprint (Week 41-48)
    (41, 43, "真题套卷", "数二历年真题套卷 (09-26年，共18套) - 每天1套，严格限时3h，当天订正"),
    (44, 44, "题型整理", "浓缩真题错题本，梳理常考题型解题套路"),
    (45, 46, "模拟冲刺", "李林6+4模拟卷 (10套) - 每天1套，保持手感"),
    (47, 47, "技巧回归", "武忠祥选填技巧课 + 复习所有错题本"),
    (48, 48, "最后调整", "做近3年真题(24/25/26)找感觉，回归基础概念，调整心态")
]

english_schedule = [
    (1, 24, "单词积累", "唯一任务：背单词 APP《不背单词》 - 考研核心词3000个，暑假前刷3遍 (每天100词)"),
    (25, 40, "真题精读", "英二真题 (2010-2025) - 2天1套 (不写作文) - 重点：用APP如有《真题伴侣》背真题生词，全程单词不断"),
    (41, 44, "二刷真题", "重点二刷错题较多的真题套卷"),
    (45, 48, "作文冲刺", "Monkey老师作文模板课 (背模板+积累主题词) - 每周手写2篇，持续背单词")
]

politics_schedule = [
    (1, 40, "暂缓", "前期不建议复习政治，主要精力给数学英语"),
    (41, 44, "基础背诵", "腿姐冲刺背诵手册 (熟读) + 苍盾小程序刷选择题 (每天1套30题)"),
    (45, 46, "强化巩固", "熟读 澄箫宇'政治一页纸' + 持续刷苍盾小程序"),
    (47, 48, "冲刺背诵", "肖四大题背诵 (抄材料技巧) + 考前3天B站'考研政治抄材料'视频")
]

professional_schedule = [
    (1, 28, "基础了解", "自行安排，建议每周3h，阅读教材"),
    (29, 40, "强化复习", "自行安排，建议每周3-5h，做课后题/真题"),
    (41, 48, "冲刺背诵", "集中背诵考点，每周5-8h")
]

# Generate Weekly Plans
weeks_data = []
current_date = start_date

for week_num in range(1, total_weeks + 1):
    end_date = current_date + datetime.timedelta(days=6)
    date_str = f"{current_date.strftime('%Y.%m.%d')} - {end_date.strftime('%m.%d')}"
    
    subjects = []
    
    # Math
    math_task = "复习巩固"
    for start, end, phase, content in math_schedule:
        if start <= week_num <= end:
            math_task = f"【{phase}】 {content}"
            break
    subjects.append({
        "name": "数学",
        "content": math_task + " (目标: 110分)",
        "tasks": [{"name": math_task.split(' ', 1)[-1] if ' ' in math_task else math_task, "status": "pending"}]
    })
    
    # English
    eng_task = "背单词"
    for start, end, phase, content in english_schedule:
        if start <= week_num <= end:
            eng_task = f"【{phase}】 {content}"
            break
    subjects.append({
        "name": "英语",
        "content": eng_task,
        "tasks": [{"name": eng_task.split(' ', 1)[-1] if ' ' in eng_task else eng_task, "status": "pending"}]
    })
    
    # Politics
    pol_task = "暂无"
    for start, end, phase, content in politics_schedule:
        if start <= week_num <= end:
            pol_task = f"【{phase}】 {content}"
            break
    if week_num >= 41:
        subjects.append({
            "name": "政治",
            "content": pol_task,
            "tasks": [{"name": pol_task.split(' ', 1)[-1] if ' ' in pol_task else pol_task, "status": "pending"}]
        })
    else:
         subjects.append({
            "name": "政治",
            "content": "暂不复习 (10月开始)",
             "tasks": []
        })

    # Professional
    prof_task = "自行安排"
    for start, end, phase, content in professional_schedule:
        if start <= week_num <= end:
            prof_task = f"【{phase}】 {content}"
            break
    subjects.append({
        "name": "专业课",
        "content": prof_task,
        "tasks": []
    })

    weeks_data.append({
        "week": week_num,
        "dates": date_str,
        "items": subjects
    })
    
    current_date += datetime.timedelta(days=7)

# Save JSON
output_data = {
    "student": student_name,
    "target": "中山大学 - 085700 - 330分",
    "timeline": "48 Weeks",
    "weeks": weeks_data
}

with open(r'd:\myblog\source\kaoyan\wangsang_plan.json', 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

# Generate Markdown
md_content = f"# {student_name} 2026考研全程周规划 (Word版)\n\n"
md_content += f"**目标院校**：中山大学 085700资源与环境（专硕）\n"
md_content += f"**目标分数**：330分 (数110/英65/政65/专90)\n"
md_content += f"**规划周期**：2026.01.19 - 2026.12.20 (共48周)\n\n"
md_content += "---\n\n"

for week in weeks_data:
    md_content += f"## 第{week['week']}周 ({week['dates']})\n\n"
    for subj in week['items']:
        if subj['name'] == '政治' and '暂' in subj['content']:
            continue
        md_content += f"### {subj['name']}\n"
        md_content += f"- {subj['content']}\n\n"
    md_content += "---\n\n"

with open(r'd:\myblog\source\kaoyan\wangsang_plan.md', 'w', encoding='utf-8') as f:
    f.write(md_content)

print("Planning files generated successfully.")
