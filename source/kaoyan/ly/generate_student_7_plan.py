# -*- coding: utf-8 -*-
import json
from datetime import datetime, timedelta

def get_full_plan_student_7():
    weeks = []
    # 起始日期 2026年3月6日
    start_date = datetime(2026, 3, 6)
    
    def get_date_str(week_idx):
        s = start_date + timedelta(days=(week_idx-1)*7)
        e = s + timedelta(days=6)
        return f"{s.strftime('%m.%d')} - {e.strftime('%m.%d')}"

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
        if pol:
            week_data["politics"] = pol
        weeks.append(week_data)

    # 41个真实的经验补充（针对数学一、英语一的工科生。语气干练平实，去除了冗余修饰）
    tips = [
        "（复习建议：数学一内容较数学二多出近三分之一，包括空间解析几何、无穷级数和概率论。基础阶段需保持进度连贯，避免前松后紧。）",
        "（复习建议：张宇三十讲的课后题和1000题基础篇是本阶段核心。如果卡壳，直接使用B站（如千羽、777等）的解析视频定位知识盲区，这比重新听冗长课程效率高。）",
        "（复习建议：做题时若毫无头绪，思考两分钟后直接看答案。理解解题核心步骤后，在草稿纸上独立复现一遍。）",
        "（复习建议：数学一的三重积分和曲线曲面积分（三大公式）是重中之重。基础阶段需将基本概念和计算规则理清，后期再集中攻克综合应用。）",
        "（复习建议：微分方程的解法规律性很强。建议将常系数线性非齐次微分方程的特解表格完全背诵下来，作为常备解题工具。）",
        "（复习建议：线性代数中，初等行变换是解决矩阵求秩、求逆和方程组求解的核心工具。熟练掌握这一基本运算至关重要。）",
        "（复习建议：向量组的线性相关性定义抽象。理解概念本身比机械记忆更重要，可以通过具体的矩阵例子辅助理解其秩的关系。）",
        "（复习建议：实对称矩阵的对角化是线代考题的高频命门，计算步骤往往多达一层纸。平时刻意训练计算正确率。）",
        "（复习建议：定期回顾错题能有效巩固知识。停下来将前几周标记的错题重新计算，有助于打通知识点之间的关联。）",
        "（复习建议：概率论与数理统计在数学一中占分可观，且题型相对固定。重点掌握各分布函数的性质和参数估计的计算流程。）",
        "（复习建议：无穷级数是难点，尤其是幂级数的展开与求和。基础阶段掌握收敛域的求法和常见函数的展开式即可，不深究冷门题。）",
        "（复习建议：在观看B站“澄箫宇”大观系列时，务必先暂停视频独立思考或尝试解答，然后再听讲解。这可以检验自己对知识点的实际掌控能力。）",
        "（复习建议：大观系列涵盖了大量习题讲解和基础知识整合。建议按照每两天一个视频的节奏推进，做好配套的笔记整理。）",
        "（复习建议：660题的选择填空考察非常细致，遇到连错现象很正常。重点在于通过对答案的解析，修补概念理解上的微小盲区。）",
        "（复习建议：660题的速刷原则：会做的迅速拿下，两分钟没思路的跳过去看答案并订正。这有助于快速遍历整个知识面的缺陷。）",
        "（复习建议：整理660题的错题时，不需要一字不漏抄写原题。将其对应的知识点或易错概念记录下来即可，方便后续查阅。）",
        "（复习建议：于文涛的《真题一本通》是数学复习最重要的资料。务必准备一个单独的按章节分类的错题本，详细记录每道错题的病因。）",
        "（复习建议：历年真题是把握命题方向的唯一标准。把练习册和模拟卷的证明题直接跳过，只专注于认真对待真题中的证明题。）",
        "（复习建议：真题训练时，计算能力的要求会显著提高。遇到复杂的计算题，务必在草稿纸上一步步算到底，切勿眼高手低。）",
        "（复习建议：线代真题通常综合了多章考点，比如将特征值与二次型结合考察。做题时要注意培养跨章节的统筹联想能力。）",
        "（复习建议：一本通第一轮完成后，你的专属错题本将成为后续复习的弹药库。定期对错题本进行筛选，划掉已经完全掌握的题目。）",
        "（复习建议：概率论真题的考查往往较为模式化。掌握二维随机变量及其分布、矩估计和最大似然估计的计算套路即可稳拿此部分分数。）",
        "（复习建议：二刷“澄箫宇”大观系列时，因为你已经做过真题，会发现看视频的视角完全变了，更容易理解他总结的高阶技巧。）",
        "（复习建议：开始成套刷真题（如09-26年套卷）时，严格遵守3小时的考试时间限制。训练自己在高压环境下的时间分配能力。）",
        "（复习建议：套卷的成绩会跟随试卷年份的难度大幅波动，不必因单次分数低而受挫。认真分析错因，查漏补缺才是关键。）",
        "（复习建议：完成套卷后，将错题归类到总结本对应的题型模块中去。这能帮助你清晰地看到自己是计算失误还是知识漏洞。）",
        "（复习建议：李林6套卷等模拟卷的难度通常略高于真题。做此类模拟卷的意义在于见识新颖的出题角度，锻炼考场上的应变能力。）",
        "（复习建议：模拟卷（如李林6+4）同样不看证明题。重点吸收解析中提供的选择填空解题优化思路和多元计算技巧。）",
        "（复习建议：武忠祥的选填技巧课能有效提高小题的解题速度。熟练运用特值法、图形法等技巧，为最后的大题争取宝贵的书写时间。）",
        "（复习建议：对于政治，10月初才是开始复习的正常时间节点。严禁花费大量时间观看冗长的基础课程，直接使用腿姐冲刺手册与刷题。）",
        "（复习建议：政治选择题建议使用《苍盾小程序》进行每日一测，利用通勤等碎片时间完成即可。坚决摒弃传统的题海战术盲刷肖1000题。）",
        "（复习建议：最后冲刺阶段不要再做新的模拟怪题。将重心完全放回近3年的真题卷上，重新熟悉官方考官的命题语言和试卷原始结构。）",
        "（复习建议：冲刺期务必保持数学的绝对手感。每天仍需完成几道完整的综合计算题，确保计算步骤的连贯性和手写速度。）",
        "（复习建议：不断翻阅武忠祥选填技巧以及错题本上的典型纠正思路，保持对常用解题套路的敏感度。）",
        "（复习建议：12月《肖四》出版后，主观题优先背诵其核心加粗内容。即使不能通篇朗诵，掌握下划线的核心答题句柄同样能斩获高分。）",
        "（复习建议：应对政治大题的突发冷门题，建议在考前学习B站关于“考研政治怎么抄材料”的保底得分视频，确保任何情况下都能交出饱满的答卷。）",
        "（复习建议：可以制作一张简易备忘录，记录如泰勒展开、傅里叶级数、全概率公式等易混淆知识，考前几天反复快速浏览。）",
        "（复习建议：英语前期的核心只有背单词。由于你本身有六级500+的基础，可加快过词速度，但仍需坚持每日打卡《不背单词》APP。）",
        "（复习建议：暑假开始，英一真题应保持每两天一套阅读的正常推进。配合使用《真题伴侣》等软件，专注攻克真题内部的生词与熟词僻义。）",
        "（复习建议：英语二作文从暑假即可开始准备。直接背诵Monkey老师的作文模板框架，并在日常积累适用于各类社会话题的骨干词汇。）",
        "（复习建议：考前一周全面停止高强度的知识新入。整理好各类文具准考证，回归之前总结的定型手稿材料，平稳心态迎接考试。）"
    ]

    # ================= 基础阶段：高数核心 (Week 1-7) =================
    
    add_week(1, "高数基础：极限与连续", 
             "起始阶段必须摆正态度：只听课是假努力的重灾区，唯有动笔算对题才能转换为考场分数。本周重点是极限部分。对于专业课，本周也须完成相应的一周定额。\n" + tips[0],
             {"title": "禁止漫长听课，直击30讲与1000题", "content": "🚫 绝对避坑原则：不要去听冗长的考研全科基础视频课。\n✅ 唯一任务：直接做张宇30讲第1-2讲的课后题，并配合作完1000题的基础篇。遇到泰勒公式和等价无穷小的痛点题目，果断上B站搜索UP主（千羽、考研数学777等）对应知识点视频，看懂就立刻重算一遍。"},
             {"title": "疯狂堆砌：核心大纲词汇启动", "content": "🚫 绝对避坑原则：不许购买手译本逐句精翻！\n✅ 此阶段唯一任务：使用《不背单词》或类似App，疯狂滚动背诵考研大纲的核心3000词。鉴于你有六级500+的基础，你的看词速度应该大于普通考生。暑假前目标是完全刷完这3000词的3轮记忆法。"})

    add_week(2, "高数基础：导数与微分", 
             "导数部分虽然基础但计算极易出错，务必在草稿纸上把过程写出。继续保持公共课与专业课的时间平衡。\n" + tips[1],
             {"title": "攻坚30讲：第3-5讲导数与应用", "content": "✅ 核心任务：做对应的小节课后题及1000题基础篇习题。重点练习复合函数和隐函数的导数。\n🚫 高能避错：凡是张宇讲义中夹杂的“超实数”、微分算子法、stolz法则、各类怪异极限证明以及任何过于前沿的理论，直接全数跳过，完全不看！"},
             {"title": "延续词汇输入，扩大见面频率", "content": "✅ 重复执行：不要管之前有没有记住上周的词，继续推进新词并完成APP提示的复习计划。记住，只要不断见面，熟词僻义在考研英语一的长文里也能通过语感被唤醒。"})

    add_week(3, "高数基础：中值定理与一元积分", 
             "中值定理的构造比较艰涩，但在练习册和模拟题期间绝对不浪费时间磕它的证明书写。\n" + tips[2],
             {"title": "定积分的启动预热：第6-8讲对应", "content": "✅ 核心任务：掌握常规函数的换元积分和分部积分运算，并独立完成1000题基础上的相关题型。\n🚫 硬性跳过：练习册和模拟卷上所有的包含中值定理的【纯证明题】，不论其看起来多么精巧，一律划掉不做。把时间留给积分计算。"},
             {"title": "单调而必要的词汇苦旅", "content": "✅ 高频眼熟法：不要在某个拼写上卡很久，重点记单词发音及其在历年真题里常考的第一个释义。你的基础决定了你只要词汇到位，英语阅读的地基就已经盖好了。"})

    add_week(4, "高数基础：定积分及其应用", 
             "这是一元微积分的巅峰章。变限积分求导和定积分的几何物理应用公式是考点常客。请妥善安排晚上和周末的完整时间做题，别忘了留时间给专业课。\n" + tips[3],
             {"title": "30讲综合演练：第9-12讲核心", "content": "✅ 核心任务：完成变限积分的求导练习，并把求面积、体积、弧长的各类公式记认真背诵牢。计算题中但凡有一步卡住超两分钟，果断看答案分析步骤，并立马重算一次以形成定势反应。"},
             {"title": "保持进度不松懈", "content": "✅ 持续推进：完成每天预设的200个以上新旧词打卡。《不背单词》的数据反馈会让你对自己最薄弱的那几十个钉子户词汇有直观了解。"})

    add_week(5, "高数基础：微分方程与空间解析几何", 
             "这一周迎来数学一的专属部分，空间解析几何是后续多元微积分计算物理模型的基础。\n" + tips[4],
             {"title": "吃透30讲：第13-14讲+空间几何", "content": "✅ 核心任务：针对常系数及非齐次线性微分方程的特解对照表格，不仅要理解还要背下来。空间解析几何的各种经典曲面（圆锥面、旋转抛物面）要有基础的心里成像能力并完成对应1000题计算。"},
             {"title": "总结难词清单", "content": "✅ 建立重点：将那些见了好几次仍然想不起来的词，整理到一个备忘本上，后期在通勤或者食堂排队时经常翻看加深肌肉记忆。"})

    add_week(6, "高数基础：多元函数微分与无穷级数", 
             "数学一大片江山的难点区——无穷级数终于到来，收敛域与幂级数展开需形成条件反射。\n" + tips[10],
             {"title": "30讲：多元微分与无穷级数应用", "content": "✅ 核心任务：多元偏微分的链式法则计算必须练到行云流水。无穷级数只要求熟知常见的五个标准函数展开式。\n🚫 战略放弃：对于无穷级数的一些偏僻判别法证明及海涅定理分析，全面放手不看，时间用于实打实的连带计算。"},
             {"title": "词汇量的一千关口跨越", "content": "✅ 不听英语语法课：在你的基础下，不建议听任何大篇幅的语法长句子拆解课，用做题来带语感即可。确保目前背单词的大周期不停摆。"})

    add_week(7, "高数基础：重积分与曲线曲面积分", 
             "数学一最大计算密集区。这周也是检验你的耐性是否达标的周，坚持住。\n" + tips[3],
             {"title": "30讲硬核：重积分与三大物理公式", "content": "✅ 核心任务：认真对待到底，完成二重、三重积分计算，以及格林公式、高斯公式、斯托克斯公式的转换条件并落实到1000题上。\n计算题再长也必须在纸上得出最终数值才准停下。完成这周，高数宣告阶段性完成。"},
             {"title": "达成一轮词汇通关", "content": "✅ 稳固安排：继续用背词APP消灭考研红库，准备迎接即将到来的暑假和更为真枪实弹的英语一阅读打法。"})

    # ================= 基础阶段：线代与概率论 (Week 8-12) =================
    
    add_week(8, "线代基础：行列式与矩阵", 
             "线代的复习逻辑完全不同于高数，初等行变换就是打开线代大门的唯一钥匙。\n" + tips[5],
             {"title": "张宇线代(1-3讲)与1000对应", "content": "✅ 核心任务：不要听庞杂的三十讲线代基础课。直接做课后题和基础篇，总结矩阵相乘、求逆、伴随的规律。行变换务必练得足够熟！"},
             {"title": "开启词汇二刷提速期", "content": "✅ 任务升级：此时部分词汇你已经能形成肌肉关联。提高单日复习量上限，加快翻看速度。"})

    add_week(9, "线代基础：向量组与线性方程组", 
             "这里是线代极其容易造成混淆的地方，相关的秩数关系和基础解系需要配合图像或者例子加深印象。\n" + tips[6],
             {"title": "线代重灾区：4-5讲内容全通", "content": "✅ 核心任务：能通过系数矩阵的秩，快速判定方程组的解的数量。依然奉行跳过偏难证明题，如果理解方程组抽象推导吃力，马上去B站点播专门的解题技巧单章视频来看。"},
             {"title": "词汇连贯打击", "content": "✅ 坚持背完当天的份额，不留给明天。为之后开真题阅读清扫生词障碍。"})

    add_week(10, "线代基础：特征值与二次型", 
             "每年线代大题必定在此出场，特征方程及正交化是一定要吃透的。\n" + tips[7],
             {"title": "线代结尾：第6讲大收局", "content": "✅ 核心任务：施密特正交化的复杂根号转换，务必一字一字写下来计算！二次型化标准型的方法必须门清。线代至此结束，抽空将前期线代的错题再算一遍。"},
             {"title": "英一真题预热", "content": "✅ 心理建设：可以准备好英语一最早年份的几套早年干卷（先不买有解析的），准备在下个阶段接入阅读环境。"})

    add_week(11, "概率论基础：随机事件与变量", 
             "概率论是数学一中相对收益比最高的一门课，很多题实质在考测你前面积分的知识。\n" + tips[9],
             {"title": "概率论1-3讲梳理", "content": "✅ 核心任务：熟悉离散型和连续型的分布函数套路。全概率与贝叶斯公式的适用场景一定要记清楚，这是第一大题的常驻嘉宾。"},
             {"title": "保持词汇第三轮极速过", "content": "✅ 热手练习：在每天闲散的时间，以极快的扫视眼光将背单词软件里的考研核心词汇进行第三轮狂刷。"})
             
    add_week(12, "概率论基础：数字特征与数理统计", 
             "这部分属于大片大片的固定步骤得分地带。背诵参数估计算法并按套路带入即可得全分。\n" + tips[21],
             {"title": "概率最后冲刺：数字特征与参数估计", "content": "✅ 核心任务：八大分布的期望和方差是必须张口就来的。多重积分计算相关的二维随机变量协方差要会算。\n彻底搞定理清楚最大似然估计的六部曲写卷步骤。所有数一基础理论宣告通关！"},
             {"title": "英语词库的全面制霸", "content": "✅ 最终检视：确信自己对英语高频常用词义已具有60%以上的一眼辨认识别率。"})

    # ================= 强化阶段：大观与660 (Week 13-16) =================

    add_week(13, "强化推进：大观视频（高数部分）（一）", 
             "基础打完，你需要对题型有个居高临下的全景掌握，澄箫宇的大观在此极度适用。另外注意兼顾你的专业课程排期。\n" + tips[11],
             {"title": "重点看B站：澄箫宇大观高数部分", "content": "✅ 核心任务：按两天一个长视频的速度推进高数的大观。\n🔥 绝对红线：他在视频里抛出例题时，不准直接听他顺着讲完。必须按下暂停，自己在纸上推演出一个你认为对的结论，再看他的解析。没做题就听等同于白看。"},
             {"title": "暑期英一真题阅读出鞘", "content": "✅ 进入真题阅读：安排每两天写一套英一早年真题阅读区（暂不启动作文与完型）。\n配合使用《真题伴侣》APP（买个会员即可），不认识的阅读生词全在APP里点亮标出，进行专门二次复背！"})

    add_week(14, "强化推进：大观视频（高数部分）（二）", 
             "在大观中你会看明各种秒杀小结论和知识联动的网状结构，把这些结论移植到你的高频笔记上。\n" + tips[12],
             {"title": "大观高数后半轴扫尾", "content": "✅ 核心任务：继续看大观，补齐二重积分及无穷级数的题型破局点。遇到听不懂他为啥这么假设的地方，马上倒退重看。"},
             {"title": "真题阅读精进模式", "content": "✅ 持续操练阅读：注意英一文章选项设陷的区别方式。对阅读理解做结构分析，而非毫无意义地进行全文精译中文。"})

    add_week(15, "速刷利器：660题高数段进场", 
             "660题的选择填空切入极其刁毒，错50%都是家常便饭。这正是帮你修补基础盲区的绝佳探针。\n" + tips[14],
             {"title": "660题一阶速刷法执行", "content": "✅ 任务：开展高数部分的660速刷。\n⚠️ 速刷心法：第一排除了计算粗心造成的错误外，剩下的一定是知识盲区。一旦两分钟没有思路切入，绝不死等硬憋，果断看答案分析步骤，用红笔将此题在书上圈出，当即去补该概念课本内容。不求正确率，求扫雷的全面性。"},
             {"title": "真题伴侣词汇固化", "content": "✅ 专项攻克：现在不背单词APP里的泛背基本可停止，将主要精力全盘转交给《真题伴侣》里面真题特定语境的生词强力打卡攻克。"})

    add_week(16, "速刷利器：660题线代概率段进场", 
             "线代和概率在660中也是极度抽象的存在。\n" + tips[15],
             {"title": "660题线代/概率快速做完", "content": "✅ 任务：利用速刷法则迅速过掉线代概率的选填雷区。\n做错的题不要抄题！把错点如“不相关的充分条件”等总结在归纳本上即可。"},
             {"title": "Monkey老师的作文初窥门径", "content": "✅ 开练写作课：开始听Monkey老师的作文课！不要去学那些庞杂高深难写的句型。\n你唯一的任务是：全盘接受并认真背诵下来他的作文定式模板框架，每天默写强化骨架，往里面填自己的储备词。"})

    # ================= 真题一轮实战：《真题一本通》 (Week 17-23) =================

    add_week(17, "真题实测卷一：极限、微分段下场", 
             "于文涛的《真题一本通》正是你考研能提大分的保命核心。历年真题是所有市面资料的总纲！\n" + tips[16],
             {"title": "认真对待一本通数一上篇", "content": "✅ 重点任务：开动《真题一本通》的第一分卷。\n必须独立建立一个真题专属的【按章节分类的错题本记录册】。对于数一真题里的证明题，这是你全备考唯一需要老老实实手敲证明的素材对象。"},
             {"title": "阅读真题中期稳定", "content": "✅ 推进进度：维持两天解决一套阅读的速度，把早期真卷全吃透。随着真词库的扩展，读懂题面的障碍会大幅锐减。"})

    # ================= 政治首次浮出水面 (约在此处，8月份至10月初均可启动) =================
    
    add_week(18, "真题实测卷二：积分综合大题的狂殴", 
             "积分大题错一步满盘皆输，在此必须训练绝不心算的肌肉记忆规范排版。\n" + tips[29],
             {"title": "一本通中篇积分实战", "content": "✅ 核心任务：遇到卡顿直接搜各大UP的该题解析单章，并用红笔抄解题逻辑于错题本。千万小心不要眼高手低。"},
             {"title": "作文定式演练", "content": "Monkey的模板能一分钟顺畅默写完毕即达标，在里面加一点有关经济社会的背单词APP里积累的主题词汇。"},
             {"title": "政治轻量化建账", "content": "🚫 极限避坑：不用去买肖1000去死做厚书，也不用去听徐涛马原的漫长系统课！\n✅ 任务：仅仅去买或打印一本《腿姐冲刺背诵手册》，当小说或杂志把它熟读，对各大历史会议有些印象。"})

    add_week(19, "真题实测卷三：多元与级数硬仗区", 
             "数一区别于数二就在于这里无穷无尽的长串计算式，必须抗打抗压，耐心算到底出结果。\n" + tips[19],
             {"title": "一本通无穷级数与多重积分", "content": "✅ 核心任务：将三大积分定理在真题里的花样考法全数吃尽。对常错知识点依然进行错题本转移作业。"},
             {"title": "最难文章的回望处理", "content": "用《真题伴侣》看懂之前记录下错满天飞的杀手级文章（如纺织工、长难科技文）到底难在哪。"},
             {"title": "苍盾小程序的碎片打击", "content": "✅ 任务：利用中午饭后或下班时间在《苍盾小程序》刷每日的政治模拟题卷！限制每天也就是一套（只看单选多选），在错题积累中补充知识盲区。"})

    add_week(20, "真题实测卷四：线代大综合的洗礼", 
             "往往会从多项式的系数推到正定，考察你的全局掌控力。\n" + tips[21],
             {"title": "线代真题总攻", "content": "✅ 核心任务：所有线代的压轴解答题全部拿来验证自己的化标准型技术和方程推导，建立对错题全景画像。"},
             {"title": "词汇量固若金汤期", "content": "此时英语应该不存在词汇严重匮乏造成的卡壳，作文框架也能按场景填充自如。"},
             {"title": "政治稳健每日测", "content": "苍盾选择错题看看自己混淆了哪个中国共产党的关键文件时期，简单备注于冲刺手册边缝中。"})

    add_week(21, "真题实测卷五：概率送分地带与首轮沉淀", 
             "这是最容易让你看到提分希望的地方，不要被计算式吓到，背下套路公式就是满分得主。\n" + tips[22],
             {"title": "概率真题全收割+大观二刷起飞", "content": "✅ 核心任务一：刷尽参数估计和二维正态的一切真题。\n✅ 核心任务二：开始二刷！把“澄箫宇大观”再看一遍。既然已经被真题洗练过，此时二刷大观会有极其通透的全局连接感，很多考法瞬间明了。"},
             {"title": "重刷早年典型阅读篇", "content": "可以抽时间重构过去错乱的文章，审视自己现在的思维路线是否顺应出题者的反向陷阱。"},
             {"title": "政治背诵手册再次翻阅", "content": "把腿姐背诵手册过第二遍。"})

    for i in range(22, 24):
        msg = tips[i-2]
        add_week(i, f"专属错题本沉淀消化排雷周 (第{i}周)", 
                 "第一轮真题与之前所有错题的大过滤洗牌局。停下前进步伐，就此对弱点施以重拳。\n" + msg,
                 {"title": "首发清洗真题专属错题本", "content": "✅ 核心任务：遮盖住之前在一本通错题本上的解析，强行自行演算到底。如果有一次非常顺利写对算完的，毫不留恋地将其从绝密错题本上重重划掉。剩下那些两遍甚至三遍还是算错或者做错方向的题，就是你最终决战的关键。"},
                 {"title": "各科目综合练习", "content": "默写作文结构、使用真题伴侣查漏单词、阅读保持熟练。\n开始尝试带入些翻译句子的自我训练（遇到复杂的用中文在腹内构架出主干）。"},
                 {"title": "苍盾不间断", "content": "政治只需要维持这每天十多分钟小程序的存在感即可。把专业课的大背诵时间拉足。"})

    # ================= 套卷横刷，全面测试体系抗压性 (Week 24-34) =================

    add_week(24, "真题套刷期：全真全景（09年-26年）", 
             "散题复习无法建立整体统御性。唯有通过真实的套卷连续作战，方可探测你的得分区间与算力分配体能极值。\n" + tips[23],
             {"title": "每天一套数一成卷对战", "content": "✅ 核心任务：必须保证上午用极其连贯的、连续不断的整整3小时来进行一次数一往年真卷（除开刚考的近三到四年卷作防守考前用）的仿真模拟。\n要求：到点无论剩几道证明大题统统停笔。做完马上对案批改。把新增的致命硬伤题再补充进原错题集内。"},
             {"title": "英语全卷真感操练", "content": "把作文部分也加入平时的仿真考里，验证自己的全盘答题策略耗时分布。"},
             {"title": "保持闲散读册", "content": "腿姐的手册再当报纸看一会儿。"})

    for i in range(25, 29):
        msg = tips[i-1]
        add_week(i, f"数学真题套刷长途推进 (第{i}周)", 
                 "你的分数会随着试题难易大起大落，不要慌乱，那些没有得分的地方才是这套试卷对于你的无价价值。\n" + msg,
                 {"title": "继续真题套局每日一打", "content": "✅ 核心任务：雷打不动的早晨套题目测。\n💡 核心动作：把那些反复出错的同一个概念板块，圈出来，重新去找B站等单集强化补丁视频深度复刻，搞懂为何总是中计。"},
                 {"title": "英语作文流水线成型", "content": "要求你能对着随便一年的题，毫不思考五分钟之内将Monkey全部骨架框架默出在草稿上。"},
                 {"title": "政治小程序刷至满腹错题点", "content": "苍盾模拟选项错的逐渐可以串起一部近现代史和中特思维导图。"})

    add_week(29, "高效技巧：武忠祥选填课加入与李林开始", 
             "真题套阶段初步完结，该动用技巧性辅助提高选填效率拿大题时间。并迎接李林套题的奇峰迭测。\n" + tips[28],
             {"title": "同线并举：李林6+4(开始) 与选取技巧", "content": "✅ 任务：利用李林6套卷进行每天的套题更换（不写李题的任何证明题类！）。\n同时间开看武忠祥大师的选填绝技秘方，掌握特值推演等不讲武德但也必不可少的捞分技去对付选择题。"},
             {"title": "英语词汇最高强收网", "content": "真卷伴侣上的那些老错的生熟僻义已经可以熟练叫出。"},
             {"title": "政治一页纸总纲建立", "content": "✅ 任务：去熟悉并搞到“澄箫宇定稿的政治一页纸”，开始高强度背诵，这种极简化的树形网络总纲对于政治结构极度友好。"})

    for i in range(30, 35):
        msg = tips[i-3]
        add_week(i, f"模拟真源融合期与李四冲击 (第{i}周)", 
                 "李林模拟卷四套难度骤升，不要在乎分数只提取解析里的优良捷径。用技巧处理以前那些写满一大黑板推演的笨重选项。\n" + msg,
                 {"title": "李林4套杀完与错题归途", "content": "✅ 任务：把李林系列收官并整合所有含金量高的新路子新思路单设一册模拟集要。\n用武忠祥的高级技巧再次审视一本通的那个错题本核心战区，进行全面复习！"},
                 {"title": "定型英语战术排布", "content": "明确上了考场，自己到底是先写大小作文，还是先干掉哪两篇擅长话题的阅读理解。确立固定攻击次序不作更改。"},
                 {"title": "政治常规背诵加注", "content": "维持极简框架熟记的基线不变。"})

    # ================= 考场最后绝唱：冲刺与保底法门 (Week 35-41) =================

    add_week(35, "回归近年原始真迹", 
             "摒弃外面所有的偏门模拟！这是最后阶段唯一核心铁律！只有回归近几年的真实统考局风格才最匹配考场要求。\n" + tips[31],
             {"title": "近三年真题的模拟重演", "content": "✅ 极度核心任务：之前舍不得做或者做过忘了的近几年统考真套！全部拿出！严格限时按实战排布。这是考官当前命眼最最直接的表达。\n做错的题哪怕熬夜也必须重新顺着答案算至零误差点。"},
             {"title": "英语几年卷重做", "content": "把英语一近期几年的卷面用干净的新版面重新扫做一遍验证思维通路。"},
             {"title": "政治维持框架与结构记忆", "content": "不需花大块时间。"})

    for i in range(36, 38):
        msg = tips[i-3]
        add_week(i, f"全线错题最终核定排查 (第{i}周)", 
                 "不做新题绝不认真对待怪难题！把以往记录的所有痛点重温至免疫体质！\n" + msg,
                 {"title": "只盯你的厚重的唯一错案本", "content": "✅ 任务：除了每天维持一两道比如级数大题或者参数估计的手感保持的演练外。数学其他一切时间都用在重翻你的错题本的复习上。已经看明白的彻底划掉不再浪费一分。\n那些三番五次依然不会的只重点看它的解题思路。"},
                 {"title": "在答题卡上练习写作文", "content": "每天保持必须写一个段落英语维持发热量。"},
                 {"title": "政治等待最后的重要复习资料", "content": "等待12月的王者：肖四大军进场。"})

    add_week(38, "肖四正式下发（政治集中背诵期）", 
             "这一周乃至考试前，属于你早中晚集中背诵的最重要时间点！放下数学的复杂怪点！\n" + tips[34],
             {"title": "最后保持简单的保温与自我自信重建", "content": "✅ 任务：看一眼小错卡纸提示，做点极为基础的复合微积分或简单积分以保思维思维连贯即可。"},
             {"title": "格式细节纠正与底盘维护", "content": "注意英语大写和小品书信格式莫错。不再重兵把守。"},
             {"title": "🔥最终冲刺：认真背诵肖四大体文字块骨架", "content": "✅ 终极压轴：把《肖四》捧到手，集中背诵它加粗体或段首的重点采分名词！\n对于论述你不仅要会写甚至要求你能形成模块堆叠拼接。"})

    add_week(39, "考场应急：如何抄材料", 
             "这个技巧将带给你上考场毫无畏缩直面完全未见名词真题的主力支撑底气。\n" + tips[35],
             {"title": "大范围极速回视小公式", "content": "✅ 任务：防止在泰勒第二项系数这种智障点丢全分，狂背公式册与冷点属性表。"},
             {"title": "底线保留手感与不忘词", "content": "维持不冷即可。"},
             {"title": "政治压仓技巧：如何优雅抄论述资料拿高分", "content": "🔥 必决任务：强力推荐今年马上到考研点时B站必会弹出的关于“如果没有背上原题，考研政治现场如何抄写摘取阅读材料进行符合逻辑的答案”的教程！确保无偏好绝不丢面！"})

    add_week(40, "收紧缩口安排与装备清点", 
             "你度过了所有艰难岁月！现在你需要的是一觉好梦及平和的步子迈进考场门内。\n" + tips[36],
             {"title": "什么新资料都不做！连多看一题怪路偏题都会损伤你自信度", "content": "✅ 保守：把脑子的线代理论体系架构图画一下，确保主干清晰即可。"},
             {"title": "顺几遍Monkey框架", "content": "最后一遍全写。"},
             {"title": "政治思路顺线梳理", "content": "重温你的考法提纲树向。文具检查及防寒核验。"})

    add_week(41, "征战顶峰测试大周", 
             "将你的所有不理解与惊扰放下，你拥有的武器足以完全掌握绝大多数只会低效打卡的人。\n" + tips[40],
             {"title": "考场果断如砍瓜切菜——拿应有的分", "content": "只挑熟悉的且练得非常熟悉的公式计算写，遇到硬卡超过15分钟的证明大字骨题，先留白后处理，以极大拿到算筹分量为第一优先！"},
             {"title": "作文默打、精准涂卡无错翻漏查", "content": "稳定发挥。"},
             {"title": "遇到多反转题干大胆落体材料论述不留空纸！", "content": "所有纸面一律写满，尽量多写。发挥一切你能发挥的招式。"})


    data = {"student": "ly", "weeks": weeks[:41]}
    
    with open("D:/myblog/source/kaoyan/ly/LibaibaiStylePlan.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    html_template = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ly 2027考研全程深度定制规划</title>
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
            font-size: 2rem;
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
        .grid-math { background: rgba(244,114,182,0.08); border-left: 3px solid #f472b6; }
        .grid-english { background: rgba(52,211,153,0.08); border-left: 3px solid #34d399; }
        .grid-politics { background: rgba(251,191,36,0.08); border-left: 3px solid #fbbf24; }
        
        h3 { margin-bottom: 12px; font-size: 1.1rem; }
        .grid-math h3 { color: #f472b6; }
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
            margin-bottom: 20px; border-left: 3px solid var(--accent); font-style: italic; font-weight: bold; color: #fff;
        }
        .subject { background: rgba(255, 255, 255, 0.03); border-radius: 8px; padding: 16px; margin-bottom: 16px; border: 1px solid rgba(255,255,255,0.05); }
        .subject-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 8px; }
        .subject-name { font-weight: bold; font-size: 1.05rem; }
        .subject-name.math { color: #f472b6; }
        .subject-name.english { color: #34d399; }
        .subject-name.politics { color: #fbbf24; }
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
            <h1>ly 2027考研全程深度定制规划</h1>
            <div class="meta">
                <span>🎯 东南大学·控制科学与工程或电子信息</span>
                <span>📅 周期：2026.03.06 - 2026.12 考前 (共41周)</span>
            </div>
            <div class="meta" style="margin-top: 8px;">
                <span>📚 必考：数学一 / 英语一 / 政治 / 统考专业课</span>
            </div>
        </header>

        <!-- 总体规划概览 -->
        <div class="overview">
            <h2>🎯 全局时间红线与认真对待原则</h2>
            
            <p class="strategy">
                <strong>🔥 核心要求：所有科目都不准单纯当「听课机器」！听课永远学不会，只有通过做题才能真正在考场上写出来！多想多算多做，务必落实到草稿纸上！</strong><br><br>
                <span style="color: #ffb86c;">⚠️ 时间分配：抛开专业课，公共课的学习精力比重大致为数学 60%、英语 30%、政治 10%。注意，此处为“公共课内分配”，不包括专业课时间，务必在日常排期中优先把【专业课】的时间独立且固定排入！</span>
            </p>
            
            <div class="grid-box">
                <div class="grid-item grid-math">
                    <h3>📐 数学一（占公共课精力 60%）</h3>
                    <ul>
                        <li><strong style="color: #fff;">果断弃课投题：</strong>不推荐听老师讲大量的基础理论连轴课！做题时不会的直接去B站搜播放量高的干货UP主讲解（千羽、考研数学777、没咋了均可），比大机构视频效率高十倍！</li>
                        <li><strong style="color: #fff;">绝对不需要学的部分：</strong>张宇“超实数”、微分算子法、stolz法则、海涅定理、压缩映射原理。就算想考150分的人也全都不需要学不需要看！！！</li>
                        <li><strong style="color: #fff;">练习策略铁律：</strong>真题分类位列最首要级别 -> 之后才是基础习题册 -> 模拟题只求辅助开拓见识。<br>所有习题册+模拟卷【全部果断跳过证明题】，只准手写真题里的证明题！</li>
                        <li><strong style="color: #fff;">核心资料体系：</strong>前期推《三十讲》过关+《1000题》基础+《660》找茬速刷；跟进B站澄箫宇大观系列先敲钟再听详讲。一轮真题绝对指定且唯一重视：《真题一本通》——于文涛。收官采用李林6+4+武忠祥强推选填抢分手艺视频。</li>
                    </ul>
                </div>
                
                <div class="grid-item grid-english">
                    <h3>📖 英语一（占公共课精力 30%）</h3>
                    <ul>
                        <li><strong style="color: #fff;">底线极简原则：</strong>绝不买又厚且全废的手译本精翻文章！少听一切大部头长课语法。前期所有的唯一工作只有狂刷单词阅读，后期暑假跟猴子（Monkey）听模板强堆写作，最后直接背诵输出拿高分。</li>
                        <li><strong style="color: #fff;">反复滚动刷词：</strong>暑期大关前所有的任务均靠用《不背单词》APP啃断核心3000词，最少反复磨它刷满3遍！后期开启针对《真题伴侣》中阅读文里的语境意思反复充值记忆库。</li>
                    </ul>
                </div>
                
                <div class="grid-item grid-politics">
                    <h3>🏛️ 政治（占公共课精力 10%）</h3>
                    <ul>
                        <li><strong style="color: #f43f5e;">🚫 10月初前绝对封印不动：</strong>最早10月初进场！严禁过早进入浪费算力期！远离徐涛等所有长篇大论的课程，坚决躲避肖1000题这种让你迷失在无意义细节里的巨厚黑砖！</li>
                        <li><strong style="color: #fff;">突击点打法：</strong>熟读一页纸或腿姐冲刺背诵手册，靠《苍盾小程序》进行每日排雷选择错题点。末期12月拿到了唯一的核心资料《肖四》之后就一件事背到底，哪怕只能背关键词！必须去B站参拜‘如何使用材料满分抄’的究极视频手段作为你的铁皮底裤！</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="expand-all">
            <button onclick="toggleAll()">展开/收起全部计划周</button>
        </div>

        <div id="weeks-container"></div>
        
        <footer>
            <p>💪 这份时间线没有任何花里胡哨，全是前人踩过的雷总结出的干货，执行到底必定上岸！</p>
        </footer>
    </div>

    <script>
    const planData = ''' + json.dumps(data["weeks"], ensure_ascii=False) + ''';

    function renderWeeks() {
        const container = document.getElementById('weeks-container');
        planData.forEach((week, index) => {
            const card = document.createElement('div');
            card.className = 'week-card';

            let subjectsHtml = `
                <div class="subject">
                    <div class="subject-header">
                        <span class="subject-name math">📐 数学</span>
                        <span class="hours">${week.math.hours}</span>
                    </div>
                    <div class="subject-title">${week.math.title}</div>
                    <div class="subject-content">${week.math.content.replace(/\\n/g, '<br/>')}</div>
                </div>
                <div class="subject">
                    <div class="subject-header">
                        <span class="subject-name english">📖 英语</span>
                        <span class="hours">${week.english.hours}</span>
                    </div>
                    <div class="subject-title">${week.english.title}</div>
                    <div class="subject-content">${week.english.content.replace(/\\n/g, '<br/>')}</div>
                </div>
            `;

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
                    <div class="message">💡 ${week.message}</div>
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

    with open("D:/myblog/source/kaoyan/ly/LibaibaiStylePlan.html", "w", encoding="utf-8") as f:
        f.write(html_template)
        
if __name__ == "__main__":
    get_full_plan_student_7()
