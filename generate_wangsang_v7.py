# -*- coding: utf-8 -*-
import json
from datetime import datetime, timedelta

def build():
    weeks = []
    start_date = datetime(2026, 3, 2)
    
    # Mathematical Stages calculation (Total 42 weeks)
    math_stages = [
        (8, "【高数基础】三十讲课后题+1000题基础", "张宇基础三十讲课后题+1000题基础做完。\n⚠️不听张宇课！遇到不懂直接去B站搜“1000题讲解”(千羽、考研数学777、没咋了等)。"),
        (4, "【线代基础】三十讲课后题+1000题基础", "张宇三十讲线代课后题+1000题基础做完。\n⚠️同样不听课！有不懂直接去B站搜播放量高的UP主讲解。"),
        (3, "【澄箫宇大观】第一遍", "b站“澄箫宇”大观系列首刷，大概7个视频，两天看一个。\n⚠️核心绝杀：每讲一个题之前必须【暂停自己先做一遍】，做不出来再继续听小宇讲！"),
        (4, "【660题速刷】一阶速刷", "660一阶题速刷。\n⚠️速刷意思是把会做的做了，但凡2分钟没思路的直接跳过，然后对答案订正。别死磕，填补漏洞即可。"),
        (7, "【第一轮真题】真题一本通（于文涛）", "整个考研期最重要的习题册没有之一！\n✅ 搞个单独错题本，按章节分类整理，每个题务必弄懂！\n✅ 以计算题为重点复习，所有习题册只做这里的证明题！"),
        (2, "【澄箫宇大观】二刷", "带着真题的磨砺，二刷澄箫宇大观。这一次重点串联知识点网络，寻找顿悟的时刻。"),
        (3, "【二轮真题】数二真题", "每天一套数二（09-26年）。\n✅ 借套卷把真题错题本浓缩一下，整理对应的题型。咱们考数二专硕，稳扎稳打以计算为王！"),
        (2, "【全真模拟】李林6+4", "每天一套李林6+4（10套）。练习真实考场分配节奏。"),
        (4, "【武忠祥选填课+错题本】", "啃两本错题：真题错题本、模拟卷错题本。\n✅ 配合武忠祥选填技巧课，对应错题知识点看网课视频查漏补缺。"),
        (5, "【考前冲刺】近3年真题再刷", "最后阶段主要是看错题，不要光看，要动手算！\n✅ 整理错题与知识点。\n✅ 做近3年真题熟悉考试风格（和模拟卷出入大，最相似的就是近3年卷子）。")
    ]
    math_tasks = []
    for duration, title, content in math_stages:
        for _ in range(duration):
            math_tasks.append({"title": title, "content": content, "hours": "占大盘60%"})

    # Adjust math tasks to exactly 42 weeks
    while len(math_tasks) < 42:
        math_tasks.append(math_tasks[-1])
    math_tasks = math_tasks[:42]

    # English Stages (42 weeks)
    eng_stages = [
        (16, "【暑假前】疯狂背单词", "唯一的任务：疯狂背考研核心词（约3000个）。\n⚠️强推《不背单词》APP，暑假前最好刷三遍！\n🚫考研英语少听课或者不听课，每天读阅读和背单词，不精翻文章，不买手译本！"),
        (18, "【暑假开始】英一真题+Monkey作文课", "✅ 两天一套英一真题（不写作文）。\n✅ 用《真题伴侣》APP标生词，反复背真题里的意思（期间原单词APP不能断！）。\n✅ 听Monkey考研作文模板课，背模板并积累主题词！"),
        (8, "【冲刺时间】二刷真题+练熟模板", "✅ 重点二刷错题。\n✅ 把作文模板练熟练透。\n⚠️ 持续背单词，绝对不能断！")
    ]
    eng_tasks = []
    for duration, title, content in eng_stages:
        for _ in range(duration):
            eng_tasks.append({"title": title, "content": content, "hours": "占大盘30%"})
            
    while len(eng_tasks) < 42:
        eng_tasks.append(eng_tasks[-1])
    eng_tasks = eng_tasks[:42]

    # Politics Stages (42 weeks)
    pol_stages = [
        (31, None, None), # March 2 to early October is roughly 31 weeks
        (8, "【十月初起步】腿姐手册+苍盾刷题+一页纸", "⚠️ 远离徐涛冗长课，远离肖1000题！\n✅ 腿姐冲刺背诵手册（熟读）。\n✅《苍盾小程序》每天刷一套(30选择题)。\n✅ 熟读澄箫宇“政治一页纸”。"),
        (3, "【冲刺保命】死背肖四+B站抄材料", "✅ 等肖四出来后直接背大题（背不住没关系，对成绩影响不大）。\n🔥 最后几天务必看B站“考研政治抄材料”，上了考场基本只能抄材料，学会绝杀！")
    ]
    pol_tasks = []
    for duration, title, content in pol_stages:
        for _ in range(duration):
            if title is None:
                pol_tasks.append(None)
            else:
                pol_tasks.append({"title": title, "content": content, "hours": "占大盘10%"})
                
    while len(pol_tasks) < 42:
        pol_tasks.append(pol_tasks[-1])
    pol_tasks = pol_tasks[:42]

    messages = [
        "所有科目都不准当「耐听王」，多想多算多做，一定要亲自落实到笔头上！",
        "时间安排务必合理！这里的时间100%是排除了专业课，别忘了自行在日程里给专业课留出预定时间！",
        "专业课的学习时间默认比数学少一点，请自行把控好天平的倾斜度！",
        "不要大量时间听课！听课永远学不会，靠做题才能真正在考场写出来！",
        "遇到不会的题目直接去B站搜播放量高的UP主，很多比大机构讲得都要好！",
        "张宇“超实数”、微分算子法、海涅定理、压缩映射原理、stolz法则，连想考150的都不需要看！",
        "明确优先级：真题最优先，习题册往后稍稍，模拟题少做！",
        "所有习题册+模拟卷均不做证明题，我们只写历年真题的证明题！"
    ]

    for i in range(42):
        cur = start_date + timedelta(days=i*7)
        nxt = start_date + timedelta(days=i*7+6)
        
        week_data = {
            "week": i + 1,
            "dates": f"{cur.month}月{cur.day}日 - {nxt.month}月{nxt.day}日",
            "theme": math_tasks[i]["title"].split("】")[0].replace("【", ""),
            "message": messages[i % len(messages)],
            "math": math_tasks[i],
            "english": eng_tasks[i]
        }
        
        if pol_tasks[i]:
            week_data["politics"] = pol_tasks[i]
            
        weeks.append(week_data)

    data = {"student": "汪桑", "weeks": weeks}
    
    with open("D:/myblog/source/kaoyan/wangsang_detail_final.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    build()
