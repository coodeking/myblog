# -*- coding: utf-8 -*-
import json
from datetime import datetime, timedelta

def get_full_plan_libaibai():
    weeks = []
    start_date = datetime(2026, 3, 5)
    
    def get_date_str(week_idx):
        s = start_date + timedelta(days=(week_idx-1)*7)
        e = s + timedelta(days=6)
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
        if pol:
            week_data["politics"] = pol
        weeks.append(week_data)

    # ================= 基础阶段：高数 (Week 1-6) =================
    
    add_week(1, "高数基础：极限与连续", 
             "备考初期切忌自我感动式学习，必须以‘能做对题’为唯一标准。极限是微积分的基石，计算不熟练，后面寸步难行。",
             {"title": "张宇30讲：第1-2讲 + 1000题", "content": "🚫 避坑指南：坚决不看张宇基础课，太废时间！直接做30讲课后题+1000题基础篇。\n✅ 核心点：重点攻克泰勒公式和等价无穷小。遇到不会的去B站搜‘1000题讲解’（千羽、考研数学777等）。", "hours": "占大盘60%"},
             {"title": "死磕单词", "content": "✅APP锁定：《不背单词》。\n只背考研核心词（约3000个）。每天雷打不动背单词，一遍遍过，直到产生肌肉记忆。", "hours": "占大盘30%"})

    add_week(2, "高数基础：导数与微分", 
             "这周开始啃硬骨头。遇到卡壳的知识点直接去B站搜播放量高的干货UP主，这往往比大几十小时的网课更直接有效。",
             {"title": "张宇30讲：第3-5讲 + 1000题", "content": "✅ 核心任务：完成导数对应课后题和1000题。\n⚠️ 注意：张宇的‘超实数’、微分算子法、stolz法则，目标150的也不需要学！直接跳过！不会的题赶紧去B站看讲解。", "hours": "占大盘60%"},
             {"title": "疯狂单词", "content": "英语不需要手译本精翻，效率极低！把时间花在核心词汇重复记忆上，每天滚动。", "hours": "占大盘30%"})

    add_week(3, "高数基础：中值定理与一元积分", 
             "中值定理证明题极难，但不用怕！所有习题册的证明题一律直接划掉不做！我们只在真题阶段死磕证明题。",
             {"title": "张宇30讲：第6-8讲 + 1000题", "content": "✅ 核心任务：完成课后题和对应1000题。\n💡 技巧：积分没有捷径，就是大量刷题凑微分。如果做两分钟没思路，毫不犹豫跳过看答案订正！", "hours": "占大盘60%"},
             {"title": "疯狂单词", "content": "坚持住。遗忘是正常的，只管闭眼刷《不背单词》，暑假前最好刷三遍！", "hours": "占大盘30%"})

    add_week(4, "高数基础：定积分及其应用", 
             "定积分不仅是计算，更是后面二重积分的基础。变上限积分求导是必考重点，必须练到肌肉记忆。",
             {"title": "张宇30讲：第9-12讲 + 1000题", "content": "✅ 核心任务：完成定积分与应用部分的习题。\n⚠️ 重点警示：变上限积分函数的求导结合极限经常考，必须拿下！不会的直接看B站切片。", "hours": "占大盘60%"},
             {"title": "疯狂单词", "content": "持续用APP刷核心词。不要精翻文章，不买手译本！", "hours": "占大盘30%"})

    add_week(5, "高数基础：微分方程与多元微分", 
             "多元微分要把一元微分的降维打击运用好。微分方程属于送分题，记住表格套路就行。",
             {"title": "张宇30讲：第13-17讲 + 1000题", "content": "✅ 核心任务：完成对应课后题和1000题。\n💡 方法：微分方程特解设法的表格必须死记硬背。偏导数链式求导法则画树状图解决。", "hours": "占大盘60%"},
             {"title": "疯狂单词", "content": "不要被别人的进度干扰。考研英语少听课或者不听课，背好单词就赢了一半。", "hours": "占大盘30%"})

    add_week(6, "高数基础：二重积分与无穷级数", 
             "二重积分是计算量的试金石；级数是数一的专属难点（数二不考）。但也不要怕，级数判敛有固定套路。",
             {"title": "张宇30讲：第18-20讲 + 1000题", "content": "✅ 任务：完成二重积分和级数的习题。\n⚠️ 避坑：海涅定理绝对不看！级数求和函数计算量极大，做错了也要完整订正一遍步骤。", "hours": "占大盘60%"},
             {"title": "疯狂单词", "content": "第一轮核心词汇即将过半。继续坚持雷打不动。", "hours": "占大盘30%"})

    # ================= 基础阶段：线代 (Week 7-10) =================
    
    add_week(7, "线代基础：行列式与矩阵", 
             "线代与高数不同，它更侧重逻辑。初等变换是线代的灵魂。记得给自己留出专业课的复习时间！",
             {"title": "三十讲线代(1-3讲) + 1000题", "content": "✅ 任务：课后题+1000题基础。\n🚫 还是那句话：不看冗长的课！不懂直接去B站搜单点讲解。多想多算！", "hours": "占大盘60%"},
             {"title": "疯狂单词", "content": "继续背单词。词汇量是考研阅读的唯一底气。", "hours": "占大盘30%"})

    add_week(8, "线代基础：向量与方程组", 
             "方程组的解与向量的线性相关性是线代的心脏，也是最难理解的地方。画图，联想矩阵的秩！",
             {"title": "三十讲线代(4-5讲) + 1000题", "content": "✅ 任务：课后题+1000题基础。\n💡 核心：这部分错的多不要紧，整理在错题本上，后面强化看视频自然就通透了。", "hours": "占大盘60%"},
             {"title": "疯狂单词", "content": "单词第一遍快刷完了吧？准备进入二刷。", "hours": "占大盘30%"})

    add_week(9, "线代基础：特征值与二次型", 
             "这是线代大题的高频考点。实对称矩阵必可对角化是金钥匙，配方法化标准型必须熟练。",
             {"title": "三十讲线代(6讲) + 1000题", "content": "✅ 任务：完成线代最后一部分习题。\n⚠️ 注意：计算施密特正交化极容易错，必须要落到笔头上亲自算到底！", "hours": "占大盘60%"},
             {"title": "疯狂单词", "content": "开启第二轮背诵。把不会的词挑出来反复死磕。", "hours": "占大盘30%"})

    add_week(10, "线代复盘与消化", 
             "这周暂停推进新知识，把前面线代做错的题全部重新算一遍。别把自己当只进不出的听课机器。",
             {"title": "整理错题", "content": "✅ 任务：重做线代错题。\n根据错题去针对性地找B站视频看，哪里不会看哪里。", "hours": "占大盘60%"},
             {"title": "疯狂单词", "content": "继续二刷单词。速度要提升上来。", "hours": "占大盘30%"})

    # ================= 基础阶段：概率论 (Week 11-13) =================

    add_week(11, "概率基础：随机事件与一维变量", 
             "概率论（数一考，数二不考）极度套路。只要把高数的积分算对，概率论就是送分题。",
             {"title": "三十讲概率(1-3讲) + 1000题", "content": "✅ 任务：完成前三讲及对应1000题。\n⚠️ 原则：全科保持以练带学，只做计算，不论习题册多难，证明题直接打叉！", "hours": "占大盘60%"},
             {"title": "疯狂单词", "content": "继续刷单词。遇到总忘的钉子户，截图做锁屏。", "hours": "占大盘30%"})

    add_week(12, "概率基础：多维变量与数字特征", 
             "这是概率论的大题命题重灾区，本质上就是考二重积分。算不对说明高数没学好。",
             {"title": "三十讲概率(4-5讲) + 1000题", "content": "✅ 任务：完成课后题+对应1000题。\n💡 核心：协方差、相关系数的公式必须倒背如流。各种分布的期望方差也要记住。", "hours": "占大盘60%"},
             {"title": "疯狂单词", "content": "坚持！每天看一半新词加一半旧词。", "hours": "占大盘30%"})

    add_week(13, "概率基础：大数定律与参数估计", 
             "参数估计（最大似然估计和矩估计）是数一的死板大题。记住套路：求导、令为0、解方程。",
             {"title": "三十讲概率(6讲) + 复盘", "content": "✅ 任务：完成概率论收尾。重做所有错题。\n此时，你的数学三大模块（高数+线代+概率）基础全部跑完一轮！", "hours": "占大盘60%"},
             {"title": "疯狂单词", "content": "暑假前完成单词三遍的目标就快实现了。", "hours": "占大盘30%"})

    # ================= 强化阶段：大观与660 (Week 14-18) =================

    add_week(14, "强化起航：澄箫宇大观（上）", 
             "要开启大观了！请死死记住：大观里包含基础知识点+大量绝杀讲题，必须按正确姿势看！",
             {"title": "大观系列：高数部分", "content": "✅ 任务：约两天看一个大观（目前共7个）。\n🔥 核心绝杀：他讲每道题之前，你必须按暂停键！自己在草稿纸上做一遍！然后再放视频听他讲！", "hours": "占大盘60%"},
             {"title": "疯狂单词", "content": "继续狂背！词汇量不够，后面真题根本读不懂。", "hours": "占大盘30%"})

    add_week(15, "强化推进：澄箫宇大观（下）", 
             "大观不仅是知识，是教你怎么站在出题人的视角看坑。这些精选例题往往包含极深的方法论。",
             {"title": "大观系列：线代/概率部分", "content": "✅ 任务：继续看大观系列。\n💡 重点：把视频里让你“顿悟”的思路记在笔记本上。这些是后续解真题的利器。", "hours": "占大盘60%"},
             {"title": "疯狂单词", "content": "坚持背单词。背到看到英文就条件反射出中文意思就行。", "hours": "占大盘30%"})

    add_week(16, "速刷利器：660题高数", 
             "开始刷660选择填空了。记住‘速刷’的奥义：发现知识盲区，而不是死磕一道难题浪费半天。",
             {"title": "660题一阶速刷：高数", "content": "✅ 任务：高数部分速刷！\n⚠️ 速刷法则：第一遍只做会做的，如果一道题2分钟没思路，毫不犹豫看答案对答案订正！", "hours": "占大盘60%"},
             {"title": "英语大转折：启动真题", "content": "✅ 两天一套英一真题（先不写作文）。\n强烈推荐下载《真题伴侣》（建议充会员）！把真题里不会的词在App里重点背生僻词义。", "hours": "占大盘30%"})

    add_week(17, "速刷利器：660题线代/概率", 
             "这周数学继续填坑。660题做错一大半都是正常的，因为它的考察视角极度刁钻。错题做好标记。",
             {"title": "660题一阶速刷：线代+概率", "content": "✅ 任务：完成线代和概率的速刷。\n💡 建议：把660里涉及到的概念辨析（比如极限存在与连续的关系）单独记下来。", "hours": "占大盘60%"},
             {"title": "英一真题推进", "content": "✅ 保持两天一套真题阅读。\n期间《不背单词》不能停！英语的核心只有：真题阅读+背单词。", "hours": "占大盘30%"})

    add_week(18, "660题错题消化", 
             "速刷收尾阶段。别纠结正确率，纠结的是这道错题背后你忘了哪个基本定理。认真订正错题。",
             {"title": "整理660错题", "content": "✅ 任务：把660跳过的、做错的题目重做一遍。\n准备下周迎接整个考研最核心的神秘武器。", "hours": "占大盘60%"},
             {"title": "背单词+真题阅读", "content": "不要精翻文章！只要逻辑读顺，能把题目做对即可。生词继续在《真题伴侣》里记。", "hours": "占大盘30%"})

    # ================= 真题一轮：一本通 (Week 19-25) =================

    add_week(19, "真题封神：《真题一本通》第1卷", 
             "《真题一本通》降临！这就是你整个备考期最核心的宝贝（于文涛编），没有之一。",
             {"title": "一本通：高数（极限/导数）", "content": "✅ 核心任务：彻底搞懂每一道真题！\n⚠️ 铁律：搞个专属厚错题本，真题错题按章节分类。这本错题本就是你上岸的通行证。", "hours": "占大盘60%"},
             {"title": "英一真题+作文启动", "content": "✅ 继续刷真题。\n✅ 听Monkey老师考研作文模板课。只需要背他的模板，不需要自己憋句子！", "hours": "占大盘30%"})

    add_week(20, "真题封神：《真题一本通》第2卷", 
             "真题是最强武器！所有习题册和模拟卷的证明题可以直接丢，我们只死磕这本书里的真题证明题！",
             {"title": "一本通：高数（积分/微方）", "content": "✅ 核心任务：以计算大题为重。\n💡 遇到不懂的知识点，直接去B站搜这个知识点的全网最高播放讲解视频，比大机构老师好！", "hours": "占大盘60%"},
             {"title": "英一真题+背模板", "content": "除了刷阅读，平时开始积累Monkey作文课里的“主题词”，确保每种话题都有词可用。", "hours": "占大盘30%"})

    add_week(21, "真题封神：《真题一本通》第3卷", 
             "真题计算量往往极大，一道二重积分可能让你算两页纸。不要看一眼思路感觉会了就跳，必须算！",
             {"title": "一本通：高数（多元/级数）", "content": "✅ 核心任务：死磕多元微分和级数真题。\n尤其是数一独有的曲线曲面积分（格林、高斯、斯托克斯），多算多练熟悉套路。", "hours": "占大盘60%"},
             {"title": "英一真题+背单词", "content": "单词不能断。英语一出题人特别喜欢生僻义熟词（如 game 考猎物），重点记真题释义。", "hours": "占大盘30%"})

    add_week(22, "真题封神：《真题一本通》第4卷", 
             "一本通体量极大，要有心理准备。遇到卡壳是很正常的，记在错题本上，这都是提分的养料。",
             {"title": "一本通：线代真题", "content": "✅ 核心任务：线代真题。\n线代真题综合性极强，往往一道题把方程组和二次型全考一遍，总结大题的固定命题轨迹。", "hours": "占大盘60%"},
             {"title": "英一真题", "content": "阅读正确率如果不高别慌，分析出题人的挖坑思路（偷换概念、强加因果等）。", "hours": "占大盘30%"})

    add_week(23, "真题封神：《真题一本通》第5卷", 
             "概率论真题一旦你跨过微积分的计算门槛，其实非常简单。把真题模板提取出来就能拿满。",
             {"title": "一本通：概率真题", "content": "✅ 核心任务：概率真题。\n最大似然估计每年必考，它的求导计算量也大，一定要算到最后一行得数才算对。", "hours": "占大盘60%"},
             {"title": "英一真题", "content": "阅读继续保持节奏。作文模板应该已经能熟练背诵了。", "hours": "占大盘30%"})

    add_week(24, "真题封神总结：错题重构", 
             "这几天是不是感觉有点疲了？撑住。第一轮真题刷完，这段时间正是拉开差距的分水岭，坚决不放松。",
             {"title": "整理一本通错题本", "content": "✅ 任务：把前期分类的错题本拿出来，把不会的题遮住答案再算一遍。\n错题里反映出来的知识漏洞，去B站看相关点补齐。", "hours": "占大盘60%"},
             {"title": "英一二刷准备", "content": "前期早年真题如果刷完了，可以准备二刷近年真题错的题。", "hours": "占大盘30%"})

    add_week(25, "大观降临：二刷大观", 
             "二刷澄箫宇大观！这次你看视频的视角完全不一样了，因为你被真题毒打过了，会觉得这些技巧都是神技。",
             {"title": "大观二刷：高数+线代+概率", "content": "✅ 任务：带着前期的磨砺重看大观系列。\n💡 重点：串联你的知识点网络，寻找顿悟时刻。看他怎么用秒杀技巧解决真题里的坑。", "hours": "占大盘60%"},
             {"title": "英语真题错题二刷", "content": "对阅读错题重新做，看自己是不是又被同一个坑绊倒了。", "hours": "占大盘30%"})

    # ================= 二轮真题与冲刺 (Week 26-38) =================

    add_week(26, "二轮真题：套卷训练", 
             "散题做完，开始套卷！数学一每天来一套09-26年真题套卷。开始接触完整3小时的高压实战。",
             {"title": "数一真题成套刷（1）", "content": "✅ 任务：每天一套 09-26 年数一真题。\n⚠️ 要求：哪怕算得头昏脑涨，也要定时写完！并把卷子错的题，对应浓缩补充到你的专属病历（错题本）里。", "hours": "占大盘60%"},
             {"title": "练熟模板", "content": "把背下来的Monkey模板往历年真题的话题里强行套写，多练手感。", "hours": "占大盘30%"})

    add_week(27, "二轮真题：套卷训练", 
             "错题本开始发挥绝对威力。把多套历年真题卷子上重复做错的同类题圈在一起，它就是你的死穴，专门攻克。",
             {"title": "数一真题成套刷（2）", "content": "✅ 任务：继续每天一套套卷。\n💡 核心：这期间如果遇到不会的冷门证明，再去对照大观或者去B站找解析。", "hours": "占大盘60%"},
             {"title": "练熟模板+单词", "content": "别忘了单词不能断。一天不背单词就倒退。", "hours": "占大盘30%"})

    add_week(28, "二轮真题：套卷训练", 
             "套卷练习结束。历年真题已经被你吃干抹净了。现在的你，底盘已经足够扎实稳固。",
             {"title": "数一真题成套刷（3）", "content": "✅ 任务：真题收尾并整理全部错题。\n为下周极其折磨人的李林模拟卷留足心理预期。", "hours": "占大盘60%"},
             {"title": "英语二刷错题", "content": "持续。英语进入冲刺的平稳期。", "hours": "占大盘30%"})

    add_week(29, "全真模拟：李林6套卷", 
             "这周上了李林卷，肯定会被虐得很惨。别在意分数，李林卷子本来就是让你在考场上见到新题恶心题不慌的预演。",
             {"title": "李林6+4（李6部分）", "content": "✅ 任务：每天做一套李林模拟卷。\n⚠️ 核心铁律：严格控制时间！同样，模拟卷的证明题一！律！不！看！只做计算选填。", "hours": "占大盘60%"},
             {"title": "练熟模板", "content": "保持作文每周手写两篇的频率以保证卷面工整。", "hours": "占大盘30%"})

    add_week(30, "全真模拟：李林4套卷", 
             "哪怕考60、70分也别放弃，认真把李林的错点吸收掉。这10套里的技巧能极大概率押中真题逻辑。",
             {"title": "李林6+4（李4部分）", "content": "✅ 任务：完成李林最后的几套神卷。\n💡 建议：李林错题本额外建立，和真题错题本放在一起并排复习。", "hours": "占大盘60%"},
             {"title": "英语真题", "content": "维持阅读手感，每天读一篇阅读文章，不用多做题，就当小说看。", "hours": "占大盘30%"})

    add_week(31, "政治启动：腿姐与苍盾", 
             "政治终于进场！请严守纪律：不看徐涛长视频，也别碰肖1000这样海量没价值的刷题！",
             {"title": "技巧课与错题本", "content": "✅ 任务：回归真题+李林错题本！\n啃这俩本神仙错题的骨头是最香的！配合看武忠祥【选填技巧课】，各种特值法安排上！", "hours": "占大盘60%"},
             {"title": "英语真题", "content": "保持语感。死守核心词。", "hours": "占大盘20%"},
             {"title": "政治启动（10月初）", "content": "🚫 远离徐涛冗长课，远离肖1000题！\n✅ 买《腿姐冲刺背诵手册》，只要求熟读。\n✅ 上下班通勤去刷《苍盾小程序》，每天一套30个选择即可。", "hours": "占大盘10%"})

    add_week(32, "抢分组合拳：选填特训", 
             "武忠祥选填技巧课加上你的错题本，这就是考前最核心的‘抢分组合拳’。选填往往是拉开差距的关键。",
             {"title": "武忠祥选填技巧课继续", "content": "✅ 任务：继续刷技巧课和啃老错题。\n把图形法、极限保号性等能秒速解选择题的绝学练成了化境。", "hours": "占大盘60%"},
             {"title": "英语真题", "content": "保证模板烂熟于胸。", "hours": "占大盘20%"},
             {"title": "政治背诵+刷题", "content": "✅ 腿姐手册继续背，苍盾小程序继续刷。花的时间很少，收益很高。", "hours": "占大盘10%"})

    add_week(33, "政治蓄力：一页纸", 
             "这几天加上“政治一页纸”。这东西浓缩度极高，往往能正中红心，省掉大笔记翻来翻去的时间。",
             {"title": "啃最后两本错题", "content": "✅ 任务：错题本进入二刷三刷状态。\n看到题就能条件反射出要用拉格朗日还是用极坐标。", "hours": "占大盘60%"},
             {"title": "英语真题+背单词", "content": "单词不能断。背到考场大门关上的一刻。", "hours": "占大盘20%"},
             {"title": "政治诵读", "content": "✅ 熟读澄箫宇“政治一页纸”。每天只花极少的时间但重在天天看。", "hours": "占大盘10%"})

    add_week(34, "近三年真题复位", 
             "进入考前倒计时！严禁去搞没见过的新杂牌怪题。重温近3年的真题，这是最原汁原味的考风。",
             {"title": "近三年真题重刷（1）", "content": "✅ 任务：找崭新的试卷，重做近3年真题。\n找那种真实考场的压迫感，严格卡三个小时计时闭卷。", "hours": "占大盘60%"},
             {"title": "默写作文", "content": "买答题卡，像考试一样默写作文模板，看自己字迹和拼写有没有严重问题。", "hours": "占大盘20%"},
             {"title": "政治刷题", "content": "苍盾选择套卷继续保持手感。很多选择题考的是眼熟，错多了别在意。", "hours": "占大盘10%"})

    add_week(35, "近三年真题复位", 
             "这几年的数学一难度波动大但逻辑同源，如果能把它们做得如丝般顺滑，你上场绝对不慌。",
             {"title": "近三年真题重刷（2）", "content": "✅ 任务：继续刷这几套原卷，然后重点看卷子上的错点。\n并翻阅自己的真题本/模拟本错题集。", "hours": "占大盘60%"},
             {"title": "练真题阅读", "content": "不要让手生，必须保证每天还能解构一两篇长难句，找到答案出处。", "hours": "占大盘20%"},
             {"title": "政治等肖四大作", "content": "这几天选择题已经刷腻了，暴风雨前的宁静，等神级大作肖四出版。", "hours": "占大盘10%"})

    add_week(36, "错题反刍：不动新题", 
             "把以前错的计算题拿出来，不看答案，重新在一张白纸上算到底。计算的手感在这个节骨眼绝不能凉。",
             {"title": "绝不碰新题，只啃错题本", "content": "✅ 任务：除了近3年卷之外不再开新卷子。\n不断翻错题本，如果还有生僻知识点死活不懂，果断放弃（不含常考重磅核心）。", "hours": "占大盘60%"},
             {"title": "英语全真模拟", "content": "全科三小时卡点做一套英语，看看自己分配给作文阅读的时间是否合理。", "hours": "占大盘20%"},
             {"title": "政治死等肖四", "content": "继续读腿姐和一页纸，保持基础得分率。", "hours": "占大盘10%"})

    add_week(37, "死磕肖四", 
             "肖四终于来了！拿到手别废话，直接看大题的加粗黑体字开背，政治的背诵决战拉开帷幕。",
             {"title": "维持计算手感", "content": "✅ 任务：每天挑几道积分、微分方程或者二次型的题硬算算得数。\n保证在考前不出任何计算偏差。", "hours": "占大盘50%"},
             {"title": "英语单词+模板", "content": "每天保持。你的作文模板应该达到下笔肌肉记忆的程度了。", "hours": "占大盘20%"},
             {"title": "政治：死背肖四大题", "content": "✅ 核心狂暴任务：拿到《肖四》之后，死背它的大题标准答案（黑体部分）！", "hours": "占大盘30%"})

    add_week(38, "抄材料绝学", 
             "这周务必去B站看懂‘考研政治抄材料’技巧！一旦遇到完全没见过的肖四题，就靠这绝招拿保底分。",
             {"title": "回顾总结", "content": "✅ 任务：随便翻看错题本，大脑里推导过程就行。\n不要过度消耗精力了，以保持心态平稳为主。", "hours": "占大盘40%"},
             {"title": "英语阅读手感", "content": "就当看杂志一样看看英语短文。", "hours": "占大盘20%"},
             {"title": "政治：抄材料神技", "content": "🔥 必杀技：背不下肖四别焦虑（背不住影响不大）！务必去B站搜‘考研政治抄材料’，学会绝杀！上了考场基本都要用。 ", "hours": "占大盘40%"})

    add_week(39, "调整作息", 
             "最后一周，调作息、看考点、准备文具。不要再纠结某一道偏执的难题。兄弟，这一趟走到底，绝对岸上见！",
             {"title": "复位基础公式", "content": "✅ 任务：对着大纲，把牛顿莱布尼兹、泰勒、各种求导表、随机事件概率公式全写一遍！\n上考场要是公式忘了那才叫痛苦。", "hours": "占大盘40%"},
             {"title": "英语最后检查", "content": "检查模板拼写不要出错。", "hours": "占大盘20%"},
             {"title": "政治肖四终结", "content": "不管会不会，考场上去疯狂抄材料和写背过的那些话术。", "hours": "占大盘40%"})
             
    # Fill remaining 2 weeks explicitly as "考前冲刺周补充" to reach 41
    add_week(40, "最后冲刺（一）", 
             "保持心态是最好的答卷。不要再为了模拟题的低分懊恼了，真正的考试没那么变态。",
             {"title": "保持计算手感", "content": "每天算一道最套路的多维概率或者级数大题找感觉即可。", "hours": "最后保温"},
             {"title": "英语模板收尾", "content": "看看有无遗漏大小写、标点格式。", "hours": "最后保温"},
             {"title": "政治背诵收尾", "content": "再瞄一眼腿姐背诵手册的目录树。", "hours": "最后保温"})

    add_week(41, "最后冲刺（二）：考场见！", 
             "尽人事，听天命。所有试卷和错题都已经吃干抹净，带着它们上战场去兑换属于你的分数！",
             {"title": "心态调整", "content": "什么题都不做了。确认身份证、准考证、文具笔套。\n上了考场死死咬住算完！你可以的！", "hours": "全力以赴"},
             {"title": "英语必胜", "content": "自信上场，按分配好的顺序答题。", "hours": "全力以赴"},
             {"title": "政治必胜", "content": "疯狂书写，直到交卷铃声响起。", "hours": "全力以赴"})

    data = {"student": "李白白", "weeks": weeks[:41]}
    
    with open("D:/myblog/source/kaoyan/李白白/libaibai.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    html_template = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>李白白 2027考研全程深度定制规划</title>
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
            <h1>李白白 2027考研全程深度定制规划</h1>
            <div class="meta">
                <span>🎯 南京邮电大学·物联网学院</span>
                <span>📅 周期：2026.03.05 - 2026.12 考前 (共41周)</span>
            </div>
            <div class="meta" style="margin-top: 8px;">
                <span>📚 必考：数学一 / 英语一 / 政治 / 统考专业课</span>
            </div>
        </header>

        <!-- 总体规划概览 -->
        <div class="overview">
            <h2>🎯 全局时间红线与死磕原则</h2>
            
            <p class="strategy">
                <strong>🔥 核心绝杀：所有科目都不准当「耐听王」！听课永远学不会，只有通过做题才能真正在考场上写出来！多想多算多做，务必落实到笔头上！</strong><br><br>
                <span style="color: #ffb86c;">⚠️ 时间分配：抛开专业课，公共课的学习精力比重大致为数学 60%、英语 30%、政治 10%。注意，务必在自己的日常排期中优先把【专业课】的雷打不动时间固定下来。</span>
            </p>
            
            <div class="grid-box">
                <div class="grid-item grid-math">
                    <h3>📐 数学一（占公共课精力 60%）</h3>
                    <ul>
                        <li><strong style="color: #fff;">果断弃课投题：</strong>不推荐长期看张宇的课程！做题时不会的直接去B站搜播放量高的干货UP主讲解（千羽、考研数学777、没咋了等），比大机构视频好很多！</li>
                        <li><strong style="color: #fff;">不需要学的部分：</strong>张宇“超实数”、微分算子法、海涅定理、压缩映射原理、stolz法则。想考150分的人也完全不需要看这些！</li>
                        <li><strong style="color: #fff;">练习策略铁律：</strong>真题分类最优先 -> 习题册往后推 -> 模拟题少做。<br>所有习题册+模拟卷【全部跳过证明题】，只手写历年真题里的证明题！</li>
                    </ul>
                </div>
                
                <div class="grid-item grid-english">
                    <h3>📖 英语一（占公共课精力 30%）</h3>
                    <ul>
                        <li><strong style="color: #fff;">底线原则：</strong>绝不买手译本精翻文章！少听课或不听课。前期只搞阅读和记单词，暑假起听Monkey慢慢练作文，最后不慌不忙拿高分。</li>
                        <li><strong style="color: #fff;">背诵死命推：</strong>暑假前唯一任务就是用《不背单词》背核心3000词，最少刷3遍！中后期转入《真题伴侣》，着重背真题阅读语境里的生冷意思。</li>
                    </ul>
                </div>
                
                <div class="grid-item grid-politics">
                    <h3>🏛️ 政治（占公共课精力 10%）</h3>
                    <ul>
                        <li><strong style="color: #f43f5e;">🚫 10月初前绝对不动：</strong>最早10月初进场！绝不去听徐涛等名师的长篇大论课，坚决不用肖1000题题海战术！</li>
                        <li><strong style="color: #fff;">短平快收尾：</strong>只需腿姐冲刺背诵手册熟读+《苍盾小程序》刷模拟单选。12月等肖四出版直接背大题（背不下来没关系，影响不大）。最后期必看B站政治抄材料绝杀操作！</li>
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

    with open("D:/myblog/source/kaoyan/李白白/libaibai.html", "w", encoding="utf-8") as f:
        f.write(html_template)
        
if __name__ == "__main__":
    get_full_plan_libaibai()
