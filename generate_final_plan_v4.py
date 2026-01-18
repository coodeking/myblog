
import json
import datetime

# 汪桑 2026考研全程规划 (2026.01.19 - 2026.12.20)
# V4修正：动态政治栏、具体日期区间、严格遵循用户规划

def get_full_plan_v4():
    weeks = []
    start_date = datetime.date(2026, 1, 19)
    
    def get_date_str(week_idx):
        # Calculate start/end date for the week
        # week_idx is 1-based
        s = start_date + datetime.timedelta(days=(week_idx-1)*7)
        e = s + datetime.timedelta(days=6)
        return f"{s.month}月{s.day}日 - {e.month}月{e.day}日"

    def add_week(week_num, theme, msg, math, eng, pol=None):
        dates = get_date_str(week_num)
        
        week_data = {
            "week": week_num,
            "dates": dates,
            "theme": theme,
            "message": msg,
            "math": math,
            "english": eng
        }
        
        # Politics only added if explicitly provided (Structure: Start Oct)
        if pol:
            week_data["politics"] = pol
            
        weeks.append(week_data)

    # ================= 基础阶段：高数 (Week 1-12) =================
    
    add_week(1, "高数基础：极限与连续", 
             "万事开头难。本周核心是极限计算，泰勒公式是必背的‘核武器’（解题利器），务必熟练。",
             {"title": "张宇30讲：第1-2讲", "content": "完成函数极限与数列极限。重点练习‘七种未定式’计算，区分洛必达与泰勒的使用场景。", "hours": 20},
             {"title": "死磕单词", "content": "《不背单词》APP每日100新词。前期不碰阅读，积累词汇量是第一要务。", "hours": 10})

    add_week(2, "高数基础：导数与微分", 
             "导数公式表要背熟。反三角函数求导、莱布尼茨公式容易忘，多写几遍。",
             {"title": "张宇30讲：第3-5讲", "content": "重点：导数定义（特别是凑形式）、隐函数求导、参数方程求导。", "hours": 18},
             {"title": "坚持背词", "content": "复习比新学重要。利用碎片时间刷单词，不求拼写，只求认识。", "hours": 10})

    add_week(3, "高数基础：中值定理", 
             "中值定理是难点。基础阶段掌握罗尔、拉格朗日、柯西的‘计算应用’即可，证明题先不深究。",
             {"title": "张宇30讲：第6-7讲", "content": "学会通过结论构造辅助函数。纯证明题如果太难，基础阶段可跳过。", "hours": 20},
             {"title": "单词打卡", "content": "每天早晚各30分钟，坚持就是胜利。", "hours": 8})

    add_week(4, "高数基础：不定积分", 
             "不定积分没有捷径，全靠‘凑微分’的手感。归纳常见函数的凑微分形式。",
             {"title": "张宇30讲：第8讲", "content": "熟记积分公式表。尝试做1000题里的简单不定积分，找找换元的感觉。", "hours": 20},
             {"title": "单词积累", "content": "继续积累。注意熟词僻义。", "hours": 8})

    add_week(5, "高数基础：定积分及其应用", 
             "定积分计算基于牛莱公式。应用部分几何应用（旋转体体积）是必考点。",
             {"title": "张宇30讲：第9-12讲", "content": "重点：变上限积分函数的求导！这是每年必考题，必须拿下。", "hours": 18},
             {"title": "单词积累", "content": "继续背诵。", "hours": 8})
             
    add_week(6, "高数基础：微分方程", 
             "微分方程就是‘背公式、套题型’。一阶线性、二阶常系数必须烂熟于心。",
             {"title": "张宇30讲：第13-15讲", "content": "背诵：二阶常系数非齐次方程特解的设法表格。这是死知识，背过就会。", "hours": 18},
             {"title": "单词积累", "content": "持续进行。", "hours": 8})

    add_week(7, "高数基础：多元函数微分", 
             "多元微分需理清连续、可偏导、可微的关系。计算重点是链式法则。",
             {"title": "张宇30讲：第16-17讲", "content": "练习隐函数求导和复合函数求导。注意全微分存在的充要条件。", "hours": 18},
             {"title": "单词积累", "content": "持续进行。", "hours": 8})

    add_week(8, "高数基础：二重积分", 
             "二重积分是高数计算的重头戏。交换积分次序、极坐标变换要非常熟练。",
             {"title": "张宇30讲：第18讲", "content": "利用区域对称性和函数奇偶性简化计算。完成30讲高数剩余习题。", "hours": 18},
             {"title": "单词积累", "content": "3000核心词第一轮即将结束。", "hours": 8})

    add_week(9, "高数习题：极限与连续", 
             "开始大量刷题。通过计算强化概念，检验准确率。",
             {"title": "张宇1000题：第一章", "content": "做A组基础题。不看视频，先硬做。做不出来再看B站‘千羽’讲解。", "hours": 22},
             {"title": "词汇二轮", "content": "开始二刷单词。遮住中文看英文，反应时间不超过1秒。", "hours": 8})
             
    add_week(10, "高数习题：一元微积分", 
             "导数积分计算量巨大。要在草稿纸上规范步骤，避免算错。",
             {"title": "张宇1000题：第二、三章", "content": "每天至少30题。重点练不定积分的凑微分。", "hours": 22},
             {"title": "词汇二轮", "content": "持续进行。", "hours": 8})
             
    add_week(11, "高数习题：微分方程", 
             "总结微分方程的常见陷阱，比如特解设法里x的次数。",
             {"title": "张宇1000题：第四、五章", "content": "整理错题至错题本。", "hours": 18},
             {"title": "词汇二轮", "content": "持续进行。", "hours": 8})
             
    add_week(12, "高数习题：多元微积分", 
             "二重积分一定要算对。注意积分限和正负号。",
             {"title": "张宇1000题：第六、七章", "content": "完成高数基础题。回顾前12周错题，准备进入线代。", "hours": 18},
             {"title": "词汇二轮", "content": "持续进行。", "hours": 8})

    # ================= 基础阶段：线代 (Week 13-18) =================
    
    add_week(13, "线代基础：行列式与矩阵", 
             "线代注重运算规则。行列式性质和矩阵初等变换是基本功。",
             {"title": "张宇30讲线代：第1-2讲", "content": "熟记矩阵乘法、逆矩阵、伴随矩阵公式。注意矩阵乘法不满足交换律。", "hours": 18},
             {"title": "词汇二轮", "content": "持续进行。", "hours": 8})
             
    add_week(14, "线代基础：向量与方程组", 
             "向量组线性相关是核心。线性相关对应方程组有非零解。",
             {"title": "张宇30讲线代：第3-4讲", "content": "学习极大线性无关组和基础解系求法。这是解答题的必考步骤。", "hours": 18},
             {"title": "词汇二轮", "content": "持续进行。", "hours": 8})
             
    add_week(15, "线代基础：特征值与二次型", 
             "特征值是高频考点。实对称矩阵正交对角化必须掌握。",
             {"title": "张宇30讲线代：第5-6讲", "content": "练习施密特正交化。掌握配方法化二次型。", "hours": 18},
             {"title": "词汇二轮", "content": "持续进行。", "hours": 8})
             
    add_week(16, "线代习题：全章节", 
             "通过刷题把线代知识串起来。秩、解、相关性往往是一回事。",
             {"title": "张宇1000题：线代部分", "content": "集中完成A组基础题。重点：秩的应用及方程组解的判定。", "hours": 20},
             {"title": "词汇二轮", "content": "持续进行。", "hours": 8})

    add_week(17, "基础复盘：高数错题", 
             "暂停新课，专门回顾错题。基础不牢，地动山摇。",
             {"title": "错题重做", "content": "重做1000题高数错题。重复错的知识点，回去补视频。", "hours": 16},
             {"title": "词汇二轮", "content": "本周结束二轮复习。", "hours": 6})
             
    add_week(18, "基础复盘：线代错题", 
             "梳理线代逻辑，特别是秩与方程组解的关系。",
             {"title": "错题重做", "content": "重做1000题线代错题。构建线代思维导图。", "hours": 16},
             {"title": "词汇三轮", "content": "开始第三轮。攻克‘钉子户’单词。", "hours": 6})
             
    # ================= 强化阶段：大观 + 660 (Week 19-29) =================
    
    add_week(19, "强化阶段：大观-极限导数", 
             "进入强化。澄箫宇‘大观’系列能提升解题高度。",
             {"title": "高数强化课程", "content": "看极限、导数大观。要求：暂停视频，先自己做，再看讲解。", "hours": 18},
             {"title": "词汇三轮", "content": "利用碎片时间。", "hours": 6})
             
    add_week(20, "强化阶段：大观-积分", 
             "掌握区间再现公式、华里士公式等高级技巧。",
             {"title": "高数强化课程", "content": "看积分大观。整理特殊积分技巧。", "hours": 18},
             {"title": "词汇三轮", "content": "持续进行。", "hours": 6})
             
    add_week(21, "强化阶段：大观-多元微方", 
             "强化处理复杂计算的能力。",
             {"title": "高数强化课程", "content": "看多元微分、二重积分、微分方程大观。整理典型例题。", "hours": 18},
             {"title": "词汇三轮", "content": "持续进行。", "hours": 6})
             
    add_week(22, "强化阶段：大观-线代", 
             "打通线代各章节壁垒。",
             {"title": "线代强化课程", "content": "看线性代数大观。理解行列式、矩阵、方程组、特征值的联系。", "hours": 18},
             {"title": "词汇三轮", "content": "可适当阅读外刊。", "hours": 6})
             
    add_week(23, "强化习题：660题高数(1)", 
             "660题专攻选填，概念抠得很细。2分钟没思路就跳过。",
             {"title": "660题一阶：高数1-50题", "content": "核对答案，记录知识盲点。不要死磕。", "hours": 20},
             {"title": "英语真题启动", "content": "《真题伴侣》APP。做2010年英二阅读Part A（2篇）。精读，查生词。", "hours": 10})
             
    add_week(24, "强化习题：660题高数(2)", 
             "分析错误选项为什么错，深化概念理解。",
             {"title": "660题一阶：高数51-100题", "content": "继续做高数习题。分析是概念混淆还是计算失误。", "hours": 20},
             {"title": "英语真题研读", "content": "2010年英二剩余阅读。生词整理背诵。", "hours": 10})

    add_week(25, "强化习题：660题线代", 
             "线代选择题积累‘反例矩阵’，用排除法解题。",
             {"title": "660题一阶：线代全刷", "content": "完成线代选填。总结常用反例。", "hours": 20},
             {"title": "英语真题研读", "content": "2011年英二阅读Part A。", "hours": 10})

    add_week(26, "强化复盘：错题整理", 
             "只刷不总结等于白刷。这周专门消化错题。",
             {"title": "错题消化", "content": "分类整理660错题。薄弱点回去看书。", "hours": 18},
             {"title": "英语真题研读", "content": "2012年英二阅读。复习前两年真题生词。", "hours": 10})

    add_week(27, "真题演练：高数上篇 (1)", 
             "《真题一本通》按章节刷。先做计算题。",
             {"title": "真题一本通：第1章", "content": "函数极限真题。体会命题风格。", "hours": 20},
             {"title": "英语真题研读", "content": "2013年英二阅读。关注长难句分析。", "hours": 10})

    add_week(28, "真题演练：高数上篇 (2)", 
             "导数中值定理。证明题只看真题考过的类型。",
             {"title": "真题一本通：第2-3章", "content": "证明题重点学习‘辅助函数构造’。", "hours": 20},
             {"title": "英语真题研读", "content": "2014年英二阅读。理解文章逻辑。", "hours": 10})

    add_week(29, "真题演练：高数下篇 (1)", 
             "积分真题计算量大，必须算到底。",
             {"title": "真题一本通：第4章", "content": "不定积分、定积分真题。注意周期性奇偶性应用。", "hours": 20},
             {"title": "英语真题研读", "content": "2015年英二阅读。分析干扰项。", "hours": 10})
    
    # ================= 巩固与突破 (Week 30-36) =================

    add_week(30, "真题演练：高数下篇 (2)", 
             "微方多元真题。二重积分大题是重点。",
             {"title": "真题一本通：第5-6章", "content": "总结二重积分换元法。", "hours": 20},
             {"title": "英语真题研读", "content": "2016年英二阅读。", "hours": 10})

    add_week(31, "真题演练：线代全篇", 
             "线代真题综合性强。方程组+特征值。",
             {"title": "真题一本通：线代部分", "content": "掌握‘第一问证概念，第二问算结果’套路。", "hours": 20},
             {"title": "英语真题研读", "content": "2017年英二阅读。", "hours": 10})

    add_week(32, "真题演练：查漏补缺", 
             "一本通刷完，整理‘终极错题本’。",
             {"title": "错题复盘", "content": "整理所有真题错题，作为后期核心资料。", "hours": 18},
             {"title": "英语真题研读", "content": "2018年英二阅读。", "hours": 10})

    add_week(33, "二刷：大观系列", 
             "带着真题经验回看大观，会有新体会。",
             {"title": "二刷大观：高数", "content": "倍速播放。看之前没懂的，以及‘秒杀技巧’的应用。", "hours": 18},
             {"title": "英语真题研读", "content": "2019年英二阅读。", "hours": 10})

    add_week(34, "二刷：大观系列", 
             "再理一遍线代体系。",
             {"title": "二刷大观：线代", "content": "重点复习配方法和正交变换。", "hours": 18},
             {"title": "英语真题研读", "content": "2020年英二阅读。", "hours": 10})

    add_week(35, "专题突破：弱项特训", 
             "哪里不会练哪里。",
             {"title": "弱项攻坚", "content": "从中值定理、物理应用等薄弱环节找题练。", "hours": 18},
             {"title": "英语真题研读", "content": "2021年英二阅读。", "hours": 10})

    add_week(36, "专题突破：计算特训", 
             "后期拼的就是计算准确率。",
             {"title": "计算力特训", "content": "每天半小时限时计算训练。一次算对。", "hours": 18},
             {"title": "英语作文启动", "content": "听Monkey作文课。背功能段落模板（无需全篇）。", "hours": 10})

    # ================= 政治启动 & 冲刺 (Week 37-48) =================

    add_week(37, "政治启动：马原", 
             "10月中旬，政治正式进场。用《腿姐手册》。",
             {"title": "政治基础", "content": "背马原原理（对立统一等）。苍盾小程序刷30题。", "hours": 6},
             {"title": "数学保温", "content": "每日复习错题，保持手感。", "hours": 20},
             {"title": "政治", "content": "开始复习", "hours": 6}) # For logic

    # Note: add_week handles politics specially. We call it with pol obj.
    # Re-call add_week 37 correctly
    weeks.pop() # Remove the dummy call above
    add_week(37, "政治启动：马原", 
             "10月中旬，政治正式进场。用《腿姐手册》。",
             {"title": "数学保温", "content": "复习错题。", "hours": 20},
             {"title": "英语真题", "content": "2022年阅读。", "hours": 8},
             {"title": "政治基础", "content": "背马原原理。苍盾刷30题。", "hours": 6})

    add_week(38, "政治推进：史纲/毛中特", 
             "梳理史纲时间轴，关注毛中特新大纲。",
             {"title": "数学备战", "content": "整理09-26真题卷，准备模拟。", "hours": 20},
             {"title": "英语作文", "content": "2023年阅读。每周套模板写一篇。", "hours": 6},
             {"title": "政治背诵", "content": "熟读史纲毛中特。刷对应章节选择题。", "hours": 6})

    add_week(39, "冲刺实战：真题套卷(1)", 
             "每天一套数学真题，严格限时3小时（8:30-11:30）。",
             {"title": "数二真题 09-14", "content": "模拟考场。做完立即批改，分析失分。", "hours": 22},
             {"title": "英语/政治", "content": "英语练手写。政治刷选择题。", "hours": 8},
             {"title": "政治刷题", "content": "利用碎片时间刷苍盾。", "hours": 0}) # Merged into Eng for display logic usually but here separate

    add_week(40, "冲刺实战：真题套卷(2)", 
             "中期真题参考价值高。控制选填时间。",
             {"title": "数二真题 15-20", "content": "分析错题原因。建立考试心态。", "hours": 22},
             {"title": "英语/政治", "content": "英语2024阅读。政治读澄箫宇‘一页纸’。", "hours": 8},
             {"title": "政治诵读", "content": "澄箫宇‘一页纸’核心考点。", "hours": 0})

    add_week(41, "冲刺实战：真题套卷(3)", 
             "近年真题难度大。保持平和，查漏补缺。",
             {"title": "数二真题 21-23", "content": "24-26留作最后模考。本周做21-23。", "hours": 22},
             {"title": "英语/政治", "content": "英语2025阅读。政治腿姐手册回顾。", "hours": 8},
             {"title": "政治巩固", "content": "腿姐手册多轮复习。", "hours": 0})

    add_week(42, "模拟冲刺：李林六套卷(1)", 
             "李林卷计算量大。重在见识新题型。",
             {"title": "李林六套卷 1-3", "content": "认真看解析，掌握补充考点。", "hours": 22},
             {"title": "英语背诵", "content": "背大作文小作文万能模板各一套。", "hours": 8},
             {"title": "政治", "content": "继续刷题。", "hours": 0})

    add_week(43, "模拟冲刺：李林六套卷(2)", 
             "保持高强度，克服疲劳。",
             {"title": "李林六套卷 4-6", "content": "总结新题型切入点。", "hours": 22},
             {"title": "政治重点", "content": "肖八出版！死磕选择题！搞懂每个选项。", "hours": 8})

    add_week(44, "模拟冲刺：李林四套卷", 
             "五星推荐。全真模拟。",
             {"title": "李林四套卷", "content": "完全按考试时间模拟。最后查漏补缺。", "hours": 22},
             {"title": "政治刷题", "content": "二刷肖八选择题。刷名师押题卷选择题。", "hours": 8},
             {"title": "政治", "content": "刷名师押题卷。", "hours": 0})

    add_week(45, "技巧回归：选填特训", 
             "最后阶段，得选填者得天下。看武忠祥技巧课。",
             {"title": "选填技巧", "content": "学习赋值法、排除法。保证准确率。", "hours": 18},
             {"title": "政治押题", "content": "肖四出版！背前两套大题！", "hours": 12})
             
    add_week(46, "回归复盘：错题温习", 
             "停做新题（除模考）。回顾错题本。",
             {"title": "终极复盘", "content": "浏览错题思路，确保不犯旧错。", "hours": 18},
             {"title": "政治背诵", "content": "背肖四。学B站‘抄材料’技巧。", "hours": 12})

    add_week(47, "考前演练：全真模拟", 
             "调整作息。上午数学，下午英语。",
             {"title": "24/25年真题模考", "content": "全真模拟，评分增强信心。", "hours": 18},
             {"title": "考前突击", "content": "狂背肖四。默写英语模板。", "hours": 12})

    add_week(48, "考试周：心态调整", 
             "放松，保证睡眠。准备文具。",
             {"title": "回归基础", "content": "看目录公式。不做难题。", "hours": 10},
             {"title": "必胜", "content": "确认准考证。相信自己，金榜题名！", "hours": 5},
             {"title": "政治", "content": "最后看一眼肖四。", "hours": 0})

    return weeks

def generate_custom_word_doc(plan):
    html = """
    <html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word' xmlns='http://www.w3.org/TR/REC-html40'>
    <head>
        <meta charset="utf-8">
        <title>汪桑 2026考研全程定制规划 (终极版)</title>
        <style>
            body { font-family: 'SimSun', 'Microsoft YaHei', sans-serif; }
            h1 { text-align: center; color: #000; margin-bottom: 20px;}
            .info { text-align: center; color: #444; margin-bottom: 30px; border-bottom: 2px solid #000; padding-bottom: 10px;}
            .week-block { border: 1px solid #999; padding: 10px; margin-bottom: 15px; page-break-inside: avoid; }
            .week-header { background: #eee; padding: 5px 10px; font-weight: bold; border-bottom: 1px solid #999; display: flex; justify-content: space-between; }
            .msg { padding: 8px 10px; font-style: italic; color: #333; }
            table { width: 100%; border-collapse: collapse; margin-top: 5px;}
            td { padding: 6px; border: 1px solid #ccc; vertical-align: top; font-size: 10.5pt; }
            .sub-name { width: 15%; font-weight: bold; background-color: #f9f9f9;}
            .sub-hours { width: 10%; text-align: center; white-space: nowrap; }
        </style>
    </head>
    <body>
        <h1>汪桑 2026考研全程定制规划</h1>
        <div class="info">
            <p><strong>目标院校：</strong>中山大学 (085700) &nbsp;|&nbsp; <strong>规划周期：</strong>48周 (2026.01.19 - 2026.12.20)</p>
            <p><strong>备考策略：</strong>数学核心(60%) / 英语积累(30%) / 政治冲刺(10%)</p>
        </div>
    """
    
    for week in plan:
        html += f"""
        <div class="week-block">
            <div class="week-header">
                <span>第 {week['week']} 周：{week['theme']}</span>
                <span style="font-weight:normal; font-size: 0.9em;">{week['dates']}</span>
            </div>
            <div class="msg">指导：{week['message']}</div>
            <table>
                <tr>
                    <td class="sub-name">数 学</td>
                    <td>
                        <strong>{week['math']['title']}</strong><br/>
                        {week['math']['content']}
                    </td>
                    <td class="sub-hours">{week['math']['hours']}h</td>
                </tr>
                <tr>
                    <td class="sub-name">英 语</td>
                    <td>
                        <strong>{week['english'].get('title', '')}</strong><br/>
                        {week['english']['content']}
                    </td>
                    <td class="sub-hours">{week['english'].get('hours', '')}h</td>
                </tr>
        """
        # Conditional Politics Render
        if 'politics' in week:
             html += f"""
                <tr>
                    <td class="sub-name">政 治</td>
                    <td>
                        <strong>{week['politics'].get('title', '')}</strong><br/>
                        {week['politics']['content']}
                    </td>
                    <td class="sub-hours">{week['politics'].get('hours', '')}h</td>
                </tr>
            """
        html += "</table></div>"
        
    html += "</body></html>"
    
    with open(r'd:\myblog\source\kaoyan\wangsang_custom_v4.doc', 'w', encoding='utf-8') as f:
        f.write(html)

def generate_json(plan):
    with open(r'd:\myblog\source\kaoyan\wangsang_detail_v4.json', 'w', encoding='utf-8') as f:
        json.dump({"student": "汪桑", "weeks": plan}, f, ensure_ascii=False)

if __name__ == "__main__":
    plan = get_full_plan_v4()
    generate_custom_word_doc(plan)
    generate_json(plan)
    print("Full customized plan v4 generated.")
