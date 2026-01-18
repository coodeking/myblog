
import json
import datetime

# 汪桑 2026考研全程规划 (2026.01.19 - 2026.12.20)
# 核心原则：去AI味，口语化，重执行，全覆盖

def get_full_plan():
    weeks = []
    
    # 辅助函数：周次生成
    def add_week(week_num, theme, msg, math, eng, pol=None, prof=None):
        weeks.append({
            "week": week_num,
            "theme": theme,
            "message": msg,
            "math": math,
            "english": eng,
            "politics": pol if pol else {"content": "暂不复习"},
            "professional": prof if prof else {"content": "自行安排 (建议每周5h)"}
        })

    # ================= 基础阶段：高数 (Week 1-12) =================
    # 目标：吃透张宇30讲高数 + 1000题A组
    
    add_week(1, "🔥 破冰周：极限计算", 
             "别在这周纠结概念定义，会算才是硬道理！泰勒公式是考研数学的‘核武器’，必须背得滚瓜烂熟。",
             {"title": "张宇30讲：第1-2讲", "content": "重点搞定【函数极限】和【数列极限】。遇到‘七种未定式’要迅速反应出用洛必达还是泰勒。课后题全做，错题标记。", "hours": 20},
             {"title": "死磕单词", "content": "《不背单词》APP走起。每天100个新词，雷打不动。前期不看阅读，词汇量不够看真题就是浪费。", "hours": 10})

    add_week(2, "⚙️ 基础周：连续与导数", 
             "导数公式表背了吗？反三角函数求导、莱布尼茨公式是高频遗忘点，多写几遍！",
             {"title": "张宇30讲：第3-5讲", "content": "攻克【连续性判断】和【导数定义】。注意：导数定义题特别爱考，一定要会凑形式。", "hours": 18},
             {"title": "坚持背词", "content": "继续刷单词。觉得枯燥就读读例句，但别碰长难句书，先把砖头搬够。", "hours": 10})

    add_week(3, "⛰️ 难点周：中值定理", 
             "这周可能会很痛苦。罗尔、拉格朗日、柯西，不要去背证明过程，要学会‘通过结论构造辅助函数’。",
             {"title": "张宇30讲：第6-7讲", "content": "只看计算应用（求极限、证不等式）。纯证明题如果实在看不懂，第一遍基础阶段可以先放过，做好标记。", "hours": 20},
             {"title": "单词打卡", "content": "复习比新学重要！利用坐车、排队碎片时间刷复习模式。", "hours": 8})

    add_week(4, "🌊 积分周：凑微分", 
             "不定积分没有捷径，就是‘猜’！凑微分法要有手感，这周建议多花点时间刷计算题。",
             {"title": "张宇30讲：第8讲", "content": "把基本积分表贴在书桌前。每天睡前看一遍。1000题里不定积分的计算题先试着做20道找找感觉。", "hours": 20},
             {"title": "单词进度1/5", "content": "坚持住，前两周的热度过了，现在拼的是习惯。", "hours": 8})

    add_week(5, "📏 积分周：定积分应用", 
             "几何应用（面积、体积）全是公式，物理应用（功、压力）考得少但不能不会。",
             {"title": "张宇30讲：第9-12讲", "content": "重点关注【变上限积分函数】的求导，这是每年必考题！这一块搞不定，后面全崩。", "hours": 18},
             {"title": "单词积累", "content": "继续背。可以开始试着在APP里听单词的例句发音，增加记忆维度。", "hours": 8})
             
    add_week(6, "⛓️ 难点周：微分方程", 
             "微分方程就是‘认题型套公式’。要把那几种标准形式（一阶线性、伯努利、二阶常系数）背得比手机号还熟。",
             {"title": "张宇30讲：第13-15讲", "content": "特别注意：二阶常系数非齐次方程的【特解设法】，那个表格必须背写默写下来！", "hours": 18},
             {"title": "单词", "content": "没什么好说的，背就完事了。", "hours": 8})

    add_week(7, "🌌 多元周：偏导计算", 
             "从一元到多元，别晕。全微分的定义是核心，它和连续、可偏导的关系图要理顺。",
             {"title": "张宇30讲：第16-17讲", "content": "重点练【隐函数求导】和【复合函数求导】的链式法则。画树状图是个好习惯。", "hours": 18},
             {"title": "单词", "content": "进度条过半了吗？加油。", "hours": 8})

    add_week(8, "📦 多元周：二重积分", 
             "高数收官战！二重积分最怕算错。极坐标变换、交换积分次序，这两个技巧要炉火纯青。",
             {"title": "张宇30讲：第18讲", "content": "尤其是利用【对称性】简化积分，能省一半时间。基础阶段课后题做完，高数第一轮算过关。", "hours": 18},
             {"title": "单词", "content": "这时候你应该积累了快1500词了。稳住。", "hours": 8})

    add_week(9, "🏋️‍♂️ 刷题周：1000题-极限", 
             "不看视频，纯动手算！如果你发现看着都会，一做就废，说明计算量不够。",
             {"title": "张宇1000题：第一章", "content": "做A组基础题。做不出来的题，去B站搜‘千羽’的讲解视频，只看自己不会的那几道。", "hours": 22},
             {"title": "单词", "content": "继续。", "hours": 8})
             
    add_week(10, "🏋️‍♂️ 刷题周：1000题-导数积分", 
             "这周任务量很大，做好心理准备。积分算不对是由于凑微分不熟，回去翻书复习。",
             {"title": "张宇1000题：第二、三章", "content": "每天至少30题。错题用红笔圈出来，别写解题过程在书上，写在草稿纸上。", "hours": 22},
             {"title": "单词", "content": "继续。", "hours": 8})
             
    add_week(11, "🏋️‍♂️ 刷题周：1000题-微方", 
             "微分方程的题坑多，注意特解里的x是不是要乘，乘几次。",
             {"title": "张宇1000题：第四、五章", "content": "整理一波【常见的微分方程坑点】到错题本上。", "hours": 18},
             {"title": "单词", "content": "快要把3000词刷完第一遍了吧？", "hours": 8})
             
    add_week(12, "🏋️‍♂️ 刷题周：1000题-多元", 
             "高数刷题结束。把错题回顾一遍，准备迎接线代。",
             {"title": "张宇1000题：第六、七章", "content": "重点检查二重积分的计算准确率。如果低于70%，罚自己重做十道题。", "hours": 18},
             {"title": "单词", "content": "第一轮背词结束？准备开启第二轮复习背诵。", "hours": 8})

    # ================= 基础阶段：线代 (Week 13-18) =================
    
    add_week(13, "🧱 线代周：行列式与矩阵", 
             "线代和高数不一样，它是‘整块’的知识。行列式计算就那几招，行变换最常用。",
             {"title": "张宇30讲线代：第1-2讲", "content": "矩阵运算（乘法、转置、伴随、逆）的性质非常多，搞个小本子记下来，随时看。", "hours": 18},
             {"title": "单词二轮", "content": "开始二刷单词。这次要遮住中文释义，看英文反应中文。", "hours": 8})
             
    add_week(14, "🧱 线代周：向量与方程组", 
             "这是线代最抽象的地方。线性相关=有非零解，线性无关=只有零解。这个对应关系必须建立起来。",
             {"title": "张宇30讲线代：第3-4讲", "content": "重点攻克【极大线性无关组】和【基础解系】的求法。这是大题必考步骤。", "hours": 18},
             {"title": "单词二轮", "content": "速度可以加快，熟词直接划走。", "hours": 8})
             
    add_week(15, "🧱 线代周：特征值二次型", 
             "线代两大难点汇合。实对称矩阵必可对角化，这个结论是解题金钥匙。",
             {"title": "张宇30讲线代：第5-6讲", "content": "配方法化二次型标准型，虽然简单但容易算错数，多练几道。", "hours": 18},
             {"title": "单词二轮", "content": "坚持。", "hours": 8})
             
    add_week(16, "🏋️‍♂️ 刷题周：1000题-线代", 
             "线代一定要大量刷题才能把知识点串起来。你会发现很多题其实是一个意思。",
             {"title": "张宇1000题：线代部分", "content": "集中火力刷A组题。遇到卡壳的，多半是概念没理清，回去翻30讲。", "hours": 20},
             {"title": "单词二轮", "content": "继续。", "hours": 8})

    add_week(17, "📝 整理周：高数错题", 
             "停得下来才能跑得快。这周不学新知识，专门收拾烂摊子。",
             {"title": "复盘高数", "content": "拿出1000题的高数错题。遮住答案重做。如果还错，标记为‘死穴’，重点看B站相关知识点视频补漏。", "hours": 16},
             {"title": "单词二轮", "content": "保持每天半小时。", "hours": 6})
             
    add_week(18, "📝 整理周：线代错题", 
             "线代概念多，容易混。试试自己画一张线代思维导图？",
             {"title": "复盘线代", "content": "重做1000题线代错题。理清秩、解、线性相关性之间的逻辑链条。", "hours": 16},
             {"title": "单词二轮", "content": "月底前结束第二轮背词。", "hours": 6})
             
    # ================= 强化阶段：大观 + 660 (Week 19-29) =================
    
    add_week(19, "🚀 强化启动：大观1-2", 
             "澄箫宇的大观系列是神作。他会教你站在出题人的角度看问题。",
             {"title": "高数强化：极限/导数", "content": "看大观视频。必须暂停！他讲题前你自己先思考2分钟，没思路再看。别当电视剧看！", "hours": 18},
             {"title": "单词三轮", "content": "第三轮，查漏补缺。只看那些还是记不住的‘钉子户’。", "hours": 6})
             
    add_week(20, "🚀 强化进阶：大观3-4", 
             "积分大观里有很多神仙技巧，比如区间再现公式、华里士公式，学会了能秒杀。",
             {"title": "高数强化：积分", "content": "看完视频后，把讲义上的题盖住答案重做一遍。整理技巧笔记。", "hours": 18},
             {"title": "单词三轮", "content": "利用碎片时间即可。", "hours": 6})
             
    add_week(21, "🚀 强化突破：大观5-6", 
             "多元和微方部分，重点看他是怎么处理复杂计算的。",
             {"title": "高数强化：多元/微方", "content": "整理大观里的典型例题。这些题很可能是真题的变体。", "hours": 18},
             {"title": "单词三轮", "content": "继续。", "hours": 6})
             
    add_week(22, "🚀 强化收官：大观7", 
             "线代大观会帮你把三本书（行列式矩阵、向量方程、特征值）打通。",
             {"title": "线代强化：线代大观", "content": "画出全书逻辑图。搞懂它们是怎么互相推导的。", "hours": 18},
             {"title": "单词三轮", "content": "如果你觉得熟练了，可以开始读一点外刊保持语感。", "hours": 6})
             
    add_week(23, "⚡ 速刷周：660高数(1)", 
             "暑假来了！黄金期！660全是选填，也是考研最容易丢分的地方。概念抠得很细。",
             {"title": "660题一阶：高数1-50题", "content": "2分钟没思路直接跳！别死磕！不会就看答案，然后把这个知识点记下来。", "hours": 20},
             {"title": "真题启动", "content": "英语真题开启！APP《真题伴侣》备好。本周做2010年英二阅读（2篇）。精读！查清每个生词。", "hours": 10})
             
    add_week(24, "⚡ 速刷周：660高数(2)", 
             "错得多别慌，660就是来打击你的。每一个概念陷阱都是为了考场上不踩雷。",
             {"title": "660题一阶：高数51-100题", "content": "分析错误选项为什么错，这个比选对更重要。", "hours": 20},
             {"title": "真题研读", "content": "2010年英二剩余阅读。把文章里所有生词在APP里特别标记，反复背。", "hours": 10})

    add_week(25, "⚡ 速刷周：660线代", 
             "线代的选择题有时候比大题还难，因为可以用特值法排除，但正向推导很难。",
             {"title": "660题一阶：线代全刷", "content": "重点积累‘举反例’的素材。什么样的矩阵比如(1 0; 0 0)经常用来推翻结论？", "hours": 20},
             {"title": "真题研读", "content": "2011年英二阅读。不写作文，不写完型，只搞阅读Part A。", "hours": 10})

    add_week(26, "📝 强化复盘：错题本", 
             "刷完660，你手上应该有一堆错题了。这周不新做题，把错题吃透。",
             {"title": "消化660错题", "content": "把做错的题归类：是概念不清？计算失误？还是题意理解偏差？", "hours": 18},
             {"title": "真题研读", "content": "2012年英二阅读。生词本应该越来越厚了，每天复习前一天的生词。", "hours": 10})

    add_week(27, "🏹 真题一轮：高数上篇 (1)", 
             "终于开始做真题了！《真题一本通》按章节来的。先做每章的计算题。",
             {"title": "真题一本通：第1章", "content": "函数极限的真题。你会发现真题的套路其实比模拟题清晰。", "hours": 20},
             {"title": "真题研读", "content": "2013年英二阅读。注意分析长难句，不用特意学语法，读懂结构就行。", "hours": 10})

    add_week(28, "🏹 真题一轮：高数上篇 (2)", 
             "导数和中值定理的真题。证明题只看真题里的，其他不看。",
             {"title": "真题一本通：第2-3章", "content": "对于证明题，尝试默写逻辑链条：‘构造F(x) -> 用罗尔定理 -> 得证’。", "hours": 20},
             {"title": "真题研读", "content": "2014年英二阅读。正确率不重要，看懂最重要。", "hours": 10})

    add_week(29, "🏹 真题一轮：高数下篇 (1)", 
             "积分真题。计算量通常比较大，一定算到底，别眼高手低。",
             {"title": "真题一本通：第4章", "content": "不定积分和定积分的计算。注意奇偶性、周期性在定积分里的应用。", "hours": 20},
             {"title": "真题研读", "content": "2015年英二阅读。开始体会出题人的干扰项设置，是偷换概念还是无中生有？", "hours": 10})
    
    # ================= 巩固于突破 (Week 30-36) =================

    add_week(30, "🏹 真题一轮：高数下篇 (2)", 
             "微方和多元。真题里微方通常送分，多元积分大题是硬骨头。",
             {"title": "真题一本通：第5-6章", "content": "把所有考过的二重积分大题都刷一遍，总结一下有几种换元方式。", "hours": 20},
             {"title": "真题研读", "content": "2016年英二阅读。", "hours": 10})

    add_week(31, "🏹 真题一轮：线代全篇", 
             "线代真题往往综合性很强，一道题考半本书。",
             {"title": "真题一本通：线代部分", "content": "重点做方程组和特征值的大题。注意第一问证概念，第二问算结果的套路。", "hours": 20},
             {"title": "真题研读", "content": "2017年英二阅读。感受一下近十年的难度变化。", "hours": 10})

    add_week(32, "🏹 真题一轮：查漏补缺", 
             "一本通刷完了？把错题整理到你的‘终极错题本’上。",
             {"title": "复盘真题错题", "content": "这些错题是你之后冲刺阶段的复习核心。分类整理。", "hours": 18},
             {"title": "真题研读", "content": "2018年英二阅读。", "hours": 10})

    add_week(33, "🔄 二刷启动：大观", 
             "现在你做过真题了，再回看澄箫宇的大观，会有新体会。",
             {"title": "二刷大观：高数部分", "content": "倍速播放。重点看之前没懂的，以及他讲的‘秒杀技巧’在真题里能不能用。", "hours": 18},
             {"title": "真题研读", "content": "2019年英二阅读。", "hours": 10})

    add_week(34, "🔄 二刷启动：线代", 
             "线代大观二刷。这一遍要达到‘从头推到尾’的境界。",
             {"title": "二刷大观：线代部分", "content": "特别是二次型化标准型那块，再熟练一下配方法。", "hours": 18},
             {"title": "真题研读", "content": "2020年英二阅读。", "hours": 10})

    add_week(35, "🧱 专题突破：弱项特训", 
             "你自己最怕哪块？极限？中值？还是级数（哦数二不考）？这周专门治它。",
             {"title": "弱项攻坚", "content": "回到1000题或者一本通，专门找你怕的章节，集中火力再刷20题。", "hours": 18},
             {"title": "真题研读", "content": "2021年英二阅读。", "hours": 10})

    add_week(36, "🧱 专题突破：计算特训", 
             "后期最大的敌人是‘算不对’。每天抽半小时专门算复杂的定积分。",
             {"title": "计算力特训", "content": "找那种步骤很多的题，盖住答案算，算不对不吃饭。", "hours": 18},
             {"title": "作文启动", "content": "Monkey作文课启动！只听课，背他的‘功能段落’模板。不用全篇背。", "hours": 10})

    # ================= 政治启动 & 冲刺 (Week 37-48) =================

    add_week(37, "🚩 政治上线：马原", 
             "10月中旬了，政治该进场了。不用买精讲精练，直接上背诵手册。",
             {"title": "政治启动", "content": "腿姐手册-马原部分。马原重点是理解原理（对立统一、质量互变）。苍盾小程序每天刷30题。", "hours": 6},
             {"title": "持续保温", "content": "数学每天复习错题，保持手感。英语2022年阅读。", "hours": 20})

    add_week(38, "🚩 政治推进：史纲/毛中特", 
             "史纲有时间轴，毛中特跟着新大纲走。",
             {"title": "腿姐手册刷题", "content": "重点背史纲的时间线。苍盾小程序刷对应章节的选择题。", "hours": 6},
             {"title": "数学套卷准备", "content": "整理好09-26年的真题试卷。下周开始实战。", "hours": 20},
             {"title": "英语", "content": "2023年阅读。作文开始动笔写，每周套用模板写一篇。", "hours": 6})

    add_week(39, "🏁 冲刺实战：真题套卷(1)", 
             "真题套卷每天一套，严格限时！早晨8:30-11:30，雷打不动！",
             {"title": "数二真题 09-14", "content": "做完立刻批改。分数不重要，重要的是适应3小时高强度思考。", "hours": 22},
             {"title": "英语/政治", "content": "英语作文练手写。政治每天刷苍盾选择题，吃饭时候看。", "hours": 8})

    add_week(40, "🏁 冲刺实战：真题套卷(2)", 
             "这几年的真题比较有参考价值。注意时间分配，选填控制在45分钟内。",
             {"title": "数二真题 15-20", "content": "分析错题：是因为紧张？还是知识盲区？", "hours": 22},
             {"title": "英语/政治", "content": "英语2024年阅读。政治熟读澄箫宇‘政治一页纸’，抓核心考点。", "hours": 8})

    add_week(41, "🏁 冲刺实战：真题套卷(3)", 
             "近年的题难度较大（除了25年较简单）。被虐也别哭，模拟考场心态。",
             {"title": "数二真题 21-25", "content": "2024和2025年的卷子留着最后考前一周全真模拟。", "hours": 22},
             {"title": "英语/政治", "content": "英语2025年阅读。政治腿姐手册多翻翻，选择题要稳住35分+。", "hours": 8})

    add_week(42, "📝 模拟冲刺：李林六套卷(1)", 
             "李林的卷子预测性很强，但计算量大。可能会做不完，正常。",
             {"title": "李林六套卷 1-3", "content": "做完认真看解析，李林的解析里有很多补充的生僻考点。", "hours": 22},
             {"title": "作文背诵", "content": "英语大作文、小作文模板各背熟一套万能的。", "hours": 8})

    add_week(43, "📝 模拟冲刺：李林六套卷(2)", 
             "继续磨练。这时候你会觉得很累，咬牙坚持。",
             {"title": "李林六套卷 4-6", "content": "总结这六套卷子里的新题型。", "hours": 22},
             {"title": "政治背诵", "content": "肖八出来了！只做选择题！大题不用背！选择题把每个选项都搞懂。", "hours": 8})

    add_week(44, "📝 模拟冲刺：李林四套卷", 
             "四套卷是精华。必须认真对待。",
             {"title": "李林四套卷", "content": "当成正式考试做。查漏补缺的最后机会。", "hours": 22},
             {"title": "政治选择", "content": "二刷肖八选择题。苍盾上刷各个名师的押题卷选择题。", "hours": 8})

    add_week(45, "🔧 技巧回归：选填特训", 
             "最后阶段，得选填者得天下。看武忠祥的选填技巧课。",
             {"title": "武忠祥技巧课", "content": "学会赋值法、排除法、几何法。能不算就不算，能秒杀就秒杀。", "hours": 18},
             {"title": "政治大题", "content": "肖四来了！背！背前两套也是背！", "hours": 12})
             
    add_week(46, "🔧 技巧回归：错题温习", 
             "别做新题了。把这一年所有的错题本拿出来。",
             {"title": "终极复盘", "content": "看着错题想思路，不用每道都算。确保以前的坑不再踩。", "hours": 18},
             {"title": "政治大题", "content": "肖四背诵进行时。学会B站‘抄材料’技巧，万一没背到也能编。", "hours": 12})

    add_week(47, "🎯 考前演练：全真模拟", 
             "最后一周！调整作息，按考试时间（上午数学下午英语）模考。",
             {"title": "24/25年真题模考", "content": "留的那两套真题拿出来，完全模拟考场环境。做完给自己打个分，树立信心。", "hours": 18},
             {"title": "政治最后抱佛脚", "content": "狂背肖四。英语背一下作文模板。", "hours": 12})

    add_week(48, "🧘‍♀️ 考试周：心态调整", 
             "这一周，放松。你已经准备好了。去考场是去拿录取通知书的。",
             {"title": "回归课本", "content": "翻翻公式，看看目录。不要做难题了。保证睡眠。", "hours": 10},
             {"title": "必胜", "content": "准备好准考证、文具。周六周日，你可以的！", "hours": 5})

    return weeks

def generate_custom_word_doc(plan):
    html = """
    <html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word' xmlns='http://www.w3.org/TR/REC-html40'>
    <head>
        <meta charset="utf-8">
        <title>汪桑 2026考研全程定制规划</title>
        <style>
            body { font-family: 'SimSun', 'Microsoft YaHei', sans-serif; }
            h1 { text-align: center; color: #333; }
            .info { text-align: center; color: #666; margin-bottom: 30px; }
            .week-block { border: 1px solid #ccc; padding: 15px; margin-bottom: 20px; box-shadow: 2px 2px 5px #eee; }
            .week-header { background: #f4f6f9; padding: 10px; font-weight: bold; border-bottom: 1px solid #ddd; }
            .msg { background: #fffbe6; padding: 10px; margin: 10px 0; border-left: 3px solid #f39c12; color: #555; }
            table { width: 100%; border-collapse: collapse; }
            td { padding: 8px; border-bottom: 1px solid #eee; vertical-align: top; }
            .sub-name { width: 15%; font-weight: bold; color: #0056b3; }
            .sub-content { width: 75%; }
            .sub-hours { width: 10%; text-align: right; color: #999; }
        </style>
    </head>
    <body>
        <h1>汪桑 2026考研全程定制规划</h1>
        <div class="info">
            <p>目标院校：中山大学 (085700) | 目标分数：330分</p>
            <p>规划周期：48周 (2026.01.19 - 2026.12.20)</p>
        </div>
    """
    
    for week in plan:
        html += f"""
        <div class="week-block">
            <div class="week-header">第 {week['week']} 周：{week['theme']}</div>
            <div class="msg">💡 指导建议：{week['message']}</div>
            <table>
                <tr>
                    <td class="sub-name">📐 数学</td>
                    <td class="sub-content">
                        <strong>{week['math']['title']}</strong><br/>
                        {week['math']['content']}
                    </td>
                    <td class="sub-hours">{week['math']['hours']}h</td>
                </tr>
                <tr>
                    <td class="sub-name">📖 英语</td>
                    <td class="sub-content">
                        <strong>{week['english'].get('title', '')}</strong><br/>
                        {week['english']['content']}
                    </td>
                    <td class="sub-hours">{week['english'].get('hours', '')}h</td>
                </tr>
        """
        if week['politics']['content'] != "暂不复习":
            html += f"""
                <tr>
                    <td class="sub-name">🏛️ 政治</td>
                    <td class="sub-content">
                        <strong>{week['politics'].get('title', '')}</strong><br/>
                        {week['politics']['content']}
                    </td>
                    <td class="sub-hours">{week['politics'].get('hours', '')}h</td>
                </tr>
            """
        if week['professional']['content'] != "自行安排 (建议每周5h)":
             html += f"""
                <tr>
                    <td class="sub-name">📚 专业课</td>
                    <td class="sub-content">{week['professional']['content']}</td>
                    <td class="sub-hours">5h</td>
                </tr>
            """
        html += "</table></div>"
        
    html += "</body></html>"
    
    with open(r'd:\myblog\source\kaoyan\wangsang_custom_v2.doc', 'w', encoding='utf-8') as f:
        f.write(html)

def generate_json(plan):
    with open(r'd:\myblog\source\kaoyan\wangsang_detail_v2.json', 'w', encoding='utf-8') as f:
        json.dump({"student": "汪桑", "weeks": plan}, f, ensure_ascii=False)

if __name__ == "__main__":
    plan = get_full_plan()
    generate_custom_word_doc(plan)
    generate_json(plan)
    print("Full customized plan generated.")
