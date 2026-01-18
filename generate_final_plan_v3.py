
import json
import datetime

# 汪桑 2026考研全程规划 (2026.01.19 - 2026.12.20)
# 修正重点：严肃、专业、无网络烂梗、政治全程可见

def get_full_plan():
    weeks = []
    
    def add_week(week_num, theme, msg, math, eng, pol=None):
        # Professional course logic: User said "Don't mention it" but "reserve time".
        # We will not add a specific row for it to avoid cluttering or annoying the user, 
        # but the daily schedule implies it (weekday <4h, weekend 8-10h). 
        # The prompt said "Don't say his pro course" 3 times. So I will omit the pro course row.
        
        # Default Politics Content for early weeks
        politics = pol if pol else {"title": "本阶段暂无任务", "content": "规划于10月（第37周）正式启动", "hours": 0}
        
        weeks.append({
            "week": week_num,
            "theme": theme,
            "message": msg,
            "math": math,
            "english": eng,
            "politics": politics
        })

    # ================= 基础阶段：高数 (Week 1-12) =================
    
    add_week(1, "高数基础：极限与连续", 
             "本周重点掌握极限的计算方法。泰勒公式是解决复杂极限问题的核心工具，务必熟练掌握其展开式。",
             {"title": "张宇30讲：第1-2讲", "content": "完成函数极限与数列极限的学习。重点练习‘七种未定式’的计算，区分洛必达法则与泰勒公式的适用场景。", "hours": 20},
             {"title": "基础词汇积累", "content": "使用《不背单词》APP，每日背诵新词100个。前期专注于词汇量积累，暂不进行阅读训练。", "hours": 10})

    add_week(2, "高数基础：导数与微分", 
             "导数是高数计算的基础。需重点记忆基本求导公式、反三角函数求导及莱布尼茨公式。",
             {"title": "张宇30讲：第3-5讲", "content": "学习导数定义、连续性判断及各类求导法则。隐函数求导和参数方程求导是高频考点，需多加练习。", "hours": 18},
             {"title": "基础词汇积累", "content": "坚持每日背诵。复习旧词比学习新词更重要，利用碎片时间巩固记忆。", "hours": 10})

    add_week(3, "高数基础：中值定理", 
             "中值定理是难点。基础阶段重点掌握辅助函数的构造方法，用于解决极限计算或不等式证明。",
             {"title": "张宇30讲：第6-7讲", "content": "重点学习罗尔、拉格朗日、柯西三大定理的应用。对于复杂的纯证明题，基础阶段可先做标记，不做深究。", "hours": 20},
             {"title": "基础词汇积累", "content": "保持背词习惯，每日早晚各30分钟。", "hours": 8})

    add_week(4, "高数基础：不定积分", 
             "不定积分的核心在于‘凑微分法’。建议归纳常见函数的凑微分形式，建立函数敏感度。",
             {"title": "张宇30讲：第8讲", "content": "熟记基本积分公式表。尝试完成1000题中的部分简单不定积分计算，体会换元法的应用。", "hours": 20},
             {"title": "基础词汇积累", "content": "继续积累词汇，注意熟词僻义。", "hours": 8})

    add_week(5, "高数基础：定积分及其应用", 
             "定积分计算基于牛顿-莱布尼茨公式。应用部分重点掌握几何应用（如旋转体体积）和变上限积分函数的求导。",
             {"title": "张宇30讲：第9-12讲", "content": "变上限积分求导是必考点，需熟练掌握其求导公式及与极限结合的题型。", "hours": 18},
             {"title": "基础词汇积累", "content": "继续背诵。可尝试听例句发音，辅助记忆。", "hours": 8})
             
    add_week(6, "高数基础：微分方程", 
             "微分方程复习重点在于识别方程类型并套用对应解法公式。",
             {"title": "张宇30讲：第13-15讲", "content": "熟背一阶线性、二阶常系数这一类方程的通解公式。特别注意二阶常系数非齐次方程特解的设法表格。", "hours": 18},
             {"title": "基础词汇积累", "content": "持续进行。", "hours": 8})

    add_week(7, "高数基础：多元函数微分", 
             "多元微分需理清连续、可偏导、可微之间的逻辑关系。计算上重点练习链式求导法则。",
             {"title": "张宇30讲：第16-17讲", "content": "练习隐函数求导和复合函数求导。注意全微分存在的充分必要条件。", "hours": 18},
             {"title": "基础词汇积累", "content": "持续进行。", "hours": 8})

    add_week(8, "高数基础：二重积分", 
             "二重积分计算是必考大题。重点掌握交换积分次序和极坐标变换与直角坐标的互换。",
             {"title": "张宇30讲：第18讲", "content": "学习利用区域对称性和函数奇偶性简化积分计算。完成30讲高数部分所有剩余习题。", "hours": 18},
             {"title": "基础词汇积累", "content": "完成3000核心词的第一轮背诵。", "hours": 8})

    add_week(9, "高数习题训练：极限与连续", 
             "开始集中刷题。通过大量计算强化对概念的理解，重点检验计算准确率。",
             {"title": "张宇1000题：第一章", "content": "完成A组基础题。遇到解题困难再查阅B站‘千羽’等UP主的讲解视频，避免依赖视频。", "hours": 22},
             {"title": "词汇二轮复习", "content": "开始第二轮单词背诵，重点复习遗忘率高的单词。", "hours": 8})
             
    add_week(10, "高数习题训练：一元微积分", 
             "导数与积分是计算量最大的部分。需规范答题步骤，避免计算失误。",
             {"title": "张宇1000题：第二、三章", "content": "每天保持30题以上的训练量。重点练习不定积分的凑微分技巧。", "hours": 22},
             {"title": "词汇二轮复习", "content": "持续进行。", "hours": 8})
             
    add_week(11, "高数习题训练：微分方程", 
             "通过刷题总结微分方程常见的陷阱，如特解设法中的x乘幂次数。",
             {"title": "张宇1000题：第四、五章", "content": "整理微分方程常见题型及易错点至错题本。", "hours": 18},
             {"title": "词汇二轮复习", "content": "持续进行。", "hours": 8})
             
    add_week(12, "高数习题训练：多元微积分", 
             "二重积分计算需细心。注意积分限的确定及正负号判断。",
             {"title": "张宇1000题：第六、七章", "content": "完成高数部分基础题训练。整理前12周的错题，进行阶段性复盘。", "hours": 18},
             {"title": "词汇二轮复习", "content": "持续进行。", "hours": 8})

    # ================= 基础阶段：线代 (Week 13-18) =================
    
    add_week(13, "线代基础：行列式与矩阵", 
             "线性代数重点在于运算规则。需熟练掌握行列式性质及矩阵的初等变换。",
             {"title": "张宇30讲线代：第1-2讲", "content": "掌握行列式展开法。熟记矩阵乘法、逆矩阵、伴随矩阵的相关公式及性质。", "hours": 18},
             {"title": "词汇二轮复习", "content": "遮挡中文释义进行测试，提高反应速度。", "hours": 8})
             
    add_week(14, "线代基础：向量与方程组", 
             "向量组线性相关性是线代的核心概念。需建立几何直观与代数定义的联系。",
             {"title": "张宇30讲线代：第3-4讲", "content": "学习极大线性无关组及基础解系的求法。这是解答线性方程组大题的关键步骤。", "hours": 18},
             {"title": "词汇二轮复习", "content": "持续进行。", "hours": 8})
             
    add_week(15, "线代基础：特征值与二次型", 
             "特征值与特征向量是高频考点。实对称矩阵正交对角化是标准化流程，必须掌握。",
             {"title": "张宇30讲线代：第5-6讲", "content": "练习施密特正交化方法。掌握用配方法化二次型为标准型。", "hours": 18},
             {"title": "词汇二轮复习", "content": "持续进行。", "hours": 8})
             
    add_week(16, "线代习题训练：全章节", 
             "线代知识点前后关联紧密，通过刷题将孤立的知识点串联成网。",
             {"title": "张宇1000题：线代部分", "content": "集中完成A组基础题。重点关注秩的应用及方程组解的判定。", "hours": 20},
             {"title": "词汇二轮复习", "content": "持续进行。", "hours": 8})

    add_week(17, "基础阶段复盘：高数错题", 
             "暂停新知识学习，专门回顾基础阶段错题，夯实基础。",
             {"title": "错题重做", "content": "重做1000题中的高数错题。对于重复错误的知识点，查阅教材或视频进行补漏。", "hours": 16},
             {"title": "词汇二轮复习", "content": "本周结束第二轮复习。", "hours": 6})
             
    add_week(18, "基础阶段复盘：线代错题", 
             "梳理线代逻辑体系，特别是秩、方程组解与向量相关性之间的关系。",
             {"title": "错题重做", "content": "重做1000题中的线代错题。尝试构建线代知识思维导图。", "hours": 16},
             {"title": "词汇三轮复习", "content": "开始第三轮复习，重点攻克‘钉子户’词汇。", "hours": 6})
             
    # ================= 强化阶段：大观 + 660 (Week 19-29) =================
    
    add_week(19, "强化阶段：大观-极限与导数", 
             "进入强化阶段，重点提升解题技巧和综合分析能力。观看澄箫宇‘大观’系列。",
             {"title": "高数强化课程", "content": "观看极限、导数大观视频。要求：每道例题先独立思考2分钟，尝试解答后再看讲解。", "hours": 18},
             {"title": "词汇三轮复习", "content": "利用碎片时间维持记忆。", "hours": 6})
             
    add_week(20, "强化阶段：大观-积分", 
             "掌握积分的高级计算技巧，如区间再现公式、华里士公式等。",
             {"title": "高数强化课程", "content": "观看积分大观视频。整理视频中的特殊积分技巧和典型例题。", "hours": 18},
             {"title": "词汇三轮复习", "content": "持续进行。", "hours": 6})
             
    add_week(21, "强化阶段：大观-多元与微方", 
             "强化多元函数微分及二重积分的计算能力，学习处理复杂计算。",
             {"title": "高数强化课程", "content": "观看多元微分、二重积分及微分方程大观。重点整理计算题的解题套路。", "hours": 18},
             {"title": "词汇三轮复习", "content": "持续进行。", "hours": 6})
             
    add_week(22, "强化阶段：大观-线代", 
             "从宏观角度统摄线代知识，打通各章节壁垒。",
             {"title": "线代强化课程", "content": "观看线性代数大观。重点理解行列式、矩阵、方程组与特征值之间的内在联系。", "hours": 18},
             {"title": "词汇三轮复习", "content": "持续进行。本周起可适当阅读英语外刊。", "hours": 6})
             
    add_week(23, "强化习题：660题高数(1)", 
             "开始做《660题》。该阶段专注于选择填空题，考察对概念的精准理解。",
             {"title": "660题一阶：高数1-50题", "content": "严格控制做题时间。2分钟无思路直接跳过，核对答案后记录知识盲点。", "hours": 20},
             {"title": "英语真题启动", "content": "使用《真题伴侣》APP。做2010年英二阅读Part A（2篇）。精读文章，查漏生词。", "hours": 10})
             
    add_week(24, "强化习题：660题高数(2)", 
             "通过题目解析分析错误选项的设置原因，深化对概念的理解。",
             {"title": "660题一阶：高数51-100题", "content": "继续完成高数剩余习题。重点分析错误原因：概念混淆、计算失误还是审题不清。", "hours": 20},
             {"title": "英语真题研读", "content": "做2010年英二剩余阅读。将生词整理至生词本，反复背诵。", "hours": 10})

    add_week(25, "强化习题：660题线代", 
             "线代选择题常使用特值法或举反例法。需积累常见的反例矩阵。",
             {"title": "660题一阶：线代全刷", "content": "完成线代部分选择填空。注意总结常用反例，用于排除错误选项。", "hours": 20},
             {"title": "英语真题研读", "content": "2011年英二阅读Part A。只做阅读，不涉及其他题型。", "hours": 10})

    add_week(26, "强化复盘：错题整理", 
             "回顾660题错题，总结常考概念陷阱。",
             {"title": "错题消化", "content": "分类整理660题错题。针对薄弱环节再次查阅相关知识点。", "hours": 18},
             {"title": "英语真题研读", "content": "2012年英二阅读。复习前两年的真题生词。", "hours": 10})

    add_week(27, "真题演练：高数上篇 (1)", 
             "进入真题阶段。使用《真题一本通》，按章节进行训练。",
             {"title": "真题一本通：第1章", "content": "完成函数极限相关真题。体会真题的命题风格和难度。", "hours": 20},
             {"title": "英语真题研读", "content": "2013年英二阅读。开始关注长难句的句法结构分析。", "hours": 10})

    add_week(28, "真题演练：高数上篇 (2)", 
             "针对导数与中值定理真题。仅做计算与应用题，证明题仅限于真题出现过的类型。",
             {"title": "真题一本通：第2-3章", "content": "对于证明题，重点学习‘辅助函数构造’的逻辑。", "hours": 20},
             {"title": "英语真题研读", "content": "2014年英二阅读。注重理解文章主旨和段落逻辑。", "hours": 10})

    add_week(29, "真题演练：高数下篇 (1)", 
             "积分真题训练。计算量大，需耐心算到底，避免眼高手低。",
             {"title": "真题一本通：第4章", "content": "完成不定积分与定积分计算真题。注意周期性、奇偶性在定积分中的应用。", "hours": 20},
             {"title": "英语真题研读", "content": "2015年英二阅读。分析干扰项特征：偷换概念、无中生有等。", "hours": 10})
    
    # ================= 巩固与突破 (Week 30-36) =================

    add_week(30, "真题演练：高数下篇 (2)", 
             "微方与多元积分真题。重点攻克二重积分大题。",
             {"title": "真题一本通：第5-6章", "content": "总结二重积分的换元方法及计算步骤。", "hours": 20},
             {"title": "英语真题研读", "content": "2016年英二阅读。", "hours": 10})

    add_week(31, "真题演练：线代全篇", 
             "线代真题综合性强。重点练习方程组与特征值的综合大题。",
             {"title": "真题一本通：线代部分", "content": "掌握‘第一问证概念，第二问算结果’的常见题型结构。", "hours": 20},
             {"title": "英语真题研读", "content": "2017年英二阅读。", "hours": 10})

    add_week(32, "真题演练：查漏补缺", 
             "完成真题一本通后，整理所有真题错题。",
             {"title": "错题复盘", "content": "将真题错题整理至‘终极错题本’，按考点分类，作为后期复习核心资料。", "hours": 18},
             {"title": "英语真题研读", "content": "2018年英二阅读。", "hours": 10})

    add_week(33, "二刷：大观系列", 
             "结合真题经验再次观看大观视频，深化理解。",
             {"title": "二刷大观：高数", "content": "倍速播放。重点关注之前未理解的难点及讲师提到的‘秒杀技巧’。", "hours": 18},
             {"title": "英语真题研读", "content": "2019年英二阅读。", "hours": 10})

    add_week(34, "二刷：大观系列", 
             "再次梳理线代知识体系，确保逻辑链条清晰。",
             {"title": "二刷大观：线代", "content": "重点复习二次型化标准型的配方法和正交变换法。", "hours": 18},
             {"title": "英语真题研读", "content": "2020年英二阅读。", "hours": 10})

    add_week(35, "专题突破：弱项特训", 
             "针对个人薄弱章节（如中值定理或物理应用）进行集中强化。",
             {"title": "弱项攻坚", "content": "从1000题或一本通中挑选薄弱章节习题，进行针对性训练。", "hours": 18},
             {"title": "英语真题研读", "content": "2021年英二阅读。", "hours": 10})

    add_week(36, "专题突破：计算特训", 
             "提升计算速度与准确率。后期计算能力决定得分上限。",
             {"title": "计算力特训", "content": "每日抽取步骤繁琐的计算题进行限时训练，要求一次算对。", "hours": 18},
             {"title": "英语作文启动", "content": "开始听Monkey作文课。重点背诵其功能段落模板，无需全篇背诵。", "hours": 10})

    # ================= 政治启动 & 冲刺 (Week 37-48) =================

    add_week(37, "政治启动：马原", 
             "10月中旬，政治复习开始。使用《腿姐冲刺背诵手册》。",
             {"title": "政治基础", "content": "背诵马原原理（对立统一、质量互变等）。每日刷苍盾小程序选择题30道。", "hours": 6},
             {"title": "数学保温", "content": "每日复习错题，保持手感。", "hours": 20})

    add_week(38, "政治推进：史纲/毛中特", 
             "重点梳理史纲时间轴及毛中特新大纲内容。",
             {"title": "政治背诵与刷题", "content": "熟读手册中史纲与毛中特部分。苍盾小程序刷对应章节选择题。", "hours": 6},
             {"title": "数学套卷准备", "content": "整理09-26年真题试卷，准备下周开始实战训练。", "hours": 20},
             {"title": "英语作文", "content": "做2023年阅读。每周套用模板练习写作一篇。", "hours": 6})

    add_week(39, "冲刺实战：真题套卷(1)", 
             "每日一套数学真题，严格限时3小时（建议8:30-11:30）。",
             {"title": "数二真题 09-14", "content": "模拟考场环境。做完立即批改，分析失分原因。适应高强度考试节奏。", "hours": 22},
             {"title": "英语/政治", "content": "英语练习作文手写。政治利用碎片时间刷选择题。", "hours": 8})

    add_week(40, "冲刺实战：真题套卷(2)", 
             "中期真题参考价值较高。注意控制选填题用时。",
             {"title": "数二真题 15-20", "content": "重点分析错题原因：是知识盲区还是考试心态问题。", "hours": 22},
             {"title": "英语/政治", "content": "英语做2024年阅读。政治熟读澄箫宇‘政治一页纸’，掌握核心关键词。", "hours": 8})

    add_week(41, "冲刺实战：真题套卷(3)", 
             "近年真题难度较大。保持平和心态，重在查漏补缺。",
             {"title": "数二真题 21-23", "content": "近三年真题（24-26）留作最后模考。本周完成21-23年试卷。", "hours": 22},
             {"title": "英语/政治", "content": "英语做2025年阅读。政治腿姐手册多轮回顾，确保选择题正确率。", "hours": 8})

    add_week(42, "模拟冲刺：李林六套卷(1)", 
             "李林试卷预测性强但计算量大。重在见识新题型。",
             {"title": "李林六套卷 1-3", "content": "认真研读解析，掌握解析中补充的生僻考点。", "hours": 22},
             {"title": "英语背诵", "content": "熟背大作文与小作文万能模板各一套。", "hours": 8})

    add_week(43, "模拟冲刺：李林六套卷(2)", 
             "继续保持高强度训练，克服疲劳期。",
             {"title": "李林六套卷 4-6", "content": "总结六套卷中的常考新题型及解题切入点。", "hours": 22},
             {"title": "政治背诵", "content": "肖八出版，重点研究选择题。每一个选项都要搞懂为何对错。", "hours": 8})

    add_week(44, "模拟冲刺：李林四套卷", 
             "四套卷质量极高，需全真模拟。",
             {"title": "李林四套卷", "content": "完全按考试时间进行模拟。这是考前最后一次查漏补缺的机会。", "hours": 22},
             {"title": "政治刷题", "content": "二刷肖八选择题。在小程序上尽可能多刷名师押题卷的选择题。", "hours": 8})

    add_week(45, "技巧回归：选填特训", 
             "最后阶段专注于选填题正确率。观看武忠祥选填技巧课。",
             {"title": "选填技巧", "content": "学习赋值法、排除法、几何法等技巧。力求在选填题上节省时间且保证准确。", "hours": 18},
             {"title": "政治押题", "content": "肖四出版。重点背诵前两套的大题，熟读后两套。", "hours": 12})
             
    add_week(46, "回归复盘：错题温习", 
             "停止做新题（除模考外），全面回顾错题本。",
             {"title": "终极复盘", "content": "浏览所有错题，脑补解题思路，无需动笔细算。确保不再犯同样的错误。", "hours": 18},
             {"title": "政治技巧", "content": "继续背诵肖四。学习B站‘抄材料’技巧，掌握答题格式和套话。", "hours": 12})

    add_week(47, "考前演练：全真模拟", 
             "调整生物钟，适应上午考数学、下午考英语的节奏。",
             {"title": "24/25年真题模考", "content": "使用留存的真题进行全真模拟。做完进行评分，增强信心。", "hours": 18},
             {"title": "考前突击", "content": "狂背肖四。默写英语作文模板，确保字迹工整。", "hours": 12})

    add_week(48, "考试周：心态调整", 
             "放松心态，保证睡眠。准备考试用品。",
             {"title": "回归基础", "content": "翻看教材目录和基本公式表。不做难题，维持题感即可。", "hours": 10},
             {"title": "必胜信念", "content": "确认准考证、文具。相信自己48周的努力，祝金榜题名！", "hours": 5})

    return weeks

def generate_custom_word_doc(plan):
    html = """
    <html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word' xmlns='http://www.w3.org/TR/REC-html40'>
    <head>
        <meta charset="utf-8">
        <title>汪桑 2026考研全程定制规划 (终极修正版)</title>
        <style>
            body { font-family: 'SimSun', 'Microsoft YaHei', sans-serif; }
            h1 { text-align: center; color: #000; margin-bottom: 20px;}
            .info { text-align: center; color: #444; margin-bottom: 30px; border-bottom: 2px solid #000; padding-bottom: 10px;}
            .week-block { border: 1px solid #999; padding: 10px; margin-bottom: 15px; page-break-inside: avoid; }
            .week-header { background: #eee; padding: 5px 10px; font-weight: bold; border-bottom: 1px solid #999; }
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
            <p><strong>核心策略：</strong>数学优先 (60%) / 英语积累 (30%) / 政治突击 (10%) / 严控执行</p>
        </div>
    """
    
    for week in plan:
        html += f"""
        <div class="week-block">
            <div class="week-header">第 {week['week']} 周：{week['theme']}</div>
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
                <tr>
                    <td class="sub-name">政 治</td>
                    <td>
                        <strong>{week['politics'].get('title', '')}</strong><br/>
                        {week['politics']['content']}
                    </td>
                    <td class="sub-hours">{week['politics'].get('hours', '')}h</td>
                </tr>
            </table>
        </div>
        """
        
    html += "</body></html>"
    
    with open(r'd:\myblog\source\kaoyan\wangsang_custom_v3.doc', 'w', encoding='utf-8') as f:
        f.write(html)

def generate_json(plan):
    with open(r'd:\myblog\source\kaoyan\wangsang_detail_v3.json', 'w', encoding='utf-8') as f:
        json.dump({"student": "汪桑", "weeks": plan}, f, ensure_ascii=False)

if __name__ == "__main__":
    plan = get_full_plan()
    generate_custom_word_doc(plan)
    generate_json(plan)
    print("Full customized plan v3 generated.")
