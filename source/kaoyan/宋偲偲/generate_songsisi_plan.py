# -*- coding: utf-8 -*-
import json
from datetime import datetime, timedelta

def get_full_plan_songsisi():
    weeks = []
    # 宋偲偲 start date
    start_date = datetime(2026, 3, 15)
    
    def get_date_str(week_idx):
        s = start_date + timedelta(days=(week_idx-1)*7)
        e = s + timedelta(days=6)
        return f"{s.strftime('%m.%d')} - {e.strftime('%m.%d')}"

    def add_week(week_num, theme, msg, eng, pol=None, mind=None):
        dates = get_date_str(week_num)
        week_data = {
            "week": week_num,
            "dates": dates,
            "theme": theme,
            "message": msg,
            "english": eng
        }
        if pol:
            week_data["politics"] = pol
        if mind:
            week_data["mindset"] = mind
        weeks.append(week_data)

    # 41个真实的干货经验补充（语气客观、平实）
    tips = [
        "（复习建议：备考初期的核心是建立每天学习的习惯。每天需留出固定的时间复习英语单词，这是达到国家线的基础。）",
        "（复习建议：考研英语一的核心在于词汇量和长难句解析。前期推荐踏实背诵单词，暂时不需要看冗长的阅读网课。）",
        "（复习建议：背单词不要追求一次记住拼写和所有意思。可以使用《不背单词》APP快速浏览核心词汇，每天200个以上。）",
        "（复习建议：如果英语语法基础薄弱，可以参考【田静】老师的《句句真研》，重点学习划分主谓宾和理解从句结构。）",
        "（复习建议：背单词时出现遗忘是正常现象。即使前一天背过的词汇看起来很生疏，也请继续推进，软件的记忆曲线会辅助巩固。）",
        "（复习建议：听完语法课后，建议使用历年真题（如2000-2005年）中的长难句进行切分练习，将理论转化为实际能力。）",
        "（复习建议：每天的基础任务必须明确，英语单词打卡是必须完成的。即使时间紧张，花30分钟过一遍单词也能保持学习连贯性。）",
        "（复习建议：遇到难以记忆的单词，可以尝试结合发音或词根词缀进行联想记忆。）",
        "（复习建议：不建议在词汇网课上花费过多时间，词汇的掌握更多依赖个人的高频重复记忆。）",
        "（复习建议：在能基本理解长难句主干后，可以尝试每天读半篇早期真题阅读。初期不要求做对题目，重点练习理清句子的逻辑关系。）",
        "（复习建议：英语一完型填空的得分难度较大。前期复习阶段可以暂时放下完型和新题型，将精力集中在单词和长难句上。）",
        "（复习建议：对于在职或实习的同学，建议充分利用碎片时间，如通勤或排队时使用单词APP进行复习。）",
        "（复习建议：词汇的积累需要过程，建议在暑假前将核心大纲词汇复习三遍左右。）",
        "（复习建议：暑假前一般不需要启动政治复习，过早开始容易遗忘且占用时间。）",
        "（复习建议：检验基础阶段长难句是否过关的方法，通常是能否在较短时间内迅速判断出历年真题长句中的主谓结构。）",
        "（复习建议：保持作息的规律。周末可以适当休息，但要注意避免打乱整体学习节奏，保持复习的连贯性。）",
        
        "（复习建议：7月份进入暑期复习关键期，此时可以正式进入英语阅读解题和政治基础阶段的学习。）",
        "（复习建议：英语阅读解题方面，可以参考【唐迟】老师的《阅读的逻辑》，学习如何通过命题逻辑和同义替换来解题。）",
        "（复习建议：刚接触英语一真题阅读时有很多不懂的地方是正常的。可以结合《真题伴侣》APP，标注生词以便后续循环复习。）",
        "（复习建议：政治复习正式启动。如果政治基础较弱，可以听【徐涛】的强化班（特别是马哲部分），帮助理解概念。）",
        "（复习建议：听完政治课程后，需要配套做题以检验效果。建议使用小程序刷对应的章节选择题巩固考点。）",
        "（复习建议：分析英语阅读真题时，重点在于理解正确选项在原文中的同义替换情况，以及错误选项的干扰方式。）",
        "（复习建议：如果某道英语题听了解析后依然不解，可以暂时跳过。在考研英语中掌握80%的基础题逻辑即可。）",
        "（复习建议：暑期复习容易疲惫，可以在下午或晚上状态一般时观看政治网课，作为学习内容的调节。）",
        
        "（复习建议：英语第一轮真题做完后，复习重点转向二刷。二刷时需要说出每个选项在文章中的具体出处和对应关系。）",
        "（复习建议：9月份英语作文需要提上日程。对于大部分同学，建议参考【Monkey老师】的作文模板课，梳理出通用的逻辑框架。）",
        "（复习建议：政治基础课听完后进入强化刷题期。每天可利用碎片时间在小程序上刷一两套选择题，保持题目手感。）",
        "（复习建议：结合通用作文模板，平时可根据不同题材（如环保、美德、科技等）归纳对应的替换主题词和相关素材。）",
        "（复习建议：政治马哲偏重理解，史纲重在时间线索。可以尝试自己梳理近代史的各个重要事件和时间轴，加深记忆。）",
        
        "（复习建议：10月份，政治复习开始使用精简资料。可以购买《腿姐冲刺背诵手册》，不需要再看长视频课程，每天翻看手册加深记忆。）",
        "（复习建议：可以配合【澄箫宇】的“政治一页纸”等资料整理易混淆知识点。此时重点依然在客观选择题，暂缓长篇主观题背诵。）",
        "（复习建议：如果英语其他题型已成体系且想提高翻译成绩，可以听听【唐静】老师的翻译课，学习句子的拆分与组合方法。）",
        "（复习建议：这个阶段英语作文模板必须开始动笔练习。将脑中的框架落实到纸上，保证卷面整洁，避免基础拼写和时态错误。）",
        "（复习建议：英语一的新题型考查重点在于段落间的逻辑衔接和代词指代。可以通过练习近年真题来熟悉词义复现等解题规律。）",
        
        "（复习建议：11月份，每周建议安排一个下午（14:00-17:00）完全按照考试时间进行英语全套真卷模拟。）",
        "（复习建议：成套做题时可以摸索自己最合适的答题顺序（如：作文->阅读->新题型->翻译->完型），在限时压力下锻炼解题能力。）",
        "（复习建议：各类政治模拟卷开始陆续出版。可以使用肖八主要进行客观选择题的查漏补缺和时政知识点扩充。）",
        
        "（复习建议：12月重点关注政治主观题。资料《肖四》出版后，主攻背诵其主观大题要点。）",
        "（复习建议：如果在考场上遇到未准备的政治材料题，需要沉着应对。可以考前了解如何利用卷面材料并结合已知原理分点作答的方法。）",
        "（复习建议：最后半个月，英语不建议做新的模拟卷。主要复习以往的错题真题，巩固作文模板，每天适度翻阅词汇保持语感。）",
        "（复习建议：考前最后几天重点调整心态和作息。检查好文具和相关考务信息，以平稳的状态上了考场即是胜利。）"
    ]

    # ================= 阶段一：词汇深耕与语法长难句 (Week 1-16) 政治不启动 =================
    
    add_week(1, "基础养成：进入备考状态", 
             "备考初期的核心是建立每天学习的习惯，稳步打好英语词汇基础。\n" + tips[0],
             {"title": "词汇复习计划入门", "hours": "日常安排", "content": "✅ 核心任务：下载《不背单词》或类似APP，设定每天核心词汇量任务。\n操作建议：初期学习不需要耗费时间拼写，重点在于快速认知。看到单词能回忆起基本的中文释义即可，遇到想不起来的直接查看答案，通过频率来克服遗忘。"})

    add_week(2, "词汇循环：克服遗忘焦虑", 
             "单词背了忘是正常的记忆规律，不需要为此感到挫败。坚持重复复习即可。\n" + tips[2],
             {"title": "大纲词汇长线复习", "hours": "日常安排", "content": "✅ 核心任务：每天完成APP里分配的新词和复习词。\n建议将主要精力放在自主重复记忆上，此时不需要学习时间过长的前期词汇视频课。"})

    for i in range(3, 17):
        msg = tips[i]
        add_week(i, f"词汇巩固与长难句预热 (第{i}周)", 
                 "这段时间复习可能较为枯燥，阶段重点仍为外语词汇记忆与长难句理解。\n" + msg,
                 {"title": "语法课程引入与词汇推进", "hours": "阶段重点", "content": "✅ 任务：继续通过软件滚动复习词汇，目标在进入暑假前较熟练地掌握大纲词。\n✅ 课程：如果语法基础较弱，可以听【田静】老师的《句句真研》。课程需适度观看，重点掌握划分主谓宾和辨识从句。听懂后可选取部分早年历年真题中的长句进行拆分练习。"})

    # ================= 阶段二：英语真题阅读初期 + 政治正式启动 (Week 17-24) =================

    add_week(17, "英语阅读实战入门 & 政治启动", 
             "7月份进入暑期，考研复习将更加深入。计划开始介入长篇阅读分析并开启政治科目。\n" + tips[16],
             {"title": "《阅读的逻辑》启蒙", "hours": "专项训练", "content": "✅ 安排：可以开始做英语一早期年份的阅读理解真题，每两三天一篇即可。\n✅ 课程：做完并对答案后，推荐观看【唐迟】老师的阅读讲解。学习阅读中的逻辑关联及同义替换思路。"},
             {"title": "政治课程起手", "hours": "稳步推进", "content": "✅ 安排：政治复习正式启动。可以听【徐涛】老师的强化班视频（建议先听马哲部分）。听课后需及时配套《苍盾小程序》或练习册做相应的章节选择题巩固。"})

    for i in range(18, 25):
        msg = tips[i]
        add_week(i, f"真题阅读分析与政治框架学习 (第{i}周)", 
                 "暑期的持续学习能为后期的冲刺打下坚实的基础。\n" + msg,
                 {"title": "真题阅读专项练习", "hours": "专项训练", "content": "✅ 任务：维持规律的真题阅读进度，结合相关真题解析课程加深理解。\n✅ 辅助工具：在做真题时可以使用《真题伴侣》等APP标记阻碍理解的实词，软件会安排后续的循环背诵。不建议大范围通篇手写翻译整篇文章。"},
                 {"title": "政治强化课程与刷题", "hours": "日常安排", "content": "✅ 任务：稳步推进政治强化课的学习，尤其是原理性较强的章节需重点注意。\n✅ 练习：听完相应章节后，务必要用小程序或习题册刷对应的高频选择题，以此检验听课效果。"})

    # ================= 阶段三：英语二刷定型与作文起步 (Week 25-28) =================

    add_week(25, "真题二刷与作文课程引入", 
             "暑假过后，随着阅读方法基本掌握，可转入二刷阶段。英语作文也需要开始基础学习。\n" + tips[24],
             {"title": "真题回看与作文模板学习", "hours": "能力提升", "content": "✅ 任务一：二刷之前做过的阅读真题。二刷重点在于能否准确定位每个选项对应的原文依据及句义替换过程。\n✅ 任务二：开始规划英语作文学习，推荐了解类似【Monkey老师】的英语大作文课程，梳理通用框架模板，保证基本的结构分。"},
             {"title": "整理政治史纲时间轴", "hours": "知识归纳", "content": "✅ 任务：随着强化课进入尾声，可以尝试拿几张白纸，自己画出中国近代史的会议、核心条约及时间轴脉络，有助于日后梳理客观选择题的考点。"})

    for i in range(26, 29):
        msg = tips[i-1]
        add_week(i, f"英语作文素材整理 (第{i}周)", 
                 "掌握了作文基本逻辑后，建议根据自身的备考资料填充积累相应的词汇库。\n" + msg,
                 {"title": "积累相关主题素材词汇", "hours": "能力提升", "content": "✅ 任务：针对不同常见题材（如环保、美德、网络科技、文化等），自主归纳一些替换词和得体的短语。\n在掌握通用结构的基础上，合理的词汇替换能让文章更加充实。"},
                 {"title": "政治选择题日测", "hours": "日常安排", "content": "✅ 任务：每天利用相对细碎的时间，使用小程序刷一定数量的政治选择题。通过查阅错题解析补充之前遗忘的知识点。"})

    # ================= 阶段四：政治冲刺发力与套卷压测 (Week 29-35) =================
    
    add_week(29, "政治背诵资料引入与英语翻译", 
             "进入十月份后，市面上的各类精简版政治资料会陆续出版，政治的重点逐渐转向要点记忆。\n" + tips[29],
             {"title": "翻译技能学习与作文默写", "hours": "进度补充", "content": "✅ 翻译：如果阅读方法已较成熟，想提高翻译精确度，可以听听【唐静】老师的相关翻译课程，学习长难句拆分组合的基本技巧。\n✅ 作文：作文模板和框架需要开始落实到纸面上进行默写，以排查拼写及语法错误。"},
             {"title": "《腿姐冲刺背诵手册》或同类资料", "hours": "归纳记忆", "content": "✅ 安排：购入类似《腿姐冲刺背诵手册》等复习资料。现阶段不需要再看基础的长课程，将复习重点放在翻看和熟练背诵手册中的各重点选择题高频考点。"})

    for i in range(30, 36):
        msg = tips[i-1]
        add_week(i, f"英语套卷限时与政治提纯 (第{i}周)", 
                 "公共课的复习开始逐渐进入套卷演练和限时答题的时期。\n" + msg,
                 {"title": "英语真题套卷计时考核", "hours": "全真模拟", "content": "✅ 安排：建议每周安排一个完整的下午（14:00-17:00），做一套近年未使用过的真题全套试卷。\n✅ 目标：寻找最适合自己的考场答题顺序（如：作文->阅读->新题型->翻译->完型）。在遇到生词时练习合理猜词的能力。"},
                 {"title": "客观题易混知识点梳理", "hours": "日常复习", "content": "✅ 安排：继续保持通过小程序或练习册进行日测。\n✅ 辅助：可配合类似“政治一页纸”等资料将易混淆的会议、概念要点理顺。此时学习精力依然主要集中在客观选择题上。"})

    # ================= 阶段五：考前定盘与应试策略 (Week 36-41) =================

    add_week(36, "时政补充与维持答题手感", 
             "进入11月中下旬，各类政治时政总结和模拟卷逐渐面世。\n" + tips[36],
             {"title": "复看错题本与固化作文", "hours": "手感维持", "content": "✅ 安排：把前期积累的真题实词错题本拿出来快速重温。确保作文能够流畅书写不同情境的词汇。不建议在此阶段大量涉猎未知的机构自编模拟卷。"},
             {"title": "关注时政内容与考前名师预测卷", "hours": "选择题拓展", "content": "✅ 安排：在名师考前模拟卷（如肖八等）出版后，主要使用它们进行**客观选择题**练习。不必过于关注得分，重点在于查漏补缺和扩宽视野以应对陌生考点。"})

    for i in range(37, 39):
        msg = tips[i]
        add_week(i, f"知识体系收尾与稳固 (第{i}周)", 
                 "临近备考尾声，无需盲目开拓新内容，应当复盘并守住已掌握的知识点。\n" + msg,
                 {"title": "英语词汇和模板常态化保温", "hours": "手感维持", "content": "✅ 任务：减少长难句拆分的时间耗费，每天保证翻阅熟悉常错生词，并适时默写一次作文片段。预留最新的两套英语一真题到考前两周再限时模拟一次。"},
                 {"title": "客观题高频错题归类", "hours": "重点复盘", "content": "✅ 任务：将在练习（如苍盾小程序或者名师预测卷）中频繁出错的高频易混淆考点，集中手写整理在A4纸上，作为考前带进考场最后浏览的简要资料。"})

    add_week(39, "重点主观题资料背诵", 
             "12月份，将会迎来政治复习的核心资料出版期。\n" + tips[38],
             {"title": "最后的临考全真模拟", "hours": "考前测试", "content": "✅ 安排：选取之前预留的最新年份的真题，在安静的环境下按照考试真实时间严格闭卷模拟。\n做完核对答案了解整体水平即可，不必为了个别错题产生过度焦虑。"},
             {"title": "集中记忆核心考前主观题资料", "hours": "冲刺背诵", "content": "✅ 任务一：《肖四》等考前重点背诵资料到手后，集中主要精力背诵其列出的主观大题骨架及要点。\n✅ 任务二：可在视频平台上了解关于“考场主观题如何结合材料分析作答”的应试实战方法。如果遇到未充分准备的考点，能运用该法结合材料和学科原理有条理地解答十分关键。"})

    add_week(40, "考前调整与心态建设", 
             "备考的最后阶段，平稳积极的心态是核心环节。\n" + tips[39],
             {"title": "温习英语作文模板与格式", "hours": "常态复看", "content": "最后几天就不需强制背记新的生僻词。可每天抽出时间在与考场相似的格子答题纸上规范书写一遍作文模板，保持字迹工整清晰，寻找手感。"},
             {"title": "梳理背过的术语及考具准备", "hours": "状态保持", "content": "总体回顾重点资料中的加粗专业术语，关注流畅的语句表述即可。提前确认并整理好考场所需的准考证及各类文具。"})

    add_week(41, "正式考试周", 
             "请带着平和自信的心态参加考试，顺利完成考试整个流程。\n" + tips[40],
             {"title": "英语科目：合理安排时间保全大局", "hours": "考场策略", "content": "上考场后建议优先完成自己预定好易得分模块（如作文等）。遇到少数理解有难度的文章时不必过度纠结或慌张，应优先将有把握的题目做对。"},
             {"title": "政治科目：利用材料有理有据分点作答", "hours": "考场策略", "content": "答政治主观题时需要仔细阅读材料。在作答区应当将记忆过的学科知识和材料信息有效结合。保持字迹清晰，严禁大量不分段书写，作答点前后要注意加上明确序号以显条理清晰。"})

    data = {"student": "宋偲偲", "weeks": weeks[:41]}
    
    # Generate HTML matching the Li Baibai dark theme layout perfectly, without Hexo frontmatter.
    html_template = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>宋偲偲 2027考研深度定制规划</title>
    <style>
        :root {
            --bg-color: #0a0a0f;
            --card-bg: #12121a;
            --text-color: #e0e0e0;
            --accent: #d946ef;
            --accent-light: #f472b6;
            --border-color: #2a2a3a;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Inter', 'Noto Sans SC', sans-serif;
            background: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
            min-height: 100vh;
        }
        .container { max-width: 900px; margin: 0 auto; padding: 20px; }
        header {
            text-align: center;
            padding: 40px 20px;
            background: linear-gradient(135deg, #1a1a2e 0%, #311b3d 100%);
            border-radius: 16px;
            margin-bottom: 30px;
            border: 1px solid var(--border-color);
        }
        header h1 {
            font-size: 2.2rem;
            background: linear-gradient(90deg, var(--accent), var(--accent-light));
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 15px;
        }
        .meta { color: #888; font-size: 0.95rem; }
        .meta span { margin: 0 10px; display: inline-block; }
        .overview {
            background: linear-gradient(135deg, #1a1a2e 0%, #311b3d 100%);
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 30px;
            border: 1px solid var(--border-color);
        }
        .overview h2 {
            color: var(--accent-light);
            margin-bottom: 20px;
            font-size: 1.3rem;
            border-left: 4px solid var(--accent);
            padding-left: 10px;
        }
        .strategy {
            margin-bottom: 16px; 
            padding: 12px; 
            background: rgba(217, 70, 239, 0.15); 
            border-radius: 8px; 
            border-left: 3px solid var(--accent);
            color: #fff; 
            line-height: 1.8;
            font-size: 1.05rem;
        }
        .grid-box { display: grid; gap: 16px; margin-bottom: 20px; }
        .grid-item { padding: 18px; border-radius: 8px; }
        .grid-english { background: rgba(52,211,153,0.08); border-left: 3px solid #34d399; }
        .grid-politics { background: rgba(251,191,36,0.08); border-left: 3px solid #fbbf24; }
        
        h3 { margin-bottom: 12px; font-size: 1.1rem; }
        .grid-english h3 { color: #34d399; }
        .grid-politics h3 { color: #fbbf24; }
        
        ul { margin-left: 20px; color: #ddd; }
        li { margin-bottom: 8px; }
        
        .week-card {
            background: var(--card-bg);
            border-radius: 12px;
            margin-bottom: 20px;
            border: 1px solid var(--border-color);
            overflow: hidden;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .week-card:hover { transform: translateY(-2px); box-shadow: 0 8px 30px rgba(217, 70, 239, 0.15); }
        .week-header {
            background: linear-gradient(90deg, rgba(217, 70, 239, 0.2), rgba(217, 70, 239, 0.05));
            padding: 16px 20px; display: flex; justify-content: space-between; align-items: center; cursor: pointer;
        }
        .week-header h3 { font-size: 1.1rem; color: var(--accent-light); margin: 0; }
        .week-header .dates { color: #aaa; font-size: 0.9rem; font-family: monospace; }
        .week-content { padding: 20px; display: none; }
        .week-content.active { display: block; }
        .message {
            background: rgba(217, 70, 239, 0.1); padding: 14px 18px; border-radius: 8px;
            margin-bottom: 20px; border-left: 3px solid var(--accent); font-style: italic; color: #fff;
            line-height: 1.6; font-size: 0.95rem;
        }
        .subject { background: rgba(255, 255, 255, 0.03); border-radius: 8px; padding: 16px; margin-bottom: 16px; border: 1px solid rgba(255,255,255,0.05); }
        .subject-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 8px; }
        .subject-name { font-weight: bold; font-size: 1.05rem; }
        .subject-name.english { color: #34d399; }
        .subject-name.politics { color: #fbbf24; }
        .subject-name.mindset { color: #8b5cf6; }
        .hours { background: rgba(255, 255, 255, 0.1); padding: 4px 12px; border-radius: 12px; font-size: 0.85rem; color: #ddd; }
        .subject-title { font-weight: bold; margin-bottom: 8px; color: #fff; }
        .subject-content { color: #bbb; white-space: pre-line; font-size: 0.95rem; line-height: 1.7; }
        .expand-all { text-align: center; margin-bottom: 25px; }
        .expand-all button {
            background: var(--accent); color: white; border: none; padding: 12px 28px;
            border-radius: 8px; cursor: pointer; font-size: 1rem; font-weight: bold; transition: background 0.2s;
        }
        .expand-all button:hover { background: var(--accent-light); }
        footer { text-align: center; padding: 30px; color: #666; font-size: 0.9rem; margin-top: 20px; border-top: 1px solid var(--border-color); }
        
        @media(max-width: 600px) { .week-header { flex-direction: column; align-items: flex-start; gap: 8px; } }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>宋偲偲 2027考研全程定制规划 (公共课版)</h1>
            <div class="meta">
                <span>🎯 目标院校：华中师范大学 (211)</span>
                <span>📅 周期：2026.03.15 起 (约41周)</span>
            </div>
            <div class="meta" style="margin-top: 8px;">
                <span>📚 必考科目：英语一 / 政治</span>
            </div>
        </header>

        <!-- 总体规划概览 -->
        <div class="overview">
            <h2>🎯 全局阶段复习要点</h2>
            
            <p class="strategy">
                <strong>多思考并保持规律的练习，将知识点落实到日常刷题中。通过定期的练习来巩固理解会比只听理论课程更有效。</strong><br><br>
                <span style="color: #ffb86c;">注：本复习计划依据常规备考进度和经验总结，侧重于复习效率和资料整合建议。</span>
            </p>
            
            <div class="grid-box">
                <div class="grid-item grid-english">
                    <h3>📖 英语一备考建议</h3>
                    <ul>
                        <li><strong style="color: #fff;">词汇解析与长难句基础：</strong>前期建议借助单词APP持续背记核心词汇。基础一般者可参考相关资料学习长难句主干划分方法，无需逐词手写精翻。</li>
                        <li><strong style="color: #fff;">阅读解题与同义替换：</strong>暑期后引入真题练习，建议跟随辅导课程培养逻辑理解和识别“同义替换”的能力，遇到生词通过语境加强记忆。</li>
                        <li><strong style="color: #fff;">作文与翻译应对：</strong>秋季逐渐介入写作，通过借鉴通用段落大纲建立自身模板；翻译题根据个人水平追求达意即可，合理分配精力避免在低分环节过度消耗。</li>
                    </ul>
                </div>
                
                <div class="grid-item grid-politics">
                    <h3>🏛️ 政治复习指导</h3>
                    <ul>
                        <li><strong style="color: #f43f5e;">按步就班，避免过早消耗：</strong>一般7月进入基础知识理解期，以了解马哲等核心概念为主，无需强求深度背诵，随后结合选择题练习初步检验。</li>
                        <li><strong style="color: #fff;">秋季选择考点高频练习：</strong>10月转入对各类政治知识点的系统练习，借助精简背诵版材料和线上题库进行日常打卡，夯实客观题得分基础。</li>
                        <li><strong style="color: #fff;">12月主观资料集中研习：</strong>考前一月需侧重应对主观题。通过系统背记权威模拟卷分析题答案及知识骨架为主，考场上能够将阅读材料与知识原理相结合也是重要应答技巧。</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="expand-all">
            <button onclick="toggleAll()">展开/收起全部计划周</button>
        </div>

        <div id="weeks-container"></div>
        
    </div>

    <script>
    const planData = ''' + json.dumps(data["weeks"], ensure_ascii=False) + ''';

    function renderWeeks() {
        const container = document.getElementById('weeks-container');
        planData.forEach((week, index) => {
            const card = document.createElement('div');
            card.className = 'week-card';

            let subjectsHtml = '';

            if (week.english) {
                subjectsHtml += `
                    <div class="subject">
                        <div class="subject-header">
                            <span class="subject-name english">📖 英语一</span>
                            <span class="hours">${week.english.hours}</span>
                        </div>
                        <div class="subject-title">${week.english.title}</div>
                        <div class="subject-content">${week.english.content.replace(/\\n/g, '<br/>')}</div>
                    </div>
                `;
            }

            if (week.politics) {
                subjectsHtml += `
                    <div class="subject">
                        <div class="subject-header">
                            <span class="subject-name politics">🏛️ 政治</span>
                            <span class="hours">${week.politics.hours}</span>
                        </div>
                        <div class="subject-title">${week.politics.title}</div>
                        <div class="subject-content">${week.politics.content.replace(/\\n/g, '<br/>')}</div>
                    </div>
                `;
            }

            card.innerHTML = `
                <div class="week-header" onclick="toggleWeek(${index})">
                    <h3>第 ${week.week} 周：${week.theme}</h3>
                    <span class="dates">${week.dates}</span>
                </div>
                <div class="week-content" id="week-${index}">
                    <div class="message">${week.message}</div>
                    ${subjectsHtml}
                </div>
            `;

            container.appendChild(card);
        });

        document.getElementById('week-0').classList.add('active');
    }

    function toggleWeek(index) {
        document.getElementById('week-' + index).classList.toggle('active');
    }

    let allExpanded = false;
    function toggleAll() {
        allExpanded = !allExpanded;
        document.querySelectorAll('.week-content').forEach(el => {
            el.classList.toggle('active', allExpanded);
        });
    }

    renderWeeks();
    </script>
</body>
</html>
'''

    with open("D:/myblog/source/kaoyan/songsisi.html", "w", encoding="utf-8") as f:
        f.write(html_template)
        
if __name__ == "__main__":
    get_full_plan_songsisi()
