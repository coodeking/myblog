# -*- coding: utf-8 -*-
import json
from datetime import datetime, timedelta

def generate_tingting_v3():
    weeks = []
    
    # Timeline starts Feb 23, 2026. Exam is typically third weekend of Dec (e.g., Dec 19-20, 2026).
    start_date = datetime(2026, 2, 23)
    exam_date = datetime(2026, 12, 19)
    total_days = (exam_date - start_date).days
    total_weeks = total_days // 7 + 1 # roughly 43 weeks
    
    # 按照用户的极度严格顺序分配数学任务:
    # 1. 高数基础：张宇30讲课后 + 1000题基础 -> 整理错题选看网课
    # 2. 线代基础：张宇30讲课后 + 1000题基础 -> 整理错题选看网课
    # （不听张宇课，遇阻看B站1000题讲解 千羽/考研数学777/没咋了）
    # 3. 澄箫宇大观（每个大观先做后听，两天一个，约7个）
    # 4. 660一阶题速刷（不会直接跳）
    # 5. 第一轮真题《真题一本通》于文涛（最重要，搞单独错题本按章节分类）重点计算题
    # 6. 二刷澄箫宇大观
    # 7. 二轮真题 数二每天一套(09-26年) -> 浓缩真题错题本，整理对应题型
    # 8. 李林6+4(10套) 每天一套
    # 9. 真题/模拟题错题本 + 武忠祥选填技巧（对应看视频）
    # 10. 最后阶段整理，近3年真题再刷一遍
    
    math_schedule = []
    # 阶段1：高数基础 (10周)
    for i in range(10): math_schedule.append(("【高数基础】三十讲课后 + 1000题基础", "重点完成高数部分基础覆盖，整理错题。\n⚠️ 不听张宇长课，利用B站千羽等搜1000题讲解。不做任何证明题。"))
    # 阶段2：线代基础 (5周)
    for i in range(5): math_schedule.append(("【线代基础】三十讲课后 + 1000题基础", "重点完成线代部分基础覆盖，整理错题。\n⚠️ 同样不听名师长课，有问题搜B站讲解。不做证明题。"))
    # 阶段3：澄箫宇大观 (3周)
    for i in range(3): math_schedule.append(("【强力拔高】B站“澄箫宇”大观首刷", "每两天看一个大观（共约7个）。\n⚠️ 铁律：必须先暂停自己做一遍，再听他讲！"))
    # 阶段4：660题速刷 (3周)
    for i in range(3): math_schedule.append(("【客观题速刷】660一阶题", "第一遍只做会做的，2分钟没思路直接跳过对答案订正。\n⚠️ 不要深陷偏难怪概念。"))
    # 阶段5：一本通一轮 (8周)
    for i in range(8): math_schedule.append(("【核心大头】第一轮真题：《真题一本通》", "整个考研期最重要的习题册！\n✅ 建立专属《真题错题本》，按章节分类整理。\n✅ 所有习题册只做这里的真题证明题，其余全攻计算！"))
    # 阶段6：二刷大观 (2周)
    for i in range(2): math_schedule.append(("【串联体系】二刷“澄箫宇”大观", "带着前期的真题错题感悟，二刷大观，把零散知识点结成网。"))
    # 阶段7：数二二轮真题 (3周)
    for i in range(3): math_schedule.append(("【套卷演练】二轮真题：数二套卷", "每天一套数二(09-26年)。\n✅ 借此机会把《真题错题本》浓缩一下，整理对应的题型。"))
    # 阶段8：李林6+4 (2周)
    for i in range(2): math_schedule.append(("【全真模考】李林6+4(10套)", "每天一套，雷打不动。见识新题，查漏补缺。"))
    # 阶段9：选填技巧与错题 (3周)
    for i in range(3): math_schedule.append(("【选填保命】武忠祥选填技巧 + 消化两大错题本", "复习《真题错题本》和《模拟卷错题本》。\n✅ 结合武忠祥选填课技巧，哪里不懂点对点看视频。"))
    # 阶段10：最后冲刺 (4周)
    for i in range(4): math_schedule.append(("【大道至简】回归错题 + 近3年真题", "专注错题本与知识点整理。\n✅ 重新刷一遍近3年的真题，熟悉命题老头真实风格（不碰杂牌模拟卷了）。"))

    # 如果有富余周数，补在冲刺
    while len(math_schedule) < total_weeks:
        math_schedule.append(("【考前静心】回归错题本 + 基本手感保温", "不要再做压轴难题，保持每天能算对2道题的手感即可。"))

    # 英语进度表
    # 暑假前 (到6月底约18周): 疯狂背单词
    # 暑假及以后 (第19周起): 两天一套英二真题阅读 + B站Monkey作文课 + 单词不断
    # 冲刺期: 熟练模板
    eng_schedule = []
    for i in range(18): eng_schedule.append(("【词汇狂飙】疯狂背单词", "唯一任务：用《不背单词》APP疯狂背考研大纲核心三千词。\n💡 目标暑假前刷满三遍！不搞精翻和手译本！"))
    for i in range(total_weeks - 18 - 8): eng_schedule.append(("【真题与作文】英二真题 + Monkey作文课", "✅ 两天一套英二真题（用《真题伴侣》标生词死背）。\n✅ 开始听Monkey作文模板课，积累主题词。"))
    for i in range(8): eng_schedule.append(("【冲刺防守】二刷真题 + 熟写作文模板", "✅ 重点二刷错题。\n✅ 每天把作文模板像默写古诗一样形成肌肉记忆。\n⚠️ 单词背到上考场前一天！"))

    # 政治进度表
    # 最早10月初开始（例如按照倒计时最后11周计算）
    pol_schedule = []
    for i in range(total_weeks):
        if i < total_weeks - 11:
            pol_schedule.append(None)
        elif i < total_weeks - 3:
            pol_schedule.append(("【选择题扫盲】腿姐手册 + 苍盾小程序 + 一页纸", "✅ 熟读腿姐冲刺背诵手册、澄箫宇政治一页纸。\n✅ 每天在马桶时间用《苍盾小程序》刷一套(30道)选择题。"))
        else:
            pol_schedule.append(("【大题底牌】死背肖四 + B站抄材料神技", "✅ 疯狂背诵肖四大题。\n🔥 考前几天务必学会B站【政治怎么抄材料】，这是考场大题最终保命绝技！"))

    msg_pool = [
        "不准当耐听王！听课永远学不会，只有通过做题才能在考场上写出来！",
        "张宇超实数、微分算子、海涅定理、Stolz定理，统统不要看！",
        "遇到不会的，直接去B站搜播放量高的UP主找某一道题的讲解！",
        "永远记住：真题分类最优先！《真题一本通》是整个考研期最重要的书！",
        "每天的公共课分配中，数学要占60%，英语30%，政治10%。记得预留专业课的时间！",
        "数学所有习题册和模拟卷【都不做证明题】（真题中的证明题除外）！"
    ]

    for i in range(total_weeks):
        current_date_str = (start_date + timedelta(days=i*7)).strftime("%m.%d")
        end_date_str = (start_date + timedelta(days=i*7+6)).strftime("%m.%d")
        
        m_title, m_cnt = math_schedule[i]
        e_title, e_cnt = eng_schedule[i]
        p_data = pol_schedule[i]

        msg = msg_pool[i % len(msg_pool)]
        if "大观" in m_title:
            msg = "澄箫宇大观：切记一定要先暂停自己动笔做，然后再继续听讲解！"
        elif "一本通" in m_title:
            msg = "这阶段搞一个单独的错误本！按章节分类，把一本通的错题全部吃透！"
        elif "数二套卷" in m_title:
            msg = "刷数二套卷是为了保持计算手感，把真题错题本拿出来浓缩整理题型！"

        week_data = {
            "week": i + 1,
            "dates": f"{current_date_str} - {end_date_str}",
            "theme": m_title.split("】")[0].replace("【", ""),
            "message": msg,
            "math": {
                "title": m_title,
                "content": m_cnt,
                "hours": "占大盘60%"
            },
            "english": {
                "title": e_title,
                "content": e_cnt,
                "hours": "占大盘30%"
            }
        }

        if p_data:
            week_data["politics"] = {
                "title": p_data[0],
                "content": p_data[1],
                "hours": "占大盘10%"
            }

        weeks.append(week_data)

    data = {
        "student": "婷婷",
        "weeks": weeks
    }

    with open("D:/myblog/source/kaoyan/tt/tingting_v3.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    generate_tingting_v3()
    print("V3 JSON generated.")

